#  Goals:
#  1. create ML modle utilising https://pytorch.org/tutorials/beginner/basics/saveloadrun_tutorial.html
#  2. utilise https://pytorch.org/tutorials/beginner/nn_tutorial.html for insperation

import torch
from torch.utils.data import Dataset
from torchvision import datasets
from torchvision.transforms import ToTensor
import matplotlib.pyplot as plt
from torch.utils.data import DataLoader

# =======================
#1.get data 
trainData = datasets.MNIST(root="", train=True, download=True, transform=ToTensor())
testData = datasets.MNIST(root="", train=False, download=True, transform=ToTensor())

#1a. split / load data into batches 
train_dataLoader = DataLoader(trainData, batch_size=64, shuffle=True)
test_dataLoader  = DataLoader(testData,  batch_size=64, shuffle=True)

for i, batch in enumerate(test_dataLoader):
    
    #print(i)
    
    if i >= 1:
        break
    
    for i in range(0, len(batch[0])):
        image = batch[0][i]
        lable = batch[1][i]
        # print(image)
        # print(lable)

        # img, label = train_dataLoader.dataset[1]
        # plt.figure()
        plt.title(lable)
        plt.axis("off")
        plt.imshow(image.squeeze(), cmap="gray")
        plt.savefig("output.png")


#2.build neural network 
#    use CNN layers 

#3.create loss function 

#4.create training loop 
#   entrophy loss ? 
#   result given an input ?? 

#5.save model e.g. weights


