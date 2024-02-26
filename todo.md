# To Do List #
- [x] Write out README with file conversions
- [ ] Fix file paths in convertToKitti.m
- [ ] Make file paths dynamic for scripts (including .m output)
- [ ] Figure out better way to access kitti .m script (it's an absolute path atm)
- [ ] Maybe dynamically find the working directory so I can use absolute file paths for MatLab scripts

# Side To Dos ##
- [ ] Write script to compare train and test velodyne files to make sure they are all different
      It looks like they might be, but if that's the case, where are the labels
      that are used to test the test data from the preloaded KITTI dataset?
- [ ] Figure out a way to automate velodyne export