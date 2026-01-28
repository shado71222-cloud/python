from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.saucedemo.com/")
    user=page.locator("[id='user-name']")
    user.fill("standard_user")
    password=page.locator("[id='password']")
    password.fill("secret_sauce")
    login=page.locator("[id='login-button']")
    login.click()

    url=page.url
    print(url)

    page.close()
    browser.close()
    print ("Test End")