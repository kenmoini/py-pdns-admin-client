# MapStatisticItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of this item (e.g. ‘uptime’) | [optional] 
**type** | **str** | set to \&quot;MapStatisticItem\&quot; | [optional] 
**value** | [**List[MapStatisticItemAllOfValue]**](MapStatisticItemAllOfValue.md) | named statistic values | [optional] 

## Example

```python
from pdns_admin_client.models.map_statistic_item import MapStatisticItem

# TODO update the JSON string below
json = "{}"
# create an instance of MapStatisticItem from a JSON string
map_statistic_item_instance = MapStatisticItem.from_json(json)
# print the JSON string representation of the object
print(MapStatisticItem.to_json())

# convert the object into a dict
map_statistic_item_dict = map_statistic_item_instance.to_dict()
# create an instance of MapStatisticItem from a dict
map_statistic_item_form_dict = map_statistic_item.from_dict(map_statistic_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


