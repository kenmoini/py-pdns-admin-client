# BaseStatisticItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of this item (e.g. ‘uptime’) | [optional] 

## Example

```python
from pdns_admin_client.models.base_statistic_item import BaseStatisticItem

# TODO update the JSON string below
json = "{}"
# create an instance of BaseStatisticItem from a JSON string
base_statistic_item_instance = BaseStatisticItem.from_json(json)
# print the JSON string representation of the object
print(BaseStatisticItem.to_json())

# convert the object into a dict
base_statistic_item_dict = base_statistic_item_instance.to_dict()
# create an instance of BaseStatisticItem from a dict
base_statistic_item_form_dict = base_statistic_item.from_dict(base_statistic_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


