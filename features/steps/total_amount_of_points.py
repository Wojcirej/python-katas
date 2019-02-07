from behave import *
import ast
from katas.total_amount_of_points.total_amount_of_points import total_amount_of_points

@given("a {games}")
def step_impl(context, games):
    context.games = ast.literal_eval(games)

@when("function 'total_amount_of_points' called")
def step_impl(context):
    context.result = total_amount_of_points(context.games)

@then("it returns {result:d}")
def step_impl(context, result):
    assert(context.result == result)
