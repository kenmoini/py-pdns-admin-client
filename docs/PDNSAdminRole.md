# PDNSAdminRole

Roles of PowerDNS Admin

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID for this PDNSAdmin role | [optional] [readonly] 
**name** | **str** | The Name of PDNSAdmin role | [optional] 

## Example

```python
from pdns_admin_client.models.pdns_admin_role import PDNSAdminRole

# TODO update the JSON string below
json = "{}"
# create an instance of PDNSAdminRole from a JSON string
pdns_admin_role_instance = PDNSAdminRole.from_json(json)
# print the JSON string representation of the object
print(PDNSAdminRole.to_json())

# convert the object into a dict
pdns_admin_role_dict = pdns_admin_role_instance.to_dict()
# create an instance of PDNSAdminRole from a dict
pdns_admin_role_form_dict = pdns_admin_role.from_dict(pdns_admin_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


