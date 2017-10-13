# **Advanced Lane Finding Project**

The goals/steps of this project are the following:

* Compute the camera calibration matrix and distortion coefficients given a set of chessboard images.
* Apply a distortion correction to raw images.
* Use color transforms, gradients, etc., to create a thresholded binary image.
* Apply a perspective transform to rectify binary image ("birds-eye view").
* Detect lane pixels and fit to find the lane boundary.
* Determine the curvature of the lane and vehicle position with respect to center.
* Warp the detected lane boundaries back onto the original image.
* Output visual display of the lane boundaries and numerical estimation of lane curvature and vehicle position.

[//]: # (Image References)

[image1]: ./results/result_undist_image_1.png "Undistorted 1"
[image2]: ./results/result_undist_image_2.png "Undistorted 2"
[image3]: ./results/result_undist_image_3.png "Undistorted 3"
[image4]: ./results/result_color_and_gradient_1.png "Color and Gradient 1"
[image5]: ./results/result_color_and_gradient_2.png "Color and Gradient 2"
[image6]: ./results/result_perspective_transform_1.png "Perspective Transform 1"
[image7]: ./results/result_perspective_transform_2.png "Perspective Transform 2"
[image8]: ./results/result_final_image_1.png "Final Image 1"
[image9]: ./results/result_final_image_2.png "Final Image 2"
[image10]: ./results/result_final_image_3.png "Final Image 3"
[image11]: ./results/result_final_image_4.png "Final Image 4"




[image6]: ./examples/example_output.jpg "Output"
[video1]: ./project_video.mp4 "Video"

## [Rubric](https://review.udacity.com/#!/rubrics/571/view) Points

### Here I will consider the rubric points individually and describe how I addressed each point in my implementation.  

---

### Camera Calibration

#### 1. Briefly state how you computed the camera matrix and distortion coefficients. Provide an example of a distortion corrected calibration image.

The code for this step is contained in the first code cell of the IPython notebook located in "./CarND-Advanced-Lane-Lines.ipynb#calibrate_camera". The details can be founded in module "./utils/camera_calibration.py".

I start by preparing "object points", which will be the (x, y, z) coordinates of the chessboard corners in the world. Here I am assuming the chessboard is fixed on the (x, y) plane at z=0, such that the object points are the same for each calibration image.  Thus, `objp` is just a replicated array of coordinates, and `objpoints` will be appended with a copy of it every time I successfully detect all chessboard corners in a test image.  `imgpoints` will be appended with the (x, y) pixel position of each of the corners in the image plane with each successful chessboard detection.  

I then used the output `objpoints` and `imgpoints` to compute the camera calibration and distortion coefficients using the `cv2.calibrateCamera()` function.  I applied this distortion correction to the test image using the `cv2.undistort()` function and obtained this result: 

![Undistorted 1][image1]
![Undistorted 3][image3]

### Pipeline (single images)

#### 1. Provide an example of a distortion-corrected image.

To demonstrate this step, I will describe how I apply the distortion correction to one of the test images like this one:

![Undistorted 2][image2]

#### 2. Describe how (and identify where in your code) you used color transforms, gradients or other methods to create a thresholded binary image.  Provide an example of a binary image result.

I used a combination of color and gradient thresholds to generate a binary image (thresholding steps at lines "./CarND-Advanced-Lane-Lines.ipynb#color_and_gradient").  Here's an example of my output for this step.

![Color and Gradient 1][image4]
![Color and Gradient 2][image5]

#### 3. Describe how (and identify where in your code) you performed a perspective transform and provide an example of a transformed image.

The code for my perspective transform includes a function called `warper()`, which appears in cell "./CarND-Advanced-Lane-Lines.ipynb#perspective_transform".  The `perspective_transform()` function takes as inputs an image (`img`).  I chose the hardcode the source and destination points in the following manner:

```python
src = np.float32(
    [[(img_size[0] / 2) - 55, img_size[1] / 2 + 100],
    [((img_size[0] / 6) - 10), img_size[1]],
    [(img_size[0] * 5 / 6) + 60, img_size[1]],
    [(img_size[0] / 2 + 55), img_size[1] / 2 + 100]])
dst = np.float32(
    [[(img_size[0] / 4), 0],
    [(img_size[0] / 4), img_size[1]],
    [(img_size[0] * 3 / 4), img_size[1]],
    [(img_size[0] * 3 / 4), 0]])
```

This resulted in the following source and destination points:

| Source        | Destination   | 
|:-------------:|:-------------:| 
| 585, 460      | 320, 0        | 
| 203, 720      | 320, 720      |
| 1127, 720     | 960, 720      |
| 695, 460      | 960, 0        |

![Perspective Transform 1][image6]
![Perspective Transform 2][image7]

#### 4. Describe how (and identify where in your code) you identified lane-line pixels and fit their positions with a polynomial?

Then, based on the histogram I used a sliding window to fit a polynomial like this:

![Final Image 1][image8]
![Final Image 1][image9]
![Final Image 1][image10]
![Final Image 1][image11]

#### 5. Describe how (and identify where in your code) you calculated the radius of curvature of the lane and the position of the vehicle with respect to center.

I did this in cell "./CarND-Advanced-Lane-Lines.ipynb#perspective_transform" in my python notebook.

#### 6. Provide an example image of your result plotted back down onto the road such that the lane area is identified clearly.

I implemented this step in cell "./CarND-Advanced-Lane-Lines.ipynb#plot_back" in my python notebook in the function `sliding_window_polynomial()`.  Here is an example of my result on a test image:

![Final Image 1][image11]

---

### Pipeline (video)

#### 1. Provide a link to your final video output.  Your pipeline should perform reasonably well on the entire project video (wobbly lines are ok but no catastrophic failures that would cause the car to drive off the road!).

Here's a [link to my video result](https://github.com/patriciapampanelli/CarND-Advanced-Lane-Lines/blob/master/project_video_output.mp4)
---

### Discussion

#### 1. Briefly discuss any problems / issues you faced in your implementation of this project.  Where will your pipeline likely fail?  What could you do to make it more robust?

Manually tuning parameters for Computer Vision pipeline is extremely tedious. It made me realize the significance of Machine Learning and Deep learning based approach used in the previous project.

I also believe that a more robust method than using histogram can significantly improve this results, especially for the challenge videos.
