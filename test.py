import torch
import torch.utils.data as data_utils
from dataloader import DHCDataset

dhcd_train = DHCDataset(npz_file='./dataset/dataset.npz')
dhcd_test =  DHCDataset(npz_file='./dataset/dataset.npz', train=False)

train_loader = data_utils.DataLoader(dhcd_train, batch_size=5, shuffle=True)
test_loader = data_utils.DataLoader(dhcd_test, batch_size=5, shuffle=True)

print("Training dataset length {} \nTesting dataset length {}".format(len(dhcd_train), len(dhcd_test)))

for batch_idx, (data, label) in enumerate(train_loader):
    image = data
    target = label

for batch_idx, (data, label) in enumerate(test_loader):
    image = data
    target = label

print("Tested. OK")
