def calibrate_camera(cal_images, nx, ny):
    # Numpy http://www.numpy.org/
    import numpy as np
    # print("Numpy version: {}".format(np.__version__))
    
    # Opencv http://docs.opencv.org/3.0-beta/modules/refman.html
    import cv2
    # print("Opencv version: {}".format(cv2.__version__))
    
    objpoints = []  # 3D points
    imgpoints = []  # 2D points
    
    objp = np.zeros((nx*ny,3), np.float32)
    objp[:,:2] = np.mgrid[0:nx,0:ny].T.reshape(-1, 2)
    
    # Finding corners
    for image in cal_images:
        ret, corners = cv2.findChessboardCorners(image, (nx, ny), None)
        if ret == True:
            objpoints.append(objp)
            imgpoints.append(corners)

    ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, cal_images[0].shape[::-1],None,None)
    
    return mtx, dist

def camera_setup(images):
    nx, ny = 9, 6
    cam_mtx, cam_dist = calibrate_camera(images, nx, ny)
    return cam_mtx, cam_dist
    
def undistort_image(image, camera_matrix, distortion_coefficients):
	# Opencv http://docs.opencv.org/3.0-beta/modules/refman.html
	import cv2
   # print("Opencv version: {}".format(cv2.__version__))
	result = cv2.undistort(image, camera_matrix, distortion_coefficients, None, camera_matrix)
	return result