from playwright.sync_api import Playwright, sync_playwright, expect
from pom.home_page_elements import HomePage
import pytest

@pytest.mark.integration
def test_homepage(login_set_up):

    page = login_set_up

    home_page = HomePage(page)

    expect(home_page.product_header).to_be_visible()
    expect(home_page.product_email).to_be_visible()

