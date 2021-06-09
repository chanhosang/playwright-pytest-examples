"""
An example on how to load configuration data from JSON file

For example,
    pytest tests/test_example.py --variables config/environments.json --password=<password>
"""

import pytest
import json

@pytest.mark.smoke
def test_goto(page,variables, password):
    print("name:"+variables.get('name'))
    print("password:"+password)
    page.goto(variables.get('url'))


