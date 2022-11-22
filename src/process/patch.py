import numpy as np
import os
import os.path
import matplotlib.pyplot as plt
import nibabel as nib
from src.utils.data import writeData, getDataPandas, getMeta, writePatch

def generatePatch(tag):
    meta = getMeta()
    coords = meta['img_config']['thalamus_voxel_coords']
    offsets = meta['img_config']['offsets']
    
    data = getDataPandas()
    
    gmlist = data['GM_PATH']
    reconstruct_list_list = []
    for gmpath in gmlist:
        subpath = gmpath[:-14]
        img_data = nib.load(gmpath).get_fdata()
        reconstruct_list = []
        #os.mkdir(os.path.join(subpath, 'patches'))
        idx = 0
        for vox in coords:
            x, y, z = vox
            dx, dy, dz = offsets
            slcx = img_data[x,y-dy:y+dy+1,z-dz:z+dz+1]
            slcy = img_data[x-dx:x+dx+1,y,z-dz:z+dz+1]
            slcz = img_data[x-dx:x+dx+1,y-dy:y+dy+1,z]
            slcx = (slcx-np.min(slcx))/(np.max(slcx)-np.min(slcx))
            slcy = (slcy-np.min(slcy))/(np.max(slcy)-np.min(slcy))
            slcz = (slcz-np.min(slcz))/(np.max(slcz)-np.min(slcz))
            reconstruct = np.array([slcx, slcy, slcz])
            reconstruct = np.swapaxes(reconstruct, 0, 1)
            reconstruct = np.swapaxes(reconstruct, 1, 2)
            imgpath = os.path.join(subpath, 'patches', str(x)+'x'+str(y)+'x'+str(z)+'.jpg')
            plt.imsave(imgpath, reconstruct)
            reconstruct_list.append(imgpath)
            idx += 1
        reconstruct_list_list.append(reconstruct_list)
    data['PATCH_PATH'] = reconstruct_list_list
    writeData(data.to_dict(orient='records'))
    
    data = data.explode('PATCH_PATH').reset_index(drop=True)[['PATNO', 'EVENT_ID', 'SCORE', 'AGE_AT_VISIT', 'SEX', 'DURATION', 'TIV', 'PATCH_PATH']]
    writePatch(data.to_dict(orient='records'), tag)