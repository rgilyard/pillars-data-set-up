function convertToKitti(file)
    % Check if an input argument is provided
    if nargin < 1
        file = 'groundTruthLidarTest.mat'; % Default file name
    end

    fprintf('\nIn matlab script')

    fprintf('\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n');

    % Create output file if it doesn't exist
    outputDir = '../preprocessed_arcs_data/labels';

    % Check if the directory exists
    if ~exist(outputDir, 'dir')
        % If the directory doesn't exist, create it
        mkdir(outputDir);
    end

    % Load data and get ground truth
    Data = load(file);
    gTruthData = Data.gTruth;
    % Get LabelData table
    labelData = gTruthData.LabelData;

    % For "each" row in the timetable (example: first 10 rows)
    for rowIndex = 1:100
        % Access the cell containing the struct array for 'car'
        carCell = labelData{rowIndex, 'car'};
        carStructArray = carCell{1};

        % Open a file to write the KITTI format data for each timestamp
        filename = sprintf('labels/%06d.txt', rowIndex - 1);
        fileID = fopen(filename, 'w');

        for carIndex = 1:numel(carStructArray)
            % Access the struct representing the car
            carStruct = carStructArray(carIndex);

            % Map the fields from carStruct to KITTI format
            object_type = 'Car';
            truncation = carStruct.truncation;
            occlusion = carStruct.occlusion;
            observation_angle = 0; % Placeholder, needs camera data
            % Assuming xctr, yctr, zctr are the center and xlen, ylen, zlen are the dimensions
            % Placeholder for 2D bounding box [xmin ymin xmax ymax]
            bbox = [0 0 0 0]; % Needs camera calibration data to calculate
            dimensions = [carStruct.Position(1), carStruct.Position(2), carStruct.Position(3)]; % height, width, length
            location = [carStruct.Position(4), carStruct.Position(5), carStruct.Position(6)]; % x, y, z
            rotation_y = carStruct.Position(9) * (pi / 180); % Convert from degrees to radians

            % Write to file in KITTI format
            fprintf(fileID, '%s %.2f %d %.2f %.2f %.2f %.2f %.2f %.2f %.2f %.2f %.2f %.2f %.2f %.2f\n', ...
                    object_type, truncation, occlusion, observation_angle, ...
                    bbox(1), bbox(2), bbox(3), bbox(4), dimensions(1), dimensions(2), dimensions(3), ...
                    location(1), location(2), location(3), rotation_y);
        end

        fclose(fileID);
    end
end


    %  ProjectedCuboid ROI
    %
    % {
    % "id": Unique Annotation ID,
    % "image_id": Image ID,
    % "category_id": Category ID,
    % "position": List of the form [xctr, yctr, zctr, xlen, ylen, zlen, xrot, yrot, zrot],
    %   "attributes": Contains attributes data,
    %   "sublabels": Contains sublabels data
    % }
    %
    %     xctr, yctr, and zctr specify the center of the projected cuboid and are 0-indexed.
    %
    %     xlen, ylen, and zlen specify the length of the projected cuboid along the x-axis,
    %     y-axis, and z-axis, respectively, before rotation has been applied.
    %
    %     xrot, yrot, and zrot specify the rotation angles for the projected cuboid along
    %     the x-axis, y-axis, and z-axis, respectively. These angles are clockwise-positive
    %     when looking in the forward direction of their corresponding axes.
