def convert_to_gray(images):
	# Opencv http://docs.opencv.org/3.0-beta/modules/refman.html
	import cv2
   # print("Opencv version: {}".format(cv2.__version__))	
   
	images_gray = []
	for image in images:	
		# Convert BGR to HSV
		gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
		images_gray.append(gray)
	
	return images_gray