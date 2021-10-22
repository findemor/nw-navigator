from gui.ocr_location_column.components.position import *
from gui.ocr_location_column.components.show_button import *
import utils.global_variables as gv
from tkinter import Label, LabelFrame

def ocr_location_column():
    ocr_location_column = LabelFrame(gv.root)
    ocr_location_column.grid(row=3, column=0, padx=(10, 10),pady=(10, 10))
    ocr_location_column_position_header = Label(ocr_location_column, text = "Location Position")
    ocr_location_column_position_header.grid(row=0, column=0)

    ocr_location_column_position(ocr_location_column)
    ocr_location_column_show(ocr_location_column)
