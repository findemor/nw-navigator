from utils.config import dict
from numpy import array
import cv2
import pytesseract #https://nanonets.com/blog/ocr-with-tesseract/
from PIL import ImageGrab
import utils.global_variables as gv
from PIL import Image

def text_recognition(x, y, w, h):
    region=(x, y, x+w, y+h)
    img = ImageGrab.grab(bbox = region)
    

    # escala de grises, Gaussian blur, Otsu's threshold
    gray = cv2.cvtColor(array(img), cv2.COLOR_BGR2GRAY)
    #blur = cv2.GaussianBlur(gray, (3,3), 0)
    #thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    # Morph open para eliminar ruido e invertir la imagen
    #kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
    #opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)
    #invert = 255 - opening

    if (gv.events["on_new_compass_img"]):
        gv.events["on_new_compass_img"](Image.fromarray(gray), "")

    # Extraemos el texto
    data = pytesseract.image_to_string(gray, lang='eng', config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789EXPLORERView')
    #config='--psm 6')

    #cv2.imshow('thresh', thresh)


    return data