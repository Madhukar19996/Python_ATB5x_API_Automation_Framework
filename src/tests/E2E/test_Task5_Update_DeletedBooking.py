# Try to Update the Deleted Booking

import pytest
import allure

from src.helpers.API_requests_Wrapper import *
from src.constants.API_Contants import APIConstants
from src.helpers.payload_manager import *
from src.helpers.common_verification import *
from src.utils.Utils import Utils

class Test_Update_deleted_booking(object):
    @allure.title("E2E Verify deleted booking id can be updated")
    @allure.description("Verify that updating a deleted booking id gives 404 error-Delete operation testcase")
    def test_delete_Booking_id(self, create_token, create_booking_id):
        booking_id = create_booking_id
        token = create_token
        delete_url = APIConstants.url_patch_put_delete(booking_id)
        response = delete_requests(
            url=delete_url,
            auth=None,
            headers=Utils().common_header_put_delete_patch_cookie(token=token),
            in_json=False
        )
        print(response.text)
        verify_http_status_code(response_data=response, expected_data=201)
        verify_response_delete(response=response.text)