import cv2
import os

# Read the video from specified path
cam = cv2.VideoCapture('cat.mp4')

try:
    if not os.path.exists('temp'):
        os.mkdir('temp')
except OSError:
    print("Error: Creating Directory")

# Frame
currentframe = 0

while (True):
    ret, frame = cam.read()

    if ret:
        name = './temp/' + str(currentframe) + '.jpg'
        print('Creating Frame', currentframe)
        cv2.imwrite(name, frame)
        currentframe += 1
    else:
        break

cam.release()
cv2.destroyAllWindows()