# pdns_admin_client.StatsApi

All URIs are relative to *http://localhost:80/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_stats**](StatsApi.md#get_stats) | **GET** /servers/{server_id}/statistics | Query statistics.


# **get_stats**
> List[MapStatisticItem] get_stats(server_id)

Query statistics.

Query PowerDNS internal statistics. Returns a list of BaseStatisticItem derived elements.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import pdns_admin_client
from pdns_admin_client.models.map_statistic_item import MapStatisticItem
from pdns_admin_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:80/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = pdns_admin_client.Configuration(
    host = "http://localhost:80/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with pdns_admin_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pdns_admin_client.StatsApi(api_client)
    server_id = 'server_id_example' # str | The id of the server to retrieve

    try:
        # Query statistics.
        api_response = api_instance.get_stats(server_id)
        print("The response of StatsApi->get_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatsApi->get_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The id of the server to retrieve | 

### Return type

[**List[MapStatisticItem]**](MapStatisticItem.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of Statistic Items |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

