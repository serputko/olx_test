from behave import *
import behave
from behave_tests.pages.homepage import HomePage

use_step_matcher("re")


class LoginSteps(behave.matchers.Matcher):
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
