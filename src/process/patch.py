import numpy as np
import os
import os.path
import matplotlib.pyplot as plt
import nilearn as nil
import nibabel as nib
from utils.data import getConfigs, getDataPandas, getMeta

def calMaskCoords():
    configs = getConfigs()
    thalamus_mask = configs['thalamus_mask']
    p_value_map_path = os.path.join(configs['spm_path'], 'TFCE_log_pFWE_0001.nii')
    
    p_data = nil.image.get_data(p_value_map_path)
    p_data[np.isnan(p_data)] = 0
    p_data[p_data < -np.log10(0.05)] = 0
    
    roi_img = nil.image.load_img(thalamus_mask)
    roi = nil.image.get_data(roi_img)
    roi = np.pad(roi, ((27,27),(47,47),(41,41)))
    p_roi = np.logical_and(p_data, roi)
    
    coordslist = []
    for x in range(113):
        for y in range(137):
            for z in range(113):
                if p_roi[x,y,z] == True:
                    coordslist.append((x,y,z))
                    
    return coordslist

def generatePatch():
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