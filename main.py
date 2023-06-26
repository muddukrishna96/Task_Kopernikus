# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 17:08:29 2023

@author: muddu krishna galavalli

"""
import cv2
import imutils
import os
from imaging_interview  import preprocess_image_change_detection
from imaging_interview  import compare_frames_change_detection
from PIL import Image
import shutil

class Config():
    """Base configuration class. For custom configurations, create a
    sub-class that inherits from this one and override properties
    that need to be changed.
    """
    gaussian_blur_radius_list = None
    black_mask=(5, 10, 5, 0)
    min_contour_area=0.5
    similarity_tresh = 40
    new_shape = (640, 480)  # New width and height

    
config = Config()

print(config.gaussian_blur_radius_list)


if __name__ == "__main__" :
    
    #TODO: Specify the directory path where the images are stored
    directory = r"C:\Users\mgalaval\Desktop\personal\kopernikus_task\dataset"# Dataset dir
    similar_img_dir = r'C:\Users\mgalaval\Desktop\personal\kopernikus_task\similar_images' # Directory to store similar images
    
    # Get the list of files in the directory
    files = os.listdir(directory)
    
    # Filter the files to keep only the .png images
    png_files = [file for file in files if file.endswith(".png")]
    j = 1 #counter to move next_image
    k = 0 #counter to move prev_image
    
    print('Checking for similar images this could take a bit of time.....')
    
    # Iterate through the images
    for i in range(int(len(png_files)/2)):
        prev_frame = cv2.imread(os.path.join(directory,png_files[k])) # Reading the iamge from its directory
        prev_frame_resized = cv2.resize(prev_frame, config.new_shape) # Reshape the image to a new shape
        prev_frame = preprocess_image_change_detection(prev_frame_resized, config.gaussian_blur_radius_list, config.black_mask) #pre processing
    
    
        next_frame = cv2.imread(os.path.join(directory,png_files[j])) 
        next_frame_resized = cv2.resize(next_frame, config.new_shape) # Reshape the image to a new shape
        next_frame = preprocess_image_change_detection(next_frame_resized, config.gaussian_blur_radius_list, config.black_mask) #pre processing
        
        
        
        score, res_cnts, thresh,similarity= compare_frames_change_detection(prev_frame, next_frame, config.min_contour_area)
        
        '''
        if the similarity score is greater than a pre assigned trushold .
        the image in the next_image variable is moved to a pre determined
        directory and the next image in the list is assigned to next_image variable .
        
        else,
        the image in the next_image variable is assigned to the prev_image variable,
        and the subsequent image is assigned to the next_image variable.
        '''
        
        if similarity > config.similarity_tresh: 
            destination_path = os.path.join(similar_img_dir, png_files[j])
            source_path=os.path.join(directory,png_files[j])
            shutil.move(source_path, destination_path)
            j = j+1
        else:
            i=j
            j=j+1
            
    print('Check for the similar images complete you can check the simmilar images in Directory to store similar images ')

