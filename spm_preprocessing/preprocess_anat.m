function preprocess_anat(subjId,sessions,missing)
% Function features:
%
% (input)   subjId: subject ID
%           sessions: logical row vector of size equal total number of
%               sessions with true value for sessions of interest 
%           missing: structure informing about available .nii files
%
% (1)   copies T1s from original BIDS structure to /derivatives
% (2)   performs standard T1 preprocessing, e.g. segmentation
%
%       Required functions:
%       + assemble_path.m
%       + batch_anat_job.m
%
% Author: Kamil Bonna
% ICNT, 07/04/2018
% Ver: MATLAB R2017a
%--- what is present ------------------------------------------------------
isAnat = missing.isAnat;
isRequested = ( isAnat & sessions ); %(sessions for which T1 is present and analysis is requested)
%% copy T1s
for ses = find(isRequested)
    % if T1 is not already copied
    if ~logical(exist(assemble_path(fullfile(missing.root,'derivatives'),subjId,ses,0),'file'))
    source = assemble_path(missing.root,subjId,ses,0);
    destination = assemble_path(fullfile(missing.root,'derivatives'),subjId,ses,0,true);
    %--- move T1 to \derivatives ------------------------------------------
    fprintf('Copying %s...\n',source);
    copyfile(source,destination);
    end
end
clear source destination;
%% preprocess T1
%--- initialize SPM -------------------------------------------------------
spm('Defaults','fMRI');
spm_jobman('initcfg');
%--- loop over sessions ---------------------------------------------------
for ses = find(isRequested)
    filePath = assemble_path(fullfile(missing.root,'derivatives'),subjId,ses,0);
    matlabbatch = batch_anat_job(filePath);
    %--- preprocessing ----------------------------------------------------
    spm_jobman('serial',matlabbatch)
    %----------------------------------------------------------------------
    clear matlabbatch
    clear filePath
end
end




