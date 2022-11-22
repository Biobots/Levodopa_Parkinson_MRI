import numpy as np
import os
import os.path
import nibabel as nib
from src.utils.data import writeData, getDataPandas, getMeta, writeBlock, getDataTagPandas

def generateBlock():
    meta = getMeta()
    coords = meta['img_config']['thalamus_voxel_coords']
    data = getDataPandas()
    
    coords = np.array(coords)
    x = [np.min(coords[:, 0]), np.max(coords[:, 0])]
    y = [np.min(coords[:, 1]), np.max(coords[:, 1])]
    z = [np.min(coords[:, 2]), np.max(coords[:, 2])]
    
    gmlist = data['GM_PATH']
    for gmpath in gmlist:
        subpath = gmpath[:-14]
        img_data = nib.load(gmpath).get_fdata()
        #os.mkdir(os.path.join(subpath, 'blocks'))
        img_data = img_data[x[0]:x[1], y[0]:y[1], z[0]:z[1]]
        imgpath = os.path.join(subpath, 'blocks', 'block.npy')
        np.save(imgpath, img_data)
        data['BLOCK_PATH'] = imgpath
        
    writeData(data.to_dict(orient='records'))
    
def expandBlock(tag):
    meta = getMeta()
    coords = meta['img_config']['thalamus_voxel_coords']
    offsets = meta['img_config']['offsets']
    
    data = getDataTagPandas(tag)
    
    gmlist = data['GM_PATH']
    reconstruct_list_list = []
    for gmpath in gmlist:
        subpath = gmpath[:-14]
        img_data = nib.load(gmpath).get_fdata()
        reconstruct_list = []
        #os.mkdir(os.path.join(subpath, 'blocks'))
        idx = 0
        for vox in coords:
            x, y, z = vox
            dx, dy, dz = offsets
            tmp_data = img_data[x-dx:x+dx, y-dy:y+dy, z-dz:z+dz]
            imgpath = os.path.join(subpath, 'blocks', str(x)+'x'+str(y)+'x'+str(z)+'.npy')
            np.save(imgpath, tmp_data)
            reconstruct_list.append(imgpath)
            idx += 1
        reconstruct_list_list.append(reconstruct_list)
    data['BLOCK_PATH'] = reconstruct_list_list
    writeData(data.to_dict(orient='records'))
    
    data = data.explode('BLOCK_PATH').reset_index(drop=True)[['PATNO', 'EVENT_ID', 'SCORE', 'AGE_AT_VISIT', 'SEX', 'DURATION', 'TIV', 'BLOCK_PATH']]
    writeBlock(data.to_dict(orient='records'), tag)