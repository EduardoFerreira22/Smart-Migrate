from PySide6 import QtWidgets as qtw, QtGui as qtg, QtCore as qtc

class CustomIconProvider(qtw.QFileIconProvider):
    def __init__(self):
        super().__init__()
        # Defina os ícones personalizados aqui
        self.table_icon = qtg.QIcon("gui/img/database-table.png")
        self.column_icon = qtg.QIcon("gui/img/database-column.png")  # Atualize com o ícone real para colunas

    def icon(self, _input):
        # A lógica para fornecer ícones personalizados
        if isinstance(_input, qtc.QFileInfo):
            if _input.isDir():
                return self.table_icon
            elif _input.isFile():
                return self.column_icon
        else:
            if _input == qtg.QAbstractFileIconProvider.Folder:
                return self.table_icon
            elif _input == qtg.QAbstractFileIconProvider.File:
                return self.column_icon
        return super().icon(_input)
