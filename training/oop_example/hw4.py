from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://demo.applitools.com/#")
    login=page.locator("[id='log-in']")
    login.click()

    url=page.url
    print(url)

    page.close()
    browser.close()
    print ("Test End")