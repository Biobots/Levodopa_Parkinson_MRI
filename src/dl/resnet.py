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
        self.relu = nn.functional.relu
        self.conv1 = nn.Conv3d(1, 16, kernel_size=(3, 3, 3), stride=(1, 1, 1), padding=(3, 3, 3)) #1x113x137x113->16x117x141x117
        self.pool1 = nn.MaxPool3d(3, 3) #16x39x47x39
        self.conv2 = nn.Conv3d(16, 32, kernel_size=(3, 3, 3), stride=(2, 2, 2), padding=(1, 1, 1)) #32x20x24x20
        self.pool2 = nn.MaxPool3d(2, 2) #32x10x12x10
        self.fc1 = nn.Linear(32*10*12*10+4, 100)
        self.fc2 = nn.Linear(100, 32)
        self.fc3 = nn.Linear(32, 1)
        
    def forward(self, image, labels):
        x = self.relu(self.conv1(image))
        x = self.pool1(x)
        x = self.relu(self.conv2(x))
        x = self.pool2(x)
        x = x.view(-1, 32*10*12*10)
        x = torch.cat((x, labels), dim=1)
        x = self.relu(self.fc1(x))
        x = self.relu(self.fc2(x))
        x = self.fc3(x)
        return x