# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import datetime
from typing import TYPE_CHECKING
import warnings

from azure.core.exceptions import HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, List, Optional, TypeVar

    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class ActivityRunOperations(object):
    """ActivityRunOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~data_factory_management_client.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    def query_by_pipeline_run(
        self,
        resource_group_name,  # type: str
        factory_name,  # type: str
        run_id,  # type: str
        last_updated_after,  # type: datetime.datetime
        last_updated_before,  # type: datetime.datetime
        continuation_token=None,  # type: Optional[str]
        filters=None,  # type: Optional[List["models.RunQueryFilter"]]
        order_by=None,  # type: Optional[List["models.RunQueryOrderBy"]]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.ActivityRunsQueryResponse"
        """Query activity runs based on input filter conditions.

        :param resource_group_name: The resource group name.
        :type resource_group_name: str
        :param factory_name: The factory name.
        :type factory_name: str
        :param run_id: The pipeline run identifier.
        :type run_id: str
        :param last_updated_after: The time at or after which the run event was updated in 'ISO 8601'
         format.
        :type last_updated_after: ~datetime.datetime
        :param last_updated_before: The time at or before which the run event was updated in 'ISO 8601'
         format.
        :type last_updated_before: ~datetime.datetime
        :param continuation_token: The continuation token for getting the next page of results. Null
         for first page.
        :type continuation_token: str
        :param filters: List of filters.
        :type filters: list[~data_factory_management_client.models.RunQueryFilter]
        :param order_by: List of OrderBy option.
        :type order_by: list[~data_factory_management_client.models.RunQueryOrderBy]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ActivityRunsQueryResponse, or the result of cls(response)
        :rtype: ~data_factory_management_client.models.ActivityRunsQueryResponse
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.ActivityRunsQueryResponse"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _filter_parameters = models.RunFilterParameters(continuation_token=continuation_token, last_updated_after=last_updated_after, last_updated_before=last_updated_before, filters=filters, order_by=order_by)
        api_version = "2018-06-01"
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self.query_by_pipeline_run.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
            'factoryName': self._serialize.url("factory_name", factory_name, 'str', max_length=63, min_length=3, pattern=r'^[A-Za-z0-9]+(?:-[A-Za-z0-9]+)*$'),
            'runId': self._serialize.url("run_id", run_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(_filter_parameters, 'RunFilterParameters')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('ActivityRunsQueryResponse', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    query_by_pipeline_run.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/pipelineruns/{runId}/queryActivityruns'}  # type: ignore
