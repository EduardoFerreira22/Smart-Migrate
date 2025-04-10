import asyncio
from PySide6.QtCore import QCoreApplication,QUrl,QTimer,Qt, QEvent,QObject
from PySide6.QtGui import QGuiApplication, QIcon,QFont,QColor,QDesktopServices, QKeyEvent
from PySide6 import QtCore
from PySide6.QtWidgets import (QApplication,QMainWindow,QMessageBox,QProgressBar,QDialog, QVBoxLayout, QPushButton,QTableWidgetItem,QFileDialog,QMenu, QWidgetAction,
                                    QPlainTextEdit, QPushButton, QVBoxLayout, QWidget, QSystemTrayIcon, QMenu)

from ui.ui_main import Ui_PrincipalWindow
from components.progress_bar import CSVLoaderThread, ProgressBarWindow
import ui.app_instance as app_instance
from components import controladores as i
from components import objetos as obj
from functions import functions_csv as f_csv


        

class WindowPrincipal(QMainWindow, Ui_PrincipalWindow):
    def __init__(self):
        super(WindowPrincipal, self).__init__()
        self.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)#Remove a barra padrão
        self.old_pos = None  # Variável para armazenar a posição do mouse
        self.full_size_window()
        app_instance.set_ui_instance(self)
        self.show_frames = i.FramesControler()
        self.visibilidade_objetos()

        
        
    def visibilidade_objetos(self):
        self.btn_salvar_geral.setEnabled(False)
        self.btn_opcoes_pesquisas.setEnabled(False)
        self.btn_opcoes_processamento.setEnabled(False)
        self.show_frames.showFrames(status=False)


        # Obtendo o tamanho da tela corretamente no PySide6
    def full_size_window(self):
        screen = QGuiApplication.primaryScreen().geometry()
        self.setGeometry(0, 0, screen.width(), screen.height())
        self.setup_buttons()

    #Funções que permitem arrastar a tela //////////////////////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        """Armazena a posição do clique inicial ao pressionar o botão esquerdo do mouse."""
        if event.button() == Qt.LeftButton:
            self.old_pos = event.globalPos()

    def mouseMoveEvent(self, event):
        """Move a janela com base na posição do mouse."""
        if self.old_pos is not None:
            delta = event.globalPos() - self.old_pos
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.old_pos = event.globalPos()

    def mouseReleaseEvent(self, event):
        """Libera o movimento ao soltar o botão do mouse."""
        if event.button() == Qt.LeftButton:
            self.old_pos = None       
    #///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    def setup_buttons(self):
        # Estado da Janela (Maximizada ou não)
        self.isMaximized = False  
        # Conectar os botões às funções
        self.btn_minimize.clicked.connect(self.minimize_window)
        
        self.btn_maximize.clicked.connect(self.maximize_restore_window)
        
        self.btn_close_window.clicked.connect(self.close_window)
        self.btn_importar_file.clicked.connect(self.buscar_csv)
        self.btn_opcoes_pesquisas.clicked.connect(lambda: self.mostrar_opcoes('pesquisar'))
        self.btn_opcoes_processamento.clicked.connect(lambda: self.mostrar_opcoes('processar'))

    # Método buscar_csv ajustado
    def buscar_csv(self):
        path_file = obj.search_file()
        if path_file:
            # Cria e exibe a janela de progresso
            self.progress_window = ProgressBarWindow(path_file, parent=self)  # Passa self como parent
            self.progress_window.thread.data_loaded.connect(self.on_csv_loaded)
            self.progress_window.show()

    def on_csv_loaded(self, data):
        """Callback executado quando os dados do CSV são carregados"""
        if data:
            f_csv.load_data_InTable(table=self.table_principal, data=data)
            self.btn_salvar_geral.setEnabled(True)
            self.btn_opcoes_pesquisas.setEnabled(True)
            self.btn_opcoes_processamento.setEnabled(True)
        self.progress_window.close()

    def mostrar_opcoes(self, acao):
        if acao == "pesquisar":
            self.show_frames.frames[0].setVisible(True)
            self.page_opcoes_processamento.setVisible(False)
            self.page_opcoes_busca.setVisible(True)
        elif acao == "processar":
            self.show_frames.frames[0].setVisible(True)
            self.page_opcoes_processamento.setVisible(True)
            self.page_opcoes_busca.setVisible(False)

    def minimize_window(self):
        """Minimiza a janela."""
        self.showMinimized()

    def maximize_restore_window(self):
        """Alterna entre maximizar e restaurar o tamanho original da janela."""
        if self.isMaximized:
            self.showNormal()  # Restaura o tamanho original
            self.full_size_window()
            self.isMaximized = False
        else:
            self.showMaximized()  # Maximiza a janela
            # self.resize(1400, 800)
            self.isMaximized = True

    def close_window(self):
        """Fecha a janela."""
        self.close()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)  # Crie a instância de QApplication
    window = WindowPrincipal()
    window.show()
    sys.exit(app.exec())  # Execute o loop de eventos e finalize o programa corretamente