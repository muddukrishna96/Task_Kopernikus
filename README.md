# Task_Kopernikus
# Change Detection in Image Frames

This repository contains code for performing change detection in a series of image frames. The code compares consecutive frames and identifies changes based on a similarity threshold.

## Prerequisites

To run the code, you need to have the following dependencies installed:

- Python 3.x
- OpenCV
- imutils
- PIL

## Getting Started

1. Clone this repository to your local machine.
2. Ensure that the required dependencies are installed by running `pip install -r requirements.txt`.
3. Update the file paths in the code to specify the directory where the images are stored (`directory`) and the directory to store similar images (`similar_img_dir`).
4. Run the script by executing `main.py`.

## Configuration

The code provides a configuration class (`Config`) where you can customize various parameters:

- `gaussian_blur_radius_list`: A list of radius values for Gaussian blur. Modify it according to your requirements.
- `black_mask`: A tuple representing the black mask values in the image. Adjust it as needed.
- `min_contour_area`: The minimum contour area threshold. You can change this value based on your desired sensitivity.
- `similarity_tresh`: The similarity threshold to determine if an image change is significant. Adjust this value according to your needs.
- `new_shape`: The desired width and height of the resized images.

## Baic algorithm

Start
|
|-- Compare the similarity score with the pre-assigned threshold
|   |
|   |-- If similarity score > threshold
|   |   |
|   |   |-- Move the image in the next_image variable to a predetermined directory
|   |   |-- Assign the next image in the list to the next_image variable
|   |
|   |-- Else
|   |   |
|   |   |-- Assign the image in the next_image variable to the prev_image variable
|   |   |-- Assign the subsequent image in the list to the next_image variable
|
End
## Key takeaways from the provided code:

1) The code provided by Kopernikus is not the only method to compare similarities between two images. There are other methods available, such as calculating Mean Squared Error (MSE) or using advanced computer vision 
   techniques. It's important to explore different approaches and select the most appropriate method based on the specific requirements and characteristics of the dataset.

2) The similarity threshold plays a crucial role in determining whether images are considered similar or not. In the given code, a fixed threshold value is used. However, it may be more effective to pre-sort the data into 
   separate folders for each camera and process them individually with different threshold values. This approach allows for more flexibility and customization based on the characteristics of each camera's dataset.

3) Image resizing can significantly impact the processing speed. While resizing images to smaller dimensions can improve speed, it should be done carefully to avoid losing essential information. Balancing the trade-off 
   between speed and information loss is crucial. Experimenting with different image sizes and evaluating the impact on accuracy is recommended.

4) Overall, the provided code is a good starting point for the challenge. However, further in-depth evaluation of the datasets is necessary to develop an efficient and accurate method. Exploring additional techniques, 
   fine-tuning parameters, and testing with diverse datasets can lead to improved results.
## Output

The code compares consecutive frames and identifies changes based on the similarity threshold. If the similarity score is greater than the threshold, the image in the next_image variable is moved to the similar images directory, and the next image in the list is assigned to the next_image variable. Otherwise, the image in the next_image variable is assigned to the prev_image variable, and the subsequent image is assigned to the next_image variable.

Please note that this code assumes the image frames are in PNG format. Make sure your images are stored in the specified directory in PNG format.

Feel free to explore and modify the code to suit your specific needs. Happy coding!
