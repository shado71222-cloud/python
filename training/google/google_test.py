import time

class Test_ebay_test:
    def test_search_for_plushies(self,setup_playwright_project_example):
        page=setup_playwright_project_example
        page.goto("https://workspace.google.com/intl/en-US/gmail/")
        page.locator("[class='button button--medium header__aside__button button--desktop button--tablet button--mobile']").click()
        time.sleep(5)
        page.wait_for_selector("#identifierId")
        page.locator("[id='identifierId']").fill("shado71222")
        print("fuck")
