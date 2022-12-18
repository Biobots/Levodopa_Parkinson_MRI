import numpy as np
import os
import os.path
import nibabel as nib
from src.utils.data import writeData, getDataPandas, getMeta, writeBlock, getDataTagPandas
from sklearn.decomposition import PCA

def readVoxels():
    meta = getMeta()
    data = getDataPandas()

    coords = np.array(meta['img_config']['thalamus_voxel_coords'])
    gmlist = data['SGM_PATH']
    
    coordx = coords[:, 0]
    coordy = coords[:, 1]
    coordz = coords[:, 2]
    
    voxels = np.empty((0, len(coords)))
    
    for i in range(len(data)):
        img_data = nib.load(gmlist[i]).get_fdata()
        vox = [img_data[coordx, coordy, coordz]]
        voxels = np.append(voxels, vox, axis=0)
        
    return voxels

def imgPCA(labels, feature_num=0.999):
    pca = PCA(n_components=feature_num)
    features = pca.fit_transform(labels)
    return pca, np.array(features)