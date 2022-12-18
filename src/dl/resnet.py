import torchvision.models as models
from torch import nn
import torch

class RegressResNet18(nn.Module):
    def __init__(self):
        super(RegressResNet18, self).__init__()
        #self.resnet = models.resnet18(weights='ResNet18_Weights.IMAGENET1K_V1')
        self.resnet = models.resnet50(weights='ResNet50_Weights.IMAGENET1K_V1')
        self.fc = nn.Linear(1000, 1)
        self.relu = nn.ReLU()
        
    def forward(self, image, labels):
        x = self.resnet(image)
        #x = torch.cat((x, labels), dim=1)
        x = self.relu(self.fc(x))
        return x
    
class RegressResNet3d(nn.Module):
    def __init__(self):
        super(RegressResNet3d, self).__init__()
        self.resnet = models.video.r3d_18()
        self.resnet.stem[0] = nn.Conv3d(1, 64, kernel_size=(7, 7, 7), stride=(2, 2, 2), padding=(3, 3, 3), bias=False)
        self.fc = nn.Linear(404, 1)
        self.relu = nn.ReLU()
        
    def forward(self, image, labels):
        x = self.resnet(image)
        x = torch.cat((x, labels), dim=1)
        x = self.relu(self.fc(x))
        return x
    
class ClassifyResNet3d(nn.Module):
    def __init__(self, cat_num):
        super(ClassifyResNet3d, self).__init__()
        self.resnet = models.video.r3d_18()
        self.resnet.stem[0] = nn.Conv3d(1, 64, kernel_size=(7, 7, 7), stride=(2, 2, 2), padding=(3, 3, 3), bias=False)
        self.fc = nn.Linear(404, cat_num, bias=True)

    def forward(self, image, labels):
        x = self.resnet(image)
        x = torch.cat((x, labels), dim=1)
        x = self.fc(x)
        return x
    
class RegressCNN(nn.Module):
    def __init__(self):
        super(RegressCNN, self).__init__()
        
    def forward(self, image, labels):
        pass