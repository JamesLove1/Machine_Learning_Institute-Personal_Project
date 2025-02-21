#  Goals:
#  1. create ML model utilising https://pytorch.org/tutorials/beginner/basics/saveloadrun_tutorial.html
#  2. utilise https://pytorch.org/tutorials/beginner/nn_tutorial.html for insperation

# Torch Imports
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import DataLoader

# Torch Vision Imports
from torchvision import datasets
from torchvision.transforms import ToTensor

# Other Imports
import matplotlib.pyplot as plt

#1.build neural network  
class CNN_Network(nn.Module):
    
    def __init__(self):
        super().__init__()
    
        # Input Layer/ Feature Extraction 
        self.conv1 = nn.Conv2d(in_channels=1,
                               out_channels=16,
                               kernel_size=3, 
                               stride=1,
                               padding=1
                               )
        self.relu1 = nn.ReLU()
        self.pool1 = nn.MaxPool2d(kernel_size=2,
                                  stride=2,
                                  padding=0
                                  )
        
        # Fully Connected Layers 
        self.flatten = nn.Flatten()
        self.fc1 = nn.Linear(in_features=16*14*14, out_features=10)
            
    def forward(self, x):
        x = self.conv1(x)
        x = self.relu1(x)
        x = self.pool1(x)
        x = self.flatten(x)
        x = self.fc1(x)
        return x 

#2. Fetch Data 
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

#3. Split/load data using batches 
train_dataLoader = DataLoader(trainData, 
                              batch_size=64,
                              shuffle=True
                              )

test_dataLoader  = DataLoader(testData,
                              batch_size=64,
                              shuffle=True
                              )


# TODO: 4. Training Loop 
#   loss function 
#   optimiser weights  

# model = CNN_Network()
# print(model.state_dict())

epochs = 2
lr = 0.001
model = CNN_Network()

loss_func = nn.CrossEntropyLoss()
optimiser = torch.optim.Adam(model.parameters(), lr=lr)


for epoch in range(epochs):
    
    for images, lables in train_dataLoader:
         
        x = model(images)
        
        loss = loss_func(x, lables)

        loss.

        optimiser.zero_grad()
        
        
        

# finalOutput = torch.argmax(x, dim=1)
# print("final ", finalOutput)

# ouput from trainning ?????

# test using validation set 

# TODO: 5.save model e.g. weights
