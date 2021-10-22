from tkinter import Toplevel, Canvas, IntVar
from functools import partial
from utils.config import dict, save_data
from functionality.action_loop import action_loop
import utils.global_variables as gv

## Gestion de las ventanas que muestran el area seleccionada
def popup_rectangle_window(button, x, y, width, height):
    window = Toplevel()
    window.resizable(False, False)
    window.attributes('-fullscreen', True)
    window.wm_attributes('-transparentcolor', window['bg'])
    canvas = Canvas(window, width=10000, height=10000)
    canvas.create_rectangle(x.get(), y.get(), x.get()+width.get(), y.get()+height.get(), outline="green", width=5)
    canvas.pack()
    button.configure(command = partial(destroy_rectangle_window, window, button, x, y, width, height))

def destroy_rectangle_window(window, button, x, y, width, height):
    window.destroy()
    button.configure(command = partial(popup_rectangle_window, button, x,y,width,height))

## Botones

def start_action(button):
    changeActionState(button)
    action_loop()

def changeActionState(button):
    gv.continue_action = not gv.continue_action
    if(gv.continue_action):
        button.configure(text = "Detener")
        button.configure(command = partial(changeActionState, button))
    else:
        button.configure(text = "Iniciar")
        button.configure(command = partial(start_action, button))
    #dict['xxx']['enable']

## Eventos al cerrar la aplicacion

def on_closing():
    save_data()
    gv.root.destroy()