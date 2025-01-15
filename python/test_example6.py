import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://demo.playwright.dev/todomvc/#/")
    page.get_by_placeholder("What needs to be done?").click()
    page.get_by_placeholder("What needs to be done?").fill("read books")
    page.get_by_placeholder("What needs to be done?").press("Enter")
    page.get_by_placeholder("What needs to be done?").fill("eat")
    page.get_by_placeholder("What needs to be done?").press("Enter")
    page.get_by_role("link", name="Active").click()
    page.get_by_role("link", name="Completed").click()
    expect(page.get_by_placeholder("What needs to be done?")).to_be_visible()
    page.get_by_role("link", name="All").click()
    page.locator("li").filter(has_text="read books").get_by_label("Toggle Todo").check()
    expect(page.locator("body")).to_contain_text("eat")
    page.get_by_role("link", name="Completed").click()
    expect(page.get_by_test_id("todo-title")).to_be_visible()
