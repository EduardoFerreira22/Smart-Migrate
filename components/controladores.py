import ui.app_instance as app_instance


class FramesControler:
    def __init__(self):
        ui = app_instance.get_ui_instance()

        self.frames = [
            ui.frame_opcoes_busca_processamento,
            ui.frm_lateral_functions,
            ui.frm_combos_heads,

            ]

    def showFrames(self, status):
        for f in self.frames:
          f.setVisible(status)


class Tabelas:
    def __init__(self):
        ...

    def carregarDadosNaTabela(self, data, table, color):
        ...
              
class BomboBoxHeader:
    def __init__(self):
        self.ui = app_instance.get_ui_instance()
        self.combos = None

    def multipleCombos(self, data):
        ...
