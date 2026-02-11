class SearchPage():
    def __init__(self,page):
        self.page = page

    def search_for_item(self,item:str):
        search_menu=self.page.locator("[id='gh-ac']")
        search_menu.click()
        search_menu.fill(item)
        self.page.get_by_role("button",name="search").click()

    def get_result_after_search(self):
        print("getting results...")
        text=self.page.locator("[class='srp-controls__count-heading']").inner_text()
        # if "+" in text:
        #     index=text.index("+")
        #     text=text[:index]
        # if "," in text:
        #     text=text.replace(",","")
        # if "+" not in text:
        #     index=text.index("result")
        #     text=text[:index]
        text=text.replace(",","")
        text=text.replace("+","")
        index=text.index("result")
        text=text[:index]
        return text

    def click_on_advanced_link(self):
        self.page.get_by_role("link",name="Advanced").click()
