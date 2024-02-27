import subprocess


class RawDataset:
    raw_data_file_path = 'C:/Users/gilya/Desktop/data_set_up/raw_arcs_data/groundTruthLidarTest.mat'
    kitt_full_path = 'C:/Users/gilya/Desktop/data_set_up/matlab_scripts/convertToKitti.m'
    processed_data_file_path = '../preprocessed_arcs_data/'

    def __init__(self):
        print('Initializing RawDataset object')

    def process(self):
        print('In RawDataset\'s process method')
        print('Attempting to run matlab command')
        matlab_command = f"matlab -batch \"addpath('{type(self).kitt_full_path.rsplit('/', 1)[0]}'); \
            convertToKitti('{type(self).raw_data_file_path}'); \
            rmpath('{type(self).kitt_full_path.rsplit('/', 1)[0]}');\""

        # Execute the MATLAB script
        try:
            subprocess.run(matlab_command, check=True, shell=True)
        except subprocess.CalledProcessError as e:
            print(f"Failed to run MATLAB script: {e}")
