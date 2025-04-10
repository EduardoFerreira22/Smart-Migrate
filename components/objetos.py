
from PySide6.QtCore import QCoreApplication,QUrl,QTimer,Qt, QEvent,QObject
from PySide6.QtGui import QIcon,QFont,QColor,QDesktopServices, QKeyEvent
from PySide6 import QtCore
from PySide6.QtWidgets import (QApplication,QMainWindow,QMessageBox,QProgressBar,QDialog, QVBoxLayout, QPushButton,QTableWidgetItem,QFileDialog,QMenu, QWidgetAction,
                                    QPlainTextEdit, QPushButton, QVBoxLayout, QWidget, QSystemTrayIcon, QMenu)
                                    

def search_file():
    file_dialog = QFileDialog()
    file_dialog.setFileMode(QFileDialog.ExistingFile)
    # Definir filtros para múltiplas extensões
    file_dialog.setNameFilter("Arquivos suportados (*.csv *.xlsx);;CSV (*.csv);;Excel (*.xlsx);;Todos os arquivos (*.*)")
    
    if file_dialog.exec():
        file = file_dialog.selectedFiles()[0]
        print(file)
        return file
    return None  # Retorna None se o usuário cancelar

