from training.project_ddowiki.pages.classes_page import ClassesPage
from training.project_ddowiki.pages.main_page import MainPage

#classes example (barbarian,wizard,fighter,cleric,rogue)
#some tests are using try and except in case the search is faulty so it doesnt crush the rest of the tests

class Test_ddowiki:
    # goes to the wiki and put the text into the search bar and clicks search
    def test_basic_search(self,setup_playwright_project_wiki):
        search="shuriken"
        page = setup_playwright_project_wiki
        main_page=MainPage(page)
        main_page.search_bar(search)
        assert page.url.lower() == "https://ddowiki.com/page/"+search.lower(),"page not as expected"

        # by entering a name of a class from the game it will go to that
        # class page in the wiki and tell you which type of die they use for hp
        # the result should be "dX" where the x is the number
    def test_hit_die_check(self,setup_playwright_project_wiki):
        page = setup_playwright_project_wiki
        classes_page=ClassesPage(page)
        results_hit_dice=classes_page.hit_die_check("barbarian")
        assert "d" in results_hit_dice and len(results_hit_dice) <= 3, "couldn't find a hit die for the class"

        #goes into a class page and checks if they have the spellcasting option
        #by a joined system they all use called spell points, if they get spell point
        #on level up they return as spellcaster
    def test_spellcasting_check(self,setup_playwright_project_wiki):
        page = setup_playwright_project_wiki
        classes_page=ClassesPage(page)
        result_spellcasting_check=classes_page.spellcasting_check("wizard")
        assert result_spellcasting_check==True , "class is not a spellcaster"

        #checks that we returned to home page but also that the search actually happened
    def test_return_to_home_page(self,setup_playwright_project_wiki):
        search = "den_of_vipers"
        page = setup_playwright_project_wiki
        main_page=MainPage(page)
        searched_result=main_page.search_bar(search)
        main_page.return_to_home_page()
        assert page.url == "https://ddowiki.com/page/Home" and searched_result.lower() == "https://ddowiki.com/page/"+search.lower(),"page not as expected"

        #check what equipment slot the search item goes too
        #weapons don't count as equipment slots*
        #example for item names: black_widow_bracers,witchdoctor's_Mantle,cloak_of_the_Zephyr
        #exampe for items that will fail:sword_of_shadow
    def test_equipment_slot_check(self,setup_playwright_project_wiki):
        search="cloak_of_the_Zephyr"
        page = setup_playwright_project_wiki
        main_page=MainPage(page)
        main_page.search_bar(search)
        slot_result=main_page.equipment_slot_check()
        assert slot_result==True, "couldn't find equipment slot"

    #check if 1 class get more hitpoints than another class.
    def test_who_gets_more_hitpoints(self,setup_playwright_project_wiki):
        first_class="barbarian"
        second_class="wizard"
        page = setup_playwright_project_wiki
        classes_page = ClassesPage(page)
        first_class_result = classes_page.hit_die_check(first_class).replace("d","")
        second_class_result = classes_page.hit_die_check(second_class).replace("d","")
        assert int(first_class_result)>int(second_class_result),f"{first_class} doesn't get more hitpoints than {second_class}"

        #checks for an item weight and plat value(the currency of the game) and tells you how much its worth per weight unit
        #example for item names: black_widow_bracers,witchdoctor's_Mantle,cloak_of_the_Zephyr,sword_of_shadow
        #if you search for a non-item page or item without these values you will get 0 as the result
    def test_plat_per_weight(self,setup_playwright_project_wiki):
        search = "black_widow_bracers"
        page = setup_playwright_project_wiki
        main_page = MainPage(page)
        main_page.search_bar(search)
        plat_per_wei_result=main_page.plat_per_weight(search)
        assert plat_per_wei_result>0, "couldn't find needed values"
