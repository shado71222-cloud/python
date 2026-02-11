import re
class MainPage():
    def __init__(self,page):
        self.page=page

    def search_bar(self,search:str):
        search_line=self.page.locator(".vector-search-box-input")
        search_line.fill(search)
        self.page.locator("#searchButton").click()
        searched_page=self.page.url
        return searched_page

    def return_to_home_page(self):
        self.page.locator(".mw-wiki-logo").click()

    def equipment_slot_check(self):
        try:
            slot_finder = self.page.locator(".mw-redirect").locator("xpath=ancestor::tr").filter(has=self.page.locator("[title='Slot']"))
            slot_finder.wait_for(state="attached", timeout=4000)
            row_split = slot_finder.locator("> *").nth(1)
            slot_type=row_split.inner_text().strip()
            print(f"this item is used in the {slot_type} slot")
            slot=True
        except:
            slot=False
        return slot

    def plat_per_weight(self,search):
        try:
            raw_plat_finder=self.page.locator(".bg-color-1").locator("xpath=ancestor::tr").filter(has_text="Base Value")
            raw_plat_finder.wait_for(state="attached", timeout=3000)
            raw_weight_finder = self.page.locator(".bg-color-1").locator("xpath=ancestor::tr").filter(has_text="Weight")
            raw_weight_finder.wait_for(state="attached", timeout=3000)
            weight_finder=raw_weight_finder.inner_text()
            plat_finder=raw_plat_finder.inner_text()
            plat_value = float(re.sub(r'[^\d.]', '', plat_finder))
            weight_value = float(re.sub(r'[^\d.]', '',weight_finder))
            plat_per_wei=plat_value/weight_value
            print(f"{search} is worth {plat_per_wei} plat for each lbs")
            return plat_per_wei
        except:
            return 0