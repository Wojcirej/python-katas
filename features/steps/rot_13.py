from behave import *
import ast
from katas.rot_13.rot_13 import rot_13

@given("input = {input}")
def set_up_params_for_rot_13(context, input):
    context.input = input

@when("function 'rot_13' is called with these params")
def execute_rot_13(context):
    context.rot_13_result = rot_13(context.input)

@then("function 'rot_13' returns {result}")
def test_result_of_rot_13(context, result):
    assert(context.rot_13_result == result)
