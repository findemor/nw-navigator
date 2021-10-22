import utils.global_variables as gv
import utils.global_variables as gv
from tkinter import Button, LabelFrame
from functools import partial
from gui.gui_functions import start_action


def start_action_button():
    start_action_container = LabelFrame(gv.root)
    start_action_container.grid(row=4, column=0, padx=(10, 10),pady=(10, 10))
    start_action_button = Button(start_action_container, text = "Iniciar", font=18)
    start_action_button.configure(command = partial(start_action, start_action_button))
    start_action_button.grid(row=0, column=0)
