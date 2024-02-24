# pillars-data-set-up #

Scripts to transform LiDAR data into the format usable by MMDetection3D models

## Purpose ##

## Conversions ##

- Download the raw .pcap files from Google Drive to raw_arcs_data folder
- Import the .pcap files into MatLab to label them.
- Save the MatLab .mat labels to raw_arcs_data folder
- Open .pcap files in Veloview and export as .las files to preprocessed_arcs_data/las folder
- USAGE FOR PYTHON SCRIPT THAT HOULD

## File Structure ##
```
.
└── data_set_up/
    ├── arcs/
    │   ├── ImageSets/
    │   ├── testing/
    │   │   ├── calib/
    │   │   ├── image_2/
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

### scripts ###

The only

### raw_arcs_data ###

- **groundTruthLidarTest.mat** <br>
Contains the LiDAR .pcap files and the labels in .mat files.
- **zelzah plummer 1...** RENAME THIS <br>
Contains the .pcap LiDAR files from the Velodyne sensor

### matlab_scrips ###

- **convertToKITTI.m** <br>
    A MatLab script to convert .mat labels into .txt KITTI format labels

###  ###

###  ###


## Which tools can open which files?? ##

.pcap   Veloview, MatLab <br>
.mat    MatLab


## Velodyne Information ##


