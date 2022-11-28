# -*- coding: utf-8 -*-
"""
Candace Todd

Convert black and white images that only have 2 dimensions into
3-dimensional RGB images so that every image array is the same depth

Also resize images that are the wrong size

Don't run this, this has only been uploaded for documentation.
It won't run on anyone else's machine.

The directory that this script accesses to make the clean .npy files consists of intermediate files created during JPEGtoNPY.py .
"""
import numpy
from os import listdir
from skimage.transform import resize # There are other resizing methods we can use, I somewhat arbitrarily chose this one

# In this folder, each class has its own .npy file of image arrays
# This does not include the full data and full data labels .npy files
npyPath = "X:\\445\\Pistol Classification Arrays"
# I'm going to go into each .npy file and extract the arrays into one big file
Class_Files = [c for c in listdir(npyPath)] # generates a list of all of the class .npy file that we have images for

# Generate lists to store images and their labels
classLabels = []
allImages = []

for fileName in Class_Files:
    
    print(fileName) # Just for debugging
    
    # Load the .npy file that holds the array for all images in this class
    Images = numpy.load(npyPath + "\\" + fileName, allow_pickle=True)
    
    i=0# Just for debugging
    
    # Go through each image
    for image in Images:
        i+=1 # Just for debugging
        
        image = numpy.array(image, dtype=float) # The resize function gives you an error about not being able to convert objects to floats if you don't do this
        # didn't understand the error but I decided to do this after reading this post: https://stackoverflow.com/questions/32302180/typeerror-image-data-can-not-convert-to-float

        # Check if the image is grayscale
        if len(numpy.shape(image))==2:
            # Convert grayscale images to rgb
            image = numpy.stack((image,)*3, axis=-1) # got this line from https://stackoverflow.com/questions/40119743/convert-a-grayscale-image-to-a-3-channel-image
        
        # Check if the image is the right size: 120 by 160 by 3
        if numpy.shape(image) != (120,160,3):
           # reshaping images that are the wrong size
           image = resize(image, (120, 160, 3))
        
        # Store the image
        allImages.append(image)
        
        # Store the class label of the image
        if fileName== 'AAAPistol.npy':
            classLabels.append(1)
        else:
            classLabels.append(0)
            
        ####### May need to do this instead ##########
        #labelsForAllPictures.append(np.array(isGun))#
        ##############################################

# Convert the lists into arrays
allImagesArray = numpy.array(allImages)#, dtype=object)
classLabelsArray = numpy.array(classLabels)#, dtype=object)
# I commented out the dtype because I don't actually know why I had it before, but I did have it in other scripts

# Save the arrays
npyCleanPicFileName = "X:\\445\\full_data_clean.npy"
npyCleanLabelFileName = "X:\\445\\full_data_clean_labels.npy"
numpy.save(npyCleanPicFileName, allImagesArray)
numpy.save(npyCleanLabelFileName, classLabelsArray)
