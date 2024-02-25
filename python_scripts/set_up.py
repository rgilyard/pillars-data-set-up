from datasets import *


def prepare_data():
    print('attempting to process raw dataset')
    # raw_set = RawDataset().process()
    print('processed raw dataset')
    print('attempting to process preprocessed dataset')
    prep_set = PreprocessedDataset().process()
    print('processed preprocessed dataset')
    # Will I even need to do anything with ARCS?


if __name__ == '__main__':
    print('attempting to prepare data')
    prepare_data()
    print('done preparing data')
