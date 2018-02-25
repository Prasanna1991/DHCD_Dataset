import torch
import torch.utils.data as data_utils
import numpy as np

class DHCDDataset():
    def __init__(self, root = 'dataset/dataset.npz'):
        datasetFile = np.load(root)

        self.imageTrain = datasetFile['arr_0']
        self.labelTrain = datasetFile['arr_1']
        self.imageTest = datasetFile['arr_2']
        self.labelTest = datasetFile['arr_3']

        self.train = data_utils.TensorDataset(torch.from_numpy(self.imageTrain).type(torch.FloatTensor),
                                 torch.from_numpy(self.labelTrain).type(torch.LongTensor))
        self.test = data_utils.TensorDataset(torch.from_numpy(self.imageTest).type(torch.FloatTensor),
                                 torch.from_numpy(self.labelTest).type(torch.LongTensor))
