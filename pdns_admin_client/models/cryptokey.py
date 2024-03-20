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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class Cryptokey(BaseModel):
    """
    Describes a DNSSEC cryptographic key
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="set to \"Cryptokey\"")
    id: Optional[StrictStr] = Field(default=None, description="The internal identifier, read only")
    keytype: Optional[StrictStr] = None
    active: Optional[StrictBool] = Field(default=None, description="Whether or not the key is in active use")
    dnskey: Optional[StrictStr] = Field(default=None, description="The DNSKEY record for this key")
    ds: Optional[List[StrictStr]] = Field(default=None, description="An array of DS records for this key")
    privatekey: Optional[StrictStr] = Field(default=None, description="The private key in ISC format")
    algorithm: Optional[StrictStr] = Field(default=None, description="The name of the algorithm of the key, should be a mnemonic")
    bits: Optional[StrictInt] = Field(default=None, description="The size of the key")
    __properties: ClassVar[List[str]] = ["type", "id", "keytype", "active", "dnskey", "ds", "privatekey", "algorithm", "bits"]

    @field_validator('keytype')
    def keytype_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['ksk', 'zsk', 'csk']):
            raise ValueError("must be one of enum values ('ksk', 'zsk', 'csk')")
        return value

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
        """Create an instance of Cryptokey from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Cryptokey from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "id": obj.get("id"),
            "keytype": obj.get("keytype"),
            "active": obj.get("active"),
            "dnskey": obj.get("dnskey"),
            "ds": obj.get("ds"),
            "privatekey": obj.get("privatekey"),
            "algorithm": obj.get("algorithm"),
            "bits": obj.get("bits")
        })
        return _obj


