from behave import *
import ast
from lib.kata_generator_templater import KataGeneratorTemplater

@given("kata name underscored")
def set_up_params_for_humanize_kata_name(context):
    context.templater = KataGeneratorTemplater("underscored_kata_name", [])

@when("method 'humanize_kata_name' is called")
def execute_humanize_kata_name(context):
    context.humanize_kata_name_result = context.templater.humanize_kata_name()

@then("it returns kata name with separated words")
def test_separation_of_words(context):
    assert(context.humanize_kata_name_result == "Underscored kata name")

@then("capitalized first letter")
def test_capitalization_of_first_letter(context):
    assert(context.humanize_kata_name_result[0] == "U")

@given("params = {params}")
def set_up_params_for_format_params_string_for_given_clause(context, params):
    context.templater = KataGeneratorTemplater("test", ast.literal_eval(params))

@when("method 'format_params_string_for_given_clause' called")
def execute_format_params_string_for_given_clause(context):
    context.format_params_for_given_clause_result = context.templater.format_params_string_for_given_clause()

@then("method 'format_params_string_for_given_clause' returns {result}")
def test_format_params_for_given_clause_result(context, result):
    assert(context.format_params_for_given_clause_result == ast.literal_eval(result))

@given("array of params = {params}")
def set_up_params_for_format_params_string_for_given_decorator(context, params):
    context.templater = KataGeneratorTemplater("test", ast.literal_eval(params))

@when("method 'format_params_string_for_given_decorator' called")
def execute_format_params_string_for_given_decorator(context):
    context.format_params_for_given_decorator_result = context.templater.format_params_string_for_given_decorator()

@then("method 'format_params_string_for_given_decorator' returns {result}")
def test_format_params_for_given_decorator_result(context, result):
    assert(context.format_params_for_given_decorator_result == ast.literal_eval(result))

@given("params like {params}")
def set_up_params_for_format_params_string_for_given_method_arguments(context, params):
    context.templater = KataGeneratorTemplater("test", ast.literal_eval(params))

@when("method 'format_params_string_for_given_method_arguments' called")
def execute_format_params_string_for_given_method_arguments(context):
    context.format_params_for_given_method_arguments_result = context.templater.format_params_string_for_given_method_arguments()

@then("method 'format_params_string_for_given_method_arguments' returns {result}")
def test_format_params_for_given_method_arguments_result(context, result):
    assert(context.format_params_for_given_method_arguments_result == ast.literal_eval(result))

@given("set of params = {params}")
def set_up_params_for_format_params_string_for_given_method_definition(context, params):
    context.templater = KataGeneratorTemplater("test", ast.literal_eval(params))

@when("method 'format_params_string_for_given_method_definition' called")
def execute_format_params_string_for_given_method_definition(context):
    context.format_params_for_given_method_definition_result = context.templater.format_params_string_for_given_method_definition()

@then("method 'format_params_string_for_given_method_definition' returns {result}")
def test_format_params_for_given_method_definition_result(context, result):
    assert(context.format_params_for_given_method_definition_result == ast.literal_eval(result))

@given("list of params = {params}")
def set_up_params_for_format_params_for_method_call(context, params):
    context.templater = KataGeneratorTemplater("test", ast.literal_eval(params))

@when("method 'format_params_for_method_call' called")
def execute_format_params_for_method_call(context):
    context.format_params_for_method_call_result = context.templater.format_params_for_method_call()

@then("method 'format_params_for_method_call' returns {result}")
def test_format_params_for_method_call_result(context, result):
    assert(context.format_params_for_method_call_result == ast.literal_eval(result))
