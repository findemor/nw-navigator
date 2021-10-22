from tkinter import LabelFrame, Button
from utils.config import dict
from functools import partial
from gui.gui_functions import popup_rectangle_window

def ocr_location_column_show(ocr_location_column):
    ocr_location_column_show_button = Button(ocr_location_column, text = "Show")
    ocr_location_column_show_button.configure(command = partial(popup_rectangle_window, ocr_location_column_show_button, dict['ocr']['location']['x'], dict['ocr']['location']['y'], dict['ocr']['location']['w'], dict['ocr']['location']['h']))
    ocr_location_column_show_button.grid(row=2, column=0, padx=(10, 10),pady=(10, 10))
