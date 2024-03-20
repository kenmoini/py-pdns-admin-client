# Account

Account that 'owns' zones

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID for this account (unique) | [optional] [readonly] 
**name** | **str** | The name for this account (unique, immutable) | [optional] 
**description** | **str** | The description for this account | [optional] 
**contact** | **str** | The contact details for this account | [optional] 
**mail** | **str** | The email address of the contact for this account | [optional] 
**apikeys** | [**List[ApiKeySummary]**](ApiKeySummary.md) | A list of API Keys bound to this account | [optional] [readonly] 

## Example

```python
from pdns_admin_client.models.account import Account

# TODO update the JSON string below
json = "{}"
# create an instance of Account from a JSON string
account_instance = Account.from_json(json)
# print the JSON string representation of the object
print(Account.to_json())

# convert the object into a dict
account_dict = account_instance.to_dict()
# create an instance of Account from a dict
account_form_dict = account.from_dict(account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


