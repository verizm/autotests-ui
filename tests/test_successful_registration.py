import random

from pages.dashboard_page import DashboardPage
from pages.registration_page import RegistrationPage


def test_successful_registration(registration_page: RegistrationPage, dashboard_page: DashboardPage):
    registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    email = f"user{random.randint(0, 100)}@gmail.com"
    registration_page.fill_registration_form(email=email, user_name="vera", password="1111")
    registration_page.click_registration_button()
    dashboard_page.check_visible_dashboard_title()
