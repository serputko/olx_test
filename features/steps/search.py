from behave import *

from pages.homepage import HomePage
from pages.searchpage import SearchPage

use_step_matcher("re")


@step("User is on 'Main' page")
def step_impl(context):
    context.page = HomePage(context).open()


@step("User filled search field with (?P<search>.+)")
def step_impl(context, search):
    context.page.input_search(search)


@step("Clicked on Search button")
def step_impl(context):
    context.page = context.page.search()


@step("Selected (?P<category>.+) from the Categories")
def step_impl(context, category):
    context.page = context.page.select_category(category)


@step("A list of adverts with a (?P<search>.+) is displayed")
def step_impl(context, search):
    context.page = context.page.assert_results_consists(search)


@step("Selected all types of goods")
def step_impl(context):
    context.page.select_type_of_items('All')


@step("Selected private types of goods")
def step_impl(context):
    context.page.select_type_of_items('Private')


@step("Selected business types of goods")
def step_impl(context):
    context.page.select_type_of_items('Business')


@step("Applied new sort filter")
def step_impl(context):
    context.page.select_sorting_type('New')


@step("Applied cheap sort filter")
def step_impl(context):
    context.page.select_sorting_type('Cheap')


@step("Applied expensive sort filter")
def step_impl(context):
    context.page.select_sorting_type('Expensive')


@step("Selected currency Hryvna")
def step_impl(context):
    context.page.select_currency('HRN')


@step("Selected currency USD")
def step_impl(context):
    context.page.select_currency('USD')


@step("Selected currency EUR")
def step_impl(context):
    context.page.select_currency('EUR')
