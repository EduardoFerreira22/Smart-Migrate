from .ui_main import Ui_PrincipalWindow


ui_instance = None

def set_ui_instance(ui):
    global ui_instance
    ui_instance = ui


def get_ui_instance():
    return ui_instance