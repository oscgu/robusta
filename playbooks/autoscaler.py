from math import ceil

from robusta.api import *

HPA_NAME = "hpa_name"
NAMESPACE = "namespace"
MAX_REPLICAS = "max_replicas"
SLACK_CHANNEL = "slack_channel"

class HPALimitParams(BaseModel):
    increase_pct : int = 20
    slack_channel: str

@on_report_callback
def scale_hpa_callback(event: ReportCallbackEvent):
    context = json.loads(event.source_context)
    hpa_name = context[HPA_NAME]
    hpa_ns = context[NAMESPACE]
    hpa : HorizontalPodAutoscaler = HorizontalPodAutoscaler.readNamespacedHorizontalPodAutoscaler(hpa_name, hpa_ns).obj
    new_max_replicas = int(context[MAX_REPLICAS])
    hpa.spec.maxReplicas = new_max_replicas
    hpa.replaceNamespacedHorizontalPodAutoscaler(hpa_name, hpa_ns)
    event.report_title = f"Max replicas for HPA *{hpa_name}* in namespace *{hpa_ns}* updated to: *{new_max_replicas}*"
    event.slack_channel=context[SLACK_CHANNEL]
    send_to_slack(event)


@on_horizontalpodautoscaler_update
def alert_on_hpa_reached_limit(event : HorizontalPodAutoscalerEvent, action_params : HPALimitParams):
    logging.info(f'running alert_on_hpa_reached_limit: {event.obj.metadata.name} ns: {event.obj.metadata.namespace}')

    hpa = event.obj
    if hpa.status.currentReplicas == event.old_obj.status.currentReplicas:
        return # run only when number of replicas change

    if hpa.status.desiredReplicas != hpa.spec.maxReplicas:
        return # didn't reached max replicas limit

    avg_cpu = int(hpa.status.currentCPUUtilizationPercentage / (hpa.status.currentReplicas if hpa.status.currentReplicas > 0 else 1))
    new_max_replicas_suggestion = ceil((action_params.increase_pct + 100) * hpa.spec.maxReplicas / 100)
    choices = {
        f'Update HPA max replicas to: {new_max_replicas_suggestion}': scale_hpa_callback,
    }
    context = {
        HPA_NAME: hpa.metadata.name,
        NAMESPACE: hpa.metadata.namespace,
        MAX_REPLICAS: new_max_replicas_suggestion,
        SLACK_CHANNEL: action_params.slack_channel
    }

    event.report_title = f"HPA *{event.obj.metadata.name}* in namespace *{event.obj.metadata.namespace}* reached max replicas: *{hpa.spec.maxReplicas}*"
    event.slack_channel = action_params.slack_channel
    event.report_blocks.extend([MarkdownBlock(f"Current avg cpu utilization: *{avg_cpu} %*        -- (usage vs requested)"),
                                CallbackBlock(choices, context)])
    send_to_slack(event)
