from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.wikipedia.org")

    search = page.locator("[id='searchInput']")
    search.click()
    search.clear()
    search.fill("cats")
    search_button = page.locator("[name='pure-button pure-button-primary-progressive']")
    search_button.click()

    browser.close()
    print ("Test End")