from behave import *
import ast
from katas.total_amount_of_points.total_amount_of_points import total_amount_of_points

@given("games = {games}")
def set_up_params_for_total_amount_of_points(context, games):
    context.games = ast.literal_eval(games)

@when("function 'total_amount_of_points' is called with these params")
def execute_total_amount_of_points(context):
    context.result = total_amount_of_points(context.games)

@then("function 'total_amount_of_points' returns {result:d}")
def test_result_of_total_amount_of_points(context, result):
    assert(context.result == result)
