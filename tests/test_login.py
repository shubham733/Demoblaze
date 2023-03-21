import time
import pytest
from playwright.sync_api import Playwright, sync_playwright, expect

@pytest.mark.smoke
@pytest.mark.regression
def test_login(login_set_up):

    page = login_set_up

    expect(page.locator('text=Welcome shubham@619')).to_be_visible()
