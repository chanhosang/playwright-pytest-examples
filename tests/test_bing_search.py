# test_search.py
from pages.search import SearchPage
import pytest
from playwright.sync_api import Page

# Can be "msedge", "chrome-beta", "msedge-beta", "msedge-dev", etc.

# @pytest.fixture(scope="session")
# def browser(launch_browser: Callable[[], Browser]) -> Generator[Browser, None, None]:
#     browser = launch_browser()
#     yield browser
#     browser.close()
# in the test
@pytest.mark.demo
def test_visit_admin_dashboard(page: Page):
    search_page = SearchPage(page)
    search_page.navigate()
    search_page.search("search query")
