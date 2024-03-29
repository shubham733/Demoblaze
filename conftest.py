import os
import time
import pytest
from playwright.sync_api import Playwright, expect

PASSWORD = os.environ['PASSWORD']

@pytest.fixture(scope="session")
def context_creation(playwright):
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://www.demoblaze.com/")
    page.set_default_timeout(5000)

    page.locator("a[id='login2']").click()
    page.locator("#loginusername").fill("shubham@619")
    page.locator("#loginpassword").fill(PASSWORD)
    page.locator("button:has-text('Log in')").click()
    page.wait_for_load_state(timeout=10000)

    yield context


@pytest.fixture()
def login_set_up(context_creation):
    context = context_creation
    page = context.new_page()

    page.goto("https://www.demoblaze.com/")
    page.set_default_timeout(5000)

    yield page
    page.close()

