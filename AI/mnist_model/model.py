import torch.nn as nn
import torch
import numpy as np

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
            
    def forward(self, x: torch.Tensor):
        
        print(x.data[0][0].tolist())
        print(x.data[0][0].shape)
        
        matrix = np.array(x.data[0][0].tolist())
    
        print(len(matrix[:,0])) 
               
        x = self.conv1(x)
        x = self.relu1(x)
        x = self.pool1(x)
        x = self.flatten(x)
        x = self.fc1(x)
        return x 

