# ApiKeySummary

Summary of an ApiKey

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID for this key, used in the ApiKey URL endpoint. | [optional] [readonly] 
**description** | **str** | Some user defined description | [optional] 

## Example

```python
from pdns_admin_client.models.api_key_summary import ApiKeySummary

# TODO update the JSON string below
json = "{}"
# create an instance of ApiKeySummary from a JSON string
api_key_summary_instance = ApiKeySummary.from_json(json)
# print the JSON string representation of the object
print(ApiKeySummary.to_json())

# convert the object into a dict
api_key_summary_dict = api_key_summary_instance.to_dict()
# create an instance of ApiKeySummary from a dict
api_key_summary_form_dict = api_key_summary.from_dict(api_key_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


