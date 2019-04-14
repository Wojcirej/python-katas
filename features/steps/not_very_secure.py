from behave import *
import ast
from katas.not_very_secure.not_very_secure import not_very_secure

@given("string = {string}")
def set_up_params_for_not_very_secure(context, string):
    context.string = ast.literal_eval(string)

@when("function 'not_very_secure' is called with these params")
def execute_not_very_secure(context):
    context.not_very_secure_result = not_very_secure(context.string)

@then("function 'not_very_secure' returns {result}")
def test_result_of_not_very_secure(context, result):
    assert(context.not_very_secure_result == ast.literal_eval(result))
