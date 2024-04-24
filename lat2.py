import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('kucing.jpeg')
ax = plt.hist(img.ravel(), bins=256)
plt.show()