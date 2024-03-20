# Cryptokey

Describes a DNSSEC cryptographic key

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | set to \&quot;Cryptokey\&quot; | [optional] 
**id** | **str** | The internal identifier, read only | [optional] 
**keytype** | **str** |  | [optional] 
**active** | **bool** | Whether or not the key is in active use | [optional] 
**dnskey** | **str** | The DNSKEY record for this key | [optional] 
**ds** | **List[str]** | An array of DS records for this key | [optional] 
**privatekey** | **str** | The private key in ISC format | [optional] 
**algorithm** | **str** | The name of the algorithm of the key, should be a mnemonic | [optional] 
**bits** | **int** | The size of the key | [optional] 

## Example

```python
from pdns_admin_client.models.cryptokey import Cryptokey

# TODO update the JSON string below
json = "{}"
# create an instance of Cryptokey from a JSON string
cryptokey_instance = Cryptokey.from_json(json)
# print the JSON string representation of the object
print(Cryptokey.to_json())

# convert the object into a dict
cryptokey_dict = cryptokey_instance.to_dict()
# create an instance of Cryptokey from a dict
cryptokey_form_dict = cryptokey.from_dict(cryptokey_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


