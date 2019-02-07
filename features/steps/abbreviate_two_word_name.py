from behave import *
from katas.abbreviate_two_word_name.abbreviate_two_word_name import abbreviate_two_word_name

@given('name equals {name}')
def step_impl(context, name):
    context.name = name

@when("called function 'abbreviate_two_word_name'")
def step_impl(context):
    context.result = abbreviate_two_word_name(context.name)

@then("returns {initials}")
def step_impl(context, initials):
    assert(context.result == initials)
