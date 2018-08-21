function [ path ] = assemble_path(root,subjId,sesId,type,folder,prefix)
% Function features:
%
% (input)   root: path to BIDS root folder
%           subjId: subject ID
%           sesId: session number 
%           type: 
%               0 for T1 image
%               1 for resting-state EPI
%               2 for spatial n-back EPI
%               3 for audio n-back EPI
%               4 for dual n-back EPI
%           folder (optional): do you want function to return only folder 
%               name instead of full path to file (default: false)
%           prefix (optional): additional prefix to file (default: '')
%
% (1)   returns full path to .nii file (or folder containing .nii file)
%       specified by number of study parameters
%       
% Author: Kamil Bonna
% ICNT, 01/04/2018
% Ver: MATLAB R2017a
%--- arguments ------------------------------------------------------------
if nargin == 4 
    folder = false;
    prefix = '';
end
if nargin == 5
    prefix = '';
end
%--- body -----------------------------------------------------------------
taskNames = {'rest','spatialnback','audionback','dualnback'};
partSub = strcat('sub-',num2str(subjId,'%02i'));
partSes = strcat('ses-',num2str(sesId,'%i'));
switch type
    case 0
        partFol = 'anat';
        filename = strcat(partSub,'_',partSes,'_T1w.nii');
    case {1,2,3,4}
        partFol = 'func';
        filename = strcat(partSub,'_',partSes,'_task-',taskNames{type},'_bold.nii');
end
if folder 
    path = fullfile(root,partSub,partSes,partFol);
else
    path = fullfile(root,partSub,partSes,partFol,strcat(prefix,filename));
end
end
