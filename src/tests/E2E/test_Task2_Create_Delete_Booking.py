# Create Booking -> Delete It -> Verify
import pytest
import allure

from src.helpers.API_requests_Wrapper import delete_requests
from src.constants.API_Contants import APIConstants
from src.helpers.payload_manager import *
from src.helpers.common_verification import *
from src.utils.Utils import Utils


class Test_Create_Booking_Delete_Booking(object):
    @allure.title("E2E Verify Create Booking -> Delete Booking -> Re-verify")
    @allure.description("Verify the created booking can be deleted with the booking id")
    def test_create_delete_booking(self, create_token,create_booking_id):
        token = create_token
        booking_id = create_booking_id
        delete_url = APIConstants.url_patch_put_delete(booking_id)
        response = delete_requests(
            url=delete_url,
            headers=Utils().common_header_put_delete_patch_cookie(token=token),
            auth=None,
            in_json=False
        )
        verify_http_status_code(response_data=response, expected_data=201)
        verify_response_delete(response=response.text)