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


class XMLLoaderThread(QThread):
    progress = Signal(int)
    log = Signal(str)
    data_loaded = Signal(list)

    def __init__(self, directory):
        super().__init__()
        self.directory = directory
        self.xml_files = [f for f in os.listdir(directory) if f.endswith('.xml')]
        self.total_files = len(self.xml_files)

    def run(self):
        if not self.xml_files:
            self.log.emit("Nenhum arquivo XML encontrado no diretório.")
            self.data_loaded.emit([])
            return

        processed_files = []
        for i, xml_file in enumerate(self.xml_files):
            xml_path = os.path.join(self.directory, xml_file)
            processed_files.append(xml_path)
            progress_value = int((i + 1) / self.total_files * 100)
            self.progress.emit(progress_value)
            self.log.emit(f"Processando arquivo {i + 1} de {self.total_files}: {xml_file}")
            self.msleep(50)  # Pequena pausa para simular processamento
        self.log.emit(f"Processamento concluído: {self.total_files} arquivos XML.")
        self.data_loaded.emit(processed_files)

class ProgressBarWindow(QDialog):
    def __init__(self, path, parent=None):
        super().__init__(parent)
        self.ui = Ui_ProgressBar()
        self.ui.setupUi(self)
        self.setWindowModality(Qt.ApplicationModal)

        self.path = path

        if os.path.isdir(path):
            self.thread = XMLLoaderThread(path)
        else:
            self.thread = CSVLoaderThread(path)

        self.thread.progress.connect(self.update_progress)
        self.thread.log.connect(self.update_log)
        self.thread.data_loaded.connect(self.data_finished)
        self.thread.start()

    def update_progress(self, value):
        self.ui.progressBar.setValue(value)

    def update_log(self, message):
        self.ui.lb_informacoes_progress.setText(
            f"<html><head/><body><p align=\"center\"><span style=\" font-size:8pt; font-weight:700;\">{message}</span></p></body></html>"
        )
        
    def data_finished(self, data):
        """Executado quando os dados são carregados"""
        print(f"Dados carregados: {len(data)} linhas")
        # self.close()  # Opcional: fecha a janela ao terminar

