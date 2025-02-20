#  Goals:
#  1. create ML modle utilising https://pytorch.org/tutorials/beginner/basics/saveloadrun_tutorial.html
#  2. utilise https://pytorch.org/tutorials/beginner/nn_tutorial.html for insperation

import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import DataLoader

from torchvision import datasets
from torchvision.transforms import ToTensor

import matplotlib.pyplot as plt

#1.build neural network 
#    use CNN layers 
class CCN_Network(nn.Module):
    
    def __init__(self):
        super().__init__()
    
        # input layer - Feature Extraction 
        self.conv1 = nn.Conv2d(in_channels=1, out_channels=16,kernel_size=3, stride=1, padding=1)
        self.relu1 = nn.ReLU()
        self.pool1 = nn.MaxPool2d(kernel_size=2, stride=2, padding=0)
        
        # output layer 
        self.flatten = nn.Flatten()
        self.fc1 = nn.Linear(in_features=16*14*14, out_features=10)
            
    def forward(self, x):
        
        x = self.conv1(x)
        x = self.relu1(x)
        x = self.pool1(x)
        x = self.flatten(x)
        x = self.fc1(x)
        
        return x 

#2.get data 
trainData = datasets.MNIST(root="", 
                           train=True, 
                           download=True, 
                           transform=ToTensor()
                           )

testData = datasets.MNIST(root="", 
                          train=False, 
                          download=True, 
                          transform=ToTensor()
                          )

#3. split / load data into batches 
train_dataLoader = DataLoader(trainData, 
                              batch_size=64,
                              shuffle=True
                              )

test_dataLoader  = DataLoader(testData,
                              batch_size=64,
                              shuffle=True
                              )


# TODO: 4. create training loop 
# ==================GOT UP TO HERE====================
#   entrophy loss ? 
#   result given an input ?? 

# epochs = 2
# model = CCN_Network()

# for epoch in epochs:
    
#     for images, lables in train_dataLoader:
         
#         x = model(images)


# finalOutput = torch.argmax(x, dim=1)
# print("final ", finalOutput)


# TODO: 5.create loss function 
# loss = F.cross_entropy()

# TODO: 6.save model e.g. weights

