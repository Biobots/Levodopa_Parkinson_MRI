import os
import os.path
from nipype.pipeline.engine import Workflow, Node, MapNode
from src.utils.data import getDataPandas
import nipype.interfaces.io as nio
from nipype.interfaces.spm import Smooth
from nipype.interfaces.fsl import ApplyMask

data = getDataPandas()
key_list = data['KEY'].tolist()
wf = Workflow(name='test', base_dir='tmp')
src = Node(nio.DataGrabber(infields=['key'], outfields=['in_files']), name='src')
src.inputs.base_directory = os.path.abspath('.')
src.inputs.template = '../t1/%s/reg_Warped_pve_1.nii'
src.inputs.sort_filelist = False
src.inputs.key = key_list
sm = MapNode(Smooth(), name='sm', iterfield=['in_files'])
sm.inputs.fwhm = [4,4,4]
msk = MapNode(ApplyMask(), name='msk', iterfield=['in_file'])
msk.inputs.mask_file = '/home/biobot/levodopa/mni/PD25-atlas-mask-1mm.nii'
msk.inputs.output_type = 'NIFTI'
wf.connect([
    (src, sm, [('in_files', 'in_files')]),
    (sm, msk, [('smoothed_files', 'in_file')]),
])
wf.run(plugin='MultiProc', plugin_args={'n_procs': 8})