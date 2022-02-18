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