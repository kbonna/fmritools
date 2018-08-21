function [ toolboxPath ] = return_toolbox_path(toolboxName)
% Function features:
%
% (input)   toolboxName: string with toolbox name (e.g. spm12)
%
% (1)   this script return MATLAB search path for given toolbox
%
% Author: Kamil Bonna
% ICNT, 07/04/2018
% Ver: MATLAB R2017a
%--- get path -------------------------------------------------------------
a = path;
ind = strfind(a,toolboxName);
% if not found throw exeption
if isempty(ind)
    error('Toolbox not found!');
end
%--- find boundaries ------------------------------------------------------
i_max = ind(1);
while ~( strcmp(a(i_max),':') || ( i_max == numel(a) ) )
    i_max = i_max + 1;
end
i_min = ind(1);
while ~( strcmp(a(i_min),':') || ( i_min == 1 ) )
    i_min = i_min - 1;
end
%--- corner cases ---------------------------------------------------------
if i_min > 1
    i_min = i_min + 1;
end
if i_max ~= numel(a)
    i_max = i_max - 1;
end
%--- cut subfolders -------------------------------------------------------
a = a(i_min:i_max);
ind = strfind(a,toolboxName); ind = ind(1); %(ensure first name)
i_cut = ind + numel(toolboxName);
toolboxPath = a(1:i_cut-1);


