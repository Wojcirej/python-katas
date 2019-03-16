from behave import *
from lib.test_examples_parser import TestExamplesParser

@given("underscored kata name")
def set_up_preconditions_for_test_examples_parser(context):
    context.parser = TestExamplesParser("test_kata")

@when("method 'parse' is called")
def execute_parser(context):
    context.result = context.parser.parse()

@then("method 'parse' returns list")
def test_for_parser_returning_list(context):
    assert(isinstance(context.result, list) == True)

@then("list contains tuples")
def test_for_parser_returning_list_of_tuples(context):
    lol = [isinstance(item, tuple) for item in context.result]
    assert(lol == [True, True, True])

@then("list contains as much tuples as lines in source file")
def test_for_parser_returning_tuple_for_each_line(context):
    assert(len(context.result) == 3)
