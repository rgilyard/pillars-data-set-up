from datasets import *


def prepare_data():
    raw_set = RawDataset().process()
    prep_set = PreprocessedDataset().process()
    # Will I even need to do anything with ARCS?


if __name__ == '__main__':
    print('attempting to prepare data')
    prepare_data()
    print('done preparing data')
