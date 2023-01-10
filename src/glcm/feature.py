import numpy as np
from scipy.stats import kurtosis, skew

# First order

def first_feature_mean(img, mask):
    caudatelist = img[mask == 1]
    putamenlist = img[mask == 2]
    nigralist = img[mask == 3]
    thalamuslist = img[mask == 4]
    caudate_mean = np.mean(caudatelist)
    putamen_mean = np.mean(putamenlist)
    nigra_mean = np.mean(nigralist)
    thalamus_mean = np.mean(thalamuslist)
    return [caudate_mean, putamen_mean, nigra_mean, thalamus_mean]

def first_feature_std(img, mask):
    caudatelist = img[mask == 1]
    putamenlist = img[mask == 2]
    nigralist = img[mask == 3]
    thalamuslist = img[mask == 4]
    caudate_std = np.mean(caudatelist)
    putamen_std = np.mean(putamenlist)
    nigra_std = np.mean(nigralist)
    thalamus_std = np.mean(thalamuslist)
    return [caudate_std, putamen_std, nigra_std, thalamus_std]

def first_feature_kurt(img, mask):
    caudatelist = img[mask == 1]
    putamenlist = img[mask == 2]
    nigralist = img[mask == 3]
    thalamuslist = img[mask == 4]
    caudate_kurt = kurtosis(caudatelist)
    putamen_kurt = kurtosis(putamenlist)
    nigra_kurt = kurtosis(nigralist)
    thalamus_kurt = kurtosis(thalamuslist)
    return [caudate_kurt, putamen_kurt, nigra_kurt, thalamus_kurt]

def first_feature_skew(img, mask):
    caudatelist = img[mask == 1]
    putamenlist = img[mask == 2]
    nigralist = img[mask == 3]
    thalamuslist = img[mask == 4]
    caudate_skew = skew(caudatelist)
    putamen_skew = skew(putamenlist)
    nigra_skew = skew(nigralist)
    thalamus_skew = skew(thalamuslist)
    return [caudate_skew, putamen_skew, nigra_skew, thalamus_skew]

# Second order

# 0, 45, 90, 135, 0z
# (1, 0, 0), (1, 1, 0), (0, 1, 0), (-1, 1, 0), (0, 0, 1)
# Single ROI
def cal_GLCM(img, idxlist, offset):
    offsetIdxlist = idxlist - np.array(offset)
    # Initialize GLCM 8x8
    np.zeros((8, 8), dtype=int)
    ## Normalization
    img_ref = img.copy()
    
    ## Level
    pass