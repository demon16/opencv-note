import numpy as np
import cv2

# Read an image
"""
Mode:
    cv2.IMREAD_COLOR: 1
    cv2.IMREAD_GRAYSCALE: 0
    cv2.IMREAD_UNCHANGED: -1 (Loads image as such including alpha channel)
"""
img = cv2.imread('squirrel.jpeg', 0)

cv2.imshow('show_title', img)
cv2.waitKey(0)