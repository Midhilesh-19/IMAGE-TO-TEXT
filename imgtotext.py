# pytesseract is module to make image to text
import pytesseract
from PIL import Image
# here the location should depend on the path of where pytesseract cmd on ur particular pc after installing a module

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# opening the image
img = Image.open('py.jpg')  # in brackets we have to mention image name
# this coverts the data of paricular image
txt = pytesseract.image_to_string(img)
print(txt)
