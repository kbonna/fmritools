% Script features:
%
% (1)   creates fMRI task metadata for spatial, audio, dual n-back and rest
%       pulled from DICOM fields and save them as _bold.json file required 
%       in BIDS dataset
%
% Author: Kamil Bonna
% ICNT, 17/03/2018
% Ver: MATLAB R2017a 
%% parameters
func = {'Dual n-back','Spatial n-back','Audio n-back','Resting state'};
funcBid = {'dualnback','spatialnback','audionback','rest'};
bidRoot = 'LearningBrain/';
%% body
for i = 1 : numel(func)
    %% Task specific
    % Required fields:
    m.RepetitionTime = 2;
    m.TaskName = func{i};

    % fMRI task information
    type = m.TaskName(end-4:end);
    task = m.TaskName(1);
    switch type
        case '-back'
            m.CogAtlasID = 'https://www.cognitiveatlas.org/task/id/tsk_4a57abb949bcd/'; %(n-back)
            switch task
                case 'D'
                    m.TaskDescription = 'Dual n-back task with n=1,2; with audio stimuli (consisting of 8 different spoken letters of Polish language) and visual stimuli (consisting of 8 blue squares appearing on different places on the black screen)';    
                case 'A'
                    m.TaskDescription = 'Standard n-back task with n=1,2, audio stimuli consisting of 8 different spoken letters (Polish language)'; 
                case 'S'
                    m.TaskDescription = 'Standard n-back task with n=1,2, visual stimuli consisting of 8 blue squares appearing on different places on the black screen';
            end
        case 'state'
            m.CogAtlasID = 'https://www.cognitiveatlas.org/task/id/trm_4c8a834779883/'; %(rest)
            m.Instructions = 'Lie with eyes open, fixate on a white cross and relax';
    end

    %% Task independent
    % Scanner Hardware
    m.Manufacturer = 'GE MEDICAL SYSTEMS';
    m.ManufacturerModelName = 'DISCOVERY MR750';
    m.MagneticFieldStrength = 3;
    m.DeviceSerialNumber = '000000PL2853MR01';
    m.SoftwareVersions = '24/LX/MR Software release:DV24.0_R02_1607.b';
    m.ReceiveCoilName = '8HRBRAIN';

    % In-Plane Spatial Encoding
    m.PulseSequenceType = 'EPI';

    % Timing Parameters
    m.EchoTime = 0.03; %(in seconds)
    m.NumberOfVolumesDiscardedByScanner = 5;
    switch type
        case '-back'
            m.NumberOfVolumesDiscardedByUser = 0;
        case 'state'
            m.NumberOfVolumesDiscardedByUser = 5;
    end
    % RF&Contrast
    m.FlipAngle = 90;

    % SliceAcceleration

    % Institution information
    m.InstitutionName = 'Uniwersytet M Kopernika';
    
    % SAVE
    s = jsonencode(m);
    name = strcat('task-',funcBid{i},'_bold.json');
    fileId = fopen(fullfile(bidRoot,name),'w');
    fprintf(fileId,s);
    fclose(fileId);
end


