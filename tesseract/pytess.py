from PIL import Image
import pytesseract
import argparse
import cv2
import os
 
# load the example image and convert it to grayscale
image = cv2.imread("D:\\horolro\\tesseract\\test.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 
# write the grayscale image to disk as a temporary file so we can
# apply OCR to it
filename = "{}.png".format(os.getpid())
cv2.imwrite(filename, gray)

pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

text = pytesseract.image_to_string(Image.open(filename), lang='kor')
os.remove(filename)

print(text)
