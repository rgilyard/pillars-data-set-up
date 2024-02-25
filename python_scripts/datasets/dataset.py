# Parent class for dataset classes which all load, process, and save data
class Dataset:
    def __init__(self, from_file_path, to_file_path):
        self.from_file_path = from_file_path
        self.to_file_path = to_file_path

    def load(self):
        pass

    def process(self):
        pass

    def save(self):
        pass
