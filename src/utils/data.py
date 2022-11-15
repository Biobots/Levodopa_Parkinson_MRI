import json
import os
import os.path
import pandas as pd

def getDataPandas():
    data = pd.read_json(os.path.join('data', 'json', 'data.json'))
    return data

def getPatchPandas():
    data = pd.read_json(os.path.join('data', 'json', 'patch.json'))
    return data

def getMeta():
    with open(os.path.join('data', 'json', 'meta.json'), 'r', encoding="utf-8") as f:
        data = json.load(f)
        return data

def getConfigs():
    with open(os.path.join('data', 'json', 'config.json'), 'r', encoding="utf-8") as f:
        data = json.load(f)
        return data