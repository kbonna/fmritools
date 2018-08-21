function create_derivatives(missing)
% Function features:
%
% (input)   missing: structure informing about available .nii files
%           
% (1)   creates /derivatives folder structure (with BIDS file organisation)
%       for preprocessed images
%
% Author: Kamil Bonna
% ICNT, 01/04/2018
% Ver: MATLAB R2017a
fprintf('\nInitializing...\n');
%--------------------------------------------------------------------------
isAnat = missing.isAnat;
isTask = missing.isTask;
isSession = ( isAnat | isTask{1} | isTask{2} | isTask{3} );
isTaskAny = ( isTask{1} | isTask{2} | isTask{3} );
derRoot = fullfile(missing.root,'derivatives');
%--- subject --------------------------------------------------------------
derSub = fullfile(derRoot,strcat('sub-',num2str(missing.subjId,'%02i')));
if ~logical(exist(derSub,'dir'))
    mkdir(derSub);
    fprintf('Subject %i folder in /derivatives structure created!\n',missing.subjId);
end
    %--- sessions ---------------------------------------------------------
    for ses = find(isSession)
        derSes = fullfile(derSub,strcat('ses-',num2str(ses,'%i')));
            derTask = fullfile(derSes,'func');
            derAnat = fullfile(derSes,'anat');
        if ~logical(exist(derSes,'dir'))
            mkdir(derSes);
            fprintf('|___ Session %i folder created...\n',ses);
        end
        if ~logical(exist(derAnat,'dir')) && isAnat(ses)
            mkdir(derAnat);
            fprintf('    |___ Anatomical folder created... \n');
        end
        if ~logical(exist(derTask,'dir')) && isTaskAny(ses)
            mkdir(derTask);
            fprintf('    |___ Functional folder created... \n');
        end
    end
fprintf('Job done!\n\n');
end