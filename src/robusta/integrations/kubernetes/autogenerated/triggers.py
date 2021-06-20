# This file was autogenerated. Do not edit.

from ....utils.decorators import doublewrap
from ..base_triggers import register_k8s_playbook, register_k8s_any_playbook
from ..base_event import K8sOperationType


# Pod Triggers
@doublewrap
def on_pod_create(func, name_prefix='', namespace_prefix=''):
    return register_k8s_playbook(func, 'Pod', K8sOperationType.CREATE, name_prefix=name_prefix, namespace_prefix=namespace_prefix)


@doublewrap
def on_pod_update(func, name_prefix='', namespace_prefix=''):
    return register_k8s_playbook(func, 'Pod', K8sOperationType.UPDATE, name_prefix=name_prefix, namespace_prefix=namespace_prefix)


@doublewrap
def on_pod_delete(func, name_prefix='', namespace_prefix=''):
    return register_k8s_playbook(func, 'Pod', K8sOperationType.DELETE, name_prefix=name_prefix, namespace_prefix=namespace_prefix)


@doublewrap
def on_pod_all_changes(func, name_prefix='', namespace_prefix=''):
    return register_k8s_playbook(func, 'Pod', None, name_prefix=name_prefix, namespace_prefix=namespace_prefix)


# ReplicaSet Triggers
@doublewrap
def on_replicaset_create(func, name_prefix='', namespace_prefix=''):
    return register_k8s_playbook(func, 'ReplicaSet', K8sOperationType.CREATE, name_prefix=name_prefix, namespace_prefix=namespace_prefix)


@doublewrap
def on_replicaset_update(func, name_prefix='', namespace_prefix=''):
    return register_k8s_playbook(func, 'ReplicaSet', K8sOperationType.UPDATE, name_prefix=name_prefix, namespace_prefix=namespace_prefix)


@doublewrap
def on_replicaset_delete(func, name_prefix='', namespace_prefix=''):
    return register_k8s_playbook(func, 'ReplicaSet', K8sOperationType.DELETE, name_prefix=name_prefix, namespace_prefix=namespace_prefix)


@doublewrap
def on_replicaset_all_changes(func, name_prefix='', namespace_prefix=''):
    return register_k8s_playbook(func, 'ReplicaSet', None, name_prefix=name_prefix, namespace_prefix=namespace_prefix)


# DaemonSet Triggers
@doublewrap
def on_daemonset_create(func, name_prefix='', namespace_prefix=''):
    return register_k8s_playbook(func, 'DaemonSet', K8sOperationType.CREATE, name_prefix=name_prefix, namespace_prefix=namespace_prefix)


@doublewrap
def on_daemonset_update(func, name_prefix='', namespace_prefix=''):
    return register_k8s_playbook(func, 'DaemonSet', K8sOperationType.UPDATE, name_prefix=name_prefix, namespace_prefix=namespace_prefix)


@doublewrap
def on_daemonset_delete(func, name_prefix='', namespace_prefix=''):
    return register_k8s_playbook(func, 'DaemonSet', K8sOperationType.DELETE, name_prefix=name_prefix, namespace_prefix=namespace_prefix)


@doublewrap
def on_daemonset_all_changes(func, name_prefix='', namespace_prefix=''):
    return register_k8s_playbook(func, 'DaemonSet', None, name_prefix=name_prefix, namespace_prefix=namespace_prefix)


# Deployment Triggers
@doublewrap
def on_deployment_create(func, name_prefix='', namespace_prefix=''):
    return register_k8s_playbook(func, 'Deployment', K8sOperationType.CREATE, name_prefix=name_prefix, namespace_prefix=namespace_prefix)


@doublewrap
def on_deployment_update(func, name_prefix='', namespace_prefix=''):
    return register_k8s_playbook(func, 'Deployment', K8sOperationType.UPDATE, name_prefix=name_prefix, namespace_prefix=namespace_prefix)


@doublewrap
def on_deployment_delete(func, name_prefix='', namespace_prefix=''):
    return register_k8s_playbook(func, 'Deployment', K8sOperationType.DELETE, name_prefix=name_prefix, namespace_prefix=namespace_prefix)


@doublewrap
def on_deployment_all_changes(func, name_prefix='', namespace_prefix=''):
    return register_k8s_playbook(func, 'Deployment', None, name_prefix=name_prefix, namespace_prefix=namespace_prefix)


# Service Triggers
@doublewrap
def on_service_create(func, name_prefix='', namespace_prefix=''):
    return register_k8s_playbook(func, 'Service', K8sOperationType.CREATE, name_prefix=name_prefix, namespace_prefix=namespace_prefix)


@doublewrap
def on_service_update(func, name_prefix='', namespace_prefix=''):
    return register_k8s_playbook(func, 'Service', K8sOperationType.UPDATE, name_prefix=name_prefix, namespace_prefix=namespace_prefix)


@doublewrap
def on_service_delete(func, name_prefix='', namespace_prefix=''):
    return register_k8s_playbook(func, 'Service', K8sOperationType.DELETE, name_prefix=name_prefix, namespace_prefix=namespace_prefix)


@doublewrap
def on_service_all_changes(func, name_prefix='', namespace_prefix=''):
    return register_k8s_playbook(func, 'Service', None, name_prefix=name_prefix, namespace_prefix=namespace_prefix)


# ConfigMap Triggers
@doublewrap
def on_configmap_create(func, name_prefix='', namespace_prefix=''):
    return register_k8s_playbook(func, 'ConfigMap', K8sOperationType.CREATE, name_prefix=name_prefix, namespace_prefix=namespace_prefix)


@doublewrap
def on_configmap_update(func, name_prefix='', namespace_prefix=''):
    return register_k8s_playbook(func, 'ConfigMap', K8sOperationType.UPDATE, name_prefix=name_prefix, namespace_prefix=namespace_prefix)


@doublewrap
def on_configmap_delete(func, name_prefix='', namespace_prefix=''):
    return register_k8s_playbook(func, 'ConfigMap', K8sOperationType.DELETE, name_prefix=name_prefix, namespace_prefix=namespace_prefix)


@doublewrap
def on_configmap_all_changes(func, name_prefix='', namespace_prefix=''):
    return register_k8s_playbook(func, 'ConfigMap', None, name_prefix=name_prefix, namespace_prefix=namespace_prefix)


# Event Triggers
@doublewrap
def on_event_create(func, name_prefix='', namespace_prefix=''):
    return register_k8s_playbook(func, 'Event', K8sOperationType.CREATE, name_prefix=name_prefix, namespace_prefix=namespace_prefix)


@doublewrap
def on_event_update(func, name_prefix='', namespace_prefix=''):
    return register_k8s_playbook(func, 'Event', K8sOperationType.UPDATE, name_prefix=name_prefix, namespace_prefix=namespace_prefix)


@doublewrap
def on_event_delete(func, name_prefix='', namespace_prefix=''):
    return register_k8s_playbook(func, 'Event', K8sOperationType.DELETE, name_prefix=name_prefix, namespace_prefix=namespace_prefix)


@doublewrap
def on_event_all_changes(func, name_prefix='', namespace_prefix=''):
    return register_k8s_playbook(func, 'Event', None, name_prefix=name_prefix, namespace_prefix=namespace_prefix)


# HorizontalPodAutoscaler Triggers
@doublewrap
def on_horizontalpodautoscaler_create(func, name_prefix='', namespace_prefix=''):
    return register_k8s_playbook(func, 'HorizontalPodAutoscaler', K8sOperationType.CREATE, name_prefix=name_prefix, namespace_prefix=namespace_prefix)


@doublewrap
def on_horizontalpodautoscaler_update(func, name_prefix='', namespace_prefix=''):
    return register_k8s_playbook(func, 'HorizontalPodAutoscaler', K8sOperationType.UPDATE, name_prefix=name_prefix, namespace_prefix=namespace_prefix)


@doublewrap
def on_horizontalpodautoscaler_delete(func, name_prefix='', namespace_prefix=''):
    return register_k8s_playbook(func, 'HorizontalPodAutoscaler', K8sOperationType.DELETE, name_prefix=name_prefix, namespace_prefix=namespace_prefix)


@doublewrap
def on_horizontalpodautoscaler_all_changes(func, name_prefix='', namespace_prefix=''):
    return register_k8s_playbook(func, 'HorizontalPodAutoscaler', None, name_prefix=name_prefix, namespace_prefix=namespace_prefix)


# Kubernetes Any Triggers
@doublewrap
def on_kubernetes_any_create(func, name_prefix='', namespace_prefix=''):
    return register_k8s_any_playbook(func, K8sOperationType.CREATE, name_prefix=name_prefix, namespace_prefix=namespace_prefix)


@doublewrap
def on_kubernetes_any_update(func, name_prefix='', namespace_prefix=''):
    return register_k8s_any_playbook(func, K8sOperationType.UPDATE, name_prefix=name_prefix, namespace_prefix=namespace_prefix)


@doublewrap
def on_kubernetes_any_delete(func, name_prefix='', namespace_prefix=''):
    return register_k8s_any_playbook(func, K8sOperationType.DELETE, name_prefix=name_prefix, namespace_prefix=namespace_prefix)


@doublewrap
def on_kubernetes_any_all_changes(func, name_prefix='', namespace_prefix=''):
    return register_k8s_any_playbook(func, None, name_prefix=name_prefix, namespace_prefix=namespace_prefix)


