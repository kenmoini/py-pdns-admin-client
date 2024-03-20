# pdns_admin_client.UserApi

All URIs are relative to *http://localhost:80/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_add_account_user**](UserApi.md#api_add_account_user) | **PUT** /pdnsadmin/accounts/{account_id}/users/{user_id} | Link user to account
[**api_add_user_account**](UserApi.md#api_add_user_account) | **PUT** /pdnsadmin/accounts/users/{account_id}/{user_id} | Link user to account
[**api_create_user**](UserApi.md#api_create_user) | **POST** /pdnsadmin/users | Add a User
[**api_delete_account**](UserApi.md#api_delete_account) | **DELETE** /pdnsadmin/accounts/{account_id} | Delete a specific Account
[**api_delete_user**](UserApi.md#api_delete_user) | **DELETE** /pdnsadmin/users/{user_id} | Delete a specific User
[**api_get_account_by_name**](UserApi.md#api_get_account_by_name) | **GET** /pdnsadmin/accounts/{account_name} | Get a specific Account on the server
[**api_get_user**](UserApi.md#api_get_user) | **GET** /pdnsadmin/users/{username} | Get a specific User on the server
[**api_list_account_users**](UserApi.md#api_list_account_users) | **GET** /pdnsadmin/accounts/{account_id}/users | List users linked to a specific account
[**api_list_users**](UserApi.md#api_list_users) | **GET** /pdnsadmin/users | Get all User entries
[**api_list_users_account**](UserApi.md#api_list_users_account) | **GET** /pdnsadmin/accounts/users/{account_id} | List users linked to a specific account
[**api_remove_account_user**](UserApi.md#api_remove_account_user) | **DELETE** /pdnsadmin/accounts/{account_id}/users/{user_id} | Unlink user from account
[**api_remove_user_account**](UserApi.md#api_remove_user_account) | **DELETE** /pdnsadmin/accounts/users/{account_id}/{user_id} | Unlink user from account
[**api_update_account**](UserApi.md#api_update_account) | **PUT** /pdnsadmin/accounts/{account_id} | Modify a specific Account on the server with supplied parameters
[**api_update_user**](UserApi.md#api_update_user) | **PUT** /pdnsadmin/users/{user_id} | Modify a specific User on the server with supplied parameters


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
    api_instance = pdns_admin_client.UserApi(api_client)
    account_id = 56 # int | The id of the account to link/unlink users to account
    user_id = 56 # int | The id of the user to (un)link to/from account

    try:
        # Link user to account
        api_instance.api_add_account_user(account_id, user_id)
    except Exception as e:
        print("Exception when calling UserApi->api_add_account_user: %s\n" % e)
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
    api_instance = pdns_admin_client.UserApi(api_client)
    account_id = 56 # int | The id of the account to link/unlink users to account
    user_id = 56 # int | The id of the user to (un)link to/from account

    try:
        # Link user to account
        api_instance.api_add_user_account(account_id, user_id)
    except Exception as e:
        print("Exception when calling UserApi->api_add_user_account: %s\n" % e)
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

# **api_create_user**
> User api_create_user(user=user)

Add a User

This methods adds a new User

### Example

* Basic Authentication (basicAuth):

```python
import pdns_admin_client
from pdns_admin_client.models.api_create_user_request import ApiCreateUserRequest
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
    api_instance = pdns_admin_client.UserApi(api_client)
    user = pdns_admin_client.ApiCreateUserRequest() # ApiCreateUserRequest | The user to create (optional)

    try:
        # Add a User
        api_response = api_instance.api_create_user(user=user)
        print("The response of UserApi->api_create_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->api_create_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | [**ApiCreateUserRequest**](ApiCreateUserRequest.md)| The user to create | [optional] 

### Return type

[**User**](User.md)

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
**409** | Duplicate Entry, either the Name or the Email is already in use |  -  |
**500** | Internal Server Error. There was a problem creating the user |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_delete_account**
> api_delete_account(account_id)

Delete a specific Account

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
    api_instance = pdns_admin_client.UserApi(api_client)
    account_id = 56 # int | The id of the account to modify or delete

    try:
        # Delete a specific Account
        api_instance.api_delete_account(account_id)
    except Exception as e:
        print("Exception when calling UserApi->api_delete_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| The id of the account to modify or delete | 

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
**204** | OK. Account is deleted (empty response body) |  -  |
**401** | Unauthorized |  -  |
**404** | Not found. The Account with the specified account_id does not exist |  -  |
**500** | Internal Server Error. Contains error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_delete_user**
> api_delete_user(user_id)

Delete a specific User

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
    api_instance = pdns_admin_client.UserApi(api_client)
    user_id = 56 # int | The id of the user to modify or delete

    try:
        # Delete a specific User
        api_instance.api_delete_user(user_id)
    except Exception as e:
        print("Exception when calling UserApi->api_delete_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| The id of the user to modify or delete | 

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
**204** | OK. User is deleted (empty response body) |  -  |
**401** | Unauthorized |  -  |
**404** | Not found. The User with the specified user_id does not exist |  -  |
**500** | Internal Server Error. Contains error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_get_account_by_name**
> Account api_get_account_by_name(account_name)

Get a specific Account on the server

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
    api_instance = pdns_admin_client.UserApi(api_client)
    account_name = 'account_name_example' # str | The name of the account to retrieve

    try:
        # Get a specific Account on the server
        api_response = api_instance.api_get_account_by_name(account_name)
        print("The response of UserApi->api_get_account_by_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->api_get_account_by_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_name** | **str**| The name of the account to retrieve | 

### Return type

[**Account**](Account.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retrieve a specific account |  -  |
**401** | Unauthorized |  -  |
**404** | Not found. The Account with the specified name does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_get_user**
> UserDetailed api_get_user(username)

Get a specific User on the server

### Example

* Basic Authentication (basicAuth):

```python
import pdns_admin_client
from pdns_admin_client.models.user_detailed import UserDetailed
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
    api_instance = pdns_admin_client.UserApi(api_client)
    username = 'username_example' # str | The username of the user to retrieve

    try:
        # Get a specific User on the server
        api_response = api_instance.api_get_user(username)
        print("The response of UserApi->api_get_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->api_get_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The username of the user to retrieve | 

### Return type

[**UserDetailed**](UserDetailed.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retrieve a specific User |  -  |
**401** | Unauthorized |  -  |
**404** | Not found. The User with the specified username does not exist |  -  |
**500** | Internal Server Error, user could not be retrieved. Contains error message |  -  |

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
    api_instance = pdns_admin_client.UserApi(api_client)
    account_id = 56 # int | The id of the account to list users linked to account

    try:
        # List users linked to a specific account
        api_response = api_instance.api_list_account_users(account_id)
        print("The response of UserApi->api_list_account_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->api_list_account_users: %s\n" % e)
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

# **api_list_users**
> List[User] api_list_users()

Get all User entries

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
    api_instance = pdns_admin_client.UserApi(api_client)

    try:
        # Get all User entries
        api_response = api_instance.api_list_users()
        print("The response of UserApi->api_list_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->api_list_users: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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
**200** | List of User objects |  -  |
**401** | Unauthorized |  -  |
**500** | Internal Server Error, users could not be retrieved. Contains error message |  -  |

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
    api_instance = pdns_admin_client.UserApi(api_client)
    account_id = 56 # int | The id of the account to list users linked to account

    try:
        # List users linked to a specific account
        api_response = api_instance.api_list_users_account(account_id)
        print("The response of UserApi->api_list_users_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->api_list_users_account: %s\n" % e)
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
    api_instance = pdns_admin_client.UserApi(api_client)
    account_id = 56 # int | The id of the account to link/unlink users to account
    user_id = 56 # int | The id of the user to (un)link to/from account

    try:
        # Unlink user from account
        api_instance.api_remove_account_user(account_id, user_id)
    except Exception as e:
        print("Exception when calling UserApi->api_remove_account_user: %s\n" % e)
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
    api_instance = pdns_admin_client.UserApi(api_client)
    account_id = 56 # int | The id of the account to link/unlink users to account
    user_id = 56 # int | The id of the user to (un)link to/from account

    try:
        # Unlink user from account
        api_instance.api_remove_user_account(account_id, user_id)
    except Exception as e:
        print("Exception when calling UserApi->api_remove_user_account: %s\n" % e)
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

# **api_update_account**
> api_update_account(account_id, account=account)

Modify a specific Account on the server with supplied parameters

### Example

* Basic Authentication (basicAuth):

```python
import pdns_admin_client
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
    api_instance = pdns_admin_client.UserApi(api_client)
    account_id = 56 # int | The id of the account to modify or delete
    account = pdns_admin_client.ApiCreateAccountRequest() # ApiCreateAccountRequest |  (optional)

    try:
        # Modify a specific Account on the server with supplied parameters
        api_instance.api_update_account(account_id, account=account)
    except Exception as e:
        print("Exception when calling UserApi->api_update_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| The id of the account to modify or delete | 
 **account** | [**ApiCreateAccountRequest**](ApiCreateAccountRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | OK. Account is modified (empty response body) |  -  |
**400** | Request is not JSON |  -  |
**401** | Unauthorized |  -  |
**404** | Not found. The Account with the specified account_id does not exist |  -  |
**500** | Internal Server Error. Contains error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_update_user**
> api_update_user(user_id, user=user)

Modify a specific User on the server with supplied parameters

### Example

* Basic Authentication (basicAuth):

```python
import pdns_admin_client
from pdns_admin_client.models.api_update_user_request import ApiUpdateUserRequest
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
    api_instance = pdns_admin_client.UserApi(api_client)
    user_id = 56 # int | The id of the user to modify or delete
    user = pdns_admin_client.ApiUpdateUserRequest() # ApiUpdateUserRequest |  (optional)

    try:
        # Modify a specific User on the server with supplied parameters
        api_instance.api_update_user(user_id, user=user)
    except Exception as e:
        print("Exception when calling UserApi->api_update_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| The id of the user to modify or delete | 
 **user** | [**ApiUpdateUserRequest**](ApiUpdateUserRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | OK. User is modified (empty response body) |  -  |
**400** | Request is not JSON |  -  |
**401** | Unauthorized |  -  |
**404** | Not found. The User with the specified user_id does not exist |  -  |
**409** | Duplicate (Email already assigned to another user) |  -  |
**500** | Internal Server Error. Contains error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

