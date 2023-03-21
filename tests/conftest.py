import os
import pytest
from playwright.sync_api import Playwright, expect

PASSWORD = os.environ['PASSWORD']

@pytest.fixture(scope="function")
def set_up(browser):
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.demoblaze.com/")
    page.set_default_timeout(5000)

    yield page
    page.close()

@pytest.fixture(scope="function")
def login_set_up(set_up):

    page = set_up

    page.locator("a[id='login2']").click()
    page.locator("#loginusername").fill("shubham@619")
    page.locator("#loginpassword").fill(PASSWORD)
    page.locator("button:has-text('Log in')").click()
    expect(page.locator('text=Welcome shubham@619')).to_be_visible()

    yield page

