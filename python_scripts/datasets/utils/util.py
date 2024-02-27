import laspy
import numpy as np
import os
import shutil
import re


# I think, make the video frames at the same time
def convert_las_to_bin(infile, outfile):
    # Open the LAS file
    with laspy.open(infile) as f:
        las = f.read()

        # Assuming 'reflectivity' is a standard LAS point attribute to extract
        # along with 'x', 'y', 'z', and 'intensity'
        x = las.x
        y = las.y
        z = las.z
        raw_intensity = las.intensity

        # Normalize the intensity to be between 0 and 1 (because that's what the range is for reflectivity)
        intensity_min = np.min(raw_intensity)
        intensity_max = np.max(raw_intensity)
        normalized_intensity = (raw_intensity - intensity_min) / (intensity_max - intensity_min)

        # Combine the features into one array to include 'x', 'y', 'z', and 'intensity'
        features = np.vstack((x, y, z, normalized_intensity)).transpose()

        # Save the features to a binary file
        features.astype(np.float32).tofile(outfile)

        # This is for the video if I end up doing that later
        # timestamp = las.gps_time
        # print(timestamp)
        # return timestamp


def get_frame_number(las_file_string):
    match = re.search(r'Frame (\d+)', las_file_string)
    if match:
        frame_number = match.group(1)  # Extract the frame number
        # Pad the frame number to a fixed length of 6 with leading zeros
        padded_frame_number = frame_number.zfill(6)
        print(f"Original frame number: {frame_number}, Padded frame number: {padded_frame_number}")
        return padded_frame_number
    else:
        print("No frame number found in the file name.")
        return ''


def copy_files(list_file_path, src_dir, dest_dir):
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


# Function to save lists to files
def save_list_to_file(list_of_files, file_name):
    with open(file_name, 'w') as f:
        for item in list_of_files:
            f.write("%s\n" % item)
