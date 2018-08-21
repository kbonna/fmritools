function fix_dti_json(path)
% Function features:
%
% (input)   path: path to .json DWI file
%
% (1)   this function fixes .json DWI file converted using dicm2nii.m to be 
%       BIDS-compatibile
%
% Author: Kamil Bonna
% ICNT, 21/03/2018
% Ver: MATLAB R2017a
%% body
    fileId = fopen(path);
    S = textscan(fileId, '%s', 'delimiter', '\n');
    % find first marker
    i1 = 1;
    while ~contains(S{1}{i1},'DiffusionGradientOrientation')
       i1 = i1 + 1; 
    end
    % find second marker
    i2 = i1;
    while ~contains(S{1}{i2},'TotalReadoutTime')
       i2 = i2 + 1; 
    end
    % fix spaces
    for i = i1+1 : i2-2
       f = S{1}{i};
       f(f==' ') = ',';
       S{1}{i} = f;
    end
    % save result
        fileIdT = fopen('temp.json','w');
        fprintf(fileIdT,'%s\n',S{1}{:});
        fclose(fileIdT);
    delete(path);
    movefile('temp.json',path)
end