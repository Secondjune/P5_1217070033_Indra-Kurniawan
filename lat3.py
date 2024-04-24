import cv2
import numpy as np
import matplotlib.pyplot as plt

# read image
img = cv2.imread(r'kucing.jpeg')

# convert image grayscale
gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# resize gambar
gray = cv2.resize(gray,(0,0),fx=0.5,fy=0.5)
hist= cv2.calcHist([gray],[0],None,[256],[0,256])

plt.figure(figsize=(12,12))
plt.subplot(121)
plt.imshow(gray, cmap='gray')
plt.title('Original Image')

plt.subplot(122)
plt.plot(hist)
plt.xlabel('Pixel intensity')
plt.ylabel('Number of pixels')
plt.title('Grayscale Histogram')

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()