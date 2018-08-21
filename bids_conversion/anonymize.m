% Script features:
%
% (1)   takes folder structure specified by dcmRoot and creates mirror 
%       mirror folder structure with suffix _a
% (2)   anonymize all dicom sequences from source folders and copy them to
%       mirror structure preserving names and order
%
%       Required functions:
%       + anonymize_dicm.m
%
% Author: Kamil Bonna
% ICNT, 17/03/2018
% Ver: MATLAB R2017a 
%% parameters
% root folder for dicom files
dcmRoot = 'LearningBrain_dcm';
% root folder for anonymized mirror structure
dcm_aRoot = 'LearningBrain_dcm_a';
% subjects
subjId = 1;
%% body
% notation dcm* : refers to DICOM folders
fprintf('Initialising... \n\n'); pause(1);
fprintf('Dealing with subject %i.\n',subjId);
%% explore dataset and determine what is present
% subject folder
dcmSub = fullfile(dcmRoot,strcat('LB',num2str(subjId,'%03i')));
dcm_aSub = fullfile(dcm_aRoot,strcat('LB',num2str(subjId,'%03i')));
isdcmSub = boolean(exist(dcmSub,'dir'));
isdcm_aSub = boolean(exist(dcm_aSub,'dir'));
    if isdcmSub
        if ~isdcm_aSub
           mkdir(dcm_aSub); 
           fprintf('Subject (%i) folder created!\n',subjId);
        end
        % sessions folders
        dcmSes = str2num(ls(dcmSub));
        isdcmSes = ~isempty(dcmSes);
        if isdcmSes %(there is any session)
            dcmSesFull = cell(1,numel(dcmSes));
            dcm_aSesFull = cell(1,numel(dcmSes));
            for ses = dcmSes
               dcmSesFull{ses} = fullfile(dcmSub,num2str(ses)); 
               dcm_aSesFull{ses} = fullfile(dcm_aSub,num2str(ses));
               if ~boolean(exist(dcm_aSesFull{ses},'dir'))
                  mkdir(dcm_aSesFull{ses});
                  fprintf('Session (%i) folder created!\n',ses);
               end
            end
        end
            % scanner sequence folders
            for ses = dcmSes
                dirInfo = dir(dcmSesFull{ses});
                dirInfo = dirInfo(~ismember({dirInfo.name},{'.','..'}));
                for d = 1 : numel(dirInfo) %(every sequence folder)
                    if dirInfo(d).isdir %(it is a directory)
                        dcmFName = fullfile(dirInfo(d).folder,dirInfo(d).name);
                        dcm_aFName = fullfile(dcm_aSesFull{ses},dirInfo(d).name);
                        if ~boolean(exist(dcm_aFName,'dir'))
                            mkdir(dcm_aFName)
                            fprintf('Sequence (%s) folder created!\n',dirInfo(d).name);
                        end
                        dirInfo_a = dir(dcm_aFName);
                        dirInfo_a = dirInfo_a(~ismember({dirInfo_a.name},{'.','..'}));
                        if ~logical(numel(dirInfo_a)) %(is empty)
                            %%% ANONYMIZE %%%
                            tic
                            anonymize_dicm(dcmFName,dcm_aFName,strcat('sub-',num2str(subjId,'%02i')));
                            toc
                            fprintf('Folder %s anonymized.\n',dcm_aFName);
                        end
                    end
                end
                clear dirInfo dirInfo_a
            end        
    end
