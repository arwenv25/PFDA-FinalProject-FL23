from PIL import Image

class Color_Profile:
    def __init__(self):
        # initialize color profile attributes here
    def open_image_color(self):
        # implement code to open image
    def five_randomized_pixels():
        # implement code to iterate through each pixel of the image 
        # and randomly pick 5 to display
    def convert_rgb():
        # implement code to convert rgb to recognizable color name
    def color_psychology
        # implement code to convert color name to color psychology

class Image_Info:
    def __init__(self, image_path):
        self.image_path = image_path
        # Initialize image info attributes here

    def open_image_info(self):
        try:
            image = Image.open(self.image_path)
            return image
        except FileNotFoundError:
            print("Image file not found")
        # implement code to open image

    def calculate_ratio
        image = self.open_image_info()
        if image:
            width, height = image.size
            ratio = width/height
            return ratio
        # implement code to calculate the image's ratio

    def calculate_resolution
        image = self.open_image_info()
        if image:
            width, height = image.size
            resolution f"{width}x{height} pixels"
            return resolution
        # implement code to calculate the image's resolution

def two_option_menu():
    print("Welcome to the Image Insights Menue")
    print("Select 1 to analyze Color Profile")
    print("Select 2 to analyze Image Information")

    choice = input("Enter your choice here: ")

    if choice == "1":
        print("You chose analyze Color Profile!")
        # call respective code here from class above
    elif choice == "2":
        print("You chose analyze Image Information")
        # call respective code here from class above
    else:
        print("Invalid choice. Please choose either '1' or '2.'")



two_option_menu()

if __name__ == "__main__":
    main()

#Menu