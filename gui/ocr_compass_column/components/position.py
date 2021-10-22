from tkinter import Label, LabelFrame, Scale, Entry, HORIZONTAL
from utils.config import dict

def ocr_compass_column_position(ocr_compass_column):
    ocr_compass_column_position_header = Label(ocr_compass_column, text = "Compass Position")
    ocr_compass_column_position_header.grid(row=0, column=0)
    ocr_compass_column_position_container = LabelFrame(ocr_compass_column)
    ocr_compass_column_position_container.grid(row=1, column=0, padx=(10))

    ocr_compass_selection_column_position_x_container = Label(ocr_compass_column_position_container, height=1)
    ocr_compass_selection_column_position_x_container.grid(row=0, column=0, padx=(20,19))
    ocr_compass_selection_column_position_x_text = Label(ocr_compass_selection_column_position_x_container, text="X:")
    ocr_compass_selection_column_position_x_text.grid(row=0, column=0, pady=(20, 0))
    ocr_compass_selection_column_position_x_scale = Scale(ocr_compass_selection_column_position_x_container, from_=0, to=1980, orient=HORIZONTAL, variable=dict['ocr']['compass']['x'])
    ocr_compass_selection_column_position_x_scale.grid(row=0, column=1)
    ocr_compass_selection_column_position_x_entry = Entry(ocr_compass_selection_column_position_x_container, width=4, textvariable=dict['ocr']['compass']['x'])
    ocr_compass_selection_column_position_x_entry.grid(row=0, column=2, pady=(20, 0))
    ocr_compass_selection_column_position_y_container = Label(ocr_compass_column_position_container, height=1)
    ocr_compass_selection_column_position_y_container.grid(row=1, column=0)
    ocr_compass_selection_column_position_y_text = Label(ocr_compass_selection_column_position_y_container, text="Y:")
    ocr_compass_selection_column_position_y_text.grid(row=0, column=0, pady=(20, 0))
    ocr_compass_selection_column_position_y_scale = Scale(ocr_compass_selection_column_position_y_container, from_=0, to=1080, orient=HORIZONTAL, variable=dict['ocr']['compass']['y'])
    ocr_compass_selection_column_position_y_scale.grid(row=0, column=1)
    ocr_compass_selection_column_position_y_entry = Entry(ocr_compass_selection_column_position_y_container, width=4, textvariable=dict['ocr']['compass']['y'])
    ocr_compass_selection_column_position_y_entry.grid(row=0, column=2, pady=(20, 0))
