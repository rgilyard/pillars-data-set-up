from .dataset import Dataset


class PreprocessedDataset(Dataset):
    raw_data_file_path = '../preprocessed_arcs_data/'
    processed_data_file_path = '../arcs/'

    def __init__(self):
        super().__init__(type(self).raw_data_file_path, type(self).processed_data_file_path)
        print('initializing PreprocessedData object')

