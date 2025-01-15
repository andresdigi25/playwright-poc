import re
import pytest
from playwright.sync_api import Page, expect

@pytest.fixture(scope="function", autouse=False)
def before_each_after_each(page: Page):
    print("before test runs")
    page.goto("https://playwright.dev/")
    yield
    print("after test runs")

def test_page_has_title(page: Page, before_each_after_each):
    page.goto("https://playwright.dev/")
    expect(page).to_have_title(re.compile("Fast and reliable"))        

def test_main_navigation(page: Page, before_each_after_each):
    expect(page).to_have_url("https://playwright.dev/")