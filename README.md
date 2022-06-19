# Project Title : Asciify : ASCII Art Generator
ASCII(American Standard Code for Information Interchange) is a common encoding format used for representing strings and text data in computers.
In this project, I will use these ASCII for a different purpose.

# Project Description :
In this project, I will convert the images into an ASCII encoded strings art. It would look like the image. However, it will not just look like the image in terms of shape but also in colour.

Here’s an example :

<img src="https://user-images.githubusercontent.com/78922244/174473061-abbf0145-10ae-42e6-9cea-ab6a240874a3.jpg" width="300" height="400"> <img src="https://user-images.githubusercontent.com/78922244/174473105-4e1a4adc-9c1f-4a6d-b582-b127aae83667.jpg" width="300" height="400"> <img src="https://user-images.githubusercontent.com/78922244/174473082-35a6dcfa-5cc8-4e1a-9a82-6cc49103e370.jpg" width="300" height="400">

The first image is the original image.
The second image is an ascii encoded image with a white background.
The third image is an ascii encoded image with a black background.

In this project, I have added this concept of ascii art generation to not only on images but also to videos.

# Let's Start 
Go to:

[Ascii](https://github.com/Naman60902/ACM-Project#ascii)

[Coloured_ascii](https://github.com/Naman60902/ACM-Project#coloured_ascii)

[Video-ascii](https://github.com/Naman60902/ACM-Project#video-ascii)

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
```
```
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
```
```
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


def get_data(mode):
    font = ImageFont.truetype("DejaVuSansMono-Bold.ttf", size=20)
    scale = 2
    char_list = Character[mode]
    return char_list, font, scale


# Making Background Black or White
bg=input("Which background do you prefer(black or white)?")
```
As a coloured image has three planes viz. Red, Green and Blue, it would have three colour unit values.
```
if bg == "white":
    bg_code = (255,255,255)
elif bg == "black":
    bg_code = (0,0,0)

# Getting the character List, Font and Scaling characters for square Pixels
char_list, font, scale = get_data("complex")
num_chars = len(char_list)
num_cols = 300

# Reading Input Image
image = cv2.imread("Mt. Everest.jpg")

# Extracting height and width from Image
height, width, _ = image.shape

# Defining height and width of each cell==pixel
cell_w = width / num_cols
cell_h = scale * cell_w
num_rows = int(height / cell_h)

# Calculating Height and Width of the output Image
char_width, char_height = font.getsize("A")
out_width = char_width * num_cols
out_height = scale * char_height * num_rows

# Making a new Image using PIL
out_image = Image.new("RGB", (out_width, out_height), bg_code)
draw = ImageDraw.Draw(out_image)
```
As I did for grayscale image, in RGB also I performed the mapping process as shown below, however it is a bit different from which I did in Ascii.py:
```
#mapping characters for RGB
for i in range(num_rows) :
  for j in range(num_cols):
    partial_image=image[int(i*cell_h):min(int((i+1)*cell_h),height),int(j*cell_w):min(int((j+1)*cell_w),width),:]
    partial_avg_color=np.sum(np.sum(partial_image,axis=0),axis=0)/(cell_h*cell_w)
    partial_avg_color=tuple(partial_avg_color.astype(np.int32).tolist())
    c=char_list[min(int(np.mean(partial_image)*num_chars/255),num_chars-1)]
    draw.text((j*char_width,i*char_height),c,fill=partial_avg_color,font=font)
```
```
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
This is how I obtained the coloured ascii encoded image. I have procured the images with both black and white background which I have put in  [Coloured_ascii](https://github.com/Naman60902/ACM-Project/tree/main/Coloured_ascii) folder

# Video-ascii
For the python file, refer here : [Video-ascii.py](https://github.com/Naman60902/ACM-Project/blob/main/Video-ascii.py)
Install the opencv, pillow, numpy libraries using the following commands in the terminal.
```
$ pip install opencv-python
$ pip install pillow
$ pip install numpy
```
Import opencv,numpy,PIL,os as per the code below :
```
import cv2
import os
import numpy as np
from PIL import Image, ImageDraw, ImageOps, ImageFont
```
Following code will create a folder naming output
```
os.mkdir('./output')
```
```
vidcap = cv2.VideoCapture('vid.mp4') 
success,image = vidcap.read()
fps = vidcap.get(cv2.CAP_PROP_FPS) #for getting the framerate

count = 0
while(vidcap.isOpened()):  #running the loop unless video get finished
    success,image = vidcap.read()
    if success==True:
      cv2.imwrite("frame"+str(count)+".jpg", image)     # save frame as JPG file      
      print('Read a new frame: ', success)
      # Characters used for Mapping to Pixels
      Character = {
          "standard": "@%#*+=-:. ",
          "complex": "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
      }

# I am applying the same Coloured_ascii code on each frame of the video and will finally combine them
      def get_data(mode):
          font = ImageFont.truetype("DejaVuSansMono-Bold.ttf", size=20)
          scale = 2
          char_list = Character[mode]
          return char_list, font, scale


      # Making Background Black or White
      bg = "black"
      # bg = "white"
      if bg == "white":
          bg_code = (255,255,255)
      elif bg == "black":
          bg_code = (0,0,0)

      # Getting the character List, Font and Scaling characters for square Pixels
      char_list, font, scale = get_data("complex")
      num_chars = len(char_list)
      num_cols = 300

      # Reading Input Image
      image = cv2.imread("frame"+str(count)+".jpg")

      # Extracting height and width from Image
      height, width, _ = image.shape

      # Defining height and width of each cell==pixel
      cell_w = width / num_cols
      cell_h = scale * cell_w
      num_rows = int(height / cell_h)

      # Calculating Height and Width of the output Image
      char_width, char_height = font.getsize("A")
      out_width = char_width * num_cols
      out_height = scale * char_height * num_rows

      # Making a new Image using PIL
      out_image = Image.new("RGB", (out_width, out_height), bg_code)
      draw = ImageDraw.Draw(out_image)

      #mapping characters for RGB
      for i in range(num_rows) :
        for j in range(num_cols):
          partial_image=image[int(i*cell_h):min(int((i+1)*cell_h),height),int(j*cell_w):min(int((j+1)*cell_w),width),:]
          partial_avg_color=np.sum(np.sum(partial_image,axis=0),axis=0)/(cell_h*cell_w)
          partial_avg_color=tuple(partial_avg_color.astype(np.int32).tolist())
          c=char_list[min(int(np.mean(partial_image)*num_chars/255),num_chars-1)]
          draw.text((j*char_width,i*char_height),c,fill=partial_avg_color,font=font)

      # Inverting Image and removing excess borders
      if bg == "white":
          cropped_image = ImageOps.invert(out_image).getbbox()
      elif bg == "black":
          cropped_image = out_image.getbbox()

      # Saving the new Image
      out_image = out_image.crop(cropped_image)  
      
      out_image.save(os.path.join('./output',"output"+str(count)+".jpg"))
      count+=1
    else :
        break
```
Here, I will combine all the coloured ascii encoded images together to form a video.
```
frame = cv2.imread(os.path.join('./output',"output0.jpg"))
frame_height, frame_width, layers = frame.shape
size_vid = (frame_width,frame_height)

video = cv2.VideoWriter("vid ascii.mp4", cv2.VideoWriter_fourcc(*'xvid'), fps, size_vid)

for i in range(0,count):
    video.write(cv2.imread(os.path.join('./output',"output"+str(i)+".jpg")))
vidcap.release()
video.release()
cv2.destroyAllWindows()
```
This is how I obtained the Coloured ascii encoded video. I have put the frames, output folder, input video and output video, all in the [Video-ascii](https://github.com/Naman60902/ACM-Project/tree/main/Video-ascii) folder.
# Conclusion
By this project, I got used to PIL, opencv, OS, numpy. Also, it was very interesting to play with images and get unique outputs.I did this project on google collab. One thing with which I struggled in this project was the speed with which the code executed. It was slow. And if I had to experiment with large no. of frames it took large amount of time which made the process quite cumbersome. Nonetheless, this was a great project in the sense as it tested my understanding of python extensively and gave me the opportunity to understand the underlying processes of python which I had not known if I had not done this project.
# References 
https://stackoverflow.com ( It was a lifesaver for most of the times )
