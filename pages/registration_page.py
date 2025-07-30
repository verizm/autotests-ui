from playwright.sync_api import Page, expect

from pages.base_page import BasePage


class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.email_input = page.get_by_test_id('registration-form-email-input').locator('input')
        self.user_name_input = page.get_by_test_id('registration-form-username-input').locator('input')
        self.password_input = page.get_by_test_id('registration-form-password-input').locator('input')
        self.registration_button = page.get_by_test_id('registration-page-registration-button')
        self.login_link = page.get_by_test_id('registration-page-login-link')
        self.file_link = page.get_by_title(text="Скачать PDF файл")

    def fill_registration_form(self, email: str, user_name: str, password: str):
        self.email_input.fill(email)
        expect(self.email_input).to_have_value(email)

        self.user_name_input.fill(user_name)
        expect(self.user_name_input).to_have_value(user_name)

        self.password_input.fill(password)
        expect(self.password_input).to_have_value(password)

    def click_registration_button(self):
        self.registration_button.click()

    def click_login_link(self):
        self.login_link.click()
