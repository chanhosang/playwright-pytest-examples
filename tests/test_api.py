
import pytest
import requests
import json
from dotenv import load_dotenv, find_dotenv

# https://www.ontestautomation.com/writing-tests-for-restful-apis-in-python-using-requests-part-1-basic-tests/
# https://www.ontestautomation.com/writing-tests-for-restful-apis-in-python-using-requests-part-2-data-driven-tests

def test_get_locations_for_us_90210_check_status_code_equals_200():
     response = requests.get("http://api.zippopotam.us/us/90210")
     assert response.status_code == 200

def test_get_locations_for_us_90210_check_country_equals_united_states():
     response = requests.get("http://api.zippopotam.us/us/90210")
     response_body = response.json()
     assert response_body["country"] == "United States"

def test_get_locations_for_us_90210_check_city_equals_beverly_hills():
     response = requests.get("http://api.zippopotam.us/us/90210")
     response_body = response.json()
     assert response_body["places"][0]["place name"] == "Beverly Hills"

def test_get_locations_for_us_90210_check_one_place_is_returned():
     response = requests.get("http://api.zippopotam.us/us/90210")
     response_body = response.json()
     assert len(response_body["places"]) == 1
