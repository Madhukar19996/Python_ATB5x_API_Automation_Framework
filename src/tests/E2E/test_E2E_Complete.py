from typing import AnyStr

from src.helpers.API_requests_Wrapper import *
from src.constants.API_Contants import APIConstants
from src.helpers.payload_manager import *
from src.helpers.common_verification import *
from src.utils.Utils import Utils

import allure
import pytest


class TestE2E(object):
    @allure.title("E2E Testcase-Create Booking -->Update-->Delete Booking(Verify)")
    @allure.description("Verify that created booking id when when we update we are unable to update it and delete it also| Full CRUD  ")
    @allure.testcase(url="https://bugz.atlassian.net/browse/BUG-1",name="E2ETC1")
    def test_update_booking_with_id_token(self,create_token,get_booking_id):
        print(create_token,get_booking_id)
        booking_id = get_booking_id
        token = create_token
        put_url = APIConstants.url_patch_put_delete(booking_id=booking_id)
        print(put_url)
        response = put_requests(
            url=put_url,
            headers=Utils().common_header_put_delete_patch_cookie(token=token),
            payload=payload_update_booking(),
            auth=None,
            in_json=False
        )
        # Verification here & more
        verify_http_status_code(response_data=response, expected_data=200)

        verify_response_key(response.json()["firstname"], "Madhukar")
        verify_response_key(response.json()["lastname"], "Pandey")

    @allure.title("Test CRUD operation Delete(delete)")
    @allure.description(
        "Verify booking gets deleted with the booking ID and Token.")
    def test_delete_booking_id(self,create_token,get_booking_id):
        print(create_token, get_booking_id)
        booking_id = get_booking_id
        token = create_token
        put_url = APIConstants.url_patch_put_delete(booking_id=booking_id)
        print(put_url)

        delete_url = APIConstants.url_patch_put_delete(booking_id=booking_id)
        response = delete_requests(
            url=delete_url,
            headers=Utils().common_header_put_delete_patch_cookie(token=token),
            auth=None,
            in_json=False
        )
        verify_http_status_code(response_data=response, expected_data=201)
        verify_response_delete(response=response.text)
