import re
import pytest 

from stepmanager import step
from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    with step("Opening the webpage"):
        page.goto("https://playwright.dev/")

    with step("Website has title 'Playwright'"):
        expect(page).to_have_title(re.compile("Playwright"))

def test_get_started_link(page: Page):
    with step("Opening the webpage"):
        page.goto("https://playwright.dev/")

    with step("Click the 'Get Started' link"):
        page.get_by_role("link", name="Get started").click()

    with step("Expects page to have the heading with the name of the installation"):
        expect(page.get_by_role("heading", name="Installation")).to_be_visible()
