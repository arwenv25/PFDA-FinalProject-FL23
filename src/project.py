from PIL import Image
import os

def analyze_image(image_filename):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(script_dir, image_filename)
    
    try:
        image = Image.open(image_path)
        width, height = image.size
        ratio = width / height
        print("Image Resolution:", width, "x", height)
        print("Image Ratio:", ratio)
    except FileNotFoundError:
        print("Image file not found. Please make sure the file exists.")

# Prompt the user to enter the image filename
image_filename = input("Enter the image filename: ")

# Call the analyze_image function with the user-provided image filename
analyze_image(image_filename)

