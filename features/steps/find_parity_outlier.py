from behave import *
import ast
from katas.find_parity_outlier.find_parity_outlier import find_parity_outlier

@given("integers = {integers}")
def set_up_params_for_find_parity_outlier(context, integers):
    context.integers = ast.literal_eval(integers)

@when("function 'find_parity_outlier' is called with these params")
def execute_find_parity_outlier(context):
    context.find_parity_outlier_result = find_parity_outlier(context.integers)

@then("function 'find_parity_outlier' returns {result}")
def test_result_of_find_parity_outlier(context, result):
    assert(context.find_parity_outlier_result == ast.literal_eval(result))
