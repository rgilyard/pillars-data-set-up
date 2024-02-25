# pillars-data-set-up #

Prepare .pcap files and .mat labels for use with the PointPillars model in MMDetection3D.

## Dependencies ##

Python 3.?
Also, just get the install list.

## Usage ##

Please see [Preparation](#preparation) for the manual tasks that need to be done before running.

To start, please run:
```commandline
python python_scripts/set_up.py
```

## Preparation ##

Before running the scripts, please:
- Download the raw .pcap files from Google Drive to raw_arcs_data folder
- Import the .pcap files into MatLab to label them.
- Save the MatLab .mat labels to raw_arcs_data folder. The .pcap files must remain in the same
  folder for the matlab .m script to run properly later.
- Open .pcap files in Veloview and export as .las files to preprocessed_arcs_data/las folder.

Files must be in this structure in order for the scripts to run:
```
.
├── matlab_scripts/
│   └── convertToKitti.m
├── preprocessed_data/
│   └── las/
├── raw_arcs_data/
│   ├── groundTruthLidar.mat
│   └── zelzah.pcap
└── python_scripts/
    ├── set_up.py
    └── datasets/
```

## Conversions ##

Add flowchart for conversions

- Run the .m script to convert .mat labels to .txt files and save them to the 
  preprocessed_arcs_data/labels folder.
- For each .txt label file, divide into train, validate and test set.
  - Save information in arcs/ImageSets/.
- Copy the appropriate .txt files to the training/label and testing/label folders
- For each .txt label in the training/label and testing/label folders, convert the 
  corresponding .las file to suitable KITTI .bin file. GET FROM BIN CONVERTER FROM SERVER.
- Temporarily add blank images for the images (add still from video if time permits. Not
  necessary for training).
- Add calibration files. These are each the same in the KITTI dataset. I believe it has to
  do with the area in the LiDAR frames we want to use. I will try copying the KITTI versions,
  then adjusting them.

## File Structure ##

```
.
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
    ├── set_up.py
    └── datasets/*
```

### arcs ###

Holds the ARCS data prepared for training and testing after the scripts have been run.
I will change the arcs directory location on the server.

#### ImageSets ####

Contains .txt files that list the files to be used for testing, training, and validation sets.
- train.txt: Contains the names of the files used to train the model.
- val.txt: Contains the names of the files used to validate the model.
- trainval.txt: Contains the names of the files used to train the full model after the
  hyperparameters are chosen.
- test.txt: Contains the names of the files that are withheld during training and fine-tuning.

#### Testing ####

- calib folder: Contains the .txt files with the calibration information for each LiDAR .bin file.
- image_2 folder: Contains one (.png?) image for each frame corresponding to each LiDAR .bin file.
- label_ folder: Contains one .txt label file for each frame corresponding to each LiDAR .bin file.
- velodyne folder: Contains the .bin files for each frame of LiDAR.

#### Training ####

- calib folder: Contains the .txt files with the calibration information for each LiDAR .bin file.
- image_2 folder: Contains one (.png?) image for each frame corresponding to each LiDAR .bin file.
- label_ folder: Contains one .txt label file for each frame corresponding to each LiDAR .bin file.
- velodyne folder: Contains the .bin files for each frame of LiDAR.

### python_scripts ###

Python scripts that convert the .las LiDAR files and .mat label files into a format usable
by MMDetection3D's pointpillar model training.

ADD FILD DESCRIPTIONS WHEN FINISHED.

### matlab_scripts ###

- **convertToKITTI.m** <br>
    A MatLab script to convert .mat labels into .txt KITTI format labels

### raw_arcs_data ###

- **groundTruthLidarTest.mat** <br>
Contains the LiDAR .pcap files and the labels in .mat files.
- **zelzah plummer 1...** RENAME THIS <br>
Contains the .pcap LiDAR files from the Velodyne sensor

### preprocessed_data ###

- **labels/** <br>
Contains the .txt labels after the python script is run.
- **las/** <br>
Contains the .las LiDAR files manually exported from veloview (this needs to be done 
manually before running the script)

## Which tools use which files?? ##

| File Extention | Program                                            |
|----------------|----------------------------------------------------|
| .pcap          | Veloview, MatLab <br>                              |
| .mat           | MatLab (Python script runs the MatLab script) <br> |
| .las           | Python script <br>                                 |
| .bin           | MMDetection3D                                      |
| .txt           | MMDetection3D                                      |
| .png           | MMDetection3D                                      |

## Velodyne Information ##
Velodyn 32c.


