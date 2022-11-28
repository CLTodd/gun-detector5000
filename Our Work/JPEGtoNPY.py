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

Class_Name = [c for c in listdir(repoPath)] # generates a list of all of the class names that we have images for
    
listOfAllPictures = []
labelsForAllPictures = []
labels = { Class_Name[i] : i for i in range(len(Class_Name)) } # generates a dictionary with class name as key and the index of that class name in the class_name vector as the value

for Class in Class_Name:
    print(Class)         # just for debugging
    print(labels[Class]) # just for debugging
    # Determine if we're in the gun class
    # For the purposes of training the binary classifier (gun/not gun), convert the class labels to be binary
    if (labels[Class]==0):
        isGun = 1
    else:
        isGun = 0
    # Find full path of picture files
    fullPath = repoPath + Class + "\\"
    # List of all picture file names
    pictureFiles = [f for f in listdir(fullPath) if isfile(join(fullPath, f))]
    # Convert each picture file into an array of numbers    
    for picFileName in pictureFiles:
        # Convert the image into an array
        arrayVersionOfPicture = imageio.imread(fullPath + picFileName) # Each pixel in the picture gets 3 numbers, one number for each of the RGB values
        listOfAllPictures.append(arrayVersionOfPicture) # Store the array version of the picture
        # Store the class of the picture
        labelsForAllPictures.append(np.array(isGun)) # Storing it as a list of arrays because  I think (?) that's what the training structure was like in the tutorial I saw
    
# Conver the lists to np arrays
listOfAllPictures = np.array(listOfAllPictures, dtype=object)
labelsForAllPictures = np.array(labelsForAllPictures, dtype=object)

# Save the arrays
npyPicFileName = "X:\\445\\Pistol Classification Arrays\\full_data.npy"
npyLabelFileName = "X:\\445\\Pistol Classification Arrays\\full_data_labels.npy"

np.save(npyPicFileName, listOfAllPictures)
np.save(npyLabelFileName, labelsForAllPictures)

