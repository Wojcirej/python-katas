import os

class KataGenerator:

    def __init__(self, kata_name, logger, templater, params=[], data=[]):
        self.kata_name = kata_name
        self.kata_root_directory_path = "katas/" + kata_name
        self.kata_module_file_path = "katas/{}/__init__.py".format(kata_name)
        self.kata_readme_file_path = "katas/{}/README.md".format(kata_name)
        self.kata_definition_file_path = "katas/{}/{}.py".format(kata_name, kata_name)
        self.kata_test_scenarios_file_path = "features/{}.feature".format(kata_name)
        self.kata_test_steps_file_path = "features/steps/{}.py".format(kata_name)
        self.logger = logger
        self.templater = templater
        self.params = params
        self.data = data

    def call(self):
        self.create_main_directory()
        self.logger.log_directory_creation(self.kata_root_directory_path)
        self.create_kata_module_file()
        self.logger.log_file_generation(self.kata_module_file_path)
        self.create_readme_file()
        self.logger.log_file_generation(self.kata_readme_file_path)
        self.create_kata_definition_file()
        self.logger.log_file_generation(self.kata_definition_file_path)
        self.create_kata_test_scenarios_file()
        self.logger.log_file_generation(self.kata_test_scenarios_file_path)
        self.create_kata_test_steps_file()
        self.logger.log_file_generation(self.kata_test_steps_file_path)

    def create_main_directory(self):
        os.mkdir(self.kata_root_directory_path)

    def create_kata_module_file(self):
        open(self.kata_module_file_path, "w+")

    def create_readme_file(self):
        read_me_file = open(self.kata_readme_file_path, "w+")
        read_me_file.write(self.templater.readme_file_template_content())
        read_me_file.close()

    def create_kata_definition_file(self):
        kata_file = open(self.kata_definition_file_path, "w+")
        kata_file.write(self.templater.kata_definition_file_content())
        kata_file.close()

    def create_kata_test_scenarios_file(self):
        test_scenarios_file = open(self.kata_test_scenarios_file_path, "w+")
        test_scenarios_file.write(self.templater.kata_test_scenarios_file_content())
        test_scenarios_file.write(self.templater.insert_scenario_examples(self.data))
        test_scenarios_file.close()

    def create_kata_test_steps_file(self):
        test_steps_file = open(self.kata_test_steps_file_path, "w+")
        test_steps_file.write(self.templater.kata_test_steps_file_content())
        test_steps_file.close()
