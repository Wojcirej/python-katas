from lib.table_examples_generator import TableExamplesGenerator

class KataGeneratorTemplater:

    def __init__(self, kata_name, params):
        self.kata_name = kata_name
        self.params = params
        self.params_count = len(params)

    def readme_file_template_content(self):
        readme = (
            f"""# {self.humanize_kata_name()}\n\n"""
            f"""### Description\n"""
            f"""<!-- Add description of the kata here -->\n\n"""
            f"""### Examples\n"""
            f"""<!-- Add examples/test cases here -->\n\n"""
            f"""### Link to kata on codewars.com\n"""
            )
        return readme

    def kata_definition_file_content(self):
        params_string = ""
        if self.params:
            params_string = ", ".join(self.params)
        content = (
            f"""def {self.kata_name}({params_string}):\n"""
            f"""    #TODO insert definition of the function here..."""
            )
        return content

    def kata_test_scenarios_file_content(self):
        content = (
            f"""Feature: {self.humanize_kata_name()}\n\n"""
            f"""  Scenario Outline: One of many test cases\n"""
            f"""    Given {self.format_params_string_for_given_clause()}\n"""
            f"""    When function '{self.kata_name}' is called with these params\n"""
            f"""    Then function '{self.kata_name}' returns <result>"""
        )
        return content

    def insert_scenario_examples(self, data):
        if data == []:
            return ""
        content = "\n\n    Examples:\n"
        content += TableExamplesGenerator(data).call()
        return content

    def kata_test_steps_file_content(self):
        content = (
            f"""from behave import *\n"""
            f"""import ast\n"""
            f"""from katas.{self.kata_name}.{self.kata_name} import {self.kata_name}\n\n"""
            f"""@given("{self.format_params_string_for_given_decorator()}")\n"""
            f"""def set_up_params_for_{self.kata_name}({self.format_params_string_for_given_method_arguments()}):\n"""
            f"""{self.format_params_string_for_given_method_definition()}\n"""
            f"""@when("function '{self.kata_name}' is called with these params")\n"""
            f"""def execute_{self.kata_name}(context):\n"""
            f"""    context.{self.kata_name}_result = {self.kata_name}({self.format_params_for_method_call()})\n\n"""
            f"""@then("function '{self.kata_name}' returns {{result}}")\n"""
            f"""def test_result_of_{self.kata_name}(context, result):\n"""
            f"""    assert(context.{self.kata_name}_result == ast.literal_eval(result))"""
        )
        return content

    def humanize_kata_name(self):
        return " ".join(self.kata_name.split("_")).capitalize()

    def format_params_string_for_given_clause(self):
        content = ""
        if self.params_count == 0:
            return "no params"
        position = 0
        for param in self.params:
            position += 1
            content += "{} = <{}>".format(param, param)
            if position < self.params_count:
                content += ", "
        return content

    def format_params_string_for_given_decorator(self):
        content = ""
        if self.params_count == 0:
            return "no params"
        position = 0
        for param in self.params:
            position += 1
            content += f"{param} = {{{param}}}"
            if position < self.params_count:
                content += ", "
        return content

    def format_params_string_for_given_method_arguments(self):
        content = "context"
        if self.params_count == 0:
            return content
        content += ", "
        content += ", ".join(self.params)
        return content

    def format_params_string_for_given_method_definition(self):
        content = ""
        for param in self.params:
            content += f"    context.{param} = {param}\n"
        return content

    def format_params_for_method_call(self):
        content = ""
        position = 0
        for param in self.params:
            position += 1
            content += f"context.{param}"
            if position < self.params_count:
                content += ", "
        return content
