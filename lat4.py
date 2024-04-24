import cv2
import numpy as np
import matplotlib.pyplot as plt

# fungsi untuk menampilkan gambar menggunakan matplotlib
def show_image(image,title='image',cmap_type='gray'):
    plt.figure()
    plt.imshow(image,cmap=cmap_type)
    plt.title(title)
    plt.axis('off')
    plt.show()

# Fungsi untuk menghitung distribusi probabilitas(normalisasi histogram)
def calculate_normalized_histogram(image):
    # hitung histogram
    histogram,_=np.histogram(image, bins=256, range=(0,256))

    # hitung jumlah total pixel
    total_pixels=image.size

    #Hitung distribusi probabilitas dengan rumus ni/N
    normalized_histogram = histogram / total_pixels

    return normalized_histogram
# baca citra dari file menggunakan opencv
image_path = 'kucing.jpeg'
image = cv2.imread(image_path,cv2.IMREAD_GRAYSCALE)

# tampilkan citra asli
show_image(image,title='Citra Asli')

# hitung distribusi probabilitas
normalized_histogram = calculate_normalized_histogram(image)

# plot histogram citra asli dengan distribusi probabilitas
plt.figure()
plt.bar(range(256),normalized_histogram,color='black')
plt.title('Normalisasi Histogram Citra')
plt.xlabel('Intensitas Pixel')
plt.ylabel('Distribusi Probabilitas')
plt.show()