# import the necessary packages
import numpy as np
import argparse
import cv2
import easygui

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
# Opening an image using a File Open dialog:
f = easygui.fileopenbox()

# load the image
image = cv2.imread(f)

# define the list of boundaries
boundaries = [ #BGR
	([198, 111, 255], [128, 4, 234]), #Magenta 
	([86, 31, 4], [220, 88, 50]),
	([25, 146, 190], [62, 174, 250]),
	([103, 86, 65], [145, 133, 128]),
	([103, 86, 65], [145, 133, 128]),
	([103, 86, 65], [145, 133, 128])	
]

# loop over the boundaries
for (lower, upper) in boundaries:
	# create NumPy arrays from the boundaries
	lower = np.array(lower, dtype = "uint8")
	upper = np.array(upper, dtype = "uint8")

	# find the colors within the specified boundaries and apply
	# the mask
	mask = cv2.inRange(image, lower, upper)
	output = cv2.bitwise_and(image, image, mask = mask)

	# show the images
	cv2.imshow("images", np.hstack([image, output]))
	cv2.waitKey(0)