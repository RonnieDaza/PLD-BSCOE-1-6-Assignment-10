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
        # 9. Decode the data. Use utf-8.
        print(theCode.data.decode("utf-8"))
        # 10. Add a bounding box. For here, we will use a polygon. Convert the polygon into an array. Use np.int32.
        thePoints = np.array([theCode.polygon], np.int32)
        # 11. Reshape the array and send it to the polygon line function.
        thePoints = thePoints.reshape((-1, 1, 2))
        # 12. Create the polygon line function. This will create now the bounding box. Set it to True to close. Set the color. Set the thickness.
        cv2.polylines(theQrCode, [thePoints], True, (0, 0, 255), 5)
        # 13. Find the values of the bounding box.
        thePoints2 = theCode.rect
        # 14. Put the text above the bounding box. Specify the image which is the QR code. Put the decoded data. Specify the coordinates using the values from thePoints2. Set the font. Set the font scale. Set the font color. Set the font thickness.
        cv2.putText(theQrCode, theCode.data.decode("utf-8"), (thePoints2[0], thePoints2[1]), cv2.FONT_HERSHEY_PLAIN, 0.9, (0, 0, 255), 2)

        # 15. Create the text file. Set the mode to "a" for the text file to have multiple entries of the data read of the QR code.
        generateTextFile = open("My QR Code Data Read.txt", "a")
        # 16. Write the data from the QR code.
        generateTextFile.write(theCode.data.decode("utf-8"))
        generateTextFile.write(" \n")
        generateTextFile.write(" \n")
        # 17. Add the date and time.
        generateTextFile.write(datetime.datetime.now().__str__() + "\n")
        generateTextFile.write(" \n")
        generateTextFile.write(" \n")
        # 18. Close the text file.
        generateTextFile.close
    
    # 19. Display a window for the webcam.
    cv2.imshow("Open My Webcam", theQrCode)
    