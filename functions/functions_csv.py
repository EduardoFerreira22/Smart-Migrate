import os
import csv
import asyncio
import chardet

from PySide6.QtCore import QCoreApplication,QUrl,QTimer,Qt, QEvent,QObject
from PySide6.QtGui import QGuiApplication, QIcon,QFont,QColor,QDesktopServices, QKeyEvent
from PySide6 import QtCore
from PySide6.QtWidgets import (QApplication,QMainWindow,QMessageBox,QProgressBar,QDialog, QVBoxLayout, QPushButton,QTableWidgetItem,QFileDialog,QMenu, QWidgetAction,
                                    QPlainTextEdit, QPushButton, QVBoxLayout, QWidget, QSystemTrayIcon, QMenu, QTableWidget)


def detectar_encoding(path_csv):
    try:
        with open(path_csv, 'rb') as f:
            result = chardet.detect(f.read())
        return result['encoding']
    except Exception as e:
        print(f"Não foi possível carregar o arquivo:\n{e}")

def read_csv_file(file_path, progress_callback=None):
    """Lê o arquivo CSV sem bloquear a UI"""
    encoding = detectar_encoding(file_path)
    try:
        if encoding:
            with open(file_path, newline='', encoding=encoding) as csvfile:
                reader = csv.reader(csvfile, delimiter=';')
                all_data = []
                row_count = sum(1 for row in reader)  # Conta total de linhas
                csvfile.seek(0)  # Volta ao início
                for i, row in enumerate(reader):
                    all_data.append(row)
                    if progress_callback:
                        progress_callback(i + 1, row_count)
                return all_data
    except UnicodeDecodeError:
        with open(file_path, newline='', encoding="latin1", errors='replace') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            all_data = []
            row_count = sum(1 for row in reader)
            csvfile.seek(0)
            for i, row in enumerate(reader):
                all_data.append(row)
                if progress_callback:
                    progress_callback(i + 1, row_count)
            return all_data
        
def load_data_InTable(table: QTableWidget, data):
    try:
        if not data:
            return

        # Separa o cabeçalho e os dados
        header = data[0]
        rows_data = data[1:]

        rows = len(rows_data)
        cols = len(header)

        table.setRowCount(rows)
        table.setColumnCount(cols)
        table.setHorizontalHeaderLabels(header)

        # Popula os dados
        for i, row in enumerate(rows_data):
            for j, cell in enumerate(row):
                item = QTableWidgetItem(str(cell))
                table.setItem(i, j, item)

        table.resizeColumnsToContents()

    except Exception as e:
        print(f"Erro ao popular tabela: {str(e)}")

        