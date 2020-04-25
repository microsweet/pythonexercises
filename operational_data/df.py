from PIL import Image
import pytesseract
import os
import pdfplumber
import re
import openpyxl

Image.MAX_IMAGE_PIXELS = None
test = pytesseract.image_to_string(Image.open('/home/microsweet/slice_0_0.png'), lang='chi_sim')

with open('/home/microsweet/find.txt', 'w') as file_object:
    file_object.write(test)

