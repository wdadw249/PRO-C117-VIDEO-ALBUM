import os
import cv2

path = "Images"

images = []

for i in os.listdir(path):
    name, ext = os.path.splitext(i)
    file_name = path + "/" + i
    images.append(file_name)

frame = cv2.imread(images[0])
height, width, channel = frame.shape
size = (width,height)

output = cv2.VideoWriter("Friendship.mp4", cv2.VideoWriter_fourcc(*'DIVX'), 5, size)

for i in range(len(images)-1,-1,-1):
    frame = cv2.imread(images[i])
    output.write(frame)
    cv2.imshow("SunSet",frame)
    cv2.waitKey(1000)

output.release()
print("Done")