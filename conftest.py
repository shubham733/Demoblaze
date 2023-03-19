import os

import pytest
from playwright.sync_api import Playwright, expect

# import utils.secret_config


@pytest.fixture(scope="function")
def set_up(browser):
    # browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.demoblaze.com/")
    page.set_default_timeout(5000)

    yield page
    page.close()

@pytest.fixture(scope="function")
def login_set_up(set_up):
    # browser = playwright.chromium.launch(headless=False, slow_mo=500)
    # context = browser.new_context()
    # page = context.new_page()

    page = set_up

    page.locator("a[id='login2']").click()
    # page.locator("#loginusername").click()
    page.locator("#loginusername").fill("shubham@619")
    # page.locator("#loginusername").press("Tab")
    # page.locator("#loginpassword").fill(utils.secret_config.PASSWORD)
    page.locator("#loginpassword").fill(os.environ['PASSWORD'])
    page.locator("button:has-text('Log in')").click()
    # assert_issue = True
    # while assert_issue:
    #     if not page.locator("text=Log out").is_visible():
    #         assert page.locator('text=Welcome shubham@619').is_visible()
    #     else:
    expect(page.locator('text=Welcome shubham@619')).to_be_visible()
    # assert page.is_visible("text=Welcome shubham@619") # python specific

    yield page

