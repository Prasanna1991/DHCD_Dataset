from PIL import Image
import numpy as np
import os
import re

def getIndex(root):
    ind = re.search('_(.*)_', root)
    return ind.group(1)


image_list_train = []
label_list_train = []

image_list_test = []
label_list_test = []

path = "/home/pkg2182/Downloads/DHCD/Train/"
for root, dirs, files in os.walk(path):
    if files:
        index = getIndex(root)
    for file in files:
        im = Image.open(root+"/"+file)
        image_list_train.append(np.asarray(im))
        label_list_train.append(int(index))


path = "/home/pkg2182/Downloads/DHCD/Test/"
for root, dirs, files in os.walk(path):
    if files:
        index = getIndex(root)
    for file in files:
        im = Image.open(root+"/"+file)
        image_list_test.append(np.asarray(im))
        label_list_test.append(int(index))


np.savez('dataset/dataset.npz', image_list_train, label_list_train, image_list_test, label_list_test)
print("ok")
