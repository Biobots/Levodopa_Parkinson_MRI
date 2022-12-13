from torch.utils.data import dataset, Subset, random_split
from torchvision.transforms import transforms
from src.utils.data import getPandas
from PIL import Image
import numpy as np
import torch
from sklearn.model_selection import KFold

class PatchRedressDataset(dataset.Dataset):
    def __init__(self, tag):
        super(PatchRedressDataset, self).__init__()
        self.data = getPandas('patch_'+tag)
        self.score_data = list(self.data["SCORE"])
        self.age_data = list(self.data["AGE_AT_VISIT"] / 100)
        self.sex_data = list(self.data["SEX"])
        self.duration_data = list(self.data["DURATION"] / 100)
        self.tiv_data = list(self.data["TIV"] / 1000)
        self.img_path = list(self.data["PATCH_PATH"])
        self.transform = transforms.Compose([
            transforms.Resize([32, 32]),
            transforms.ToTensor(),
            transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
        ])

    def __getitem__(self, index):
        score = self.score_data[index]
        img = self.transform(Image.open(self.img_path[index]))
        labels = torch.FloatTensor([self.age_data[index], self.sex_data[index], self.duration_data[index], self.tiv_data[index]])
        return img, labels, score

    def __len__(self):
        return len(self.data)
        
class BlockRegressDataset(dataset.Dataset):
    def __init__(self, tag):
        super(BlockRegressDataset, self).__init__()
        self.data = getPandas('data_'+tag)
        self.data = self.data.explode('BLOCK_PATH').reset_index(drop=True)[['PATNO', 'EVENT_ID', 'SCORE', 'AGE_AT_VISIT', 'SEX', 'DURATION', 'TIV', 'BLOCK_PATH']]
        self.score_data = list(self.data["SCORE"])
        self.age_data = list(self.data["AGE_AT_VISIT"] / 100)
        self.sex_data = list(self.data["SEX"])
        self.duration_data = list(self.data["DURATION"] / 100)
        self.tiv_data = list(self.data["TIV"] / 1000)
        self.img_path = list(self.data["BLOCK_PATH"])

    def __getitem__(self, index):
        score = self.score_data[index]
        img = np.load(self.img_path[index])
        #img = ndimage.zoom(img, [32, 32, 32])
        img = torch.FloatTensor(img[np.newaxis, :])
        labels = torch.FloatTensor([self.age_data[index], self.sex_data[index], self.duration_data[index], self.tiv_data[index]])
        return img, labels, score

    def __len__(self):
        return len(self.data)
    
    
class BlockClassifyDataset(dataset.Dataset):
    def __init__(self, tag, bounds):
        super(BlockClassifyDataset, self).__init__()
        #kf = KFold(n_splits=fold_num, shuffle=True, random_state=10)
        self.data = getPandas('data_'+tag)
        self.data = self.data.explode('BLOCK_PATH').reset_index(drop=True)[['PATNO', 'EVENT_ID', 'SCORE', 'AGE_AT_VISIT', 'SEX', 'DURATION', 'TIV', 'BLOCK_PATH']]
        self.score_data = list(self.data["SCORE"])
        self.age_data = list(self.data["AGE_AT_VISIT"] / 100)
        self.sex_data = list(self.data["SEX"])
        self.duration_data = list(self.data["DURATION"] / 100)
        self.tiv_data = list(self.data["TIV"] / 1000)
        self.img_path = list(self.data["BLOCK_PATH"])
        self.bounds = bounds
        self.rst_data = list(map(self.bounds2vec, self.score_data))
        
    def bounds2vec(self, score):
        count = sum(map(lambda b: score > b, self.bounds))
        vec = np.zeros(len(self.bounds)+1, dtype=float)
        vec[count] = 1
        return count

    def __getitem__(self, index):
        #rst = torch.FloatTensor(self.rst_data[index])
        rst = self.rst_data[index]
        img = np.load(self.img_path[index])
        #img = ndimage.zoom(img, [32, 32, 32])
        img = torch.FloatTensor(img[np.newaxis, :])
        labels = torch.FloatTensor([self.age_data[index], self.sex_data[index], self.duration_data[index], self.tiv_data[index]])
        return img, labels, rst

    def __len__(self):
        return len(self.data)

def splitDataset(fold_size, fold_num, dataset):
    test_size = len(dataset) - fold_num * fold_size
    n_fold_size = len(dataset) - test_size
    folds_dataset, test_dataset = random_split(dataset, [n_fold_size, test_size], torch.manual_seed(1))
    size_list = [fold_size] * fold_num
    fold_datasets = list(random_split(folds_dataset, size_list, torch.manual_seed(1)))
    return fold_datasets, test_dataset
