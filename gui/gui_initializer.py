from functools import partial
from gui.gui_functions import start_action, on_closing
from gui.ocr_location_column.ocr_location_column import ocr_location_column
from gui.ocr_compass_column.ocr_compass_column import ocr_compass_column
from gui.start_action_button.start_action_button import start_action_button
import utils.global_variables as gv

def gui_init():
    gv.root.resizable(False, False)
    #gv.root.protocol("WM_DELETE_WINDOW", partial(on_closing))
    ocr_location_column()
    ocr_compass_column()
    start_action_button()
