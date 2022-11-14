# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 00:38:37 2022

@author: Candace Todd
"""
# Don't try to run this, this is just here to document how we preprocessed the data
# this will only work on a PSU lab computer logged into Candace's PSU account

import numpy as np
import imageio
from os import listdir
from os.path import isfile, join

repoPath ="C:\\Users\\CLT5441\\source\\repos\\gun-detector5000\\Pistol classification\\"

Class_Name = [c for c in listdir(repoPath)]
    
listOfAllPictures = []
labelsForAllPictures = []
labels = { Class_Name[i] : i for i in range(len(Class_Name)) }

for Class in Class_Name:
    print(Class)
    print(labels[Class])
    # Determine if we're in the gun class
    if (labels[Class]==0):
        isGun = 1
    else:
        isGun = 0
    # Find full path of picture files
    fullPath = repoPath + Class + "\\"
    # List of all picture file names
    pictureFiles = [f for f in listdir(fullPath) if isfile(join(fullPath, f))]
    # Convert each picture file into an array   
    for picFileName in pictureFiles:
        # Store the array version of the picture
        listOfAllPictures.append(imageio.imread(fullPath + picFileName))
        # Store the class of the picture
        # Storing it as a list of arrays because  I think (?) that's what the training structure was like in the tutorial I saw
        labelsForAllPictures.append(np.array(isGun))
    
# Conver the lists to np arrays
listOfAllPictures = np.array(listOfAllPictures, dtype=object)
labelsForAllPictures = np.array(labelsForAllPictures, dtype=object)

# Save the arrays
npyPicFileName = "X:\\445\\Pistol Classification Arrays\\full_data.npy"
npyLabelFileName = "X:\\445\\Pistol Classification Arrays\\full_data_labels.npy"

np.save(npyPicFileName, listOfAllPictures)
np.save(npyLabelFileName, labelsForAllPictures)

