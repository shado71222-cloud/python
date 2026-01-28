class TestCalculator():
    def test_calculator_bmi(self,setup_playwright):
        page=setup_playwright
        page.goto("https://www.calculator.net")
        bmi= page.get_by_text("BMI Calculator")
        bmi.click()
        assert page.url == "https://www.calculator.net/bmi-calculator.html", "wrong url"
        print("end test")

    def test_calculator_by_roll(self,setup_playwright):
        page=setup_playwright
        page.goto("https://www.calculator.net")
        payment=page.get_by_role("link",name="BMI Calculator")
        payment.click()
        assert  page.url=="https://www.calculator.net/bmi-calculator.html"
        print("end test")

    def test_Ebay_byclass(self,setup_playwright):
        page=setup_playwright
        page.goto("https://www.ebay.com")
        task=page.locator(".gh-search-button__advanced-link")
        task.click()
        assert page.url == "https://www.ebay.com/sch/ebayadvsearch", "wrong url"
        print("end test")

    def test_Ebay_byrole(self,setup_playwright):
        page=setup_playwright
        page.goto("https://www.ebay.com")
        task=page.get_by_role("link",name="Advanced")
        task.click()
        assert page.url == "https://www.ebay.com/sch/ebayadvsearch", "wrong url"
        print("end test")

    def test_flights(self,setup_playwright):
        page=setup_playwright
        page.goto("https://demo.guru99.com/test/newtours/reservation.php")
        page.locator("[value='oneway']").click()
        passe=page.locator("[name='passCount']")
        passe.select_option(index=2)
        airlines = page.locator("select[name='airline']")
        airlines.select_option(index=1)
        # page.pause()
        # page.screenshot(path="result.png")
