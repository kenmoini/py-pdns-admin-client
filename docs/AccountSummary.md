# AccountSummary

Summary of an Account that 'owns' zones

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID for this account (unique) | [optional] [readonly] 
**name** | **str** | The name for this account (unique, immutable) | [optional] 
**domains** | [**List[PDNSAdminZonesInner]**](PDNSAdminZonesInner.md) | A list of domains | [optional] 

## Example

```python
from pdns_admin_client.models.account_summary import AccountSummary

# TODO update the JSON string below
json = "{}"
# create an instance of AccountSummary from a JSON string
account_summary_instance = AccountSummary.from_json(json)
# print the JSON string representation of the object
print(AccountSummary.to_json())

# convert the object into a dict
account_summary_dict = account_summary_instance.to_dict()
# create an instance of AccountSummary from a dict
account_summary_form_dict = account_summary.from_dict(account_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


