# pillars-data-set-up #

Scripts to transform LiDAR data into the format usable by MMDetection3D models.

## Purpose ##

Prepare .pcap files and .mat labels for use with the PointPillars model in MMDetection3D.

## Conversions ##

- Download the raw .pcap files from Google Drive to raw_arcs_data folder
- Import the .pcap files into MatLab to label them.
- Save the MatLab .mat labels to raw_arcs_data folder
- Open .pcap files in Veloview and export as .las files to preprocessed_arcs_data/las folder
- USAGE FOR PYTHON SCRIPT THAT SHOULD
  - Run the .m script to convert .mat labels to .txt files and save them to the 
    preprocessed_arcs_data/labels folder
  - For each .txt label file, divide into train and test set (save that info somewhere)
  - Copy the appropriate .txt files to the training/label and testing/label folders
  - For each .txt label in the training/label and testing/label folders, convert the 
    corresponding .las file to suitable KITTI .bin file. GET FROM SERVER.
  - Temporarily add blank images for the images

## File Structure ##
```
.
└── data_set_up/
    ├── arcs/
    │   ├── ImageSets/
    │   ├── testing/
    │   │   ├── calib/
    │   │   ├── image_2/
    │   │   ├── label_2/
    │   │   └── velodyne/
    │   └── training/
    │       ├── calib/
    │       ├── image_2/
    │       ├── label_2/
    │       └── velodyne/
    ├── matlab_scripts/
    │   └── convertToKitti.m
    ├── preprocessed_data/
    │   ├── labels/
    │   └── las/
    ├── raw_arcs_data/
    │   ├── groundTruthLidar.mat
    │   └── zelzah.pcap
    └── python_scripts/
        └── main.py
```


### arcs ###

Holds the arcs data prepared for training and testing after the scripts have been run.

#### ImageSets ####

Contains .txt files that list the files to be used for testing, training, and validation sets.
- train.txt: Contains the names of the files used to train the model.
- val.txt: Contains the names of the files used to validate the model.
- trainval.txt: Contains the names of the files used to train the full model after the
  hyperparameters are chosen.
- test.txt: Contains the names of the files that are withheld during training and fine-tuning.

### python_scripts ###

The only

### matlab_scrips ###

- **convertToKITTI.m** <br>
    A MatLab script to convert .mat labels into .txt KITTI format labels

### raw_arcs_data ###

- **groundTruthLidarTest.mat** <br>
Contains the LiDAR .pcap files and the labels in .mat files.
- **zelzah plummer 1...** RENAME THIS <br>
Contains the .pcap LiDAR files from the Velodyne sensor

###  ###

###  ###


## Which tools can open which files?? ##

.pcap   Veloview, MatLab <br>
.mat    MatLab


## Velodyne Information ##


