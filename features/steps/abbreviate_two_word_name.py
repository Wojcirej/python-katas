from behave import *
from katas.abbreviate_two_word_name.abbreviate_two_word_name import abbreviate_two_word_name

@given('name = {name}')
def set_up_params_for_abbreviate_two_word_name(context, name):
    context.name = name

@when("function 'abbreviate_two_word_name' called with these params")
def execute_abbreviate_two_word_name(context):
    context.result = abbreviate_two_word_name(context.name)

@then("function 'abbreviate_two_word_name' returns {initials}")
def test_result_of_abbreviate_two_word_name(context, initials):
    assert(context.result == initials)
