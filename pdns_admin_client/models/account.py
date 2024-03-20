# coding: utf-8

"""
    PowerDNS Admin Authoritative HTTP API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.0.14
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from pdns_admin_client.models.api_key_summary import ApiKeySummary
from typing import Optional, Set
from typing_extensions import Self

class Account(BaseModel):
    """
    Account that 'owns' zones
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="The ID for this account (unique)")
    name: Optional[StrictStr] = Field(default=None, description="The name for this account (unique, immutable)")
    description: Optional[StrictStr] = Field(default=None, description="The description for this account")
    contact: Optional[StrictStr] = Field(default=None, description="The contact details for this account")
    mail: Optional[StrictStr] = Field(default=None, description="The email address of the contact for this account")
    apikeys: Optional[List[ApiKeySummary]] = Field(default=None, description="A list of API Keys bound to this account")
    __properties: ClassVar[List[str]] = ["id", "name", "description", "contact", "mail", "apikeys"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of Account from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "id",
            "apikeys",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in apikeys (list)
        _items = []
        if self.apikeys:
            for _item in self.apikeys:
                if _item:
                    _items.append(_item.to_dict())
            _dict['apikeys'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Account from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "description": obj.get("description"),
            "contact": obj.get("contact"),
            "mail": obj.get("mail"),
            "apikeys": [ApiKeySummary.from_dict(_item) for _item in obj["apikeys"]] if obj.get("apikeys") is not None else None
        })
        return _obj

