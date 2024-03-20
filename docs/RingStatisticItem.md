# RingStatisticItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of this item (e.g. ‘uptime’) | [optional] 
**type** | **str** | set to \&quot;RingStatisticItem\&quot; | [optional] 
**size** | **int** | for RingStatisticItem objects, the size of the ring | [optional] 
**value** | [**List[MapStatisticItemAllOfValue]**](MapStatisticItemAllOfValue.md) | named ring statistic values | [optional] 

## Example

```python
from pdns_admin_client.models.ring_statistic_item import RingStatisticItem

# TODO update the JSON string below
json = "{}"
# create an instance of RingStatisticItem from a JSON string
ring_statistic_item_instance = RingStatisticItem.from_json(json)
# print the JSON string representation of the object
print(RingStatisticItem.to_json())

# convert the object into a dict
ring_statistic_item_dict = ring_statistic_item_instance.to_dict()
# create an instance of RingStatisticItem from a dict
ring_statistic_item_form_dict = ring_statistic_item.from_dict(ring_statistic_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


