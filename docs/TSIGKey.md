# TSIGKey

A TSIG key that can be used to authenticate NOTIFYs and AXFRs

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the key | [optional] 
**id** | **str** | The ID for this key, used in the TSIGkey URL endpoint. | [optional] [readonly] 
**algorithm** | **str** | The algorithm of the TSIG key | [optional] 
**key** | **str** | The Base64 encoded secret key, empty when listing keys. MAY be empty when POSTing to have the server generate the key material | [optional] 
**type** | **str** | Set to \&quot;TSIGKey\&quot; | [optional] [readonly] 

## Example

```python
from pdns_admin_client.models.tsig_key import TSIGKey

# TODO update the JSON string below
json = "{}"
# create an instance of TSIGKey from a JSON string
tsig_key_instance = TSIGKey.from_json(json)
# print the JSON string representation of the object
print(TSIGKey.to_json())

# convert the object into a dict
tsig_key_dict = tsig_key_instance.to_dict()
# create an instance of TSIGKey from a dict
tsig_key_form_dict = tsig_key.from_dict(tsig_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


