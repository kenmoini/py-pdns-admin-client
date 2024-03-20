# pdns_admin_client.ApikeyApi

All URIs are relative to *http://localhost:80/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_delete_apikey**](ApikeyApi.md#api_delete_apikey) | **DELETE** /pdnsadmin/apikeys/{apikey_id} | Delete the ApiKey with apikey_id
[**api_generate_apikey**](ApikeyApi.md#api_generate_apikey) | **POST** /pdnsadmin/apikeys | Add a ApiKey key
[**api_get_apikey_by_id**](ApikeyApi.md#api_get_apikey_by_id) | **GET** /pdnsadmin/apikeys/{apikey_id} | Get a specific apikey on the server, hashed
[**api_get_apikeys**](ApikeyApi.md#api_get_apikeys) | **GET** /pdnsadmin/apikeys | Get all ApiKey on the server, except the actual key
[**api_update_apikey**](ApikeyApi.md#api_update_apikey) | **PUT** /pdnsadmin/apikeys/{apikey_id} | 


# **api_delete_apikey**
> api_delete_apikey(apikey_id)

Delete the ApiKey with apikey_id

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
    api_instance = pdns_admin_client.ApikeyApi(api_client)
    apikey_id = 56 # int | The id of the apikey to retrieve

    try:
        # Delete the ApiKey with apikey_id
        api_instance.api_delete_apikey(apikey_id)
    except Exception as e:
        print("Exception when calling ApikeyApi->api_delete_apikey: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apikey_id** | **int**| The id of the apikey to retrieve | 

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
**204** | OK, key was deleted |  -  |
**401** | Unauthorized |  -  |
**403** | The authenticated user has User role and is not allowed on any of the domains assigned to the key |  -  |
**404** | Not found. The ApiKey with the specified apikey_id does not exist |  -  |
**500** | Internal Server Error. Contains error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_generate_apikey**
> ApiKey api_generate_apikey(apikey)

Add a ApiKey key

This methods add a new ApiKey. The actual key is generated by the server

### Example

* Basic Authentication (basicAuth):

```python
import pdns_admin_client
from pdns_admin_client.models.api_key import ApiKey
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
    api_instance = pdns_admin_client.ApikeyApi(api_client)
    apikey = pdns_admin_client.ApiKey() # ApiKey | The ApiKey to add

    try:
        # Add a ApiKey key
        api_response = api_instance.api_generate_apikey(apikey)
        print("The response of ApikeyApi->api_generate_apikey:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApikeyApi->api_generate_apikey: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apikey** | [**ApiKey**](ApiKey.md)| The ApiKey to add | 

### Return type

[**ApiKey**](ApiKey.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Request is not JSON or does not respect required format |  -  |
**401** | Unauthorized |  -  |
**403** | Domain Access Forbidden |  -  |
**404** | Domain or Account Not found |  -  |
**500** | Internal Server Error. There was a problem creating the key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_get_apikey_by_id**
> ApiKey api_get_apikey_by_id(apikey_id)

Get a specific apikey on the server, hashed

### Example

* Basic Authentication (basicAuth):

```python
import pdns_admin_client
from pdns_admin_client.models.api_key import ApiKey
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
    api_instance = pdns_admin_client.ApikeyApi(api_client)
    apikey_id = 56 # int | The id of the apikey to retrieve

    try:
        # Get a specific apikey on the server, hashed
        api_response = api_instance.api_get_apikey_by_id(apikey_id)
        print("The response of ApikeyApi->api_get_apikey_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApikeyApi->api_get_apikey_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apikey_id** | **int**| The id of the apikey to retrieve | 

### Return type

[**ApiKey**](ApiKey.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK. |  -  |
**401** | Unauthorized |  -  |
**403** | The authenticated user has User role and is not allowed on any of the domains assigned to the key |  -  |
**404** | Not found. The ApiKey with the specified apikey_id does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_get_apikeys**
> List[ApiKey] api_get_apikeys()

Get all ApiKey on the server, except the actual key

### Example

* Basic Authentication (basicAuth):

```python
import pdns_admin_client
from pdns_admin_client.models.api_key import ApiKey
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
    api_instance = pdns_admin_client.ApikeyApi(api_client)

    try:
        # Get all ApiKey on the server, except the actual key
        api_response = api_instance.api_get_apikeys()
        print("The response of ApikeyApi->api_get_apikeys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApikeyApi->api_get_apikeys: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ApiKey]**](ApiKey.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of ApiKey objects |  -  |
**401** | Unauthorized |  -  |
**403** | Domain Access Forbidden |  -  |
**500** | Internal Server Error. There was a problem creating the key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_update_apikey**
> ApiKey api_update_apikey(apikey_id, apikey)



The ApiKey at apikey_id can be changed in multiple ways:  * Role, description, accounts and domains can be updated  * Role can be changed to Administrator only if user has Operator or Administrator privileges  * Domains will be updated only if user has access to them  * Accounts can be updated only by a privileged user  * With a User role, an ApiKey needs at least one account or one domain Only the relevant fields have to be provided in the request body. 

### Example

* Basic Authentication (basicAuth):

```python
import pdns_admin_client
from pdns_admin_client.models.api_key import ApiKey
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
    api_instance = pdns_admin_client.ApikeyApi(api_client)
    apikey_id = 56 # int | The id of the apikey to retrieve
    apikey = pdns_admin_client.ApiKey() # ApiKey | ApiKey object with the new values

    try:
        api_response = api_instance.api_update_apikey(apikey_id, apikey)
        print("The response of ApikeyApi->api_update_apikey:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApikeyApi->api_update_apikey: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apikey_id** | **int**| The id of the apikey to retrieve | 
 **apikey** | [**ApiKey**](ApiKey.md)| ApiKey object with the new values | 

### Return type

[**ApiKey**](ApiKey.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | OK. ApiKey is changed. |  -  |
**400** | Request is not JSON |  -  |
**401** | Unauthorized |  -  |
**403** | Domain Access Forbidden |  -  |
**404** | Not found (ApiKey, Domain or Account) |  -  |
**500** | Internal Server Error. Contains error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
