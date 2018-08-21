function fix_dti_bv(path)
% Function features:
%
% (input)   path: path to .bval or .bvec DWI file
%
% (1)   this function fixes .bval or .bvec DWI file converted using
%       dicm2nii.m to be BIDS-compatibile
%
% Author: Kamil Bonna
% ICNT, 17/03/2018
% Ver: MATLAB R2017a
%% body
    fileId = fopen(path);
    S = textscan(fileId, '%s', 'delimiter', '\n');
    for i = 1 : numel(S{1})
       S{1}{i} = regexprep(S{1}{i}, '\t', ' '); 
       S{1}{i} = regexprep(S{1}{i}, '  ', ' '); 
    end
    % save result
        fileIdT = fopen('temp','w');
        fprintf(fileIdT,'%s\n',S{1}{:});
        fclose(fileIdT);
    delete(path);
    movefile('temp',path)
end