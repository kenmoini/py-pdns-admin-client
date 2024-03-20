# pdns_admin_client.MonitoringApi

All URIs are relative to *http://localhost:80/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**health_check**](MonitoringApi.md#health_check) | **GET** /servers/{server_id}/health | Perfoms health check


# **health_check**
> str health_check(server_id)

Perfoms health check

### Example

* Api Key Authentication (APIKeyHeader):

```python
import pdns_admin_client
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
    api_instance = pdns_admin_client.MonitoringApi(api_client)
    server_id = 'server_id_example' # str | The id of the server to retrieve

    try:
        # Perfoms health check
        api_response = api_instance.health_check(server_id)
        print("The response of MonitoringApi->health_check:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MonitoringApi->health_check: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The id of the server to retrieve | 

### Return type

**str**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Healthcheck succeeded |  -  |
**503** | Healthcheck failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

