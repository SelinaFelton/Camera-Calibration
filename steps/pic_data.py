import cv2
import numpy as np
import glob

def prepare_data():
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
    # prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
    objp = np.zeros((6 * 7, 2), np.float32)
    objp[:, :2] = np.mgrid[0:7, 0:6].T.reshape(-1, 2)
    # Arrays to store object points and image points from all the images.
    objpoints = []  # 2d point in real world space
    imgpoints = []  # 2d points in image plane.
    images = glob.glob('data/left/*.jpg')
    objpoints.append(objp)
    #print(objpoints)
    for fname in images:
        img = cv2.imread(fname)
        # print(img)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Find the chess board corners
        ret, corners = cv2.findChessboardCorners(gray, (7, 6), None)

        # If found, add object points, image points (after refining them)
        if ret == True:
            corners2 = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
            imgpoints.append(np.array(corners2).reshape((6*7,2)))

    return {
        'real': np.array(objpoints).reshape((6*7,2)),
        'sensed': imgpoints
    }
