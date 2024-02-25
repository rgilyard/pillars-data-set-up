from .dataset import Dataset
import shutil
import os
import random


class PreprocessedDataset(Dataset):

    def __init__(self):
        super().__init__()
        print('initializing PreprocessedData object')
        # Strings for file tree creation
        self.LAS_FILE_PATH = '../preprocessed_arcs_data/las'
        self.SOURCE_LABELS_FILE_PATH = '../preprocessed_arcs_data/labels'
        self.ARCS_ROOT_DIR = 'arcs'
        self.IMAGE_SETS_DIR = 'ImageSets'
        self.TESTING_DIR = 'testing'
        self.TRAINING_DIR = 'training'
        self.CALIB_DIR = 'calib'
        self.IMAGE_DIR = 'image_2'
        self.LABEL_DIR = 'label_2'
        self.VELODYNE_DIR = 'velodyne'

        # List of file names from labels
        self.labels_list = self.get_labels()
        print(self.labels_list)

        # WHAT TO DO
        # For each file in imageSet (well, train and test) copy the txt files from prep/labels to arcs/.../labels

    def process(self):
        print('Attempting to save train, val, test lists')
        self.save_train_val_test_splits()
        print('Done saving lists')
        print('Attempting to copy files to arcs')
        self.copy_files_to_arcs()
        print('Done copying files to arcs')

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
        self.copy_files(file_path, self.SOURCE_LABELS_FILE_PATH, dest_dir)

    def copy_files(self, list_file_path, src_dir, dest_dir):
        # Ensure the destination directory exists
        os.makedirs(dest_dir, exist_ok=True)

        # Open the file containing the list of files to copy
        with open(list_file_path, 'r') as file_list:
            for file_name in file_list:
                file_name = file_name.strip()  # Remove any leading/trailing whitespace
                src_file_path = os.path.join(src_dir, file_name)
                dest_file_path = os.path.join(dest_dir, file_name)

                # Copy the file from the source to the destination
                shutil.copy2(src_file_path, dest_file_path)
                # print(f"Copied {src_file_path} to {dest_file_path}")

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
        self.save_list_to_file(train_files, os.path.join(root, 'train.txt'))
        self.save_list_to_file(val_files, os.path.join(root, 'val.txt'))
        self.save_list_to_file(test_files, os.path.join(root, 'test.txt'))
        self.save_list_to_file(trainval_files, os.path.join(root, 'trainval.txt'))

    # Function to save lists to files
    def save_list_to_file(self, list_of_files, file_name):
        with open(file_name, 'w') as f:
            for item in list_of_files:
                f.write("%s\n" % item)

    # First get a list of file names from labels
    def get_labels(self):
        # List all files in the directory
        file_list = [file for file in os.listdir(self.SOURCE_LABELS_FILE_PATH) if
                     os.path.isfile(os.path.join(self.SOURCE_LABELS_FILE_PATH, file))]
        return file_list

    # Pass in a list of strings to make a directory if it doesn't exist
    def create_dir_if_not_exist(self, list_of_strings):
        # Make a path from the strings
        # Create the directory if it doesn't exist
        pass
