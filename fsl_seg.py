import os
import os.path
from nipype.pipeline.engine import Workflow, Node, MapNode
from src.utils.data import getDataPandas
from nipype.interfaces.fsl import FAST
import nipype.interfaces.io as nio

data = getDataPandas()
key_list = data['KEY'].tolist()

wf = Workflow(name='test', base_dir='tmp')

src = Node(nio.DataGrabber(infields=['key'], outfields=['in_files']), name='src')
src.inputs.base_directory = os.path.abspath('.')
src.inputs.template = '../t1/%s/reg_Warped.nii.gz'
src.inputs.sort_filelist = False
src.inputs.key = key_list

seg = MapNode(FAST(), name='seg', iterfield=['in_files'])
seg.inputs.output_type = 'NIFTI'
seg.inputs.segments = True
seg.inputs.probability_maps = True
seg.inputs.number_classes = 3

sink = Node(nio.DataSink(), name='sink')
sink.inputs.base_directory = os.path.abspath('../t1/test')
seg_sub = [('_seg'+str(i), key_list[i]) for i in range(len(key_list))]
sink.inputs.substitutions = seg_sub

wf.connect([
    (src, seg, [('in_files', 'in_files')]),
    (seg, sink, [('partial_volume_files', '@seg')]),
])

wf.run(plugin='MultiProc', plugin_args={'n_procs': 8})