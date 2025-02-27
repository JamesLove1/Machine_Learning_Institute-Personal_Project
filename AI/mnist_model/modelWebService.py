from mnist_model.model import CNN_Network
import os
import torch
from torch.utils.data import DataLoader
import torch.nn.functional as F
import numpy as np
import matplotlib.pyplot as plt

path = os.path.join(os.path.dirname(os.path.abspath(__file__)),"CNN_Network.path")

model = CNN_Network()
model.load_state_dict(torch.load(path))
model.eval()

def modelWebService(data):
    
    npData = np.array(data.img)
    npData = npData.transpose((2, 0, 1))
    
    t = torch.Tensor(npData)
    t = t.unsqueeze(0)
    
    resizedT = F.interpolate(t,(28, 28), mode="bilinear", align_corners=False)
    
    singleChannel = torch.mean(resizedT, dim=1, keepdim=True)
    
    # img_matrix = singleChannel.squeeze().numpy() 
    # plt.imshow(img_matrix, cmap="gray")
    # plt.colorbar()  # Show pixel value range
    # plt.title("Preprocessed Input Image")
    # plt.savefig("./", bbox_inches="tight")
    # plt.close()
    
    res = model(singleChannel)
    res = torch.argmax(res).item()
    
    return res
    