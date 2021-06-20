import logging
from kubernetes import client
from kubernetes.client.models.v1_service import V1Service


def find_service_url(label_selector):
    """
    Get the url of an in-cluster service with a specific label
    """
    # we do it this way because there is a weird issue with hikaru's ServiceList.listServiceForAllNamespaces()
    v1 = client.CoreV1Api()
    svc: V1Service = v1.list_service_for_all_namespaces(label_selector=label_selector).items[0]
    name = svc.metadata.name
    namespace = svc.metadata.namespace
    port = svc.spec.ports[0].port
    url = f"http://{name}.{namespace}.svc:{port}"
    logging.debug(f"discovered service with label-selector: `{label_selector}` at url: `{url}`")
    return url
