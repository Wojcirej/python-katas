from lib.kata_generator import KataGenerator
from lib.kata_generator_logger import KataGeneratorLogger
from lib.kata_generator_templater import KataGeneratorTemplater
from lib.test_examples_parser import TestExamplesParser
from sys import argv

argv.pop(0)
kata_name = argv.pop(0)
params = argv
logger = KataGeneratorLogger()
templater = KataGeneratorTemplater(kata_name, params)
data = TestExamplesParser(kata_name).parse()
KataGenerator(kata_name, logger, templater, params, data).call()
