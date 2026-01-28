class TestSiteButton():

    def test_demoblaze(self, setup_playwright):
        page=setup_playwright
        page.goto("https://www.demoblaze.com")
        page.get_by_role("link", name="Contact").click()
        # page.get_by_role("button", name="Close").first.click()
        page.locator("[class='close']").first.click()
        page.pause()

    def test_zara_sale_bucket(self, setup_playwright):
        page=setup_playwright
        page.goto("https://www.zara.com")
        page.locator('[data-qa-action="go-to-store"]').click()
        # SB=page.locator("[class='layout-header-action__link layout-header-action__link--type-text link']").click()
        sb=page.locator('[data-qa-id="layout-header-go-to-cart"]')
        sbt=sb.inner_text()
        print(sbt)
        assert "0" in sbt,"0 was not found in sale bucket text"
