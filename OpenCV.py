import cv2
import sys
import numpy as np
import subprocess
import math

# adb shell settings put system show_touches 1

#- Config
marginFactor = 0.9

phoneWidth = 1440
phoneHeight = 2880

displayHeight = 1080

#|---------

#- Resize calculations
displayHeight = math.floor(displayHeight*marginFactor)
displayWidth = math.floor(phoneWidth * (displayHeight / phoneHeight))
#|----------

def onClick(event, x, y, flags, param):
    
    #|- Resize touch events to display resolution
    x = math.floor((x/displayWidth) * phoneWidth)
    y = math.floor((y/displayHeight) * phoneHeight)
    #|------------

    if (event == cv2.EVENT_LBUTTONDOWN):
        print(f"{x}, {y}")
        print(subprocess.run(["adb", "exec-out", "input", "tap", str(x), str(y)]))



print(f"Phone resolution: {phoneWidth}x{phoneHeight}")
print(f"Converting to display resolution: {displayWidth}x{displayHeight}")

cap = cv2.VideoCapture("/dev/stdin")

if (cap.isOpened()==False):
    print("Failed to open stream")

cv2.namedWindow("main", cv2.WINDOW_AUTOSIZE)
cv2.setMouseCallback("main", onClick)

while cap.isOpened():

    ret, frame = cap.read()
    if ret == True:
        frame = cv2.resize(frame, (displayWidth, displayHeight))

        cv2.imshow('main', frame)
        
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    
    else:
        break

cap.release()
cv2.destroyAllWindows()
exit()