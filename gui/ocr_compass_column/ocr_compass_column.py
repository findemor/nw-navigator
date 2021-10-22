from gui.ocr_compass_column.components.position import *
from gui.ocr_compass_column.components.show_button import *
import utils.global_variables as gv
from tkinter import Label, LabelFrame
from PIL import ImageTk, Image #pillow

def ocr_compass_show_img(img, e):
    ph = ImageTk.PhotoImage(img)
    preview = Label(gv.root, image=ph)
    preview.grid(row=4, column=0, padx=(10, 10),pady=(10, 10))
    preview.image = ph

def ocr_compass_column():
    ocr_compass_column_header = Label(gv.root, text = "OCR")
    ocr_compass_column_header.grid(row=0, column=0, padx=(10, 10),pady=(10, 10))
    ocr_compass_column = LabelFrame(gv.root)
    ocr_compass_column.grid(row=1, column=0, padx=(10, 10),pady=(10, 10))
       
    #gv.events["on_new_compass_img"] = ocr_compass_show_img

    ocr_compass_column_position(ocr_compass_column)
    ocr_compass_column_show_button(ocr_compass_column)