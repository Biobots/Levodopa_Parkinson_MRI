import nibabel as nib
import numpy as np
import pandas as pd
from scipy.stats import zscore
from sklearn.decomposition import PCA

def load_img(rec, img_path_tag):
    img_data = np.array(nib.load(rec[img_path_tag]).get_fdata())
    return img_data

def load_imgs(df, img_path_tag):
    return df.apply(lambda d: load_img(d, img_path_tag), axis=1)

def PCA_fit_transform(vox, params):
    pca = PCA(n_components=params['n_components'], random_state=params['pca_random_state'])
    features = pca.fit_transform(vox)
    features = pd.DataFrame(features, columns=['PCA_{}'.format(i+1) for i in range(features.shape[1])])
    return features, pca

def PCA_transform(vox, pca):
    features = pca.transform(vox)
    features = pd.DataFrame(features, columns=['PCA_{}'.format(i+1) for i in range(features.shape[1])])
    return features

def gen_pca(data, train_idx, test_idx, params):
    vox = load_imgs(data, params['img_path_tag'])
    vox = np.array([np.array(l) for l in vox])
    vox = np.reshape(vox, (vox.shape[0], -1))
    # Drop 0 along axis0
    #vox = vox[:, ~np.all(vox==0, axis=0)]
    #vox = zscore(vox, axis=1)
    pca_train, pca = PCA_fit_transform(vox[train_idx], params)
    pca_test = PCA_transform(vox[test_idx], pca)
    return pca_train, pca_test