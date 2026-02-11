from playwright.sync_api import expect
from training.proj_example.page.search_page import SearchPage



class Test_ebay_test:
    def test_search_for_plushies(self,setup_playwright_project_example):
        page=setup_playwright_project_example
        page.goto("https://www.ebay.com")
        search_page=SearchPage(page)
        search_page.search_for_item("plushies")
        text=search_page.get_result_after_search()
        page.wait_for_timeout(3000)
        print(text)
        assert  int(text) > 0, "couldn't find results"

    def test_s(self,setup_playwright_project_example):
        page=setup_playwright_project_example
        page.goto("https://www.ebay.com")
        search_page=SearchPage(page)
        search_page.click_on_advanced_link()
        expect (page).to_have_url("https://www.ebay.com/sch/ebayadvsearch")
        # assert page.url=="https://www.ebay.com/sch/ebayadvsearch" ,"unexpected result"
        assert page.title()=="Advanced Search | eBay" ,"unexpected page title"
