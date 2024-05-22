import pytest

@pytest.mark.skip_browser("firefox") # Skip test if firefox
def xtest_dont_run_firefox(page):
    page.goto("/")

@pytest.mark.only_browser("webkit") # Skip test unless webkit
def xtest_run_only_webkit(page):
    page.goto("/")

def test_scrollbars(page):
    page.goto("/") # Base url from command line --base-url parameter is used
    page.click("text=Scrollbars")
    page.click("#hidingButton") # Using CSS selector

def xtest_client_side_delay(page):
    page.goto("/clientdelay")
    page.click(".btn-primary") # Using class selector
    page.click("text=Data calculated on the client side.") # Playwright waits for the button's 15 second delay

def test_login(page):
    page.goto("/")
    page.click("text=Sample App")
    page.click("[placeholder='User Name']") # Most pages you don't need to click in the field before filling it, but here we do
    page.fill("[placeholder='User Name']", "Jim") # Fill name field
    page.press("[placeholder='User Name']", "Tab") # Tab to next field
    page.fill("[placeholder='********']", "pwd") # Fill password field
    page.click("#login") # Click login button to submit the form
    page.click("text=Welcome, Jim!")