import torchvision.models as models
from torch import nn
import torch

class ModifiedResNet18(nn.Module):
    def __init__(self):
        super(ModifiedResNet18, self).__init__()
        #self.resnet = models.resnet18(weights='ResNet18_Weights.IMAGENET1K_V1')
        self.resnet = models.resnet50(weights='ResNet50_Weights.IMAGENET1K_V1')
        self.fc = nn.Linear(1000, 1)
        self.relu = nn.ReLU()
        
    def forward(self, image, labels):
        x = self.resnet(image)
        #x = torch.cat((x, labels), dim=1)
        x = self.relu(self.fc(x))
        return x
    
class ModifiedResNet3d(nn.Module):
    def __init__(self):
        super(ModifiedResNet3d, self).__init__()
        self.resnet = models.video.r3d_18()
        self.resnet.stem[0] = nn.Conv3d(1, 64, kernel_size=(7, 7, 7), stride=(2, 2, 2), padding=(3, 3, 3), bias=False)
        self.fc = nn.Linear(404, 1)
        self.relu = nn.ReLU()
        
    def forward(self, image, labels):
        x = self.resnet(image)
        x = torch.cat((x, labels), dim=1)
        x = self.relu(self.fc(x))
        return x