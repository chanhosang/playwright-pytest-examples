"""
This module contains step definitions for web.feature.
It uses Selenium WebDriver for browser interactions:
https://www.seleniumhq.org/projects/webdriver/
Setup and cleanup are handled using hooks.
For a real test automation project,
use Page Object Model or Screenplay Pattern to model web interactions.
Prerequisites:
 - Firefox must be installed.
 - geckodriver must be installed and accessible on the system path.
"""

import pytest

from pytest_bdd import scenarios, given, when, then, parsers

from playwright.sync_api import Page
from pages.result import DuckDuckGoResultPage
# from pages.search import DuckDuckGoSearchPage
from pages.search import DuckDuckGoSearchPage
import time
# Scenarios

scenarios('../features/web.feature')


# Given Steps
@given('the DuckDuckGo home page is displayed')
def ddg_home(page: Page):    
    search_page = DuckDuckGoSearchPage(page)
    search_page.load()
    

# When Steps
@when(parsers.parse('the user searches for "{text}"'))
@when(parsers.parse('the user searches for the phrase:"""{text}"""'))
def search_phrase(page: Page, text):
    search_page = DuckDuckGoSearchPage(page)  
    search_page.search(text)
    print("search for "+text)
    


# Then Steps
@then(parsers.parse('results are shown for "{phrase}"'))
def search_results(page: Page, phrase):    
    result_page = DuckDuckGoResultPage(page)

    # time.sleep(5) 
    
    # Check to ensure the search result contains links that match the "phrase"
    titles = result_page.result_link_titles()
    matches = [t for t in titles if phrase.lower() in t.lower()]
    assert len(matches) > 0

    # Check to ensure the search result query is "phrase"
    assert phrase == result_page.search_input_value()