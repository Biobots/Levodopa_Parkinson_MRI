import torchvision.models as models
from torchvision.models.resnet import ResNet
import torch
from torch import nn

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