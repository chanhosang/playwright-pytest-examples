# conftest.py
from slugify import slugify
from pathlib import Path
import os
import pytest
import json
from py.xml import html

def pytest_html_report_title(report):
    report.title = "Test Report"

def pytest_html_results_summary(prefix, summary, postfix):

    # To get the summary info from 'info.json' and display in HTML report
    # Make sure the file is located in the project root
    info_file = os.path.dirname(__file__)+'/info.json'

    if os.path.exists(info_file):
        with open(info_file) as f:
            data = json.load(f)
        f.close()

        if data:
            summary = data['summary']
            prefix.extend([html.p(summary+"")])

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    To capture screenshot on failure and display in pytest-html report
    """
    pytest_html = item.config.pluginmanager.getplugin('html')

    callers = yield
    report = callers.get_result()
    report.extra = []

    # If the marker match one of the testing types, then mention it in the report
    types = ["smoke", "regression", "integration", "api"]
    for type in types:
        marker_priority = item.get_closest_marker(type)
        if marker_priority:
            item.config._metadata["Test Type"] = marker_priority.name

            print(marker_priority)

    # extra = getattr(report, "extra", [])
    # if report.when == "call":
    #     # always add url to report
    #     extra.append(pytest_html.extras.url("http://www.example.com/"))
    #     xfail = hasattr(report, "wasxfail")
    #     if (report.skipped and xfail) or (report.failed and not xfail):
    #         # only add additional html on failure
    #         extra.append(pytest_html.extras.html("<div>Additional HTML</div>"))
    #     report.extra = extra


    if "page" not in item.funcargs:
        return "page not in item.funcargs"
    page = item.funcargs["page"]
    if report.when == 'call':
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):

            # Just in case the pytest-html is not being used as reporter
            if item.config.option.htmlpath is not None:

                report_dir = os.path.dirname(item.config.option.htmlpath)
                screen_img = str(Path("images") / f"{slugify(item.nodeid)}.png")

                capture_screenshot(report_dir, screen_img, page)

                if screen_img:
                    html = '<div><img src="%s" alt="screenshot" style="height:360px;" ' \
                           'onclick="window.open(this.src)" align="right"/></div>' % screen_img
                    report.extra.append(pytest_html.extras.html(html))

def capture_screenshot(report_dir, screen_img, page):
    """
    To capture screenshot and save it to 'images' folder inside the specific html report directory.
    """
    screenshot_dir = str(Path(report_dir)/os.path.dirname(screen_img))
    screen_img = str(Path(report_dir)/screen_img)
    # print("screenshot_dir:"+screenshot_dir)
    # print("screen_img:"+screen_img)
    if not os.path.exists(screenshot_dir):
        os.makedirs(screenshot_dir)

    page.screenshot(path=screen_img)


def pytest_addoption(parser):
    """
    To get password from command line argument
    """
    parser.addoption("--password", action="store", default="test", help="password")

@pytest.fixture(scope="module")
def password(request):
    return request.config.getoption("--password")

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": {
            "width": 1920,
            "height": 1080,
        },
        "accept_downloads": True
    }

@pytest.fixture
def context(context):
    """
    To override the default timeout
    """
    context.set_default_timeout(45 * 1000) # default to 30 seconds
    # context.accept_downloads(True)
    yield context
