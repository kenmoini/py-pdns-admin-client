# UserDetailed

User that can access the gui/api

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID for this user (unique) | [optional] [readonly] 
**username** | **str** | The username for this user (unique, immutable) | [optional] 
**password** | **str** | The hashed password for this user | [optional] 
**firstname** | **str** | The firstname of this user | [optional] 
**lastname** | **str** | The lastname of this user | [optional] 
**email** | **str** | Email addres for this user | [optional] 
**otp_secret** | **str** | OTP secret | [optional] 
**confirmed** | **bool** | The confirmed status | [optional] 
**role** | [**PDNSAdminRole**](PDNSAdminRole.md) |  | [optional] 
**accounts** | [**List[AccountSummary]**](AccountSummary.md) |  | [optional] 

## Example

```python
from pdns_admin_client.models.user_detailed import UserDetailed

# TODO update the JSON string below
json = "{}"
# create an instance of UserDetailed from a JSON string
user_detailed_instance = UserDetailed.from_json(json)
# print the JSON string representation of the object
print(UserDetailed.to_json())

# convert the object into a dict
user_detailed_dict = user_detailed_instance.to_dict()
# create an instance of UserDetailed from a dict
user_detailed_form_dict = user_detailed.from_dict(user_detailed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


