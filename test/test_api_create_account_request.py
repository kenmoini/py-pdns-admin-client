# coding: utf-8

"""
    PowerDNS Admin Authoritative HTTP API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.0.14
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from pdns_admin_client.models.api_create_account_request import ApiCreateAccountRequest

class TestApiCreateAccountRequest(unittest.TestCase):
    """ApiCreateAccountRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiCreateAccountRequest:
        """Test ApiCreateAccountRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiCreateAccountRequest`
        """
        model = ApiCreateAccountRequest()
        if include_optional:
            return ApiCreateAccountRequest(
                name = '',
                description = '',
                contact = '',
                mail = ''
            )
        else:
            return ApiCreateAccountRequest(
                name = '',
        )
        """

    def testApiCreateAccountRequest(self):
        """Test ApiCreateAccountRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
