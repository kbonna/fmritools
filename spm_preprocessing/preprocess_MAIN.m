clear; clc;
for subjId = [ 1:37, 39:48 ]
clearvars -except subjId
%=== SETTINGS =============================================================
nSes = 4;                               %(total # of sessions)
sessions = [ true, true, true, true ];  %(sessions to analyze)
%=== MAIN =================================================================
%--- get missing struct ---------------------------------------------------
missing = missing_files('LearningBrain', subjId, nSes);
%--- create \derivatives folder structure ---------------------------------
create_derivatives(missing);
%--- preprocess T1 --------------------------------------------------------
preprocess_anat(subjId, sessions, missing);
%--- preprocess EPI -------------------------------------------------------
preprocess_func(subjId, 'rest', sessions, missing);
preprocess_func(subjId, 'spatialnback', sessions, missing);
preprocess_func(subjId, 'audionback', sessions, missing);
preprocess_func(subjId, 'dualnback', sessions, missing);
%==========================================================================
end