  
import pytest

@pytest.mark.smoke
def test_click(page):
    page.goto("/")
    page.click('text=Click')

@pytest.mark.intensive
def test_load_delay(page):
    page.goto("/")
    page.click('text=Load Delay')
    page.click(".btn")
    
@pytest.mark.smoke
def test_input(page):
    page.goto("/textinput")
    page.fill('#newButtonName','Test Name')
    page.click('#updatingButton')
    assert page.inner_text('#updatingButton') == "Test Name"

    
def test_scroll_bar(page):
    page.goto("/scrollbars")
    page.click("#hidingButton")

def test_login_fail(page):
    page.goto("/sampleapp")
    page.fill('//input[@placeholder="User Name"]','Tim')
    page.click("#login")
    assert page.inner_text('#loginstatus') == "Invalid username/password"
    

def test_login_logout(page):
    #login
    page.goto("/sampleapp")
    page.fill('//input[@placeholder="User Name"]','Tim')
    page.fill('//input[@name="Password"]','pwd')
    page.click("#login")
    assert page.inner_text('#loginstatus') == "Welcome, Tim!"

    # logout
    page.click("#login")
    assert page.inner_text('#loginstatus') == "XUser logged out."

def test_non_breaking_space(page):
    page.goto("/nbsp")
    page.click("text=My Button")

@pytest.mark.intensive
def test_progress_bar(page):
    page.goto("/progressbar")
    page.click("#startButton")
    page.inner_text("#progressBar[aria-valuenow='50']")
    page.click("#stopButton")    
    assert "Result: " in page.inner_text("#result")
    
    
