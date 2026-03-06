# text_more_examples.py
# Description : Extended OCR examples — image-to-string,
#               word detection, digit-only OCR, and webcam/
#               screen-capture templates using Tesseract OCR
#               and OpenCV.
# Author      : TechyElle
# Activity    : Act2 - OCR Text Detection (Coding Standards)

import cv2
import pytesseract
import numpy as np
from PIL import ImageGrab
import time

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

input_image = cv2.imread('1.png')
input_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2RGB)

# Image to String
print(pytesseract.image_to_string(input_image))

# Detecting Words
# image_to_data columns: level, page_num, block_num, par_num, line_num, word_num, left, top, width, height, conf, text
word_data = pytesseract.image_to_data(input_image)

for line_index, line in enumerate(word_data.splitlines()):
    print(line)
    if line_index != 0:
        word_fields = line.split()

        # Only process complete rows that contain actual word entries
        if len(word_fields) == 12:
            word_x      = int(word_fields[6])
            word_y      = int(word_fields[7])
            word_width  = int(word_fields[8])
            word_height = int(word_fields[9])
            word_text   = word_fields[11]

            cv2.rectangle(input_image,
                          (word_x, word_y),
                          (word_x + word_width, word_y + word_height),
                          (50, 50, 255), 2)

            cv2.putText(input_image, word_text,
                        (word_x, word_y - 5),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (50, 50, 255), 2)

cv2.imshow('word_detection_result', input_image)
cv2.waitKey(0)
