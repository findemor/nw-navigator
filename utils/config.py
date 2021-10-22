from yaml import safe_load, dump
from tkinter import IntVar
from utils.global_variables import CONFIG_PATH
import random


config = safe_load(open(CONFIG_PATH))

dict = {
    'loop':{
      'sec': config['loop']['sec']
    },
    'ocr':{
      'compass': {
        'w': IntVar(value=config['ocr']['compass']['w']),
        'h': IntVar(value=config['ocr']['compass']['h']),
        'x': IntVar(value=config['ocr']['compass']['x']),
        'y': IntVar(value=config['ocr']['compass']['y'])
      },
      'location': {
        'w': IntVar(value=config['ocr']['location']['w']),
        'h': IntVar(value=config['ocr']['location']['h']),
        'x': IntVar(value=config['ocr']['location']['x']),
        'y': IntVar(value=config['ocr']['location']['y'])
      }
    },
    'log_lvl': config['log_lvl']
  }

def save_data():
    d = {
    'loop':{
      'sec': dict['loop']['sec']
    },
    'ocr':{
      'compass': {
        'w': dict['ocr']['compass']['w'],
        'h': dict['ocr']['compass']['h'],
        'x': dict['ocr']['compass']['x'].get(),
        'y': dict['ocr']['compass']['y'].get()
      },
      'location': {
        'w': dict['ocr']['location']['w'],
        'h': dict['ocr']['location']['h'],
        'x': dict['ocr']['location']['x'].get(),
        'y': dict['ocr']['location']['y'].get()
      }
    },
    'log_lvl': dict['log_lvl']
    }
    with open(CONFIG_PATH, 'w') as yaml_file:
        dump(d, yaml_file, sort_keys=False)

def random_timeout(key):
    return round(random.uniform(key['min'], key['max']),2)
