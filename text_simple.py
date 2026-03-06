# text_simple.py
# Description : Detects and highlights individual characters
#               in an image using Tesseract OCR and OpenCV.
# Author      : TechyElle
# Activity    : Act2 - OCR Text Detection (Coding Standards)

import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

input_image = cv2.imread('1.png')
input_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2RGB)

image_height, image_width, _ = input_image.shape

# Detecting Characters
character_boxes = pytesseract.image_to_boxes(input_image)

for character_box in character_boxes.splitlines():
    box_data = character_box.split(' ')

    char_x      = int(box_data[1])
    char_y      = int(box_data[2])
    char_width  = int(box_data[3])
    char_height = int(box_data[4])
    char_label  = box_data[0]

    # Tesseract uses bottom-left origin, so y must be flipped using image_height
    cv2.rectangle(input_image,
                  (char_x, image_height - char_y),
                  (char_width, image_height - char_height),
                  (50, 50, 255), 2)

    cv2.putText(input_image, char_label,
                (char_x, image_height - char_y + 25),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (50, 50, 255), 2)

cv2.imshow('character_detection_result', input_image)
cv2.waitKey(0)
