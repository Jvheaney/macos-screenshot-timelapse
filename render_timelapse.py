import os
import sys
import cv2

num_args = len(sys.argv)

output_name = "timelapse.mp4"
fps = 30

if  num_args == 3:
    output_name = sys.argv[1]
    fps = int(sys.argv[2])
elif num_args == 2:
    output_name = sys.argv[1]


height, width, layers = cv2.imread('./screenshots/0.jpg').shape
size = (width,height)

out = cv2.VideoWriter(output_name,cv2.VideoWriter_fourcc(*'MP4V'), fps, size)

screenshots = os.listdir("./screenshots/")
number_of_screenshots = len(screenshots)

iterator = 0
for i in range(number_of_screenshots):
    image=cv2.imread(f'./screenshots/{iterator}.jpg')
    iterator = iterator + 1
    out.write(image)
out.release()
