# Project Title : Asciify : ASCII Art Generator
ASCII(American Standard Code for Information Interchange) is a common encoding format used for representing strings and text data in computers.
In this project, I will use these ASCII for a different purpose.

# Project Description :
In this project, I will convert the images into an ASCII encoded strings art. It would look like the image. However, it will not just look like the image in terms of shape but also in colour.

Here’s an example :

<img src="https://user-images.githubusercontent.com/78922244/174453068-630a3934-5289-42d8-82af-5c5ff169487d.jpg" width="300" height="400"> <img src="https://user-images.githubusercontent.com/78922244/174453249-d71b534a-802e-4ca0-8e46-428613153331.jpg" width="300" height="400"> <img src="https://user-images.githubusercontent.com/78922244/174453076-58145cb8-6ffb-47e1-a7da-1d4648e5624e.jpg" width="300" height="400">

The first image is the original image.
The second image is an ascii encoded image with a white background.
The third image is an ascii encoded image with a black background.

In this project, I have added this concept of ascii art generation to not only on images but also to videos.

# Let's Start 
Go to:

[Ascii](https://github.com/Naman60902/ACM-Project/edit/main/README.md#asciipy)

[Coloured_ascii](https://github.com/Naman60902/ACM-Project/edit/main/README.md#coloured_asciipy)

[Video-ascii](https://github.com/Naman60902/ACM-Project/edit/main/README.md#video-asciipy)

# Ascii
For the python file, refer here : [Ascii.py](https://github.com/Naman60902/ACM-Project/blob/main/Ascii.py)

Install the opencv, pillow, numpy libraries using the following commands in the terminal.
```
$ pip install opencv-python
$ pip install pillow
$ pip install numpy
```
Import opencv,numpy,PIL as per the code below :
```
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageOps, ImageFont
```
Below I have written the code for characters' mapping to pixels. The list contains ASCII characters based in ascending order of their luminosity.
‘$’ and ‘@’ has the lowest brightness, hence mapped to darker pixel values.‘ ’ has highest brightness, hence it will be mapped to lighter pixel values.
```
# Characters used for Mapping to Pixels
Character = {
    "standard": "@%#*+=-:. ",
    "complex": "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
}
```
```
def get_data(mode):
    font = ImageFont.truetype("DejaVuSansMono-Bold.ttf", size=20)
    scale = 2
    char_list = Character[mode]
    return char_list, font, scale


# Making Background Black or White
bg=input("Which background do you prefer(black or white)?")

if bg == "white":
    bg_code = 255
elif bg == "black":
    bg_code = 0

# Getting the character List, Font and Scaling characters for square Pixels
char_list, font, scale = get_data("complex")
num_chars = len(char_list)
num_cols = 300

# Reading Input Image
image = cv2.imread("zebra.jpg")

# Converting Color Image to Grayscale
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Extracting height and width from Image
height, width = image.shape

# Defining height and width of each cell==pixel
cell_w = width / num_cols
cell_h = scale * cell_w
num_rows = int(height / cell_h)

# Calculating Height and Width of the output Image
char_width, char_height = font.getsize("A")
out_width = char_width * num_cols
out_height = scale * char_height * num_rows

# Making a new Image using PIL
out_image = Image.new("L", (out_width, out_height), bg_code)
draw = ImageDraw.Draw(out_image)
```
Below, I have cropped each cell of the image, took mean of colour units present in each cell, calculated their fraction dividing by 255, then multiplying with num_chars so as to find the index of character required for that cell. Iterations takes place through each row and in each row it moves through each column. And finally it drawn as per the coordinate onto the Image I had created previously using PIL.
```
# Mapping the Characters
for i in range(num_rows):
    min_h = min(int((i + 1) * cell_h), height)
    row_pix = int(i * cell_h)
    line = "".join([char_list[
        min(int(
            np.mean(image[row_pix:min_h, int(j*cell_w)
                    :min(int((j + 1) * cell_w), width)]) / 255 * num_chars
        ), num_chars - 1)]
        for j in range(num_cols)]) + "\n"

    # Draw string at a given position (x,y)
    draw.text((0, i * char_height), line, fill=255-bg_code, font=font)


# Inverting Image and removing excess borders
if bg == "white":
    cropped_image = ImageOps.invert(out_image).getbbox()
    # Saving the new Image
    out_image = out_image.crop(cropped_image)
    out_image.save("output_w.jpg")
elif bg == "black":
    cropped_image = out_image.getbbox()
    # Saving the new Image
    out_image = out_image.crop(cropped_image)
    out_image.save("output_b.jpg")
```
This is how I obtained the uncoloured ascii encoded image. I have procured the images with both black and white background which I have put in  [Ascii](https://github.com/Naman60902/ACM-Project/tree/main/Ascii) folder
# Coloured_ascii
For the python file, refer here : [Coloured_ascii.py](https://github.com/Naman60902/ACM-Project/blob/main/Coloured_ascii.py)

# Video-ascii
For the python file, refer here : [Video-ascii.py](https://github.com/Naman60902/ACM-Project/blob/main/Video-ascii.py)



