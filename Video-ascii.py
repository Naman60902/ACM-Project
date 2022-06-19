import cv2
import os
import numpy as np
from PIL import Image, ImageDraw, ImageOps, ImageFont

os.mkdir('./output')
vidcap = cv2.VideoCapture('vid.mp4')
success,image = vidcap.read()
fps = vidcap.get(cv2.CAP_PROP_FPS)

count = 0
while(vidcap.isOpened()):
    success,image = vidcap.read()
    if success==True:
      cv2.imwrite("frame"+str(count)+".jpg", image)     # save frame as JPEG file      
      print('Read a new frame: ', success)
    
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

      # Converting Color Image to Grayscale
      #image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

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
    
frame = cv2.imread(os.path.join('./output',"output0.jpg"))
frame_height, frame_width, layers = frame.shape
size_vid = (frame_width,frame_height)

video = cv2.VideoWriter("vid ascii.mp4", cv2.VideoWriter_fourcc(*'xvid'), fps, size_vid)

for i in range(0,count):
    video.write(cv2.imread(os.path.join('./output',"output"+str(i)+".jpg")))
vidcap.release()
video.release()
cv2.destroyAllWindows()
