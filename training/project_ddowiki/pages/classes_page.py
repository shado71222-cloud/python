class ClassesPage:
    def __init__(self, page):
        self.page = page

    def hit_die_check(self, class_name):
        self.page.get_by_role("link", name="classes").first.click()
        self.page.get_by_role("link", name=class_name).first.click()
        hit_dice_line = self.page.get_by_text("Hit di", exact=False).locator("..").locator("..").locator("..").inner_text()
        alignment_failsafe_parts = hit_dice_line.split(":")
        # the wiki is inconsistent and some classes has their alignment in the same lien as the hit die this makes help
        # making sure i take the last : in case the lines are fused in the wiki
        only_dice = alignment_failsafe_parts[-1].strip()
        print(f"\nThe {class_name} class uses a {only_dice} for their hp")
        return only_dice

    def spellcasting_check(self, class_name):
        self.page.get_by_role("link", name="classes").first.click()
        self.page.get_by_role("link", name=class_name).first.click()
        find_table = self.page.get_by_text("Table: The").locator("..").locator("..").locator("..").inner_text()
        if "spell points" in find_table.lower():
            caster = True
        else:
            caster = False
        return caster
