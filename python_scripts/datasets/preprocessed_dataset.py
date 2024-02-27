from .utils import copy_files, save_list_to_file, convert_las_to_bin, get_frame_number
import os
import random
import shutil


# Probably have classes for las data, labels, video, and calibration
class PreprocessedDataset:

    def __init__(self):
        print('initializing PreprocessedData object')
        # Strings for file tree creation
        self.LAS_FILE_PATH = 'preprocessed_arcs_data\\las'
        self.SOURCE_LABELS_FILE_PATH = 'preprocessed_arcs_data\\labels'
        self.ARCS_ROOT_DIR = 'arcs'
        self.IMAGE_SETS_DIR = 'ImageSets'
        self.TESTING_DIR = 'testing'
        self.TRAINING_DIR = 'training'
        self.CALIB_DIR = 'calib'
        self.IMAGE_DIR = 'image_2'
        self.LABEL_DIR = 'label_2'
        self.VELODYNE_DIR = 'velodyne'
        self.PLACEHOLDER_IMAGE_PATH = 'python_scripts/assets/placeholder.png'

        # List of file names from labels
        self.labels_list = self.get_labels()
        print(self.labels_list)

        # MAKE SURE DIRECTORIES EXIST

    def process(self):
        self.save_train_val_test_splits()
        self.copy_files_to_arcs()
        self.convert_all_las_to_bin()

    # Converts the .las files to .bin format and saves them to the appropriate testing and training folders.
    # Also adds a placeholder image for each label/lidar frame. Later I may get images from video.
    def convert_all_las_to_bin(self):
        # Make a set for files in test file
        test_set_path = os.path.join(self.ARCS_ROOT_DIR, self.IMAGE_SETS_DIR, 'test.txt')
        with open(test_set_path, 'r') as file:
            test_set = {os.path.splitext(line.strip())[0] for line in file}
        print(test_set)

        # Make a set for files in trainval file
        trainval_set_path = os.path.join(self.ARCS_ROOT_DIR, self.IMAGE_SETS_DIR, 'trainval.txt')
        with open(trainval_set_path, 'r') as file:
            trainval_set = {os.path.splitext(line.strip())[0] for line in file}
        print(trainval_set)

        # List all files in the directory that end with .las
        las_files = [file for file in os.listdir(self.LAS_FILE_PATH) if file.endswith('.las')]
        # Make a dictionary with fixed width index as the key, and full path as the value
        in_out_dict = {}
        # For each item in the las files
        for las in las_files:
            # Get index, make fixed width so we can compare it to sets
            padded_frame_number = get_frame_number(las)

            from_path_string = os.path.join(self.LAS_FILE_PATH, las)
            # If it's in test set
            if padded_frame_number in test_set:
                # Create a to and from entry
                to_path_string = os.path.join(self.ARCS_ROOT_DIR, self.TESTING_DIR, self.VELODYNE_DIR,
                                              f'{padded_frame_number}.bin')
                # Add to the dictionary
                in_out_dict[from_path_string] = to_path_string
                # Also save a placeholder still frame file (This is hack, but I want to change it later)
                shutil.copy2(self.PLACEHOLDER_IMAGE_PATH, os.path.join(self.ARCS_ROOT_DIR, self.TESTING_DIR,
                                                                       self.IMAGE_DIR, f'{padded_frame_number}.png'))

            # Elif it's in the trainval set
            elif padded_frame_number in trainval_set:
                # Create a to and from entry
                to_path_string = os.path.join(self.ARCS_ROOT_DIR, self.TRAINING_DIR, self.VELODYNE_DIR,
                                              f'{padded_frame_number}.bin')
                # Add to the dictionary
                in_out_dict[from_path_string] = to_path_string
                # Also save a placeholder still frame file (This is hack, but I want to change it later)
                shutil.copy2(self.PLACEHOLDER_IMAGE_PATH, os.path.join(self.ARCS_ROOT_DIR, self.TRAINING_DIR,
                                                                       self.IMAGE_DIR, f'{padded_frame_number}.png'))

        # Try with just 10 files at first
        # for each file in the directory
        for las in in_out_dict.keys():
            # print('converting: ' + str(las) + ' ' + str(in_out_dict[las]))
            convert_las_to_bin(las, in_out_dict[las])

    # Copies label files from preprocessed to arcs using the splits saved in ImageSets
    def copy_files_to_arcs(self):
        self.copy_set_up('test.txt', self.TESTING_DIR)
        self.copy_set_up('trainval.txt', self.TRAINING_DIR)

    def copy_set_up(self, label_list_file, target_dir):
        # Define the source and destination directories for trainval or test files
        file_path = os.path.join(self.ARCS_ROOT_DIR, self.IMAGE_SETS_DIR, label_list_file)
        dest_dir = os.path.join(self.ARCS_ROOT_DIR, target_dir, self.LABEL_DIR)
        # Make sure directory exists
        os.makedirs(dest_dir, exist_ok=True)

        # Copy files
        copy_files(file_path, self.SOURCE_LABELS_FILE_PATH, dest_dir)

    # Make a train, val, test split, save lists to arcs/ImageSets
    def save_train_val_test_splits(self):
        # Shuffle the list to ensure randomness
        random.shuffle(self.labels_list)

        # Define split proportions
        train_split = 0.65  # 65% of the data
        val_split = 0.2  # 20% of the data
        test_split = 0.15  # 15% of the data

        # Calculate split sizes
        total_files = len(self.labels_list)
        train_size = int(total_files * train_split)
        val_size = int(total_files * val_split)

        # Split the dataset
        train_files = self.labels_list[:train_size]
        val_files = self.labels_list[train_size:train_size + val_size]
        test_files = self.labels_list[train_size + val_size:]

        # Combine train and val for trainval
        trainval_files = train_files + val_files

        root = os.path.join(self.ARCS_ROOT_DIR, self.IMAGE_SETS_DIR)
        os.makedirs(root, exist_ok=True)

        # Save to files
        save_list_to_file(train_files, os.path.join(root, 'train.txt'))
        save_list_to_file(val_files, os.path.join(root, 'val.txt'))
        save_list_to_file(test_files, os.path.join(root, 'test.txt'))
        save_list_to_file(trainval_files, os.path.join(root, 'trainval.txt'))

    # First get a list of file names from labels
    def get_labels(self):
        # List all files in the directory
        file_list = [file for file in os.listdir(self.SOURCE_LABELS_FILE_PATH) if
                     os.path.isfile(os.path.join(self.SOURCE_LABELS_FILE_PATH, file))]
        return file_list

