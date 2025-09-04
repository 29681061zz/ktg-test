from pages.login_page import LoginPage

class TestLogin:
    def test_login_success(self, driver):
        login_page = LoginPage(driver)
        assert login_page.login()
