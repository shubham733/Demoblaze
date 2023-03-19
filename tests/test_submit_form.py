import pytest
from playwright.sync_api import Playwright, sync_playwright
from pom.contact_page import ContactPage

@pytest.mark.regression
def test_submit_form(login_set_up):

    page = login_set_up

    contact_us = ContactPage(page)

    contact_us.navigate()
    contact_us.submit_form("shubham619@gmail.com", "Shubham", "Site is running slowly")

