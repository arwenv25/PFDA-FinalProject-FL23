from PIL import Image
import os
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def most_dominant_colors(img):
    resized_img = img.resize((100, 100))
    rgb_img = resized_img.convert("RGB")
    pixel_colors = np.array(rgb_img).reshape(-1, 3)
    kmeans = KMeans(n_clusters=5)
    kmeans.fit(pixel_colors)
    dominant_colors = kmeans.cluster_centers_.astype(int)
    return dominant_colors

def create_color_samples(colors):
    fig, axs = plt.subplots(1, 5, figsize=(12, 2))
    for i, color in enumerate(colors):
        axs[i].imshow([[color]], aspect='auto')
        axs[i].axis('off')
    plt.show()

def analyze_image(image_filename):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(script_dir, image_filename)
    try:
        image = Image.open(image_path)
        dominant_colors = most_dominant_colors(image)
        create_color_samples(dominant_colors)
    except FileNotFoundError:
        print("Image file not found. Please make sure the file exists.")

image_filename = input("Enter the image filename: ")
analyze_image(image_filename)

# Call the analyze_image function with the image filename
analyze_image(image_filename)

# Colors and samples