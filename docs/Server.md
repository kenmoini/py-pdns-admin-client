# Server


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Set to “Server” | [optional] 
**id** | **str** | The id of the server, “localhost” | [optional] 
**daemon_type** | **str** | “recursor” for the PowerDNS Recursor and “authoritative” for the Authoritative Server | [optional] 
**version** | **str** | The version of the server software | [optional] 
**url** | **str** | The API endpoint for this server | [optional] 
**config_url** | **str** | The API endpoint for this server’s configuration | [optional] 
**zones_url** | **str** | The API endpoint for this server’s zones | [optional] 

## Example

```python
from pdns_admin_client.models.server import Server

# TODO update the JSON string below
json = "{}"
# create an instance of Server from a JSON string
server_instance = Server.from_json(json)
# print the JSON string representation of the object
print(Server.to_json())

# convert the object into a dict
server_dict = server_instance.to_dict()
# create an instance of Server from a dict
server_form_dict = server.from_dict(server_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


