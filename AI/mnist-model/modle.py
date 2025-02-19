#  Goals:
#  1. create ML modle utilising https://pytorch.org/tutorials/beginner/basics/saveloadrun_tutorial.html
#  2. utilise https://pytorch.org/tutorials/beginner/nn_tutorial.html for insperation

import torch
import torch.nn as nn
from torch.utils.data import DataLoader

from torchvision import datasets
from torchvision.transforms import ToTensor

import matplotlib.pyplot as plt


#1.build neural network 
#    use CNN layers 

class CCN_Network(nn.Module):
    
    def __init__(self):
        super().__init__()
    
        # input layer 
        self.conInputLayer = nn.Conv2d(in_channels=1, out_channels=16,kernel_size=3, stride=1, padding=1)
        self.relu1 = nn.ReLU()
        
        # TODO : output layer 
            
    def forward(self, x):
        
        x = self.conInputLayer(x)
        x = self.relu1(x)
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
train_dataLoader = DataLoader(trainData, batch_size=64, shuffle=True)
test_dataLoader  = DataLoader(testData,  batch_size=64, shuffle=True)


# TODO: 4.create loss function 


#TODO: 5.create training loop 

#   entrophy loss ? 
#   result given an input ?? 

# shape  torch.Size([batch=64, channels=1, width=28, height=28])

model = CCN_Network()
# print(model)

images, lables = next(iter(train_dataLoader)) # for for loop when in prod 

# plt.imshow(images[0].squeeze(), cmap="gray")
# plt.savefig("input.png")

output = model(images)
print(output)

# for i in range(0, len(output)):
#     plt.imshow(output[i].detach().cpu().numpy(), cmap="gray")
#     plt.savefig(f"output{i}.png")


#TODO: 6.save model e.g. weights



# ================
# micilanious


# prints images within batches 
# for i, batch in enumerate(test_dataLoader):  
    
    # if i >= 1:
    #     break
    
    # for i in range(0, len(batch[0])):
    #     image = batch[0][i]
    #     lable = batch[1][i]
    #     plt.title(lable)
    #     plt.axis("off")
    #     plt.imshow(image.squeeze(), cmap="gray")
    #     plt.savefig("output.png")

