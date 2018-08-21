function preprocess_func(subjId,taskName,sessions,missing)
% Function features:
%
% (input)   subjId: subject ID
%           taskName: name of task images to preprocess (same as in missing
%               structure)
%           sessions: logical row vector of size equal total number of
%               sessions with true value for sessions of interest 
%           missing: structure informing about available .nii files
%
% (1)   looks for deformation fields and T1 in /derivatives (required files
%       to perform EPI preprocessing)
% (2)   copies EPI images from original BIDS structure to /derivatives
% (3)   performs standard EPI preprocessing, e.g. slice-timing correction,
%       motion correction, coregistration to T1, normalization and
%       smoothing
%
%       Required functions:
%       + assemble_path.m
%       + batch_anat_job.m
%
% Author: Kamil Bonna
% ICNT, 07/04/2018
% Ver: MATLAB R2017a
%--- what is present ------------------------------------------------------
taskId = find(strcmp(missing.taskNames(:),taskName));
if isempty(find(ismember(missing.taskNames,taskName),1))
    error('Task not exist!');
end
isTask = missing.isTask{find(ismember(missing.taskNames,taskName),1)};
%% look for T1 and deformation fields & copy EPI
isPossible = false(1,4);
for ses = find(isTask)
    % look for deformation fields & T1
    pathDefo = assemble_path(fullfile(missing.root,'derivatives'),subjId,ses,0,false,'y_');
    pathAnat = assemble_path(fullfile(missing.root,'derivatives'),subjId,ses,0);
    if logical(exist(pathDefo,'file')) && logical(exist(pathAnat,'file'))
        isPossible(ses) = true;
    end
end
    clear pathDefo
    clear pathAnat
%--- copy EPI -------------------------------------------------------------
isRequested = ( isPossible & sessions );
for ses = find(isRequested)
    % look if file is already in /derivatives
    if ~logical(exist(assemble_path(fullfile(missing.root,'derivatives'),subjId,ses,taskId),'file'))
    source = assemble_path(missing.root,subjId,ses,taskId);
    destination = assemble_path(fullfile(missing.root,'derivatives'),subjId,ses,taskId,true);
    fprintf('Copying %s...\n',source);
    copyfile(source,destination);
    end
end
clear source destination;
%% preprocess EPI
%--- initialize SPM -------------------------------------------------------
spm('Defaults','fMRI');
spm_jobman('initcfg');
%--- loop over sessions ---------------------------------------------------
for ses = find(isRequested)
    pathDefo = assemble_path(fullfile(missing.root,'derivatives'),subjId,ses,0,false,'y_');
    pathAnat = assemble_path(fullfile(missing.root,'derivatives'),subjId,ses,0);
    pathFunc = assemble_path(fullfile(missing.root,'derivatives'),subjId,ses,taskId);
    %--- create batch -----------------------------------------------------
    matlabbatch = batch_func_job(pathAnat,pathDefo,pathFunc);
    %--- preprocessing ----------------------------------------------------
    spm_jobman('serial',matlabbatch)
    %--- delete extra files -----------------------------------------------
    fprintf('Deleting %s... \n',assemble_path(fullfile(missing.root,'derivatives'),subjId,ses,taskId,false,'ra_'));
        delete(assemble_path(fullfile(missing.root,'derivatives'),subjId,ses,taskId,false,'ra_'));
    fprintf('Deleting %s... \n',assemble_path(fullfile(missing.root,'derivatives'),subjId,ses,taskId,false,'a_'));
        delete(assemble_path(fullfile(missing.root,'derivatives'),subjId,ses,taskId,false,'a_'));
    fprintf('Deleting %s... \n',pathFunc);
        delete(pathFunc);
    clear matlabbatch
    clear pathDefo pathAnat pathFunc
end
end
