# PDNSAdminZonesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID for this PDNSAdmin zone | [optional] [readonly] 
**name** | **str** | Name of the zone | [optional] 

## Example

```python
from pdns_admin_client.models.pdns_admin_zones_inner import PDNSAdminZonesInner

# TODO update the JSON string below
json = "{}"
# create an instance of PDNSAdminZonesInner from a JSON string
pdns_admin_zones_inner_instance = PDNSAdminZonesInner.from_json(json)
# print the JSON string representation of the object
print(PDNSAdminZonesInner.to_json())

# convert the object into a dict
pdns_admin_zones_inner_dict = pdns_admin_zones_inner_instance.to_dict()
# create an instance of PDNSAdminZonesInner from a dict
pdns_admin_zones_inner_form_dict = pdns_admin_zones_inner.from_dict(pdns_admin_zones_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


