from PIL import Image

class Color_Profile:

    def __init__(self):
        self.image = Image

    def open_image_color(self, image):
        try:
            self.image = Image.open(self.image)
            self.image.show()
            return self.image
        except FileNotFoundError:
            print("Image file not  found.")

    def five_randomized_pixels(self, image):
        width, height = image.size
        pixels = []
        for _ in range(5):
            x = random.randint(0, width- 1)
            y = random.randint(0, height- 1)
            pixel = image.getpixel((x,y,))
            pixels.append(pixel)
        return pixels

    def convert_rgb(self, rgb):
        color_name = webcolors.rgb_to_name(rgb)
        return color_name

    def color_psychology(self, color_name):
        psychological_effect = get_psychologigal_effect(color_name)
        return psychological_effect


class Image_Info:

    def __init__(self):
        self.image = Image

    def open_image_color(self, image):
        try:
            self.image = Image.open(self.image)
            self.image.show()
            return self.image
        except FileNotFoundError:
            print("Image file not  found.")

    def calculate_ratio():
        image = self.open_image_info()
        if image:
            width, height = image.size
            ratio = width/height
            return ratio

    def calculate_resolution():
        image = self.open_image_info()
        if image:
            width, height = image.size
            resolution = f"{width}x{height} pixels"
            return resolution


def main():

    print("Welcome to the Image Insights Menu")
    print("Select 1 to analyze Color Profile")
    print("Select 2 to analyze Image Information")

    choice = input("Enter your choice here: ")

    if choice == "1":
        print("You chose analyze Color Profile!")
        # call respective code here from class above
        color_profile = Color_Profile()
        color_profile.open_image_color(image)
    

    elif choice == "2":
        print("You chose analyze Image Information")
        # call respective code here from class above
        image_info = Image_Info()
        image_info.image_info()

    else:
        print("Invalid choice. Please choose either '1' or '2.'")

if __name__ == "__main__":
    main()