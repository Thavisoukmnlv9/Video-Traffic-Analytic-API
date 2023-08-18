import cv2
import pytesseract as pyt
from PIL import Image
import os

# Path of the image
img_path = 'apps/assets/img/123.jpg'
img = cv2.imread(img_path)
img_copy = img.copy()

gray_img = cv2.cvtColor(img_copy, cv2.COLOR_BGR2GRAY)
cv2.imwrite("gray.jpg", gray_img)
pyt.pytesseract.tesseract_cmd = r'D:\OCR\tesseract'
os.putenv('TESSDATA_PREFIX','D:\OCR\tessdata\lao.traineddata')
# Open the image using PIL

# Use Tesseract to extract text from the image
text = pyt.image_to_string(gray_img, lang='eng+lao')


# Save the text to a .txt file
with open('apps/assets/data/output.txt', mode='w', encoding='utf-8') as file:
    file.write(text)