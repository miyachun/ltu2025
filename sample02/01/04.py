from PIL import Image
import pytesseract
import numpy as np
#pytesseract.pytesseract.tesseract_cmd = r"D:\Chung_Hua_University\2024\Tesseract-OCR\tesseract.exe"
filename = '2_python-ocr.jpg'
img1 = np.array(Image.open(filename))
text = pytesseract.image_to_string(img1)
print(text)