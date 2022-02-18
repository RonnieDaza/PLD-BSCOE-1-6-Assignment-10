# Assignment 10
# Contact Tracing App
# Create a python program that will read a QR code using your webcam.
# You may use any online QR code generator to create QR code.
# All personal data are in QR code.
# You may decide which personal data to include.
# All data read from the QR code should be stored in a text file including the date and time it was read.

# 1. Import the modules.
from sre_constants import SUCCESS
from pyzbar.pyzbar import decode
import cv2
import numpy as np
import datetime

# 2. Set the video capture for the webcam.
webcamCap = cv2.VideoCapture(0)
# 3. Set the width of the webcam.
webcamCap.set(3, 640)
# 4. Set the height of the webcam.
webcamCap.set(4, 480)

# 5. Create a while loop. Set it to True. This loop will display and decode the data on the QR code everytime it is scanned.
while True:

    # 6. Read the data on the QR code.
    SUCCESS, theQrCode = webcamCap.read()
    # 7. Create a for loop for everytime the webcam scans the QR code.
    for theCode in decode(theQrCode):
        # 8. Print the type of data.
        print(theCode.type)