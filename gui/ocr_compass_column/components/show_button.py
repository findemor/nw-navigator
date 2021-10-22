from tkinter import LabelFrame, Button
from utils.config import dict
from functools import partial
from gui.gui_functions import popup_rectangle_window

def ocr_compass_column_show_button(ocr_compass_column):
    ocr_compass_column_show_button = Button(ocr_compass_column, text = "Show")
    ocr_compass_column_show_button.configure(command = partial(popup_rectangle_window, ocr_compass_column_show_button, dict['ocr']['compass']['x'], dict['ocr']['compass']['y'], dict['ocr']['compass']['w'], dict['ocr']['compass']['h']))
    ocr_compass_column_show_button.grid(row=2, column=0, padx=(10, 10),pady=(10, 10))