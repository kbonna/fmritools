function [ matlabbatch ] = batch_func_job(pathAnat,pathDefo,pathFunc)

%--- grab files -----------------------------------------------------------
matlabbatch{1}.cfg_basicio.file_dir.file_ops.cfg_named_file.name = 'EPI';
matlabbatch{1}.cfg_basicio.file_dir.file_ops.cfg_named_file.files = {cellstr(pathFunc)};
matlabbatch{2}.cfg_basicio.file_dir.file_ops.cfg_named_file.name = 'T1';
matlabbatch{2}.cfg_basicio.file_dir.file_ops.cfg_named_file.files = {cellstr(pathAnat)};
matlabbatch{3}.cfg_basicio.file_dir.file_ops.cfg_named_file.name = 'defo';
matlabbatch{3}.cfg_basicio.file_dir.file_ops.cfg_named_file.files = {cellstr(pathDefo)};

%--- slice timing ---------------------------------------------------------
matlabbatch{4}.spm.temporal.st.scans{1}(1) = cfg_dep('Named File Selector: EPI(1) - Files', substruct('.','val', '{}',{1}, '.','val', '{}',{1}, '.','val', '{}',{1}, '.','val', '{}',{1}), substruct('.','files', '{}',{1}));
matlabbatch{4}.spm.temporal.st.nslices = 42;
matlabbatch{4}.spm.temporal.st.tr = 2;
matlabbatch{4}.spm.temporal.st.ta = 1.95238095238095;
matlabbatch{4}.spm.temporal.st.so = [1 3 5 7 9 11 13 15 17 19 21 23 25 27 29 31 33 35 37 39 41 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 42];
matlabbatch{4}.spm.temporal.st.refslice = 1;
matlabbatch{4}.spm.temporal.st.prefix = 'a_';

%--- motion correction ----------------------------------------------------
matlabbatch{5}.spm.spatial.realign.estwrite.data{1}(1) = cfg_dep('Slice Timing: Slice Timing Corr. Images (Sess 1)', substruct('.','val', '{}',{4}, '.','val', '{}',{1}, '.','val', '{}',{1}), substruct('()',{1}, '.','files'));
matlabbatch{5}.spm.spatial.realign.estwrite.eoptions.quality = 0.9;
matlabbatch{5}.spm.spatial.realign.estwrite.eoptions.sep = 4;
matlabbatch{5}.spm.spatial.realign.estwrite.eoptions.fwhm = 5;
matlabbatch{5}.spm.spatial.realign.estwrite.eoptions.rtm = 1;
matlabbatch{5}.spm.spatial.realign.estwrite.eoptions.interp = 2;
matlabbatch{5}.spm.spatial.realign.estwrite.eoptions.wrap = [0 0 0];
matlabbatch{5}.spm.spatial.realign.estwrite.eoptions.weight = '';
matlabbatch{5}.spm.spatial.realign.estwrite.roptions.which = [2 1];
matlabbatch{5}.spm.spatial.realign.estwrite.roptions.interp = 4;
matlabbatch{5}.spm.spatial.realign.estwrite.roptions.wrap = [0 0 0];
matlabbatch{5}.spm.spatial.realign.estwrite.roptions.mask = 1;
matlabbatch{5}.spm.spatial.realign.estwrite.roptions.prefix = 'r';

%--- coregiestration EPI to T1 --------------------------------------------
matlabbatch{6}.spm.spatial.coreg.estimate.ref(1) = cfg_dep('Named File Selector: T1(1) - Files', substruct('.','val', '{}',{2}, '.','val', '{}',{1}, '.','val', '{}',{1}, '.','val', '{}',{1}), substruct('.','files', '{}',{1}));
matlabbatch{6}.spm.spatial.coreg.estimate.source(1) = cfg_dep('Realign: Estimate & Reslice: Mean Image', substruct('.','val', '{}',{5}, '.','val', '{}',{1}, '.','val', '{}',{1}, '.','val', '{}',{1}), substruct('.','rmean'));
matlabbatch{6}.spm.spatial.coreg.estimate.other(1) = cfg_dep('Realign: Estimate & Reslice: Resliced Images (Sess 1)', substruct('.','val', '{}',{5}, '.','val', '{}',{1}, '.','val', '{}',{1}, '.','val', '{}',{1}), substruct('.','sess', '()',{1}, '.','rfiles'));
matlabbatch{6}.spm.spatial.coreg.estimate.eoptions.cost_fun = 'nmi';
matlabbatch{6}.spm.spatial.coreg.estimate.eoptions.sep = [4 2];
matlabbatch{6}.spm.spatial.coreg.estimate.eoptions.tol = [0.02 0.02 0.02 0.001 0.001 0.001 0.01 0.01 0.01 0.001 0.001 0.001];
matlabbatch{6}.spm.spatial.coreg.estimate.eoptions.fwhm = [7 7];

%--- normalization --------------------------------------------------------
matlabbatch{7}.spm.spatial.normalise.write.subj.def(1) = cfg_dep('Named File Selector: defo(1) - Files', substruct('.','val', '{}',{3}, '.','val', '{}',{1}, '.','val', '{}',{1}, '.','val', '{}',{1}), substruct('.','files', '{}',{1}));
matlabbatch{7}.spm.spatial.normalise.write.subj.resample(1) = cfg_dep('Coregister: Estimate: Coregistered Images', substruct('.','val', '{}',{6}, '.','val', '{}',{1}, '.','val', '{}',{1}, '.','val', '{}',{1}), substruct('.','cfiles'));
matlabbatch{7}.spm.spatial.normalise.write.woptions.bb = [-78 -112 -70
                                                          78 76 85];
matlabbatch{7}.spm.spatial.normalise.write.woptions.vox = [2 2 2];
matlabbatch{7}.spm.spatial.normalise.write.woptions.interp = 4;
matlabbatch{7}.spm.spatial.normalise.write.woptions.prefix = 'w';

%--- smoothing ------------------------------------------------------------
matlabbatch{8}.spm.spatial.smooth.data(1) = cfg_dep('Normalise: Write: Normalised Images (Subj 1)', substruct('.','val', '{}',{7}, '.','val', '{}',{1}, '.','val', '{}',{1}, '.','val', '{}',{1}), substruct('()',{1}, '.','files'));
matlabbatch{8}.spm.spatial.smooth.fwhm = [8 8 8];
matlabbatch{8}.spm.spatial.smooth.dtype = 0;
matlabbatch{8}.spm.spatial.smooth.im = 0;
matlabbatch{8}.spm.spatial.smooth.prefix = 's';

end