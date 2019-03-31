from behave import *
import ast
from katas.password_validation.password_validation import password_validation

@given("password = {password}")
def set_up_params_for_password_validation(context, password):
    context.password = ast.literal_eval(password)

@when("function 'password_validation' is called with these params")
def execute_password_validation(context):
    context.password_validation_result = password_validation(context.password)

@then("function 'password_validation' returns {result}")
def test_result_of_password_validation(context, result):
    assert(context.password_validation_result == ast.literal_eval(result))
