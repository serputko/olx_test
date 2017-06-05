from behave import *
from pages.loginpage import LoginPage
from pages.homepage import HomePage
from pages.profilepage import ProfilePage

use_step_matcher("re")


@step("User clicked on 'My profile'")
def step_impl(context):
    context.page = HomePage.open_login_page(context)


@step("User login with valid credentials")
def step_impl(context):
    context.page = context.page.login_with_valid_credentials()


@step("User should be logged in")
def step_impl(context):
    context.page.is_displayed()


@step("User login with invalid credentials")
def step_impl(context):
    context.page.login_with_invalid_credentials()


@step("Error message should be displayed")
def step_impl(context):
    context.page.wrong_password_error_message_is_displayed()