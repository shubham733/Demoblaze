import time

from playwright.sync_api import Playwright, sync_playwright, expect
from pom.home_page_elements import HomePage
import pytest

@pytest.mark.integration
def test_homepage(login_set_up, assert_snapshot):

    page = login_set_up

    home_page = HomePage(page)

    expect(home_page.product_header).to_be_visible()
    expect(home_page.product_email).to_be_visible()
    time.sleep(2)
    assert_snapshot(page.screenshot(mask=[home_page.product_header]), threshold=1)

