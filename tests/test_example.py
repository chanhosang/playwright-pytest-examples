"""
An example on how to load configuration data from JSON file

For example,
    pytest tests/test_example.py --variables config/environments.json --password=<password>
"""

import pytest
import json

@pytest.mark.smoke
def test_goto_bing(page,variables, password):


    filter_name = 'bing'

    data = variables.get('environments')


    if filter_name and data:
            filter_object = [x for x in data if x['name'] == filter_name]
            # print(filter_object)
            if filter_object:
                json_environment = filter_object[0]

                print("name:"+json_environment['name'])
                print("url:"+json_environment['url'])

                print("Go to URL: "+json_environment['url'])
                page.goto(json_environment['url'])

                # Just to try out parsing password from command line
                print("password:"+password)
            else:
                assert False, "The 'name:"+filter_name+"' element not found in the variable file"
    else:
        assert False, "The 'environments' element not found in the variable file"



