from behave import *
import ast
from katas.is_divisible.is_divisible import is_divisible

@given("n = {n:d}, x = {x:d}, y = {y:d}")
def set_up_params_for_is_divisible(context, n, x, y):
    context.n = n
    context.x = x
    context.y = y

@when("function 'is_divisible' is called with these params")
def execute_is_divisible(context):
    context.is_divisible_result = is_divisible(context.n, context.x, context.y)

@then("function 'is_divisible' returns {result}")
def test_result_of_is_divisible(context, result):
    assert(context.is_divisible_result == ast.literal_eval(result))
