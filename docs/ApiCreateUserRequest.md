# ApiCreateUserRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** | Login name for user (unique, immutable) | 
**password** | **str** | Hashed password for authentication | [optional] 
**plain_text_password** | **str** | Plain text password (will be hashed) for authentication | [optional] 
**firstname** | **str** | Firstname of user | [optional] 
**lastname** | **str** | Lastname of user | [optional] 
**email** | **str** | Email address if user (must be unique) | 
**otp_secret** | **str** | OTP secret | [optional] 
**confirmed** | **str** | Confirmed status | [optional] 
**role_name** | **str** | Name of role to be assigned to user (default &#39;User&#39;) | [optional] 
**role_id** | **int** | Role ID of role to be assigned to user | [optional] 

## Example

```python
from pdns_admin_client.models.api_create_user_request import ApiCreateUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiCreateUserRequest from a JSON string
api_create_user_request_instance = ApiCreateUserRequest.from_json(json)
# print the JSON string representation of the object
print(ApiCreateUserRequest.to_json())

# convert the object into a dict
api_create_user_request_dict = api_create_user_request_instance.to_dict()
# create an instance of ApiCreateUserRequest from a dict
api_create_user_request_form_dict = api_create_user_request.from_dict(api_create_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


