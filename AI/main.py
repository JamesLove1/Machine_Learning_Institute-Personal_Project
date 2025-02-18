from pathlib import Path
import requests
import pickle
import gzip
from matplotlib import pyplot
import numpy as np
import torch
import math
from torch import nn
import torch.nn.functional as F
from torch import optim 
from torch.utils.data import TensorDataset


DATA_PATH = Path("data")
PATH = DATA_PATH / "mnist"

PATH.mkdir(parents=True, exist_ok=True)

URL="https://github.com/pytorch/tutorials/raw/main/_static/"
FILENAME="mnist.pkl.gz"

if not (PATH / FILENAME).exists():
        content = requests.get(URL + FILENAME).content
        (PATH / FILENAME).open("wb").write(content)
        
with gzip.open((PATH / FILENAME).as_posix(), "rb") as f:
        ((x_train, y_train), (x_valid, y_valid), _) = pickle.load(f, encoding="latin-1")

# pyplot.imshow(x_train[0].reshape((28,28)), cmap="gray")
# print(x_train.shape)

x_train, y_train, x_valid, y_valid = map(
    torch.tensor, (x_train, y_train, x_valid, y_valid)
)
train_ds = TensorDataset(x_train, y_train)
n, c = x_train.shape

# print(x_train, y_train)
# print(x_train.shape)
# print(y_train.min(), y_train.max())

lr = 0.5  # learning rate 
epochs = 2 # how many epochs to train for
bs = 64 # batch size

loss_func = F.cross_entropy

class Mnist_Logistic(nn.Module):
    
    def __init__(self):
        super().__init__()
        self.lin = nn.Linear(784, 10)
        
    def forward(self, xb):
        return self.lin(xb)
        
def get_model():
    model = Mnist_Logistic()
    return model, optim.SGD(model.parameters(), lr=lr)

model, opt = get_model()

def fit(): # training loop
    for epoch in range(epochs):
        for i in range((n-1) // bs + 1):
            xb, yb = train_ds[i * bs: i * bs + bs]            
            pred = model(xb)
            loss = loss_func(pred, yb)
            
            loss.backward()
            opt.step()
            opt.zero_grad()

    print()
    print(loss_func(model(xb), yb))
    print()


fit()
# ===================================================
# got up to         
# https://pytorch.org/tutorials/beginner/nn_tutorial.html#refactor-using-dataset
