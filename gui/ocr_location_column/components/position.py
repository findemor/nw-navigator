from tkinter import Label, LabelFrame, Entry, Scale, HORIZONTAL
from utils.config import dict

def ocr_location_column_position(ocr_location_column):
    ocr_location_column_position_container = LabelFrame(ocr_location_column)
    ocr_location_column_position_container.grid(row=1, column=0, padx=(10))
    ocr_location_column_position_x_container = Label(ocr_location_column_position_container, height=1)
    ocr_location_column_position_x_container.grid(row=0, column=0, padx=(5))
    ocr_location_column_position_x_text = Label(ocr_location_column_position_x_container, text="X:", anchor="s")
    ocr_location_column_position_x_text.grid(row=0, column=0, pady=(20, 0))
    ocr_location_column_position_x_scale = Scale(ocr_location_column_position_x_container, from_=0, to=1980, orient=HORIZONTAL, variable=dict['ocr']['location']['x'])
    ocr_location_column_position_x_scale.grid(row=0, column=1)
    ocr_location_column_position_x_entry = Entry(ocr_location_column_position_x_container, width=4, textvariable=dict['ocr']['location']['x'])
    ocr_location_column_position_x_entry.grid(row=0, column=2, pady=(20, 0))
    ocr_location_column_position_y_container = Label(ocr_location_column_position_container, height=1)
    ocr_location_column_position_y_container.grid(row=1, column=0)
    ocr_location_column_position_y_text = Label(ocr_location_column_position_y_container, text="Y:")
    ocr_location_column_position_y_text.grid(row=0, column=0, pady=(20, 0))
    ocr_location_column_position_y_scale = Scale(ocr_location_column_position_y_container, from_=0, to=1080, orient=HORIZONTAL, variable=dict['ocr']['location']['y'])
    ocr_location_column_position_y_scale.grid(row=0, column=1)
    ocr_location_column_position_y_entry = Entry(ocr_location_column_position_y_container, width=4, textvariable=dict['ocr']['location']['y'])
    ocr_location_column_position_y_entry.grid(row=0, column=2, pady=(20, 0))
