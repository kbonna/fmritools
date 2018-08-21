% Script features:
%
% (1)   explores fMRI dataset within folder specified by dcmRoot and find
%       all available imaging data
% (2)   creates BIDS-compatibile folder structure corresponding to explored
%       fMRI dataset (module also useful for creating /derivatives holding
%       preprocessed data)
% (3)   checks if there are any missing DICOM files and creates logfile
%       missing_data.log (in BIDS root folder) listing all of them
% (4)   converts DICOM files to .nii.gz, extracts header, copies converted
%       files to BIDS folder structure and rename them properly
%       NOTE: before running the script, please make sure that option 
%       "Save json file" in dicm2nii GUI is marked
%
%       Required functions:
%       + dicm2nii.m
%       + fix_dti_bv.m
%       + fix_dti_json.m
%
% Author: Kamil Bonna
% ICNT, 17/03/2018
% Ver: MATLAB R2017a
%% parameters
subjId = 1; %(subject number)
% proper number of DICOM files for each sequence
nofAnatReq = 176;
nofTaskReq = [ 14280, 14280, 14280, 12810 ];
nofDtiReq  = 4680;
% task names
dcmTaskNames = {'na','ns','nd','rs'};
bidTaskNames = {'task-audionback','task-spatialnback','task-dualnback','task-rest'};
nTask = numel(dcmTaskNames); %(number of tasks)
%% body
%% explore dataset and determine what is present
dcmRoot = 'LearningBrain_dcm_a';
% subject folder
dcmSub = fullfile(dcmRoot,strcat('LB',num2str(subjId,'%03i')));
    if logical(exist(dcmSub,'dir'))
    % sessions folders
    dcmSes = str2num(ls(dcmSub));
    nSes = numel(dcmSes); %(number of session folders)
    isdcmSes = ~isempty(dcmSes);
        if isdcmSes %(there is any session)
            nofdcmAnat = zeros(1,nSes);
            nofdcmTask = zeros(nTask,nSes);
            nofdcmDti  = zeros(1,nSes);
            dcmAnat = cell(1,nSes);
            dcmTask = cell(nTask,nSes);
            dcmDti  = cell(1,nSes);
            for ses = dcmSes
            % anatomical image
                dcmAnat{ses} = fullfile(dcmSub,num2str(ses),'t1');
                nofdcmAnat(ses) = number_of_files(dcmAnat{ses});
            % functional images
                for tas = 1 : nTask
                    dcmTask{ses}{tas} = fullfile(dcmSub,num2str(ses),dcmTaskNames{tas});
                    nofdcmTask(ses,tas) = number_of_files(dcmTask{ses}{tas});
                end                          
            % dti images
                dcmDti{ses} = fullfile(dcmSub,num2str(ses),'dti');
                nofdcmDti(ses) = number_of_files(dcmDti{ses});
            end            
        end
    else
        error('Subject folder not exists!');
    end
%% create bids structure (also useful for /derivatives)
bidRoot = 'LearningBrain/sourcedata';
% subject folder
bidSub = fullfile(bidRoot,strcat('sub-',num2str(subjId,'%02i')));
mkdir2(bidSub);
    % sessions folders
    bidSesFull = cell(1,nSes);
    for ses = dcmSes
        bidSesFull{ses} = fullfile(bidSub,strcat('ses-',num2str(ses)));
        mkdir2(bidSesFull{ses});
    end
        % session subfolders
        bidAnat = cell(1,nSes);
        bidTask = cell(1,nSes);
        bidDti  = cell(1,nSes);        
        for ses = dcmSes
            % anatomical folder
            bidAnat{ses} = fullfile(bidSesFull{ses},'anat');
            mkdir2(bidAnat{ses});  
            % functional folder
            bidTask{ses} = fullfile(bidSesFull{ses},'func');
            mkdir2(bidTask{ses});
            % dti folder
            bidDti{ses} = fullfile(bidSesFull{ses},'dwi');
            mkdir2(bidDti{ses});
        end
%% missing files validation
isdcmAnat = false(1,nSes);
isdcmTask = false(nTask,nSes);
isdcmDti  = false(1,nSes);
for ses = dcmSes
    % anatomical
    if nofdcmAnat(ses) == nofAnatReq %(right number of files)
        isdcmAnat(ses) = true; 
    else
        msg = strcat('Missing DICOM files: Subject[',num2str(subjId,'%02i'),'], Session[',num2str(ses),'], Modality[t1]');
        log_missing(bidRoot,msg); clear msg;
    end
    % task 
    for tas = 1 : nTask
        if nofdcmTask(ses,tas) == nofTaskReq(tas) 
            isdcmTask(ses,tas) = true;
        else
            msg = strcat('Missing DICOM files: Subject[',num2str(subjId,'%02i'),'], Session[',num2str(ses),'], Modality[',dcmTaskNames{tas},']');
            log_missing(bidRoot,msg); clear msg;
        end
    end
    % dti
    if nofdcmDti(ses) == nofDtiReq
        isdcmDti(ses) = true;
    else
        msg = strcat('Missing DICOM files: Subject[',num2str(subjId,'%02i'),'], Session[',num2str(ses),'], Modality[dti]');
        log_missing(bidRoot,msg); clear msg;
    end
end
%% convert DICOM, copy to BIDS and rename
% anatomical 
for ses = dcmSes
   if isdcmAnat(ses)
       dicm2nii(dcmAnat{ses},bidAnat{ses}); %(convert & copy)
       delete(fullfile(bidAnat{ses},'dcmHeaders.mat')); %(delete headers)
       % get information about all files within folder
       dirInfo = dir2(bidAnat{ses});
       rename_bids(dirInfo,subjId,ses,'T1w');
   end    
end
% task
for ses = dcmSes
    % temporary folder for conversion
    bidTaskTemp = fullfile(bidTask{ses},'temp');
    mkdir(bidTaskTemp); 
    for tas = 1 : nTask
        if isdcmTask(ses,tas)
        dicm2nii(dcmTask{ses}{tas},bidTaskTemp);
        delete(fullfile(bidTaskTemp,'dcmHeaders.mat')); 
        dirInfo = dir2(bidTaskTemp);
        rename_bids(dirInfo,subjId,ses,strcat(bidTaskNames{tas},'_bold'));
        % move all files to /func folder
        movefile(strcat(bidTaskTemp,'/*'),bidTask{ses});
        end
    end
    rmdir(bidTaskTemp);
end
% dti 
for ses = dcmSes
   if isdcmDti(ses)
       dicm2nii(dcmDti{ses},bidDti{ses}); 
       delete(fullfile(bidDti{ses},'dcmHeaders.mat')); 
       dirInfo = dir2(bidDti{ses});
       rename_bids(dirInfo,subjId,ses,'dwi');
       % fixing dti files
       dirInfo = dir2(bidDti{ses});
       for i = 1 : numel(dirInfo)
           [~,~,ext]=fileparts(dirInfo(i).name);
           switch ext
               case {'.bval','.bvec'}
                   fix_dti_bv(fullfile(dirInfo(i).folder,dirInfo(i).name));
               case '.json'
                   fix_dti_json(fullfile(dirInfo(i).folder,dirInfo(i).name));
           end
       end
   end  
end
%% functions
function [ dirInfo ] = dir2(path)
    dirInfo = dir(path);
    dirInfo = dirInfo(~ismember({dirInfo.name},{'.','..'}));
end
function [ nof ] = number_of_files(path)
    dirInfo = dir2(path);
    nof = numel(dirInfo);
end
% procedures
function rename_bids(dirInfo,subjId,ses,suffix)
    for i = 1 : numel(dirInfo)
        % old name
        oldNameFull = fullfile(dirInfo(i).folder,dirInfo(i).name);
        % extract extension
        [~,~,ext]=fileparts(oldNameFull);
        if isequal(ext,'.gz')
           ext = '.nii.gz'; 
        end
        % new name
        newName = strcat('sub-',num2str(subjId,'%02i'),'_ses-',num2str(ses),'_',suffix);
        newNameFull = fullfile(dirInfo(i).folder,strcat(newName,ext));
        % rename!
        movefile(oldNameFull,newNameFull)
    end
end
function mkdir2(path)
    if ~logical(exist(path,'dir')) %(folder exists)
        mkdir(path);
    end
end
function log_missing(bidRoot, string)
    fileId = fopen(fullfile(bidRoot,'missing_data.log'),'a');   
    fprintf(fileId,strcat(string,'\n'));
    fclose(fileId);
end
