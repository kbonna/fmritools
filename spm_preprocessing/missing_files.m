function [ missing ] = missing_files(root,subjId,nSes)
% Function features:
%
% (input)   root: path to BIDS root folder
%           subjId: subject ID
%           nSes: total number of sesssions
%
% (1)   creates missing structure containing information about available
%       images (both anatomical and functional)
%
%       Required functions:
%       + assemble_path.m
%
% Author: Kamil Bonna
% ICNT, 01/04/2018
% Ver: MATLAB R2017a
%--------------------------------------------------------------------------
isAnat = false(1,nSes);
isTask = cell(1,4);
for ses = 1 : nSes
    isAnat(ses) = logical(exist(assemble_path(root,subjId,ses,0),'file'));
    for task = 1 : 4
        isTask{task}(ses) = logical(exist(assemble_path(root,subjId,ses,task),'file'));
    end
end
%--------------------------------------------------------------------------
missing.isAnat = isAnat;
missing.isTask = isTask;
missing.subjId = subjId;
missing.taskNames = {'rest','spatialnback','audionback','dualnback'};
missing.root = root;
missing.nSes = nSes;
end