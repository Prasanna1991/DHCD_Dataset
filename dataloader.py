import numpy as np
from torch.utils.data import Dataset, DataLoader


class DHCDataset(Dataset):
    """ Devnagari Handwritten Character Dataset class """

    def __init__(self, npz_file, train=True):
        """
        Args:
        npz_file (string): Path to the NPZ file containing the DHCD
        """
        self.__dataset_npz = np.load(npz_file)
        self.train = train
        self.image_train = self.__dataset_npz['arr_0']
        self.label_train = self.__dataset_npz['arr_1']
        self.image_test = self.__dataset_npz['arr_2']
        self.label_test = self.__dataset_npz['arr_3']

    def __len__(self):
        """
        Returns dataset size
        """
        if self.train:
            return len(self.image_train)
        else:
            return len(self.image_test)

    def __getitem__(self, idx):
        """
        Returns indexed item
        """
        if self.train:
            img, label = self.image_train[idx, ...], self.label_train[idx]
        else:
            img, label = self.image_test[idx, ...], self.label_test[idx]
        return img, label

    def __repr__(self):
        repr_str = 'Devnagari Handwritten Character Dataset \n'
        repr_str += 'Training set contains {} images\n'.format(
            len(self.image_train))
        repr_str += 'Testing set contains {} images\n'.format(
            len(self.image_test))
        return repr_str
