import time
from behave import *
from pages.homepage import HomePage
from pages.searchpage import SearchPage

use_step_matcher("re")


@given("User is on 'Main' page")
def step_impl(context):
    HomePage(context).open()


@when("User filled search field with (?P<search>.+)")
def step_impl(context, search):
    HomePage(context).input_search(search)


@then("Clicked on Search button")
def step_impl(context):
    HomePage(context).search()


@step("Selected (?P<category>.+) from the Categories")
def step_impl(context, category):
    SearchPage(context).select_category(category)


@then("A list of adverts with a (?P<search>.+)")
def step_impl(context, search):
    SearchPage(context).assert_results_consists(search)





