from PIL import Image
import os
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import webcolors

def most_dominant_colors(img):
    resized_img = img.resize((100, 100))
    rgb_img = resized_img.convert("RGB")
    pixel_colors = np.array(rgb_img).reshape(-1, 3)
    kmeans = KMeans(n_clusters=5)
    kmeans.fit(pixel_colors)
    dominant_colors = kmeans.cluster_centers_.astype(int)
    return dominant_colors

def convert_rgb(colors):
    color_names = []
    for color in colors:
        rgb = color.astype(int)
        closest_color = webcolors.rgb_to_name(rgb)
        color_names.append(closest_color)
    return color_names

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

def get_image_resolution(image):
    width, height = image.size
    return width, height

def get_image_ratio(image):
    width, height = image.size
    ratio = width / height
    return ratio

def menu():
    print("Menu:")
    print("1. Color Profile")
    print("2. Image Info")
    choice = input("Enter your choice: ")

    if choice == "1":
        image_filename = input("Enter the image filename: ")
        analyze_image(image_filename)
        rgb_values = analyze_image(image_path)
        print("RGB Values:", rgb_values)
    elif choice == "2":
        image_filename = input("Enter the image filename: ")
        image = Image.open(image_filename)
        resolution = get_image_resolution(image)
        ratio = get_image_ratio(image)
        print("Image resolution:", resolution)
    elif choice != 1 or 2:
        print("Invalid Choice. Please choose either 1 or 2")

        
menu()