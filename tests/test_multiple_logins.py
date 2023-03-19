import time
import pytest
from playwright.sync_api import Playwright, sync_playwright, expect

@pytest.mark.parametrize("email", ["shubham@619",
                                             pytest.param("shubham", marks=pytest.mark.xfail),
                                             pytest.param("619", marks=pytest.mark.xfail)])
@pytest.mark.parametrize("password", ["123",
                                             pytest.param("1", marks=pytest.mark.xfail),
                                             pytest.param("23", marks=pytest.mark.xfail)])
def test_multiple_logins(set_up, email, password):

    page = set_up

    page.locator("a[id='login2']").click()
    page.locator("#loginusername").fill(email)
    page.locator("#loginpassword").fill(password)
    page.locator("button:has-text('Log in')").click()
    expect(page.locator('text=Welcome shubham@619')).to_be_visible()
