import csv
import chardet
import os
import sys
from PySide6.QtWidgets import QDialog, QMessageBox, QPushButton, QVBoxLayout, QApplication, QWidget
from PySide6.QtCore import QThread, Signal, QObject, QMetaObject, Qt
# Ajusta o sys.path para encontrar o módulo ui a partir do diretório raiz
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'ui')))

# Importa a UI e as funções
from ui.ui_progress import Ui_ProgressBar
from functions.functions_csv import read_csv_file, detectar_encoding

#Classe da thread de carregamento
class CSVLoaderThread(QThread):
    progress = Signal(int)
    log = Signal(str)
    data_loaded = Signal(list)

    def __init__(self, file_path):
        super().__init__()
        self.file_path = file_path

    def run(self):
        def progress_callback(current_row, total_rows):
            progress_value = int(current_row / total_rows * 100)
            self.progress.emit(progress_value)
            if current_row % 100 == 0:
                self.log.emit(f"Carregando linha {current_row} de {total_rows}")

        all_data = read_csv_file(self.file_path, progress_callback=progress_callback)
        if all_data is not None:
            encoding = detectar_encoding(self.file_path) or "latin1"
            self.log.emit(f"Planilha processada com encoding: {encoding.upper()}")
            self.data_loaded.emit(all_data)
        else:
            self.log.emit("Erro: Não foi possível carregar o arquivo")

# Classe da janela de progresso
class ProgressBarWindow(QDialog):
    def __init__(self, file_path, parent=None):
        super().__init__(parent)  # Passa o parent (None por padrão) para QDialog
        self.ui = Ui_ProgressBar()
        self.ui.setupUi(self)  # Configura a UI

        # Armazena o file_path como atributo
        self.file_path = file_path

        # Inicia a thread com o caminho do arquivo
        self.thread = CSVLoaderThread(file_path)
        self.thread.progress.connect(self.update_progress)
        self.thread.log.connect(self.update_log)
        self.thread.data_loaded.connect(self.data_finished)
        self.thread.start()

    def update_progress(self, value):
        """Atualiza a barra de progresso"""
        self.ui.progressBar.setValue(value)

    def update_log(self, message):
        """Atualiza o rótulo com mensagens de log"""
        self.ui.lb_informacoes_progress.setText(
            f"<html><head/><body><p align=\"center\"><span style=\" font-size:8pt; font-weight:700;\">{message}</span></p></body></html>"
        )

    def data_finished(self, data):
        """Executado quando os dados são carregados"""
        print(f"Dados carregados: {len(data)} linhas")
        # self.close()  # Opcional: fecha a janela ao terminar

