from playwright.sync_api import sync_playwright
import time


def go_to_race():
    race_search = "elf"
    # race_search = input("enter race here : ")
    # race_search=race_search.replace(" ", "-")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://ddowiki.com/page/Races")
        p="/page/"
        page.locator(f"[href='{p + page.get_by_text(race_search).first.inner_text()}']").first.click()
go_to_race()