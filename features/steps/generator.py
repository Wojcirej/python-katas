from behave import *
import os
from lib.kata_generator import KataGenerator
from lib.kata_generator_logger import KataGeneratorLogger
from lib.kata_generator_templater import KataGeneratorTemplater

@given("kata_name = 'test_kata'")
def set_up_test_kata_name(context):
    context.logger = KataGeneratorLogger()
    context.templater = KataGeneratorTemplater('test_kata', [])
    context.generator = KataGenerator('test_kata', context.logger, context.templater)

@when("method 'call' of class KataGenerator called")
def execute_test(context):
    context.generator.call()

@then("it creates 'test_kata' directory inside 'katas' directory")
def test_kata_main_directory_creation_result(context):
    assert(os.path.isdir("./katas/test_kata") == True)

@then("creates '__init__.py' file inside 'test_kata' directory")
def test_kata_module_file_existence(context):
    assert(os.path.isfile("./katas/test_kata/__init__.py") == True)

@then("creates 'README.md' file inside 'test_kata' directory")
def test_kata_readme_file_existence(context):
    assert(os.path.isfile("./katas/test_kata/README.md") == True)

@then("creates 'test_kata.py' file inside 'test_kata' directory")
def test_kata_definition_file_existence(context):
    assert(os.path.isfile("./katas/test_kata/test_kata.py") == True)

@then("creates 'test_kata.feature' file inside 'features' directory")
def test_kata_test_scenarios_file_existence(context):
    assert(os.path.isfile("./features/test_kata.feature") == True)

@then("creates 'test_kata.py' file inside 'features/steps' directory")
def test_kata_test_steps_file_existence(context):
    assert(os.path.isfile("./features/steps/test_kata.py") == True)
