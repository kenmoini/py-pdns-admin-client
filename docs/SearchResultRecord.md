# SearchResultRecord


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** |  | [optional] 
**disabled** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**object_type** | **str** | set to \&quot;record\&quot; | [optional] 
**zone_id** | **str** |  | [optional] 
**zone** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**ttl** | **int** |  | [optional] 

## Example

```python
from pdns_admin_client.models.search_result_record import SearchResultRecord

# TODO update the JSON string below
json = "{}"
# create an instance of SearchResultRecord from a JSON string
search_result_record_instance = SearchResultRecord.from_json(json)
# print the JSON string representation of the object
print(SearchResultRecord.to_json())

# convert the object into a dict
search_result_record_dict = search_result_record_instance.to_dict()
# create an instance of SearchResultRecord from a dict
search_result_record_form_dict = search_result_record.from_dict(search_result_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


