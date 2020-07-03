# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-lines
# pylint: disable=unused-argument

from knack.util import CLIError
from azure.cli.core.util import sdk_no_wait


def datafactory_factory_list(client,
                             resource_group_name=None):
    if resource_group_name:
        return client.list_by_resource_group(resource_group_name=resource_group_name)
    return client.list()


def datafactory_factory_show(client,
                             resource_group_name,
                             factory_name,
                             if_none_match=None):
    return client.get(resource_group_name=resource_group_name,
                      factory_name=factory_name,
                      if_none_match=if_none_match)


def datafactory_factory_create(client,
                               resource_group_name,
                               factory_name,
                               if_match=None,
                               location=None,
                               tags=None,
                               factory_vsts_configuration=None,
                               factory_git_hub_configuration=None,
                               global_parameters=None):
    all_repo_configuration = []
    if factory_vsts_configuration is not None:
        all_repo_configuration.append(factory_vsts_configuration)
    if factory_git_hub_configuration is not None:
        all_repo_configuration.append(factory_git_hub_configuration)
    if len(all_repo_configuration) > 1:
        raise CLIError('at most one of  factory_vsts_configuration, factory_git_hub_configuration is needed for '
                       'repo_configuration!')
    repo_configuration = all_repo_configuration[0] if len(all_repo_configuration) == 1 else None
    return client.create_or_update(resource_group_name=resource_group_name,
                                   factory_name=factory_name,
                                   if_match=if_match,
                                   location=location,
                                   tags=tags,
                                   identity={"type": "SystemAssigned"},
                                   repo_configuration=repo_configuration)


def datafactory_factory_update(client,
                               resource_group_name,
                               factory_name,
                               tags=None):
    return client.update(resource_group_name=resource_group_name,
                         factory_name=factory_name,
                         tags=tags,
                         identity={"type": "SystemAssigned"})


def datafactory_factory_delete(client,
                               resource_group_name,
                               factory_name):
    return client.delete(resource_group_name=resource_group_name,
                         factory_name=factory_name)


def datafactory_factory_configure_factory_repo(client,
                                               location,
                                               factory_resource_id=None,
                                               factory_vsts_configuration=None,
                                               factory_git_hub_configuration=None):
    all_repo_configuration = []
    if factory_vsts_configuration is not None:
        all_repo_configuration.append(factory_vsts_configuration)
    if factory_git_hub_configuration is not None:
        all_repo_configuration.append(factory_git_hub_configuration)
    if len(all_repo_configuration) > 1:
        raise CLIError('at most one of  factory_vsts_configuration, factory_git_hub_configuration is needed for '
                       'repo_configuration!')
    repo_configuration = all_repo_configuration[0] if len(all_repo_configuration) == 1 else None
    return client.configure_factory_repo(location_id=location,
                                         factory_resource_id=factory_resource_id,
                                         repo_configuration=repo_configuration)


def datafactory_factory_get_data_plane_access(client,
                                              resource_group_name,
                                              factory_name,
                                              permissions=None,
                                              access_resource_path=None,
                                              profile_name=None,
                                              start_time=None,
                                              expire_time=None):
    return client.get_data_plane_access(resource_group_name=resource_group_name,
                                        factory_name=factory_name,
                                        permissions=permissions,
                                        access_resource_path=access_resource_path,
                                        profile_name=profile_name,
                                        start_time=start_time,
                                        expire_time=expire_time)


def datafactory_factory_get_git_hub_access_token(client,
                                                 resource_group_name,
                                                 factory_name,
                                                 git_hub_access_code,
                                                 git_hub_access_token_base_url,
                                                 git_hub_client_id=None):
    return client.get_git_hub_access_token(resource_group_name=resource_group_name,
                                           factory_name=factory_name,
                                           git_hub_access_code=git_hub_access_code,
                                           git_hub_client_id=git_hub_client_id,
                                           git_hub_access_token_base_url=git_hub_access_token_base_url)


def datafactory_integration_runtime_list(client,
                                         resource_group_name,
                                         factory_name):
    return client.list_by_factory(resource_group_name=resource_group_name,
                                  factory_name=factory_name)


def datafactory_integration_runtime_show(client,
                                         resource_group_name,
                                         factory_name,
                                         integration_runtime_name,
                                         if_none_match=None):
    return client.get(resource_group_name=resource_group_name,
                      factory_name=factory_name,
                      integration_runtime_name=integration_runtime_name,
                      if_none_match=if_none_match)


def datafactory_integration_runtime_linked_integration_runtime_create(client,
                                                                      resource_group_name,
                                                                      factory_name,
                                                                      integration_runtime_name,
                                                                      name=None,
                                                                      subscription_id=None,
                                                                      data_factory_name=None,
                                                                      location=None):
    return client.create_linked_integration_runtime(resource_group_name=resource_group_name,
                                                    factory_name=factory_name,
                                                    integration_runtime_name=integration_runtime_name,
                                                    name=name,
                                                    subscription_id=subscription_id,
                                                    data_factory_name=data_factory_name,
                                                    data_factory_location=location)


def datafactory_integration_runtime_managed_create(client,
                                                   resource_group_name,
                                                   factory_name,
                                                   integration_runtime_name,
                                                   if_match=None,
                                                   description=None,
                                                   type_properties_compute_properties=None,
                                                   type_properties_ssis_properties=None):
    properties = {}
    properties['type'] = 'Managed'
    properties['description'] = description
    properties['compute_properties'] = type_properties_compute_properties
    properties['ssis_properties'] = type_properties_ssis_properties
    return client.create_or_update(resource_group_name=resource_group_name,
                                   factory_name=factory_name,
                                   integration_runtime_name=integration_runtime_name,
                                   if_match=if_match,
                                   properties=properties)


def datafactory_integration_runtime_self_hosted_create(client,
                                                       resource_group_name,
                                                       factory_name,
                                                       integration_runtime_name,
                                                       if_match=None,
                                                       description=None,
                                                       type_properties_linked_info=None):
    properties = {}
    properties['type'] = 'SelfHosted'
    properties['description'] = description
    properties['linked_info'] = type_properties_linked_info
    return client.create_or_update(resource_group_name=resource_group_name,
                                   factory_name=factory_name,
                                   integration_runtime_name=integration_runtime_name,
                                   if_match=if_match,
                                   properties=properties)


def datafactory_integration_runtime_update(client,
                                           resource_group_name,
                                           factory_name,
                                           integration_runtime_name,
                                           auto_update=None,
                                           update_delay_offset=None):
    return client.update(resource_group_name=resource_group_name,
                         factory_name=factory_name,
                         integration_runtime_name=integration_runtime_name,
                         auto_update=auto_update,
                         update_delay_offset=update_delay_offset)


def datafactory_integration_runtime_delete(client,
                                           resource_group_name,
                                           factory_name,
                                           integration_runtime_name):
    return client.delete(resource_group_name=resource_group_name,
                         factory_name=factory_name,
                         integration_runtime_name=integration_runtime_name)


def datafactory_integration_runtime_get_connection_info(client,
                                                        resource_group_name,
                                                        factory_name,
                                                        integration_runtime_name):
    return client.get_connection_info(resource_group_name=resource_group_name,
                                      factory_name=factory_name,
                                      integration_runtime_name=integration_runtime_name)


def datafactory_integration_runtime_get_monitoring_data(client,
                                                        resource_group_name,
                                                        factory_name,
                                                        integration_runtime_name):
    return client.get_monitoring_data(resource_group_name=resource_group_name,
                                      factory_name=factory_name,
                                      integration_runtime_name=integration_runtime_name)


def datafactory_integration_runtime_get_status(client,
                                               resource_group_name,
                                               factory_name,
                                               integration_runtime_name):
    return client.get_status(resource_group_name=resource_group_name,
                             factory_name=factory_name,
                             integration_runtime_name=integration_runtime_name)


def datafactory_integration_runtime_list_auth_key(client,
                                                  resource_group_name,
                                                  factory_name,
                                                  integration_runtime_name):
    return client.list_auth_key(resource_group_name=resource_group_name,
                                factory_name=factory_name,
                                integration_runtime_name=integration_runtime_name)


def datafactory_integration_runtime_regenerate_auth_key(client,
                                                        resource_group_name,
                                                        factory_name,
                                                        integration_runtime_name,
                                                        key_name=None):
    return client.regenerate_auth_key(resource_group_name=resource_group_name,
                                      factory_name=factory_name,
                                      integration_runtime_name=integration_runtime_name,
                                      key_name=key_name)


def datafactory_integration_runtime_remove_link(client,
                                                resource_group_name,
                                                factory_name,
                                                integration_runtime_name,
                                                linked_factory_name):
    return client.remove_link(resource_group_name=resource_group_name,
                              factory_name=factory_name,
                              integration_runtime_name=integration_runtime_name,
                              linked_factory_name=linked_factory_name)


def datafactory_integration_runtime_start(client,
                                          resource_group_name,
                                          factory_name,
                                          integration_runtime_name,
                                          no_wait=False):
    return sdk_no_wait(no_wait,
                       client.begin_start,
                       resource_group_name=resource_group_name,
                       factory_name=factory_name,
                       integration_runtime_name=integration_runtime_name)


def datafactory_integration_runtime_stop(client,
                                         resource_group_name,
                                         factory_name,
                                         integration_runtime_name,
                                         no_wait=False):
    return sdk_no_wait(no_wait,
                       client.begin_stop,
                       resource_group_name=resource_group_name,
                       factory_name=factory_name,
                       integration_runtime_name=integration_runtime_name)


def datafactory_integration_runtime_sync_credentials(client,
                                                     resource_group_name,
                                                     factory_name,
                                                     integration_runtime_name):
    return client.sync_credentials(resource_group_name=resource_group_name,
                                   factory_name=factory_name,
                                   integration_runtime_name=integration_runtime_name)


def datafactory_integration_runtime_upgrade(client,
                                            resource_group_name,
                                            factory_name,
                                            integration_runtime_name):
    return client.upgrade(resource_group_name=resource_group_name,
                          factory_name=factory_name,
                          integration_runtime_name=integration_runtime_name)


def datafactory_integration_runtime_node_show(client,
                                              resource_group_name,
                                              factory_name,
                                              integration_runtime_name,
                                              node_name):
    return client.get(resource_group_name=resource_group_name,
                      factory_name=factory_name,
                      integration_runtime_name=integration_runtime_name,
                      node_name=node_name)


def datafactory_integration_runtime_node_update(client,
                                                resource_group_name,
                                                factory_name,
                                                integration_runtime_name,
                                                node_name,
                                                concurrent_jobs_limit=None):
    return client.update(resource_group_name=resource_group_name,
                         factory_name=factory_name,
                         integration_runtime_name=integration_runtime_name,
                         node_name=node_name,
                         concurrent_jobs_limit=concurrent_jobs_limit)


def datafactory_integration_runtime_node_delete(client,
                                                resource_group_name,
                                                factory_name,
                                                integration_runtime_name,
                                                node_name):
    return client.delete(resource_group_name=resource_group_name,
                         factory_name=factory_name,
                         integration_runtime_name=integration_runtime_name,
                         node_name=node_name)


def datafactory_integration_runtime_node_get_ip_address(client,
                                                        resource_group_name,
                                                        factory_name,
                                                        integration_runtime_name,
                                                        node_name):
    return client.get_ip_address(resource_group_name=resource_group_name,
                                 factory_name=factory_name,
                                 integration_runtime_name=integration_runtime_name,
                                 node_name=node_name)


def datafactory_linked_service_list(client,
                                    resource_group_name,
                                    factory_name):
    return client.list_by_factory(resource_group_name=resource_group_name,
                                  factory_name=factory_name)


def datafactory_linked_service_show(client,
                                    resource_group_name,
                                    factory_name,
                                    linked_service_name,
                                    if_none_match=None):
    return client.get(resource_group_name=resource_group_name,
                      factory_name=factory_name,
                      linked_service_name=linked_service_name,
                      if_none_match=if_none_match)


def datafactory_linked_service_create(client,
                                      resource_group_name,
                                      factory_name,
                                      linked_service_name,
                                      properties,
                                      if_match=None):
    return client.create_or_update(resource_group_name=resource_group_name,
                                   factory_name=factory_name,
                                   linked_service_name=linked_service_name,
                                   if_match=if_match,
                                   properties=properties)


def datafactory_linked_service_delete(client,
                                      resource_group_name,
                                      factory_name,
                                      linked_service_name):
    return client.delete(resource_group_name=resource_group_name,
                         factory_name=factory_name,
                         linked_service_name=linked_service_name)


def datafactory_dataset_list(client,
                             resource_group_name,
                             factory_name):
    return client.list_by_factory(resource_group_name=resource_group_name,
                                  factory_name=factory_name)


def datafactory_dataset_show(client,
                             resource_group_name,
                             factory_name,
                             dataset_name,
                             if_none_match=None):
    return client.get(resource_group_name=resource_group_name,
                      factory_name=factory_name,
                      dataset_name=dataset_name,
                      if_none_match=if_none_match)


def datafactory_dataset_create(client,
                               resource_group_name,
                               factory_name,
                               dataset_name,
                               properties,
                               if_match=None):
    return client.create_or_update(resource_group_name=resource_group_name,
                                   factory_name=factory_name,
                                   dataset_name=dataset_name,
                                   if_match=if_match,
                                   properties=properties)


def datafactory_dataset_delete(client,
                               resource_group_name,
                               factory_name,
                               dataset_name):
    return client.delete(resource_group_name=resource_group_name,
                         factory_name=factory_name,
                         dataset_name=dataset_name)


def datafactory_pipeline_list(client,
                              resource_group_name,
                              factory_name):
    return client.list_by_factory(resource_group_name=resource_group_name,
                                  factory_name=factory_name)


def datafactory_pipeline_show(client,
                              resource_group_name,
                              factory_name,
                              pipeline_name,
                              if_none_match=None):
    return client.get(resource_group_name=resource_group_name,
                      factory_name=factory_name,
                      pipeline_name=pipeline_name,
                      if_none_match=if_none_match)


def datafactory_pipeline_create(client,
                                resource_group_name,
                                factory_name,
                                pipeline_name,
                                pipeline,
                                if_match=None):
    return client.create_or_update(resource_group_name=resource_group_name,
                                   factory_name=factory_name,
                                   pipeline_name=pipeline_name,
                                   if_match=if_match,
                                   pipeline=pipeline)


def datafactory_pipeline_update(instance,
                                resource_group_name,
                                factory_name,
                                pipeline_name,
                                if_match=None,
                                description=None,
                                activities=None,
                                parameters=None,
                                variables=None,
                                concurrency=None,
                                annotations=None,
                                run_dimensions=None,
                                folder_name=None):
    if description is not None:
        instance.description = description
    if activities is not None:
        instance.activities = activities
    if parameters is not None:
        instance.parameters = parameters
    if variables is not None:
        instance.variables = variables
    if concurrency is not None:
        instance.concurrency = concurrency
    if annotations is not None:
        instance.annotations = annotations
    if run_dimensions is not None:
        instance.run_dimensions = run_dimensions
    if folder_name is not None:
        instance.name_properties_folder_name = folder_name
    return instance


def datafactory_pipeline_delete(client,
                                resource_group_name,
                                factory_name,
                                pipeline_name):
    return client.delete(resource_group_name=resource_group_name,
                         factory_name=factory_name,
                         pipeline_name=pipeline_name)


def datafactory_pipeline_create_run(client,
                                    resource_group_name,
                                    factory_name,
                                    pipeline_name,
                                    reference_pipeline_run_id=None,
                                    is_recovery=None,
                                    start_activity_name=None,
                                    start_from_failure=None,
                                    parameters=None):
    return client.create_run(resource_group_name=resource_group_name,
                             factory_name=factory_name,
                             pipeline_name=pipeline_name,
                             reference_pipeline_run_id=reference_pipeline_run_id,
                             is_recovery=is_recovery,
                             start_activity_name=start_activity_name,
                             start_from_failure=start_from_failure,
                             parameters=parameters)


def datafactory_pipeline_run_show(client,
                                  resource_group_name,
                                  factory_name,
                                  run_id):
    return client.get(resource_group_name=resource_group_name,
                      factory_name=factory_name,
                      run_id=run_id)


def datafactory_pipeline_run_cancel(client,
                                    resource_group_name,
                                    factory_name,
                                    run_id,
                                    is_recursive=None):
    return client.cancel(resource_group_name=resource_group_name,
                         factory_name=factory_name,
                         run_id=run_id,
                         is_recursive=is_recursive)


def datafactory_pipeline_run_query_by_factory(client,
                                              resource_group_name,
                                              factory_name,
                                              last_updated_after,
                                              last_updated_before,
                                              continuation_token=None,
                                              filters=None,
                                              order_by=None):
    return client.query_by_factory(resource_group_name=resource_group_name,
                                   factory_name=factory_name,
                                   continuation_token=continuation_token,
                                   last_updated_after=last_updated_after,
                                   last_updated_before=last_updated_before,
                                   filters=filters,
                                   order_by=order_by)


def datafactory_activity_run_query_by_pipeline_run(client,
                                                   resource_group_name,
                                                   factory_name,
                                                   run_id,
                                                   last_updated_after,
                                                   last_updated_before,
                                                   continuation_token=None,
                                                   filters=None,
                                                   order_by=None):
    return client.query_by_pipeline_run(resource_group_name=resource_group_name,
                                        factory_name=factory_name,
                                        run_id=run_id,
                                        continuation_token=continuation_token,
                                        last_updated_after=last_updated_after,
                                        last_updated_before=last_updated_before,
                                        filters=filters,
                                        order_by=order_by)


def datafactory_trigger_list(client,
                             resource_group_name,
                             factory_name):
    return client.list_by_factory(resource_group_name=resource_group_name,
                                  factory_name=factory_name)


def datafactory_trigger_show(client,
                             resource_group_name,
                             factory_name,
                             trigger_name,
                             if_none_match=None):
    return client.get(resource_group_name=resource_group_name,
                      factory_name=factory_name,
                      trigger_name=trigger_name,
                      if_none_match=if_none_match)


def datafactory_trigger_create(client,
                               resource_group_name,
                               factory_name,
                               trigger_name,
                               properties,
                               if_match=None):
    return client.create_or_update(resource_group_name=resource_group_name,
                                   factory_name=factory_name,
                                   trigger_name=trigger_name,
                                   if_match=if_match,
                                   properties=properties)


def datafactory_trigger_delete(client,
                               resource_group_name,
                               factory_name,
                               trigger_name):
    return client.delete(resource_group_name=resource_group_name,
                         factory_name=factory_name,
                         trigger_name=trigger_name)


def datafactory_trigger_get_event_subscription_status(client,
                                                      resource_group_name,
                                                      factory_name,
                                                      trigger_name):
    return client.get_event_subscription_status(resource_group_name=resource_group_name,
                                                factory_name=factory_name,
                                                trigger_name=trigger_name)


def datafactory_trigger_query_by_factory(client,
                                         resource_group_name,
                                         factory_name,
                                         continuation_token=None,
                                         parent_trigger_name=None):
    return client.query_by_factory(resource_group_name=resource_group_name,
                                   factory_name=factory_name,
                                   continuation_token=continuation_token,
                                   parent_trigger_name=parent_trigger_name)


def datafactory_trigger_start(client,
                              resource_group_name,
                              factory_name,
                              trigger_name,
                              no_wait=False):
    return sdk_no_wait(no_wait,
                       client.begin_start,
                       resource_group_name=resource_group_name,
                       factory_name=factory_name,
                       trigger_name=trigger_name)


def datafactory_trigger_stop(client,
                             resource_group_name,
                             factory_name,
                             trigger_name,
                             no_wait=False):
    return sdk_no_wait(no_wait,
                       client.begin_stop,
                       resource_group_name=resource_group_name,
                       factory_name=factory_name,
                       trigger_name=trigger_name)


def datafactory_trigger_subscribe_to_event(client,
                                           resource_group_name,
                                           factory_name,
                                           trigger_name,
                                           no_wait=False):
    return sdk_no_wait(no_wait,
                       client.begin_subscribe_to_event,
                       resource_group_name=resource_group_name,
                       factory_name=factory_name,
                       trigger_name=trigger_name)


def datafactory_trigger_unsubscribe_from_event(client,
                                               resource_group_name,
                                               factory_name,
                                               trigger_name,
                                               no_wait=False):
    return sdk_no_wait(no_wait,
                       client.begin_unsubscribe_from_event,
                       resource_group_name=resource_group_name,
                       factory_name=factory_name,
                       trigger_name=trigger_name)


def datafactory_trigger_run_query_by_factory(client,
                                             resource_group_name,
                                             factory_name,
                                             last_updated_after,
                                             last_updated_before,
                                             continuation_token=None,
                                             filters=None,
                                             order_by=None):
    return client.query_by_factory(resource_group_name=resource_group_name,
                                   factory_name=factory_name,
                                   continuation_token=continuation_token,
                                   last_updated_after=last_updated_after,
                                   last_updated_before=last_updated_before,
                                   filters=filters,
                                   order_by=order_by)


def datafactory_trigger_run_rerun(client,
                                  resource_group_name,
                                  factory_name,
                                  trigger_name,
                                  run_id):
    return client.rerun(resource_group_name=resource_group_name,
                        factory_name=factory_name,
                        trigger_name=trigger_name,
                        run_id=run_id)