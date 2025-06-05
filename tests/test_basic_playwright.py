from playwright.sync_api import sync_playwright

def xtest_goto_url():
    with sync_playwright() as playwright:
        # Launch browser, headless is default, slow execution by 500 times to see what's going on
        browser = playwright.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page() # Create new page
        page.goto("https://playwright.dev/python") # Go to url
        button = page.get_by_role("link", name="GET STARTED")
        button.highlight() # You can highlight elements
        docs_link = page.get_by_role('link', name="Docs") # Locate link element with "Docs" text
        docs_link.click()
        print("Docs url: ", page.url) # Print page url
        browser.close() # Close browser

def test_role_locator():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
        url = "https://bootswatch.com/default"
        page.goto(url)
        btn = page.get_by_role("button", name="Default button")
        btn.highlight()
        btn.click()

        heading = page.get_by_role("heading", name="Heading 2")
        heading.highlight()

        radio_btn = page.get_by_role("radio", name="Option one is this and that—be sure to include why it's great")
        radio_btn.highlight()

        checkbox = page.get_by_role("checkbox", name="Default checkbox")
        checkbox.highlight()
        checkbox.check()

def test_input_field_locator():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
        url = "https://bootswatch.com/default"
        page.goto(url)
        email_input = page.get_by_label("Email address") # Locate input field by its label element
        email_input.highlight()

        text_area = page.get_by_label("Example textarea")
        text_area.highlight()

        # Locate input field by placeholder (text in input field like "Enter email")
        page.get_by_placeholder("Enter email").highlight()

def test_inner_text_locator():
    # Find "with muted text" in: <h3>"Heading"<small>with muted text</small></h3>
    # get_by_text() can be used to locate anything with text, but better to use get_by_role() and specify element type
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
        url = "https://bootswatch.com/default"
        page.goto(url)
        page.get_by_text("with muted text").highlight()

        page.get_by_text("fine print", exact=True).highlight()  # Doesn't highlight because there's no element with exactly "fine print"
        page.get_by_text("fine print").highlight()  # Highlights entire paragraph that contains "fine print". exact=True is default behavior

def xtest_alt_text_locator(): # This test uses a terrible site where the photos are always changing
    # Locate image by its alt attribute that contains text describing the image
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
        url = "https://unsplash.com"
        page.goto(url)
        page.get_by_alt_text("A person sitting on a rock with a camera").click()

def test_title_locator():
    with sync_playwright() as playwright:
        # Some elements have a title attribute: <p>"Some text"<abbr title="attribute">attr</abbr></p>
        browser = playwright.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
        url = "https://bootswatch.com/default"
        page.goto(url)
        page.get_by_title("attribute").highlight()

def test_css_locator():
    with sync_playwright() as playwright:
        # Some elements have a title attribute: <p>"Some text"<abbr title="attribute">attr</abbr></p>
        browser = playwright.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
        url = "https://bootswatch.com/default"
        page.goto(url)
        page.locator("css=h1").highlight() # highlights all h1 elements

        # Locate button with class btn-outline-success by separating with a '.': button.btn-outline-success
        page.locator("button.btn-outline-success").highlight() # The "css=" for the argument is optional

        # Locate button with id btnGroupDrop1 by separating with a '#': button#btnGroupDrop1
        page.locator("button#btnGroupDrop1").highlight()

        # Locate button with attribute by putting attribute in square brackets.
        page.locator("input[readonly]").highlight() # Here the readonly attribute doesn't have a value
        page.locator("input[value='correct value']").highlight() # Here the value attribute has value of 'correct value'

def test_css_locator_by_hierarchy():
    with sync_playwright() as playwright:
        # If you get too many matches trying to locate, try looking at parent element and locate by hierarchy
        # You don't have to include all items in hierarchy. If parent has two divs, and then the child element is in them, you don't have to include divs
        browser = playwright.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
        url = "https://bootswatch.com/default"
        page.goto(url)
        page.locator("nav.bg-dark a.nav-link.active").highlight() # Separate hierarchical elements with a space

def test_css_locator_by_pseudo_class():
    with sync_playwright() as playwright:
        # You can select by element name like h1, then narrow down by h1 with certain text
        browser = playwright.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
        url = "https://bootswatch.com/default"
        page.goto(url)
        page.locator("h1:text('Nav')").highlight() # Finds both h1 tags with "Nav" in text
        page.locator("h1:text-is('Nav')").highlight()  # Use text-is to find h1 tags with exactly only "Nav" as text

        page.locator("div.dropdown-menu:visible").highlight() # Use 'visible' psuedo class selector to only select visible element

        page.locator(":nth-match(button.btn-primary, 4)").highlight()  # Select 4th button with class btn-primary

def test_xpath_locator_by_path():
    # Select elements by tag and attribute
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
        url = "https://bootswatch.com/default"
        page.goto(url)
        page.locator("xpath=/text/header/title").highlight() # Absolute path starting at root
        page.locator("xpath=//h1").highlight() # Relative path, select all h1 elements
        page.locator("xpath=//h1[@id='navbars']").highlight()  # Select h1 with attribute of id="navbars"
        page.locator("//input[@readonly]").highlight()  # "xpath=" is optional, this finds input field with readonly attribute that has no value

def test_xpath_locator_functions():
    # Select elements by the text they contain
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
        url = "https://bootswatch.com/default"
        page.goto(url)
        page.locator("//h1[ text() = 'Heading 1' ]").highlight() # Use xpath text() to find h1 element with text exactly matching "Heading 1"
        page.locator("//h1[ contains(text(), 'Head') ]").highlight()  # Find all h1 elements containing text "Head"
        page.locator("//button[ contains(@class, 'btn-outline-primary') ]").highlight()  # Find all button elements with attribute of class containing text "btn-outline-primary"
        page.locator("//input[ contains(@value, 'correct') ]").highlight()  # Find input element with attribute "value" having a value that contains the text "correct".

def test_miscellaneous_locators():
    # Select elements by the text they contain
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
        url = "https://bootswatch.com/default"
        page.goto(url)
        page.get_by_role("button", name="Primary").locator("nth=1").highlight() # Indexed, so nth=1 gets 2nd button with name=Primary
        page.get_by_label("Email address").locator("..") # Use ".." to get parent
        page.locator("id=btnGroupDrop1") # Get by id without using css selector
        page.get_by_role("heading").filter(has_text="Heading")
        page.locator("div.form-group").filter(has=page.get_by_label("Password"))

# @pytest.mark.skip_browser("firefox") # Skip test if firefox
# def xtest_dont_run_firefox(page):
#     page.goto("/")
#
# @pytest.mark.only_browser("webkit") # Skip test unless webkit
# def xtest_run_only_webkit(page):
#     page.goto("/")
#
# def xtest_scrollbars(page):
#     page.goto("/") # Base url from command line --base-url parameter is used
#     page.click("text=Scrollbars")
#     page.click("#hidingButton") # Using CSS selector
#
# def xtest_client_side_delay(page):
#     page.goto("/clientdelay")
#     page.click(".btn-primary") # Using class selector
#     page.click("text=Data calculated on the client side.") # Playwright waits for the button's 15 second delay
#
# def xtest_login(page):
#     page.goto("/")
#     page.click("text=Sample App")
#     page.click("[placeholder='User Name']") # Most pages you don't need to click in the field before filling it, but here we do
#     page.fill("[placeholder='User Name']", "Jim") # Fill name field
#     page.press("[placeholder='User Name']", "Tab") # Tab to next field
#     page.fill("[placeholder='********']", "pwd") # Fill password field
#     page.click("#login") # Click login button to submit the form
#     page.click("text=Welcome, Jim!")