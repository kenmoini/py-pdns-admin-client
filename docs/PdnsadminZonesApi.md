# pdns_admin_client.PdnsadminZonesApi

All URIs are relative to *http://localhost:80/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_login_create_zone**](PdnsadminZonesApi.md#api_login_create_zone) | **POST** /pdnsadmin/zones | Creates a new domain, returns the Zone on creation.
[**api_login_delete_zone**](PdnsadminZonesApi.md#api_login_delete_zone) | **DELETE** /pdnsadmin/zones/{zone_id} | Deletes this zone, all attached metadata and rrsets.
[**api_login_list_zones**](PdnsadminZonesApi.md#api_login_list_zones) | **GET** /pdnsadmin/zones | List all Zones in a server
[**synchronize_domains**](PdnsadminZonesApi.md#synchronize_domains) | **GET** /sync_domains | Sync PDNS with PDNSAdmin


# **api_login_create_zone**
> Zone api_login_create_zone(zone_struct)

Creates a new domain, returns the Zone on creation.

### Example

* Basic Authentication (basicAuth):

```python
import pdns_admin_client
from pdns_admin_client.models.zone import Zone
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

# Configure HTTP basic authorization: basicAuth
configuration = pdns_admin_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with pdns_admin_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pdns_admin_client.PdnsadminZonesApi(api_client)
    zone_struct = pdns_admin_client.Zone() # Zone | The zone struct to patch with

    try:
        # Creates a new domain, returns the Zone on creation.
        api_response = api_instance.api_login_create_zone(zone_struct)
        print("The response of PdnsadminZonesApi->api_login_create_zone:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PdnsadminZonesApi->api_login_create_zone: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_struct** | [**Zone**](Zone.md)| The zone struct to patch with | 

### Return type

[**Zone**](Zone.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | A zone |  -  |
**400** | Request is not JSON |  -  |
**401** | Unauthorized |  -  |
**409** | Domain already exists (conflict) |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_login_delete_zone**
> api_login_delete_zone(zone_id)

Deletes this zone, all attached metadata and rrsets.

### Example

* Basic Authentication (basicAuth):

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

# Configure HTTP basic authorization: basicAuth
configuration = pdns_admin_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with pdns_admin_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pdns_admin_client.PdnsadminZonesApi(api_client)
    zone_id = 'zone_id_example' # str | The id of the zone to retrieve

    try:
        # Deletes this zone, all attached metadata and rrsets.
        api_instance.api_login_delete_zone(zone_id)
    except Exception as e:
        print("Exception when calling PdnsadminZonesApi->api_login_delete_zone: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_id** | **str**| The id of the zone to retrieve | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Returns 204 No Content on success. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_login_list_zones**
> List[List[PDNSAdminZonesInner]] api_login_list_zones()

List all Zones in a server

### Example

* Basic Authentication (basicAuth):

```python
import pdns_admin_client
from pdns_admin_client.models.pdns_admin_zones_inner import PDNSAdminZonesInner
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

# Configure HTTP basic authorization: basicAuth
configuration = pdns_admin_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with pdns_admin_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pdns_admin_client.PdnsadminZonesApi(api_client)

    try:
        # List all Zones in a server
        api_response = api_instance.api_login_list_zones()
        print("The response of PdnsadminZonesApi->api_login_list_zones:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PdnsadminZonesApi->api_login_list_zones: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**List[List[PDNSAdminZonesInner]]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of Zones |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **synchronize_domains**
> synchronize_domains()

Sync PDNS with PDNSAdmin

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
    api_instance = pdns_admin_client.PdnsadminZonesApi(api_client)

    try:
        # Sync PDNS with PDNSAdmin
        api_instance.synchronize_domains()
    except Exception as e:
        print("Exception when calling PdnsadminZonesApi->synchronize_domains: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Synchronize PDNS Domains with PDNSAdmin |  -  |
**403** | Wrong authentication |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

