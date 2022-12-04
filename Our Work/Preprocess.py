# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 10:37:35 2022

@author: Candace Todd
"""
import numpy
import imageio
from skimage.transform import resize # There are other resizing methods we can use, I somewhat arbitrarily chose this one

# Takes in an image file (ex, JPEG), returns a usable version of the image as a numpy array
def ImageCleaner(pathToImage):
    # Read in image as an array
    image = numpy.array(imageio.imread(pathToImage), dtype=float) # The resize function gives you an error about not being able to convert objects to floats if you don't do this
     
    # Check if the image is grayscale
    if len(numpy.shape(image))==2:
        # Convert grayscale images to 3-channel rgb
        image = numpy.stack((image,)*3, axis=-1) 
        
    # Check if the image is the right size: 120 by 160 by 3
    if numpy.shape(image) != (120,160,3):
       # reshaping images that are the wrong size
       image = resize(image, (120, 160, 3))
       
    return(image)
