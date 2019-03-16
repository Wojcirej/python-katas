import os, shutil

def after_feature(context, feature):
    if 'with_clean_up' in feature.tags:
        if os.path.isdir("katas/test_kata") == True:
            shutil.rmtree("katas/test_kata")
        if os.path.isfile("features/test_kata.feature") == True:
            os.remove("features/test_kata.feature")
        if os.path.isfile("features/steps/test_kata.py") == True:
            os.remove("features/steps/test_kata.py")
    if 'with_data_for_test_kata' in feature.tags:
        if os.path.isfile("test_examples/test_kata.txt") == True:
            os.remove("test_examples/test_kata.txt")

def before_feature(context, feature):
    if 'with_data_for_test_kata' in feature.tags:
        data_output = open("test_examples/test_kata.txt", "w+")
        data_output.write(
        """what, how, who
        lorem, that is a long value, 3.1415
        ipsum, 89798, 0.2"""
        )
        data_output.close()
