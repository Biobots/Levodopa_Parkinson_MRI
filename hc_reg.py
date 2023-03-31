import json
import os
import os.path
import pandas as pd
from nipype.pipeline.engine import Workflow, Node, MapNode
from nipype.interfaces.fsl import BET
from nipype.interfaces.ants import RegistrationSynQuick
import nipype.interfaces.io as nio
from src.utils.data import getDataPandas, getPandas

data = getPandas('hc')

src = Node(nio.DataGrabber(infields=['path'], outfields=['in_files']), name='src')
src.inputs.base_directory = os.path.abspath('.')
src.inputs.template = '%s'
src.inputs.sort_filelist = False
src.inputs.path = data['NII_PATH'].tolist()

bet = MapNode(BET(), name='BET', iterfield=['in_file'])
bet.inputs.robust = True # -R

reg = MapNode(RegistrationSynQuick(), name='RegistrationSynQuick', iterfield=['moving_image'])
reg.inputs.fixed_image = os.path.abspath('bin/template.nii.gz') # -f
reg.inputs.output_prefix = 'reg' # -o
reg.inputs.num_threads = 16 # -n

wf = Workflow(name='hc', base_dir='tmp')
wf.connect([
    (src, bet, [('in_files', 'in_file')]),
    (bet, reg, [('out_file', 'moving_image')])
])

wf.run(plugin='MultiProc', plugin_args={'n_procs': 16})