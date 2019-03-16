from colorama import Fore, Style

class KataGeneratorLogger:

    def log_directory_creation(self, path):
        print(Fore.GREEN + Style.BRIGHT + "Created " + Style.RESET_ALL + "{}".format(path))

    def log_file_generation(self, file):
        print("\t" + Fore.GREEN + Style.BRIGHT + "Generated " + Style.RESET_ALL + "{}".format(file))
