# python-playwright
A demo project to learn how to use Playwright with Python for testing.

## Initial Setup
- Run `python3 -m venv ./venv`
- Run `source ./venv/bin/activate`
- Run `pip3 install -r requirements.txt`
- Run `pytest tests/test_basic_playwright.py`

## Run Tests
- `poetry run pytest` runs all tests in the project in headless mode where you don't see the browser
- `poetry run pytest --headed` headed mode where you see the browser, which is Chromium by default
- `poetry run pytest --headed --browser firefox` specify Firefox
- `poetry run pytest --headed --browser webkit` WebKit is browser engine Safari uses
- `poetry run pytest --browser firefox  --headed --browser webkit` specify multiple browsers
- `poetry run pytest tests/test_basic_playwright.py` runs all tests in file `test_basic_playwright.py`
- `poetry run pytest --template=html1/index.html --report=report.html` uses `pytest-reporter-html1` module to generate html test result report in `report.html` instead of seeing results in terminal.
- `poetry run pytest --base-url https://example.com` specifies the base url to be used for each test, then just use the path in the tests.

## Configuration
- For examples of configuring command line flags I always want to use, see the `pytest.ini` file. Once in `pytest.ini`, these command line options don't need to be in command line, they'll automatically be included from the file.

## Playwright Code Generator
- `playwright codegen http://uitestingplayground.com` opens page where you can hover over each element, and a separate inspector window. Clicking on elements in the browser adds code in the inspector. The code added in the inspector is standard Playwright Python code, without the Pytest features.
