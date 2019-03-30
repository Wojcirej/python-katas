from behave import *
import ast
from katas.your_order_please.your_order_please import your_order_please

@given("sentence = {sentence}")
def set_up_params_for_your_order_please(context, sentence):
    context.sentence = ast.literal_eval(sentence)

@when("function 'your_order_please' is called with these params")
def execute_your_order_please(context):
    context.your_order_please_result = your_order_please(context.sentence)

@then("function 'your_order_please' returns {result}")
def test_result_of_your_order_please(context, result):
    assert(context.your_order_please_result == ast.literal_eval(result))
