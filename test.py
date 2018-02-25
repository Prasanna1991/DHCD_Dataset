import torch
import torch.utils.data as data_utils
from dataloader import DHCDDataset

dataManager = DHCDDataset()
train_loader = data_utils.DataLoader(dataManager.train, batch_size=5, shuffle=True)
test_loader = data_utils.DataLoader(dataManager.test, batch_size=5, shuffle=True)


for batch_idx, (data, label) in enumerate(train_loader):
    image = data
    target = label

for batch_idx, (data, label) in enumerate(test_loader):
    image = data
    target = label

print("Tested. OK")