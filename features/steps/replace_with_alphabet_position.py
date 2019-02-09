from behave import *
import ast
from katas.replace_with_alphabet_position.replace_with_alphabet_position import alphabet_position

@given("text = {input}")
def set_up_params_for_alphabet_position(context, input):
    context.input = input

@when("function 'alphabet_position' called with these params")
def execute_alphabet_position(context):
    context.alphabet_position_result = alphabet_position(context.input)

@then("function 'alphabet_position' returns {result}")
def test_result_of_alphabet_position(context, result):
    print("Result: {}".format(result))
    assert(context.alphabet_position_result == result)
