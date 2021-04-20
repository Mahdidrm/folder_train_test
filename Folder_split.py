# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 15:47:29 2021

@author: mehdi
"""


import os
import numpy as np
import shutil
import random

# # Creating Train / Val / Test folders (One time use)
root_dir = 'D:/XAI/DB/DISFA/48/'
classes_dir = ['/A', '/B', '/C', '/D', '/E', '/F', '/G']

val_ratio = 0.2


for cls in classes_dir:
    os.makedirs(root_dir +'/training' + cls)
    os.makedirs(root_dir +'/validation' + cls)


    # Creating partitions of the data after shuffeling
    src = root_dir + cls # Folder to copy images from

    allFileNames = os.listdir(src)
    np.random.shuffle(allFileNames)
    train_FileNames, val_FileNames = np.split(np.array(allFileNames),
                                                              [int(len(allFileNames)* (1 - val_ratio))])


    train_FileNames = [src+'/'+ name for name in train_FileNames.tolist()]
    val_FileNames = [src+'/' + name for name in val_FileNames.tolist()]
    # test_FileNames = [src+'/' + name for name in test_FileNames.tolist()]

    print('Total images: ', len(allFileNames))
    print('Training: ', len(train_FileNames))
    print('Validation: ', len(val_FileNames))
    # print('Testing: ', len(test_FileNames))

    # Copy-pasting images
    for name in train_FileNames:
        shutil.copy(name, root_dir +'/training' + cls)

    for name in val_FileNames:
        shutil.copy(name, root_dir +'/validation' + cls)
