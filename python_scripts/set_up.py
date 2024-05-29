from datasets import *
import zipfile
import pathlib


def prepare_data():
    raw_set = RawDataset().process()
    prep_set = PreprocessedDataset().process()
    # Will I even need to do anything with ARCS?


def zip_data():
    # output_file = 'arcs.zip'
    # input_dir = 'arcs'
    # with zipfile.ZipFile(output_file, 'w') as myzip:
    #     myzip.write(input_dir)

    directory = pathlib.Path('arcs/')

    with zipfile.ZipFile('arcs.zip', mode='w') as archive:
        for file_path in directory.rglob('*'):
            print(file_path)
            archive.write(file_path, arcname=file_path.relative_to(directory))


if __name__ == '__main__':
    print('attempting to prepare data')
    prepare_data()
    print('done preparing data')
    print('zipping data')
    zip_data()
    print('done zipping data')
