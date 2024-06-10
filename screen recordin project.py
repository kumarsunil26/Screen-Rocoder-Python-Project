import pyautogui
import cv2
import numpy as np
import time
import os

def generate_new_filename(base_filename):
    counter = 1
    filename, extension = os.path.splitext(base_filename)
    new_filename = base_filename
    while os.path.isfile(new_filename):
        new_filename = f"{filename}_{counter}{extension}"
        counter += 1
    return new_filename

resolution = (1920, 1080)
codec = cv2.VideoWriter_fourcc(*"XVID")
base_filename = "Recording.avi"
filename = generate_new_filename(base_filename)
fps = 10.0
out = cv2.VideoWriter(filename, codec, fps, resolution)
time.sleep(1.0/fps)
cv2.namedWindow("Live", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Live", 480, 270)
while True:
    img = pyautogui.screenshot()
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    out.write(frame)
    cv2.imshow('Live', frame)
    if cv2.waitKey(1) == ord('q'):
        break
out.release()
cv2.destroyAllWindows()