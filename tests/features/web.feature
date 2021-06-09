Feature: DuckDuckGo Web Browsing
  As a web surfer,
  I want to find information online,
  So I can learn new things and get tasks done.


  Background:
    Given the DuckDuckGo home page is displayed

  @smoke
  Scenario: Basic DuckDuckGo Search
    When the user searches for "panda"
    Then results are shown for "panda"
