import torch.nn as nn
import torch
import numpy as np
import matplotlib.pyplot as plt

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
        # self.pool1 = nn.MaxPool2d(kernel_size=2,
        #                           stride=2,
        #                           padding=0
        #                           )
        
        # Fully Connected Layers 
        self.flatten = nn.Flatten()
        self.fc1 = nn.Linear(in_features=16*28*28, out_features=10)
        # self.fc1 = nn.Linear(in_features=16*14*14, out_features=10)
            
    def forward(self, x: torch.Tensor):
        
        self.printX(x, "input")
               
        x = self.conv1(x)
        self.printX(x, "conv1")
        print("conv1", x.data.shape)
        
        x = self.relu1(x)
        print("relu1 ", x.data.shape)
        self.printX(x, "relu1")
        
        # x = self.pool1(x)
        # print("pool1", x.data.shape)
        # self.printX(x, "pool1")

        x = self.flatten(x)
        print("flatten", x.data.shape)
        # self.printX(x, "flatten")
        
        x = self.fc1(x)
        print("final", x.data.shape)
        
        return x 



    def printX(self, x, layer):
        matrix = np.array(x.data.tolist())
        for i in range(0, len(matrix[0])):
            plt.imshow(matrix[0,i], cmap="gray")
            plt.savefig(f"./{layer}_{i}.png")        
        