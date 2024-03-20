# ApiKey

An ApiKey that can be used to manage domains through API

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID for this key, used in the ApiKey URL endpoint. | [optional] [readonly] 
**plain_key** | **str** | ApiKey key is return in plain text only at first POST | [optional] 
**key** | **str** | not used on POST, POSTing to server generates the key material | [optional] 
**domains** | [**List[PDNSAdminZonesInner]**](PDNSAdminZonesInner.md) | A list of domains | [optional] 
**role** | [**PDNSAdminRole**](PDNSAdminRole.md) |  | [optional] 
**description** | **str** | Some user defined description | [optional] 
**accounts** | [**List[AccountSummary]**](AccountSummary.md) | A list of accounts bound to this ApiKey | [optional] 

## Example

```python
from pdns_admin_client.models.api_key import ApiKey

# TODO update the JSON string below
json = "{}"
# create an instance of ApiKey from a JSON string
api_key_instance = ApiKey.from_json(json)
# print the JSON string representation of the object
print(ApiKey.to_json())

# convert the object into a dict
api_key_dict = api_key_instance.to_dict()
# create an instance of ApiKey from a dict
api_key_form_dict = api_key.from_dict(api_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


