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
    
for Class in Class_Name:
    fullPath = repoPath + Class + "\\"
    pictureFiles = [f for f in listdir(fullPath) if isfile(join(fullPath, f))]
    pictures = list()    
    for picFileName in pictureFiles:
        pictures.append(imageio.imread(fullPath + picFileName))
    
    pictures = np.array(pictures, dtype=object)
    npyFileName = "X:\\445\\Pistol Classification Arrays\\" + Class + ".npy"
    print(npyFileName)
    np.save(npyFileName, pictures)

