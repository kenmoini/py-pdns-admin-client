# pdns_admin_client.SearchApi

All URIs are relative to *http://localhost:80/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search_data**](SearchApi.md#search_data) | **GET** /servers/{server_id}/search-data | Search the data inside PowerDNS


# **search_data**
> List[SearchResult] search_data(server_id, q, max)

Search the data inside PowerDNS

Search the data inside PowerDNS for search_term and return at most max_results. This includes zones, records and comments. The * character can be used in search_term as a wildcard character and the ? character can be used as a wildcard for a single character.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import pdns_admin_client
from pdns_admin_client.models.search_result import SearchResult
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
    api_instance = pdns_admin_client.SearchApi(api_client)
    server_id = 'server_id_example' # str | The id of the server to retrieve
    q = 'q_example' # str | The string to search for
    max = 56 # int | Maximum number of entries to return

    try:
        # Search the data inside PowerDNS
        api_response = api_instance.search_data(server_id, q, max)
        print("The response of SearchApi->search_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->search_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The id of the server to retrieve | 
 **q** | **str**| The string to search for | 
 **max** | **int**| Maximum number of entries to return | 

### Return type

[**List[SearchResult]**](SearchResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a JSON array with results |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

