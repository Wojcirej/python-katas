from behave import *
import ast
from katas.automorphic_number.automorphic_number import automorphic_number

@given("number = {number}")
def set_up_params_for_automorphic_number(context, number):
    context.number = ast.literal_eval(number)

@when("function 'automorphic_number' is called with these params")
def execute_automorphic_number(context):
    context.automorphic_number_result = automorphic_number(context.number)

@then("function 'automorphic_number' returns {result}")
def test_result_of_automorphic_number(context, result):
    assert(context.automorphic_number_result == ast.literal_eval(result))
