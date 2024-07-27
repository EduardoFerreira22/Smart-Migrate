# app_instance.py
from gui.ui_ui_main import Ui_MainWindow

# Crie uma variável global para armazenar a instância
ui_instance = None

def set_ui_instance(ui):
    global ui_instance
    ui_instance = ui

def get_ui_instance():
    return ui_instance