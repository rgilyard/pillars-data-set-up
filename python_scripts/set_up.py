from datasets import *


def prepare_data():
    raw_set = RawDataset().process()
    prep_set = PreprocessedDataset().process()
    # Will I even need to do anything with ARCS?


if __name__ == '__main__':
    prepare_data()
