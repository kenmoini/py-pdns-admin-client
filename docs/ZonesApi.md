# pdns_admin_client.ZonesApi

All URIs are relative to *http://localhost:80/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**axfr_export_zone**](ZonesApi.md#axfr_export_zone) | **GET** /servers/{server_id}/zones/{zone_id}/export | Returns the zone in AXFR format.
[**axfr_retrieve_zone**](ZonesApi.md#axfr_retrieve_zone) | **PUT** /servers/{server_id}/zones/{zone_id}/axfr-retrieve | Retrieve slave zone from its master.
[**check_zone**](ZonesApi.md#check_zone) | **GET** /servers/{server_id}/zones/{zone_id}/check | Verify zone contents/configuration.
[**create_zone**](ZonesApi.md#create_zone) | **POST** /servers/{server_id}/zones | Creates a new domain, returns the Zone on creation.
[**delete_zone**](ZonesApi.md#delete_zone) | **DELETE** /servers/{server_id}/zones/{zone_id} | Deletes this zone, all attached metadata and rrsets.
[**list_zone**](ZonesApi.md#list_zone) | **GET** /servers/{server_id}/zones/{zone_id} | zone managed by a server
[**list_zones**](ZonesApi.md#list_zones) | **GET** /servers/{server_id}/zones | List all Zones in a server
[**notify_zone**](ZonesApi.md#notify_zone) | **PUT** /servers/{server_id}/zones/{zone_id}/notify | Send a DNS NOTIFY to all slaves.
[**patch_zone**](ZonesApi.md#patch_zone) | **PATCH** /servers/{server_id}/zones/{zone_id} | Creates/modifies/deletes RRsets present in the payload and their comments. Returns 204 No Content on success.
[**put_zone**](ZonesApi.md#put_zone) | **PUT** /servers/{server_id}/zones/{zone_id} | Modifies basic zone data (metadata).
[**rectify_zone**](ZonesApi.md#rectify_zone) | **PUT** /servers/{server_id}/zones/{zone_id}/rectify | Rectify the zone data.


# **axfr_export_zone**
> str axfr_export_zone(server_id, zone_id)

Returns the zone in AXFR format.

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
    api_instance = pdns_admin_client.ZonesApi(api_client)
    server_id = 'server_id_example' # str | The id of the server to retrieve
    zone_id = 'zone_id_example' # str | The id of the zone to retrieve

    try:
        # Returns the zone in AXFR format.
        api_response = api_instance.axfr_export_zone(server_id, zone_id)
        print("The response of ZonesApi->axfr_export_zone:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ZonesApi->axfr_export_zone: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The id of the server to retrieve | 
 **zone_id** | **str**| The id of the zone to retrieve | 

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **axfr_retrieve_zone**
> axfr_retrieve_zone(server_id, zone_id)

Retrieve slave zone from its master.

Fails when zone kind is not Slave, or slave is disabled in the configuration. Clients MUST NOT send a body.

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
    api_instance = pdns_admin_client.ZonesApi(api_client)
    server_id = 'server_id_example' # str | The id of the server to retrieve
    zone_id = 'zone_id_example' # str | The id of the zone to retrieve

    try:
        # Retrieve slave zone from its master.
        api_instance.axfr_retrieve_zone(server_id, zone_id)
    except Exception as e:
        print("Exception when calling ZonesApi->axfr_retrieve_zone: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The id of the server to retrieve | 
 **zone_id** | **str**| The id of the zone to retrieve | 

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_zone**
> str check_zone(server_id, zone_id)

Verify zone contents/configuration.

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
    api_instance = pdns_admin_client.ZonesApi(api_client)
    server_id = 'server_id_example' # str | The id of the server to retrieve
    zone_id = 'zone_id_example' # str | The id of the zone to retrieve

    try:
        # Verify zone contents/configuration.
        api_response = api_instance.check_zone(server_id, zone_id)
        print("The response of ZonesApi->check_zone:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ZonesApi->check_zone: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The id of the server to retrieve | 
 **zone_id** | **str**| The id of the zone to retrieve | 

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_zone**
> Zone create_zone(server_id, zone_struct, rrsets=rrsets)

Creates a new domain, returns the Zone on creation.

### Example

* Api Key Authentication (APIKeyHeader):

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

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with pdns_admin_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pdns_admin_client.ZonesApi(api_client)
    server_id = 'server_id_example' # str | The id of the server to retrieve
    zone_struct = pdns_admin_client.Zone() # Zone | The zone struct to patch with
    rrsets = True # bool | “true” (default) or “false”, whether to include the “rrsets” in the response Zone object. (optional) (default to True)

    try:
        # Creates a new domain, returns the Zone on creation.
        api_response = api_instance.create_zone(server_id, zone_struct, rrsets=rrsets)
        print("The response of ZonesApi->create_zone:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ZonesApi->create_zone: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The id of the server to retrieve | 
 **zone_struct** | [**Zone**](Zone.md)| The zone struct to patch with | 
 **rrsets** | **bool**| “true” (default) or “false”, whether to include the “rrsets” in the response Zone object. | [optional] [default to True]

### Return type

[**Zone**](Zone.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | A zone |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_zone**
> delete_zone(server_id, zone_id)

Deletes this zone, all attached metadata and rrsets.

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
    api_instance = pdns_admin_client.ZonesApi(api_client)
    server_id = 'server_id_example' # str | The id of the server to retrieve
    zone_id = 'zone_id_example' # str | The id of the zone to retrieve

    try:
        # Deletes this zone, all attached metadata and rrsets.
        api_instance.delete_zone(server_id, zone_id)
    except Exception as e:
        print("Exception when calling ZonesApi->delete_zone: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The id of the server to retrieve | 
 **zone_id** | **str**| The id of the zone to retrieve | 

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
**204** | Returns 204 No Content on success. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_zone**
> Zone list_zone(server_id, zone_id)

zone managed by a server

### Example

* Api Key Authentication (APIKeyHeader):

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

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with pdns_admin_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pdns_admin_client.ZonesApi(api_client)
    server_id = 'server_id_example' # str | The id of the server to retrieve
    zone_id = 'zone_id_example' # str | The id of the zone to retrieve

    try:
        # zone managed by a server
        api_response = api_instance.list_zone(server_id, zone_id)
        print("The response of ZonesApi->list_zone:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ZonesApi->list_zone: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The id of the server to retrieve | 
 **zone_id** | **str**| The id of the zone to retrieve | 

### Return type

[**Zone**](Zone.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A Zone |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_zones**
> List[Zone] list_zones(server_id, zone=zone)

List all Zones in a server

### Example

* Api Key Authentication (APIKeyHeader):

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

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with pdns_admin_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pdns_admin_client.ZonesApi(api_client)
    server_id = 'server_id_example' # str | The id of the server to retrieve
    zone = 'zone_example' # str | When set to the name of a zone, only this zone is returned. If no zone with that name exists, the response is an empty array. This can e.g. be used to check if a zone exists in the database without having to guess/encode the zone's id or to check if a zone exists.  (optional)

    try:
        # List all Zones in a server
        api_response = api_instance.list_zones(server_id, zone=zone)
        print("The response of ZonesApi->list_zones:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ZonesApi->list_zones: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The id of the server to retrieve | 
 **zone** | **str**| When set to the name of a zone, only this zone is returned. If no zone with that name exists, the response is an empty array. This can e.g. be used to check if a zone exists in the database without having to guess/encode the zone&#39;s id or to check if a zone exists.  | [optional] 

### Return type

[**List[Zone]**](Zone.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of Zones |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notify_zone**
> notify_zone(server_id, zone_id)

Send a DNS NOTIFY to all slaves.

Fails when zone kind is not Master or Slave, or master and slave are disabled in the configuration. Only works for Slave if renotify is on. Clients MUST NOT send a body.

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
    api_instance = pdns_admin_client.ZonesApi(api_client)
    server_id = 'server_id_example' # str | The id of the server to retrieve
    zone_id = 'zone_id_example' # str | The id of the zone to retrieve

    try:
        # Send a DNS NOTIFY to all slaves.
        api_instance.notify_zone(server_id, zone_id)
    except Exception as e:
        print("Exception when calling ZonesApi->notify_zone: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The id of the server to retrieve | 
 **zone_id** | **str**| The id of the zone to retrieve | 

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_zone**
> patch_zone(server_id, zone_id, zone_struct)

Creates/modifies/deletes RRsets present in the payload and their comments. Returns 204 No Content on success.

### Example

* Api Key Authentication (APIKeyHeader):

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

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with pdns_admin_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pdns_admin_client.ZonesApi(api_client)
    server_id = 'server_id_example' # str | The id of the server to retrieve
    zone_id = 'zone_id_example' # str | 
    zone_struct = pdns_admin_client.Zone() # Zone | The zone struct to patch with

    try:
        # Creates/modifies/deletes RRsets present in the payload and their comments. Returns 204 No Content on success.
        api_instance.patch_zone(server_id, zone_id, zone_struct)
    except Exception as e:
        print("Exception when calling ZonesApi->patch_zone: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The id of the server to retrieve | 
 **zone_id** | **str**|  | 
 **zone_struct** | [**Zone**](Zone.md)| The zone struct to patch with | 

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Returns 204 No Content on success. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_zone**
> put_zone(server_id, zone_id, zone_struct)

Modifies basic zone data (metadata).

Allowed fields in client body: all except id, url and name. Returns 204 No Content on success.

### Example

* Api Key Authentication (APIKeyHeader):

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

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with pdns_admin_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pdns_admin_client.ZonesApi(api_client)
    server_id = 'server_id_example' # str | The id of the server to retrieve
    zone_id = 'zone_id_example' # str | 
    zone_struct = pdns_admin_client.Zone() # Zone | The zone struct to patch with

    try:
        # Modifies basic zone data (metadata).
        api_instance.put_zone(server_id, zone_id, zone_struct)
    except Exception as e:
        print("Exception when calling ZonesApi->put_zone: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The id of the server to retrieve | 
 **zone_id** | **str**|  | 
 **zone_struct** | [**Zone**](Zone.md)| The zone struct to patch with | 

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Returns 204 No Content on success. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rectify_zone**
> str rectify_zone(server_id, zone_id)

Rectify the zone data.

This does not take into account the API-RECTIFY metadata. Fails on slave zones and zones that do not have DNSSEC.

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
    api_instance = pdns_admin_client.ZonesApi(api_client)
    server_id = 'server_id_example' # str | The id of the server to retrieve
    zone_id = 'zone_id_example' # str | The id of the zone to retrieve

    try:
        # Rectify the zone data.
        api_response = api_instance.rectify_zone(server_id, zone_id)
        print("The response of ZonesApi->rectify_zone:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ZonesApi->rectify_zone: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The id of the server to retrieve | 
 **zone_id** | **str**| The id of the zone to retrieve | 

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

