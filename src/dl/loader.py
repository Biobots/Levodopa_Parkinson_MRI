from torch.utils.data import dataset
from torchvision.transforms import transforms
from src.utils.data import getPatchPandas
from PIL import Image
import torch

class PatchDataset(dataset.Dataset):
    def __init__(self):
        super(PatchDataset, self).__init__()
        self.data = getPatchPandas()
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
    
