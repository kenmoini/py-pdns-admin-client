# pdns_admin_client.AccountApi

All URIs are relative to *http://localhost:80/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_add_account_user**](AccountApi.md#api_add_account_user) | **PUT** /pdnsadmin/accounts/{account_id}/users/{user_id} | Link user to account
[**api_add_user_account**](AccountApi.md#api_add_user_account) | **PUT** /pdnsadmin/accounts/users/{account_id}/{user_id} | Link user to account
[**api_create_account**](AccountApi.md#api_create_account) | **POST** /pdnsadmin/accounts | Add an Account
[**api_list_account_users**](AccountApi.md#api_list_account_users) | **GET** /pdnsadmin/accounts/{account_id}/users | List users linked to a specific account
[**api_list_accounts**](AccountApi.md#api_list_accounts) | **GET** /pdnsadmin/accounts | Get all Account entries
[**api_list_users_account**](AccountApi.md#api_list_users_account) | **GET** /pdnsadmin/accounts/users/{account_id} | List users linked to a specific account
[**api_remove_account_user**](AccountApi.md#api_remove_account_user) | **DELETE** /pdnsadmin/accounts/{account_id}/users/{user_id} | Unlink user from account
[**api_remove_user_account**](AccountApi.md#api_remove_user_account) | **DELETE** /pdnsadmin/accounts/users/{account_id}/{user_id} | Unlink user from account


# **api_add_account_user**
> api_add_account_user(account_id, user_id)

Link user to account

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
    api_instance = pdns_admin_client.AccountApi(api_client)
    account_id = 56 # int | The id of the account to link/unlink users to account
    user_id = 56 # int | The id of the user to (un)link to/from account

    try:
        # Link user to account
        api_instance.api_add_account_user(account_id, user_id)
    except Exception as e:
        print("Exception when calling AccountApi->api_add_account_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| The id of the account to link/unlink users to account | 
 **user_id** | **int**| The id of the user to (un)link to/from account | 

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
**204** | OK. User is linked (empty response body) |  -  |
**400** | Request is not JSON |  -  |
**401** | Unauthorized |  -  |
**404** | Not found. The Account or User with the specified id does not exist |  -  |
**500** | Internal Server Error. Contains error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_add_user_account**
> api_add_user_account(account_id, user_id)

Link user to account

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
    api_instance = pdns_admin_client.AccountApi(api_client)
    account_id = 56 # int | The id of the account to link/unlink users to account
    user_id = 56 # int | The id of the user to (un)link to/from account

    try:
        # Link user to account
        api_instance.api_add_user_account(account_id, user_id)
    except Exception as e:
        print("Exception when calling AccountApi->api_add_user_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| The id of the account to link/unlink users to account | 
 **user_id** | **int**| The id of the user to (un)link to/from account | 

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
**204** | OK. User is linked (empty response body) |  -  |
**400** | Request is not JSON |  -  |
**401** | Unauthorized |  -  |
**404** | Not found. The Account or User with the specified id does not exist |  -  |
**500** | Internal Server Error. Contains error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_create_account**
> Account api_create_account(account=account)

Add an Account

This methods adds a new Account

### Example

* Basic Authentication (basicAuth):

```python
import pdns_admin_client
from pdns_admin_client.models.account import Account
from pdns_admin_client.models.api_create_account_request import ApiCreateAccountRequest
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
    api_instance = pdns_admin_client.AccountApi(api_client)
    account = pdns_admin_client.ApiCreateAccountRequest() # ApiCreateAccountRequest |  (optional)

    try:
        # Add an Account
        api_response = api_instance.api_create_account(account=account)
        print("The response of AccountApi->api_create_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->api_create_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | [**ApiCreateAccountRequest**](ApiCreateAccountRequest.md)|  | [optional] 

### Return type

[**Account**](Account.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Request is not JSON |  -  |
**401** | Unauthorized |  -  |
**409** | Duplicate Entry, the Name is already in use |  -  |
**500** | Internal Server Error. There was a problem creating the account |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_list_account_users**
> List[User] api_list_account_users(account_id)

List users linked to a specific account

### Example

* Basic Authentication (basicAuth):

```python
import pdns_admin_client
from pdns_admin_client.models.user import User
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
    api_instance = pdns_admin_client.AccountApi(api_client)
    account_id = 56 # int | The id of the account to list users linked to account

    try:
        # List users linked to a specific account
        api_response = api_instance.api_list_account_users(account_id)
        print("The response of AccountApi->api_list_account_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->api_list_account_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| The id of the account to list users linked to account | 

### Return type

[**List[User]**](User.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of Summarized User objects |  -  |
**401** | Unauthorized |  -  |
**404** | Not found. The Account with the specified account_id does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_list_accounts**
> List[Account] api_list_accounts()

Get all Account entries

### Example

* Basic Authentication (basicAuth):

```python
import pdns_admin_client
from pdns_admin_client.models.account import Account
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
    api_instance = pdns_admin_client.AccountApi(api_client)

    try:
        # Get all Account entries
        api_response = api_instance.api_list_accounts()
        print("The response of AccountApi->api_list_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->api_list_accounts: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Account]**](Account.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of Account objects |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_list_users_account**
> List[User] api_list_users_account(account_id)

List users linked to a specific account

### Example

* Basic Authentication (basicAuth):

```python
import pdns_admin_client
from pdns_admin_client.models.user import User
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
    api_instance = pdns_admin_client.AccountApi(api_client)
    account_id = 56 # int | The id of the account to list users linked to account

    try:
        # List users linked to a specific account
        api_response = api_instance.api_list_users_account(account_id)
        print("The response of AccountApi->api_list_users_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->api_list_users_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| The id of the account to list users linked to account | 

### Return type

[**List[User]**](User.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of Summarized User objects |  -  |
**401** | Unauthorized |  -  |
**404** | Not found. The Account with the specified account_id does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_remove_account_user**
> api_remove_account_user(account_id, user_id)

Unlink user from account

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
    api_instance = pdns_admin_client.AccountApi(api_client)
    account_id = 56 # int | The id of the account to link/unlink users to account
    user_id = 56 # int | The id of the user to (un)link to/from account

    try:
        # Unlink user from account
        api_instance.api_remove_account_user(account_id, user_id)
    except Exception as e:
        print("Exception when calling AccountApi->api_remove_account_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| The id of the account to link/unlink users to account | 
 **user_id** | **int**| The id of the user to (un)link to/from account | 

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
**204** | OK. User is unlinked (empty response body) |  -  |
**401** | Unauthorized |  -  |
**404** | Not found. The Account or User with the specified id does not exist or user was not linked to account |  -  |
**500** | Internal Server Error. Contains error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_remove_user_account**
> api_remove_user_account(account_id, user_id)

Unlink user from account

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
    api_instance = pdns_admin_client.AccountApi(api_client)
    account_id = 56 # int | The id of the account to link/unlink users to account
    user_id = 56 # int | The id of the user to (un)link to/from account

    try:
        # Unlink user from account
        api_instance.api_remove_user_account(account_id, user_id)
    except Exception as e:
        print("Exception when calling AccountApi->api_remove_user_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| The id of the account to link/unlink users to account | 
 **user_id** | **int**| The id of the user to (un)link to/from account | 

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
**204** | OK. User is unlinked (empty response body) |  -  |
**401** | Unauthorized |  -  |
**404** | Not found. The Account or User with the specified id does not exist or user was not linked to account |  -  |
**500** | Internal Server Error. Contains error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

