
from mnist_model.model import CNN_Network

import os
import sys

import torch

model = CNN_Network()


path = os.path.join(os.path.dirname(os.path.abspath(__file__)),"CNN_Network.path")

print(torch.load(path))

model.load_state_dict(torch.load(path))
model.eval()

def modelWebService(data):
    
    print(data.num)
    
    
    return
    # input = torch.randn(1, 1, 28, 28)
    
    # print(input)
    # print(input.shape)
    # print(type(input))
    
    # ======== I need to transform the input data =======
    
    # what sort of input to the modle do i need?
    
    # output = model()

    # need torch argmax here to convert logits to class labels

    # return output






#  debugging
if __name__ == "__main__":

    class Data:
        num = "10"

    modelWebService(Data())