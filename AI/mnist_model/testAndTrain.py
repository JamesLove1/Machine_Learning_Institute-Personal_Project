#  Goals:
#  1. create ML model utilising https://pytorch.org/tutorials/beginner/basics/saveloadrun_tutorial.html
#  2. utilise https://pytorch.org/tutorials/beginner/nn_tutorial.html for insperation

# Model Imports
from model import CNN_Network

# Torch Imports
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import DataLoader, ConcatDataset

# Torch Vision Imports
from torchvision import datasets, transforms
from torchvision.transforms import ToTensor

# Other Imports
import matplotlib.pyplot as plt
from tqdm import tqdm

#1. 
def fetch_data():
    print("\nFetching Data")
    
    transformations = transforms.Compose([
        transforms.RandomAffine(
            degrees=0,
            scale=(.6,1),
            translate=(0.2,0.1),
            fill=0
        ),
        transforms.ToTensor()
    ])
    
    trainData = datasets.MNIST(root="", 
                               train=True, 
                               download=True, 
                               transform=transformations
                               )

    testData = datasets.MNIST(root="", 
                              train=False, 
                              download=True, 
                              transform=ToTensor()
                              )
    
    return trainData, testData

#2.
def load_data(trainData, testData):
    print("\nLoading Data")
    train_dataLoader = DataLoader(trainData, 
                                  batch_size=64,
                                  shuffle=True
                                  )

    test_dataLoader  = DataLoader(testData,
                                  batch_size=64,
                                  shuffle=False
                                  )
    
    return train_dataLoader, test_dataLoader

#3. 
def train_model(model, train_dataLoader):
    epochs = 5 # 5 works better though dimminisihing returns post 2 epochs
    lr = 0.001
    loss_func = nn.CrossEntropyLoss()    
    optimiser = torch.optim.Adam(model.parameters(), lr=lr)

    for epoch in range(epochs):

        print(f"\nEpoch [{epoch+1}/{epochs}]") 

        for images, lables in tqdm(train_dataLoader):

            optimiser.zero_grad()

            x = model(images)

            loss = loss_func(x, lables)

            loss.backward()

            optimiser.step()

#4.
def evlauate_model(model, test_dataLoader):
    loss_func = nn.CrossEntropyLoss()   
    model.eval()
    totalLoss = 0
    cntBatches = 0
    
    totalLables = 0
    correctLables = 0
    
    with torch.no_grad():
        
        for images, lables in test_dataLoader:
            
            x = model(images)
            
            loss = loss_func(x, lables)
            
            totalLoss += loss
            cntBatches += 1
            
            totalLables += lables.size(0)
            correctLables += (torch.argmax(x, dim=1) == lables).sum().item()
            
            
    print(f"\nloss: {totalLoss/cntBatches}")
    print(f"\nAccuracy: {(correctLables/totalLables)*100}%\n")

#5.
def train_evaluate_save_Model():
    
    model = CNN_Network()
    
    trainData, testData = fetch_data()
    train_dataLoader, test_dataLoader = load_data(trainData, testData)
    
    train_model(model, train_dataLoader)
    evlauate_model(model, test_dataLoader)
    
    torch.save(model.state_dict(), "CNN_Network.path")
    
#6.
def load_model():
    
    model = CNN_Network()
    model.load_state_dict(torch.load("CNN_Network.path"))
    model.eval()
    
    trainData, testData = fetch_data()
    train_dataLoader, test_dataLoader = load_data(trainData, testData)
    
    evlauate_model(model, test_dataLoader)
    
if __name__ == "__main__":    
    
    train_evaluate_save_Model()
    
    load_model()