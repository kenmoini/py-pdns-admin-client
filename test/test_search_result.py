# coding: utf-8

"""
    PowerDNS Admin Authoritative HTTP API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.0.14
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from pdns_admin_client.models.search_result import SearchResult

class TestSearchResult(unittest.TestCase):
    """SearchResult unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SearchResult:
        """Test SearchResult
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SearchResult`
        """
        model = SearchResult()
        if include_optional:
            return SearchResult(
                content = '',
                disabled = True,
                name = '',
                object_type = '',
                zone_id = '',
                zone = '',
                type = '',
                ttl = 56
            )
        else:
            return SearchResult(
        )
        """

    def testSearchResult(self):
        """Test SearchResult"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()