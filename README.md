# playwright-pytest-examples

# Setup

* Install [Python](https://www.python.org/downloads/)

* Install [Pip](https://pip.pypa.io/en/stable/installation/)
* Then, install the python dependencies:
    ```
    pip install -r requirements.txt
    ```
* Install playright browsers (Chromium, FireFox and Webkit):
    ```
    playwright install
    ```


# How to Run?

## Pytest - Basic

To run test in headed mode on different browser (webkit, chrome, firefox):
```
pytest tests/test_web_element.py --headed --browser webkit
```
To run smoke test coverage only on chrome browser:
```
pytest tests/test_web_element.py -m smoke
```
To exclude those test cases that take longer time to complete:
```
pytest tests/test_web_element.py -m 'not intensive' --headed
```

## Pytest - Page Object Model

To run test written in page object model:
```
pytest tests/test_bing_search.py
```

## Pytest-BDD

To run pytest-bdd test and generate cucumber report:
```
pytest tests/step_defs/test_steps_web.py --cucumberjson=reports/cucumber-report.json
```

**Generate Cucumber HTML Report**

If you are running pytest-bdd, it would be beneficial to generate HTML report in BDD style for better collaboration with the team.


You can either use [Cucumber reports Jenkins Plugin](https://plugins.jenkins.io/cucumber-reports/) and publish the HTML report in Jenkins.

or

Use [Node.js](https://nodejs.org/en/download/). package, [cucumber-html-reporter](https://npm.io/package/cucumber-html-reporter) to generate the HTML report by the following command:
```
npm i cucumber-html-reporter
node generate-html-report.js
```


# Quick Tips

To run test in in headed mode:
```
pytest --headed
```

To run test in parallel with 4 workers:
```
pytest -n 4 --dist=loadfile
```
**NOTE**: IN case there are some tests within the same file that need to run in sequence. Therefore, --dist=loadfile

To run test on multiple browsers:
```
pytest --browser chromium --browser webkit --browser firefox
```

To run test and parse variables from a JSON file and command line argument:
```
pytest tests/test_example.py --variables config/environments.json --password=<password>
```


# References
* [Playwright for Python](https://playwright.dev/python/docs)
* [Playwright in Pytest](https://pypi.org/project/pytest-playwright/)
* [Playwright Crash Couse with Pytest](https://www.youtube.com/watch?v=c7QQab7e_Gs&t=258s)
* [Playwright Pytest Documentation](https://github.com/microsoft/playwright-pytest)*
* [Playwright Autowaiting](https://playwright.dev/docs/actionability/)
* [Pytest-HTML User Guide](https://pytest-html.readthedocs.io/en/latest/user_guide.html)
* [XPath Cheatsheet](https://devhints.io/xpath)
* [UI Automation Test Playground](http://www.uitestingplayground.com/​)

