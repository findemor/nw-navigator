from utils.LastResults import LastResults
from os import path
import sys
from time import time
from tkinter import Tk
import pytesseract

def rootPath():
    try:
        return sys._MEIPASS
    except Exception:
        return path.abspath(".")

ROOT_DIR  = rootPath()
CONFIG_PATH = path.join(ROOT_DIR, 'resources\config.yml')
ICON_PATH = path.join(ROOT_DIR, 'resources\\icon.ico')
TESSERACT_PATH = path.join(ROOT_DIR, 'tesseract\\x64\\tesseract.exe')
continue_action = False
last_results = LastResults()
root = Tk()

events = {
    "on_new_compass_img": False
}


# https://stackoverflow.com/questions/50951955/pytesseract-tesseractnotfound-error-tesseract-is-not-installed-or-its-not-i
pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH
