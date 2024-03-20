# ApiCreateAccountRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name for account (unique, immutable) | 
**description** | **str** | Description of account | [optional] 
**contact** | **str** | Contact information | [optional] 
**mail** | **str** | Email address for contact | [optional] 

## Example

```python
from pdns_admin_client.models.api_create_account_request import ApiCreateAccountRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiCreateAccountRequest from a JSON string
api_create_account_request_instance = ApiCreateAccountRequest.from_json(json)
# print the JSON string representation of the object
print(ApiCreateAccountRequest.to_json())

# convert the object into a dict
api_create_account_request_dict = api_create_account_request_instance.to_dict()
# create an instance of ApiCreateAccountRequest from a dict
api_create_account_request_form_dict = api_create_account_request.from_dict(api_create_account_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


