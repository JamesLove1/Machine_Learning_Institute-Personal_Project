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
    
    res = model(singleChannel)
    
    predictedNum = torch.argmax(res).item()
    
    predictionConfidence = F.softmax(res, dim=1)[0][predictedNum].item()
      
    return predictedNum, predictionConfidence
    