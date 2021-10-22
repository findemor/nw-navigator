import utils.global_variables as gv
from functionality.image_recognition import text_recognition
from wrappers.logging_wrapper import info, debug
from utils.config import dict, random_timeout
from time import time



def action_loop():
    if (not gv.continue_action):
        info('Detenido.')
        return

    debug('Nueva iteración')
    # leer recurso
    resource = text_recognition(
        dict['ocr']['compass']['x'].get(),
        dict['ocr']['compass']['y'].get(),
        dict['ocr']['compass']['w'].get(),
        dict['ocr']['compass']['h'].get())
    # leer compass
    # leer location
    info('OCR: ' + resource)

    # enviar parametros a la libreria de busqueda en el mapa
    debug('Ha devuelto...')

    # representar salida
    info ('Salida: ')
    
    # programamos repeticion del bucle
    if (gv.continue_action):
        debug('Esperamos ' + str(dict['loop']['sec']) + 's')
        gv.root.after(dict['loop']['sec'] * 1000, action_loop)