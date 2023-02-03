import json
import os
import os.path
import pandas as pd
import nilearn as nil
import numpy as np

def getPandas(name):
    data = pd.read_json(os.path.join('data', 'json', name+'.json'))
    return data

def getConfig(name):
    with open(os.path.join('pipe', name + '_config.json'), 'r', encoding="utf-8") as f:
        data = json.load(f)
        return data

def getDataPandas():
    data = pd.read_json(os.path.join('data', 'json', 'data.json'))
    return data

def getDataTagPandas(tag):
    data = pd.read_json(os.path.join('data', 'json', 'data_'+tag+'.json'))
    return data

def getPatchPandas():
    data = pd.read_json(os.path.join('data', 'json', 'patch.json'))
    return data

def getBlockPandas():
    data = pd.read_json(os.path.join('data', 'json', 'block.json'))
    return data

def getMeta():
    with open(os.path.join('data', 'json', 'meta.json'), 'r', encoding="utf-8") as f:
        data = json.load(f)
        return data

def getConfigs():
    with open(os.path.join('data', 'json', 'config.json'), 'r', encoding="utf-8") as f:
        data = json.load(f)
        return data
    
def writePandas(name, data):
    data = data.to_dict(orient='records')
    with open(os.path.join('data', 'json', name+'.json'), 'w+', encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    
def writeData(data):
    with open(os.path.join('data', 'json', 'data.json'), 'w+', encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
        
def writePatch(data, tag):
    with open(os.path.join('data', 'json', 'patch_'+tag+'.json'), 'w+', encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
        
def writeBlock(data, tag):
    with open(os.path.join('data', 'json', 'block_'+tag+'.json'), 'w+', encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def group_stratified_train_test_split(data, group, stratify, random_state=None, test_size=0.2):
    pass
        
def splitTestByRatio(name, ratio=0.2):
    data = getPandas(name)
    test = data.sample(frac=ratio, random_state=10)
    train = data.drop(test.index)
    test = test.reset_index(drop=True)
    train = train.reset_index(drop=True)
    writePandas(name+'_test', test)
    writePandas(name+'_train', train)
    
def splitTestByLen(name, num=1000):
    data = getPandas(name)
    test = data.sample(n=num, random_state=10)
    train = data.drop(test.index)
    test = test.reset_index(drop=True)
    train = train.reset_index(drop=True)
    writePandas(name+'_test', test)
    writePandas(name+'_train', train)
    
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