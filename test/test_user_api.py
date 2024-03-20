# coding: utf-8

"""
    PowerDNS Admin Authoritative HTTP API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.0.14
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from pdns_admin_client.api.user_api import UserApi


class TestUserApi(unittest.TestCase):
    """UserApi unit test stubs"""

    def setUp(self) -> None:
        self.api = UserApi()

    def tearDown(self) -> None:
        pass

    def test_api_add_account_user(self) -> None:
        """Test case for api_add_account_user

        Link user to account
        """
        pass

    def test_api_add_user_account(self) -> None:
        """Test case for api_add_user_account

        Link user to account
        """
        pass

    def test_api_create_user(self) -> None:
        """Test case for api_create_user

        Add a User
        """
        pass

    def test_api_delete_account(self) -> None:
        """Test case for api_delete_account

        Delete a specific Account
        """
        pass

    def test_api_delete_user(self) -> None:
        """Test case for api_delete_user

        Delete a specific User
        """
        pass

    def test_api_get_account_by_name(self) -> None:
        """Test case for api_get_account_by_name

        Get a specific Account on the server
        """
        pass

    def test_api_get_user(self) -> None:
        """Test case for api_get_user

        Get a specific User on the server
        """
        pass

    def test_api_list_account_users(self) -> None:
        """Test case for api_list_account_users

        List users linked to a specific account
        """
        pass

    def test_api_list_users(self) -> None:
        """Test case for api_list_users

        Get all User entries
        """
        pass

    def test_api_list_users_account(self) -> None:
        """Test case for api_list_users_account

        List users linked to a specific account
        """
        pass

    def test_api_remove_account_user(self) -> None:
        """Test case for api_remove_account_user

        Unlink user from account
        """
        pass

    def test_api_remove_user_account(self) -> None:
        """Test case for api_remove_user_account

        Unlink user from account
        """
        pass

    def test_api_update_account(self) -> None:
        """Test case for api_update_account

        Modify a specific Account on the server with supplied parameters
        """
        pass

    def test_api_update_user(self) -> None:
        """Test case for api_update_user

        Modify a specific User on the server with supplied parameters
        """
        pass


if __name__ == '__main__':
    unittest.main()
