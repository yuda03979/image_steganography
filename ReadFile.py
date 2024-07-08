
from Functions import check_path_already_exist

class ReadFile:

    def __init__(self, path):
        self.path = path
        check_path_already_exist(self.path)
        self.text = ""
        self.read_file()


    def read_file(self):
        with open(self.path, 'r') as file:
            self.text = file.read() # ask dovi if its good or to reed line by line
            file.close()

    def get_message(self):
        return self.text