from behave import *
import ast
from katas.array_diff.array_diff import array_diff

@given("first_array = {first_array}, second_array = {second_array}")
def set_up_params_for_array_diff(context, first_array, second_array):
    context.first_array = ast.literal_eval(first_array)
    context.second_array = ast.literal_eval(second_array)

@when("function 'array_diff' is called with these params")
def execute_array_diff(context):
    context.array_diff_result = array_diff(context.first_array, context.second_array)

@then("function 'array_diff' returns {result}")
def test_result_of_array_diff(context, result):
    assert(context.array_diff_result == ast.literal_eval(result))
