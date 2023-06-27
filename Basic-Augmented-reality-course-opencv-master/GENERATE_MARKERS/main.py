import cv2 as cv
from cv2 import aruco

marker_dict = aruco.Dictionary(aruco.DICT_6X6_50,100)

MARKER_SIZE = 100  # pixels

for id in range(20):

    marker_image = aruco.drawMarker(marker_dict, id, MARKER_SIZE)
    # cv.imshow("img", marker_image)
    cv.imwrite(f"markers/markder_{id}.png", marker_image)
    # cv.waitKey(0)
    # break
