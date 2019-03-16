from behave import *
from lib.table_examples_generator import TableExamplesGenerator

@given("set of data as list of tuples")
def set_up_test_data(context):
    context.data = [('what', 'how', 'who'),
             ('lorem', 'that is a long value', 3.1415),
             ('ipsum', 89798, 0.2)]
    context.table_generator = TableExamplesGenerator(context.data)

@when("method 'calculate_columns_sizes' is called")
def execute_calculate_columns_sizes_method(context):
    context.table_generator.calculate_columns_sizes()


@then("it sets 'column_sizes' property")
def test_column_sizes_presence(context):
    assert(context.table_generator.column_sizes != [])

@then("with the biggest size of item in each column")
def test_column_sizes_contents(context):
    assert(context.table_generator.column_sizes == [5, 20, 6])
