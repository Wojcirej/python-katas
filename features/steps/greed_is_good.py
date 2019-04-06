from behave import *
import ast
from katas.greed_is_good.greed_is_good import greed_is_good

@given("dice = {dice}")
def set_up_params_for_greed_is_good(context, dice):
    context.dice = ast.literal_eval(dice)

@when("function 'greed_is_good' is called with these params")
def execute_greed_is_good(context):
    context.greed_is_good_result = greed_is_good(context.dice)

@then("function 'greed_is_good' returns {result}")
def test_result_of_greed_is_good(context, result):
    assert(context.greed_is_good_result == ast.literal_eval(result))
