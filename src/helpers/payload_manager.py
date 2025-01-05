# Payloads

# Create Booking
# Update Booking
# Auth - Token

def payload_create_booking():
    payload = {
        "firstname": "Piyush",
        "lastname": "Pandey",
        "totalprice": 11000,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2025-01-12",
            "checkout": "2025-01-20"
        },
        "additionalneeds": "Lunch"
    }
    return payload


def payload_update_booking():
    payload = {
        "firstname": "Madhukar",
        "lastname": "Pandey",
        "totalprice": 12000,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2025-01-01",
            "checkout": "2025-01-10"
        },
        "additionalneeds": "Breakfast"
    }
    return payload


def payload_create_token():
    payload = {
        "username": "admin",
        "password": "password123"
    }
    return payload