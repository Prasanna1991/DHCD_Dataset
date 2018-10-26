# DHCD_Dataset
This repository contains the DHCD dataset, a dataset of Devnagari (Nepali) handwritten characters.

# LPR
License Plate Recognition (LPR) dataset is also available now at this [link](https://github.com/Prasanna1991/LPR).

## Description

![](https://github.com/Prasanna1991/DHCD_Dataset/blob/master/sample/sample.png?raw=true)

DHCD dataset contains 46 classes [36 character class and 10 digit class] (क .. +  १ .. ) of Devnagari script. Each class
has 2000 images which is divided into two sets: training and test containing 1700 and 300 images respectively. So technically, this dataset is larger both in terms of samples and classes than the famous MNIST dataset which was the initial inspiration for the creation of this dataset. 

This repo contains the dataloader for PyTorch and it can be easily transported to other libraries like TensorFlow, Keras, Caffe etc. 

Beside, the general character classification task, the dataset can also be explored for other problems like transferring style, disentanglement, semi-supervised learnign etc. as there are lot of variations within each class. 

## Example
This [work](https://gist.github.com/suvash/d9fe3aa8d570d42ab65175a057d402a4) by [Suvash Thapaliya](https://twitter.com/suvash) is a recent example of work in this dataset. Resnet-32 is used to obtain the error rate of 1.49% which is the SOTA on this dataset for the task of classification. 


## Contributors
The school children of class 6 and 7 (in 2015) from Mount Everest Higher Secondary School, Bhaktapur, Nepal contributed towards this dataset by
volunteering to write the characters which were scanned manually. Beside the manual scanning, other pre-processing tasks were 
also performed, detail of which can be found in the paper. 

If you use this dataset in your work, please cite it as follows:

## Bibtex
```
@inproceedings{acharya2015deep,
  title={Deep learning based large scale handwritten Devanagari character recognition},
  author={Acharya, Shailesh and Pant, Ashok Kumar and Gyawali, Prashnna Kumar},
  booktitle={Software, Knowledge, Information Management and Applications (SKIMA), 2015 9th International Conference on},
  pages={1--6},
  year={2015},
  organization={IEEE}
}
```
