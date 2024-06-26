# pdns-admin-client

---

## WARNING!!!1

> This is literally just `openapi-generator generate -i swagger-spec.yaml -g python --package-name pdns_admin_client -o client`

This is pretty much just for testing purposes, *maybe*.  If it doesn't work then blame the generator or the OpenAPI spec, I have no interest in maintaining a shim of sorts.

---

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 0.0.14
- Package version: 1.0.0
- Generator version: 7.4.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/kenmoini/py-pdns-admin-client.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/kenmoini/py-pdns-admin-client.git`)

Then import the package:
```python
import pdns_admin_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import pdns_admin_client
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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
    except ApiException as e:
        print("Exception when calling MonitoringApi->health_check: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost:80/api/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*MonitoringApi* | [**health_check**](docs/MonitoringApi.md#health_check) | **GET** /servers/{server_id}/health | Perfoms health check
*AccountApi* | [**api_add_account_user**](docs/AccountApi.md#api_add_account_user) | **PUT** /pdnsadmin/accounts/{account_id}/users/{user_id} | Link user to account
*AccountApi* | [**api_add_user_account**](docs/AccountApi.md#api_add_user_account) | **PUT** /pdnsadmin/accounts/users/{account_id}/{user_id} | Link user to account
*AccountApi* | [**api_create_account**](docs/AccountApi.md#api_create_account) | **POST** /pdnsadmin/accounts | Add an Account
*AccountApi* | [**api_list_account_users**](docs/AccountApi.md#api_list_account_users) | **GET** /pdnsadmin/accounts/{account_id}/users | List users linked to a specific account
*AccountApi* | [**api_list_accounts**](docs/AccountApi.md#api_list_accounts) | **GET** /pdnsadmin/accounts | Get all Account entries
*AccountApi* | [**api_list_users_account**](docs/AccountApi.md#api_list_users_account) | **GET** /pdnsadmin/accounts/users/{account_id} | List users linked to a specific account
*AccountApi* | [**api_remove_account_user**](docs/AccountApi.md#api_remove_account_user) | **DELETE** /pdnsadmin/accounts/{account_id}/users/{user_id} | Unlink user from account
*AccountApi* | [**api_remove_user_account**](docs/AccountApi.md#api_remove_user_account) | **DELETE** /pdnsadmin/accounts/users/{account_id}/{user_id} | Unlink user from account
*ApikeyApi* | [**api_delete_apikey**](docs/ApikeyApi.md#api_delete_apikey) | **DELETE** /pdnsadmin/apikeys/{apikey_id} | Delete the ApiKey with apikey_id
*ApikeyApi* | [**api_generate_apikey**](docs/ApikeyApi.md#api_generate_apikey) | **POST** /pdnsadmin/apikeys | Add a ApiKey key
*ApikeyApi* | [**api_get_apikey_by_id**](docs/ApikeyApi.md#api_get_apikey_by_id) | **GET** /pdnsadmin/apikeys/{apikey_id} | Get a specific apikey on the server, hashed
*ApikeyApi* | [**api_get_apikeys**](docs/ApikeyApi.md#api_get_apikeys) | **GET** /pdnsadmin/apikeys | Get all ApiKey on the server, except the actual key
*ApikeyApi* | [**api_update_apikey**](docs/ApikeyApi.md#api_update_apikey) | **PUT** /pdnsadmin/apikeys/{apikey_id} | 
*ConfigApi* | [**get_config**](docs/ConfigApi.md#get_config) | **GET** /servers/{server_id}/config | Returns all ConfigSettings for a single server
*ConfigApi* | [**get_config_setting**](docs/ConfigApi.md#get_config_setting) | **GET** /servers/{server_id}/config/{config_setting_name} | Returns a specific ConfigSetting for a single server
*PdnsadminZonesApi* | [**api_login_create_zone**](docs/PdnsadminZonesApi.md#api_login_create_zone) | **POST** /pdnsadmin/zones | Creates a new domain, returns the Zone on creation.
*PdnsadminZonesApi* | [**api_login_delete_zone**](docs/PdnsadminZonesApi.md#api_login_delete_zone) | **DELETE** /pdnsadmin/zones/{zone_id} | Deletes this zone, all attached metadata and rrsets.
*PdnsadminZonesApi* | [**api_login_list_zones**](docs/PdnsadminZonesApi.md#api_login_list_zones) | **GET** /pdnsadmin/zones | List all Zones in a server
*PdnsadminZonesApi* | [**synchronize_domains**](docs/PdnsadminZonesApi.md#synchronize_domains) | **GET** /sync_domains | Sync PDNS with PDNSAdmin
*SearchApi* | [**search_data**](docs/SearchApi.md#search_data) | **GET** /servers/{server_id}/search-data | Search the data inside PowerDNS
*ServersApi* | [**cache_flush_by_name**](docs/ServersApi.md#cache_flush_by_name) | **PUT** /servers/{server_id}/cache/flush | Flush a cache-entry by name
*ServersApi* | [**list_server**](docs/ServersApi.md#list_server) | **GET** /servers/{server_id} | List a server
*ServersApi* | [**list_servers**](docs/ServersApi.md#list_servers) | **GET** /servers | List all servers
*StatsApi* | [**get_stats**](docs/StatsApi.md#get_stats) | **GET** /servers/{server_id}/statistics | Query statistics.
*UserApi* | [**api_add_account_user**](docs/UserApi.md#api_add_account_user) | **PUT** /pdnsadmin/accounts/{account_id}/users/{user_id} | Link user to account
*UserApi* | [**api_add_user_account**](docs/UserApi.md#api_add_user_account) | **PUT** /pdnsadmin/accounts/users/{account_id}/{user_id} | Link user to account
*UserApi* | [**api_create_user**](docs/UserApi.md#api_create_user) | **POST** /pdnsadmin/users | Add a User
*UserApi* | [**api_delete_account**](docs/UserApi.md#api_delete_account) | **DELETE** /pdnsadmin/accounts/{account_id} | Delete a specific Account
*UserApi* | [**api_delete_user**](docs/UserApi.md#api_delete_user) | **DELETE** /pdnsadmin/users/{user_id} | Delete a specific User
*UserApi* | [**api_get_account_by_name**](docs/UserApi.md#api_get_account_by_name) | **GET** /pdnsadmin/accounts/{account_name} | Get a specific Account on the server
*UserApi* | [**api_get_user**](docs/UserApi.md#api_get_user) | **GET** /pdnsadmin/users/{username} | Get a specific User on the server
*UserApi* | [**api_list_account_users**](docs/UserApi.md#api_list_account_users) | **GET** /pdnsadmin/accounts/{account_id}/users | List users linked to a specific account
*UserApi* | [**api_list_users**](docs/UserApi.md#api_list_users) | **GET** /pdnsadmin/users | Get all User entries
*UserApi* | [**api_list_users_account**](docs/UserApi.md#api_list_users_account) | **GET** /pdnsadmin/accounts/users/{account_id} | List users linked to a specific account
*UserApi* | [**api_remove_account_user**](docs/UserApi.md#api_remove_account_user) | **DELETE** /pdnsadmin/accounts/{account_id}/users/{user_id} | Unlink user from account
*UserApi* | [**api_remove_user_account**](docs/UserApi.md#api_remove_user_account) | **DELETE** /pdnsadmin/accounts/users/{account_id}/{user_id} | Unlink user from account
*UserApi* | [**api_update_account**](docs/UserApi.md#api_update_account) | **PUT** /pdnsadmin/accounts/{account_id} | Modify a specific Account on the server with supplied parameters
*UserApi* | [**api_update_user**](docs/UserApi.md#api_update_user) | **PUT** /pdnsadmin/users/{user_id} | Modify a specific User on the server with supplied parameters
*ZonecryptokeyApi* | [**create_cryptokey**](docs/ZonecryptokeyApi.md#create_cryptokey) | **POST** /servers/{server_id}/zones/{zone_id}/cryptokeys | Creates a Cryptokey
*ZonecryptokeyApi* | [**delete_cryptokey**](docs/ZonecryptokeyApi.md#delete_cryptokey) | **DELETE** /servers/{server_id}/zones/{zone_id}/cryptokeys/{cryptokey_id} | This method deletes a key specified by cryptokey_id.
*ZonecryptokeyApi* | [**get_cryptokey**](docs/ZonecryptokeyApi.md#get_cryptokey) | **GET** /servers/{server_id}/zones/{zone_id}/cryptokeys/{cryptokey_id} | Returns all data about the CryptoKey, including the privatekey.
*ZonecryptokeyApi* | [**list_cryptokeys**](docs/ZonecryptokeyApi.md#list_cryptokeys) | **GET** /servers/{server_id}/zones/{zone_id}/cryptokeys | Get all CryptoKeys for a zone, except the privatekey
*ZonecryptokeyApi* | [**modify_cryptokey**](docs/ZonecryptokeyApi.md#modify_cryptokey) | **PUT** /servers/{server_id}/zones/{zone_id}/cryptokeys/{cryptokey_id} | This method (de)activates a key from zone_name specified by cryptokey_id
*ZonemetadataApi* | [**create_metadata**](docs/ZonemetadataApi.md#create_metadata) | **POST** /servers/{server_id}/zones/{zone_id}/metadata | Creates a set of metadata entries
*ZonemetadataApi* | [**delete_metadata**](docs/ZonemetadataApi.md#delete_metadata) | **DELETE** /servers/{server_id}/zones/{zone_id}/metadata/{metadata_kind} | Delete all items of a single kind of domain metadata.
*ZonemetadataApi* | [**get_metadata**](docs/ZonemetadataApi.md#get_metadata) | **GET** /servers/{server_id}/zones/{zone_id}/metadata/{metadata_kind} | Get the content of a single kind of domain metadata as a list of MetaData objects.
*ZonemetadataApi* | [**list_metadata**](docs/ZonemetadataApi.md#list_metadata) | **GET** /servers/{server_id}/zones/{zone_id}/metadata | Get all the MetaData associated with the zone.
*ZonemetadataApi* | [**modify_metadata**](docs/ZonemetadataApi.md#modify_metadata) | **PUT** /servers/{server_id}/zones/{zone_id}/metadata/{metadata_kind} | Modify the content of a single kind of domain metadata.
*ZonesApi* | [**axfr_export_zone**](docs/ZonesApi.md#axfr_export_zone) | **GET** /servers/{server_id}/zones/{zone_id}/export | Returns the zone in AXFR format.
*ZonesApi* | [**axfr_retrieve_zone**](docs/ZonesApi.md#axfr_retrieve_zone) | **PUT** /servers/{server_id}/zones/{zone_id}/axfr-retrieve | Retrieve slave zone from its master.
*ZonesApi* | [**check_zone**](docs/ZonesApi.md#check_zone) | **GET** /servers/{server_id}/zones/{zone_id}/check | Verify zone contents/configuration.
*ZonesApi* | [**create_zone**](docs/ZonesApi.md#create_zone) | **POST** /servers/{server_id}/zones | Creates a new domain, returns the Zone on creation.
*ZonesApi* | [**delete_zone**](docs/ZonesApi.md#delete_zone) | **DELETE** /servers/{server_id}/zones/{zone_id} | Deletes this zone, all attached metadata and rrsets.
*ZonesApi* | [**list_zone**](docs/ZonesApi.md#list_zone) | **GET** /servers/{server_id}/zones/{zone_id} | zone managed by a server
*ZonesApi* | [**list_zones**](docs/ZonesApi.md#list_zones) | **GET** /servers/{server_id}/zones | List all Zones in a server
*ZonesApi* | [**notify_zone**](docs/ZonesApi.md#notify_zone) | **PUT** /servers/{server_id}/zones/{zone_id}/notify | Send a DNS NOTIFY to all slaves.
*ZonesApi* | [**patch_zone**](docs/ZonesApi.md#patch_zone) | **PATCH** /servers/{server_id}/zones/{zone_id} | Creates/modifies/deletes RRsets present in the payload and their comments. Returns 204 No Content on success.
*ZonesApi* | [**put_zone**](docs/ZonesApi.md#put_zone) | **PUT** /servers/{server_id}/zones/{zone_id} | Modifies basic zone data (metadata).
*ZonesApi* | [**rectify_zone**](docs/ZonesApi.md#rectify_zone) | **PUT** /servers/{server_id}/zones/{zone_id}/rectify | Rectify the zone data.


## Documentation For Models

 - [Account](docs/Account.md)
 - [AccountSummary](docs/AccountSummary.md)
 - [ApiCreateAccountRequest](docs/ApiCreateAccountRequest.md)
 - [ApiCreateUserRequest](docs/ApiCreateUserRequest.md)
 - [ApiKey](docs/ApiKey.md)
 - [ApiKeySummary](docs/ApiKeySummary.md)
 - [ApiUpdateUserRequest](docs/ApiUpdateUserRequest.md)
 - [BaseStatisticItem](docs/BaseStatisticItem.md)
 - [CacheFlushResult](docs/CacheFlushResult.md)
 - [Comment](docs/Comment.md)
 - [ConfigSetting](docs/ConfigSetting.md)
 - [Cryptokey](docs/Cryptokey.md)
 - [Error](docs/Error.md)
 - [MapStatisticItem](docs/MapStatisticItem.md)
 - [MapStatisticItemAllOfValue](docs/MapStatisticItemAllOfValue.md)
 - [Metadata](docs/Metadata.md)
 - [PDNSAdminRole](docs/PDNSAdminRole.md)
 - [PDNSAdminZonesInner](docs/PDNSAdminZonesInner.md)
 - [RRSet](docs/RRSet.md)
 - [Record](docs/Record.md)
 - [RingStatisticItem](docs/RingStatisticItem.md)
 - [SearchResult](docs/SearchResult.md)
 - [SearchResultComment](docs/SearchResultComment.md)
 - [SearchResultRecord](docs/SearchResultRecord.md)
 - [SearchResultZone](docs/SearchResultZone.md)
 - [Server](docs/Server.md)
 - [StatisticItem](docs/StatisticItem.md)
 - [TSIGKey](docs/TSIGKey.md)
 - [User](docs/User.md)
 - [UserDetailed](docs/UserDetailed.md)
 - [Zone](docs/Zone.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="APIKeyHeader"></a>
### APIKeyHeader

- **Type**: API key
- **API key parameter name**: X-API-Key
- **Location**: HTTP header

<a id="basicAuth"></a>
### basicAuth

- **Type**: HTTP basic authentication


## Author




