spm('defaults','fmri');
spm_jobman('initcfg');
smooth_job = struct;

data = jsondecode(fileread('data/json/data.json'));
nii = {data.T1_GM_PATH};
nii = reshape(nii,length(nii),1);
nii = cellstr(nii);

smooth_job.matlabbatch{1}.spm.spatial.smooth.data = nii;
smooth_job.matlabbatch{1}.spm.spatial.smooth.fwhm = [4 4 4];
smooth_job.matlabbatch{1}.spm.spatial.smooth.dtype = 0;
smooth_job.matlabbatch{1}.spm.spatial.smooth.im = 0;
smooth_job.matlabbatch{1}.spm.spatial.smooth.prefix = 's';

spm_jobman('run',smooth_job.matlabbatch);