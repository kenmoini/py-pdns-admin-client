# coding: utf-8

"""
    PowerDNS Admin Authoritative HTTP API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.0.14
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from pdns_admin_client.api.pdnsadmin_zones_api import PdnsadminZonesApi


class TestPdnsadminZonesApi(unittest.TestCase):
    """PdnsadminZonesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = PdnsadminZonesApi()

    def tearDown(self) -> None:
        pass

    def test_api_login_create_zone(self) -> None:
        """Test case for api_login_create_zone

        Creates a new domain, returns the Zone on creation.
        """
        pass

    def test_api_login_delete_zone(self) -> None:
        """Test case for api_login_delete_zone

        Deletes this zone, all attached metadata and rrsets.
        """
        pass

    def test_api_login_list_zones(self) -> None:
        """Test case for api_login_list_zones

        List all Zones in a server
        """
        pass

    def test_synchronize_domains(self) -> None:
        """Test case for synchronize_domains

        Sync PDNS with PDNSAdmin
        """
        pass


if __name__ == '__main__':
    unittest.main()
