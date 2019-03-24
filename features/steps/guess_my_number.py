from behave import *
import ast
from katas.guess_my_number.guess_my_number import guess_my_number

@given("guess = {guess}")
def set_up_params_for_guess_my_number(context, guess):
    context.guess = ast.literal_eval(guess)

@when("function 'guess_my_number' is called with these params")
def execute_guess_my_number(context):
    context.guess_my_number_result = guess_my_number(context.guess)

@then("function 'guess_my_number' returns {result}")
def test_result_of_guess_my_number(context, result):
    assert(context.guess_my_number_result == ast.literal_eval(result))
