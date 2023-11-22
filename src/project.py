from PIL import Image
import os
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import webcolors
from scipy.spatial import KDTree

def convert_rgb_to_names(rgb_tuple):
    css3_db = webcolors.CSS3_NAMES_TO_HEX
    names = []
    rgb_values = []
    for color_name, color_hex in css3_db.items():
        names.append(color_name)
        rgb_values.append(webcolors.hex_to_rgb(color_hex))
    
    kdt_db = KDTree(rgb_values)
    distance, index = kdt_db.query(rgb_tuple)
    return names[index]

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
        try:
            closest_color = convert_rgb_to_names(rgb)
            color_names.append(closest_color)
            print("RGB values:", rgb, "-", "Color Name: ", closest_color)
        except ValueError:
            print("No matching color in CSS3 for RGB values:", rgb)
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
        convert_rgb(dominant_colors)
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

def main():
    print("Welcome to the Image Insights Menu")
    print("Select 1 to analyze Color Profile")
    print("Select 2 to analyze Image Information")

    choice = input("Enter your choice: ")

    if choice == "1":
        image_filename = input("Enter the image filename: ")
        analyze_image(image_filename)
        
    elif choice == "2":
        image_filename = input("Enter the image filename: ")
        image = Image.open(image_filename)
        resolution = get_image_resolution(image)
        ratio = get_image_ratio(image)
        print("Image resolution:", resolution)
        print("Image ratio:", ratio)
    elif choice != 1 or 2:
        print("Invalid Choice. Please choose either 1 or 2")


if __name__ == "__main__":
    main()