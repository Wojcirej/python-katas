import os

class TestExamplesParser(object):

    def __init__(self, kata_name):
        self.kata_name = kata_name
        self.test_examples_source_path = "test_examples/{}.txt".format(kata_name)

    def parse(self):
        source = open(self.test_examples_source_path, "r")
        final = []
        for line in source:
            final.append(tuple(line.rstrip().split(", ")))
        return final
