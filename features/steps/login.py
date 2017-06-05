from behave import *
from pages.loginpage import LoginPage
from pages.homepage import HomePage
from pages.profilepage import ProfilePage

use_step_matcher("re")


@step("User clicked on 'My profile'")
def step_impl(context):
    context.page = HomePage.open_login_page(context)


@when("User login")
def step_impl(context):
    context.page.login()


@then("User should be logged in")
def step_impl(context):
    context.page.is_displayed()
