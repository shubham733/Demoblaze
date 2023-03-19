import time
import pytest
from playwright.sync_api import Playwright, sync_playwright, expect

@pytest.mark.smoke
@pytest.mark.regression
def test_login(set_up):

    page = set_up

    page.locator("a[id='login2']").click()
    # page.locator("#loginusername").click()
    page.locator("#loginusername").fill("shubham@619")
    # page.locator("#loginusername").press("Tab")
    page.locator("#loginpassword").fill("123")
    page.locator("button:has-text('Log in')").click()
    # assert_issue = True
    # while assert_issue:
    #     if not page.locator("text=Log out").is_visible():
    #         assert page.locator('text=Welcome shubham@619').is_visible()
    #     else:
    expect(page.locator('text=Welcome shubham@619')).to_be_visible()
    # assert page.is_visible("text=Welcome shubham@619") # python specific

    # page.pause()


# def test_login_2(login_set_up):
#
#     page = login_set_up

    # page.locator("a[id='login2']").click()
    # # page.locator("#loginusername").click()
    # page.locator("#loginusername").fill("shubham@619")
    # # page.locator("#loginusername").press("Tab")
    # page.locator("#loginpassword").fill("123")
    # page.locator("button:has-text('Log in')").click()
    # # assert_issue = True
    # # while assert_issue:
    # #     if not page.locator("text=Log out").is_visible():
    # #         assert page.locator('text=Welcome shubham@619').is_visible()
    # #     else:
    # expect(page.locator('text=Welcome shubham@619')).to_be_visible()




