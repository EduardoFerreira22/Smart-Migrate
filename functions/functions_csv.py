import os
import csv
import asyncio
import chardet
from ui import app_instance
from PySide6.QtCore import QCoreApplication,QUrl,QTimer,Qt, QEvent,QObject
from PySide6.QtGui import QGuiApplication, QIcon,QFont,QColor,QDesktopServices, QKeyEvent
from PySide6 import QtCore
from PySide6.QtWidgets import (QApplication,QMainWindow,QMessageBox,QProgressBar,QDialog, QVBoxLayout, QPushButton,QTableWidgetItem,QFileDialog,QMenu, QWidgetAction,
                                    QPlainTextEdit, QPushButton, QVBoxLayout, QWidget, QSystemTrayIcon, QMenu, QTableWidget)



def combo_Columns(head):
        ui = app_instance.get_ui_instance()
        ui.cbx_coluna_processamento1.clear()
        ui.cbx_coluna_processamento2.clear()
        ui.cbx_coluna_processamento3.clear()
        ui.comboBox_opcoes_de_busca2.clear()

        ui.cbx_coluna_processamento1.addItems(head)
        ui.cbx_coluna_processamento2.addItems(head)
        ui.cbx_coluna_processamento3.addItems(head)
        ui.comboBox_opcoes_de_busca2.addItems(head)


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


def load_duplicates_to_table(duplicates, headers):
    """
    Carrega os dados de duplicados na tabela table_duplicados e ordena os dados para facilitar a análise.
    """
    ui = app_instance.get_ui_instance()
    table = ui.table_duplicados

    # Obtém a coluna selecionada no comboBox
    coluna_para_verificar = ui.combo1_colunas_opcoes_busca.currentText()

    if coluna_para_verificar not in headers:
        ui.txt_output_logs.setPlainText(f"A coluna '{coluna_para_verificar}' não está disponível nos dados de duplicados.")
        return

    # Limpa a tabela existente
    table.setRowCount(0)
    table.setColumnCount(len(headers))
    table.setHorizontalHeaderLabels(headers)

    if duplicates:
        # Cria um DataFrame com os dados duplicados
        df_duplicates = pd.DataFrame(duplicates, columns=headers)
        
        # Ordena os duplicados pela coluna que contém os valores duplicados
        df_sorted = df_duplicates.sort_values(by=[coluna_para_verificar])

        # Preenche a tabela com os dados ordenados
        table.setRowCount(df_sorted.shape[0])
        for row in range(df_sorted.shape[0]):
            for col in range(df_sorted.shape[1]):
                item = QTableWidgetItem(str(df_sorted.iloc[row, col]))
                table.setItem(row, col, item)
                # Marcar linhas duplicadas em vermelho
                item.setBackground(QColor(255, 52, 52, 63))  # Vermelho claro com transparência

        table.resizeColumnsToContents()
        table.resizeRowsToContents()
        ui.txt_output_logs.setPlainText(f"Duplicatas carregadas e ordenadas na tabela de duplicados.")
    else:
        ui.txt_output_logs.setPlainText("Nenhum dado de duplicados para carregar na tabela.")

# Essa função busca por dados duplicados na coluna selecionada pelo usuário e as marca em vermelho ordenando no inicio da tabela

def buscar_dados_duplicados(path_csv):
    
    erros = Erros()
    ui = app_instance.get_ui_instance()
    ui.txt_output_logs.setPlainText("Aguarde...")
    table = ui.table_principal

    # Obtém a coluna selecionada no comboBox
    coluna_para_verificar = ui.combo1_colunas_opcoes_busca.currentText()

    if not coluna_para_verificar:
        ui.txt_output_logs.setPlainText("Nenhuma coluna foi selecionada para análise.")
        return

    try:
        # Detectar o encoding do arquivo CSV
        encoding = detectar_encoding(path_csv)

        # Ler o arquivo CSV original usando o encoding detectado
        df = pd.read_csv(path_csv, delimiter=';', encoding=encoding)

        if coluna_para_verificar not in df.columns:
            raise ValueError(f"A coluna '{coluna_para_verificar}' não foi encontrada no CSV.")

        # Filtra linhas com valores não vazios na coluna selecionada
        df_non_empty = df[df[coluna_para_verificar].notna() & df[coluna_para_verificar].str.strip().ne('')]

        # Verifica duplicatas na coluna selecionada (ignorando células vazias)
        duplicatas = df_non_empty[df_non_empty.duplicated(subset=[coluna_para_verificar], keep=False)]

        if not duplicatas.empty:
            # Ordena o DataFrame para que as duplicatas apareçam no início
            df_non_empty = df_non_empty.sort_values(by=[coluna_para_verificar])
            duplicatas_sorted = duplicatas.sort_values(by=[coluna_para_verificar])

            # Cria um DataFrame para a tabela final
            df_final = pd.concat([duplicatas_sorted, df_non_empty[~df_non_empty.index.isin(duplicatas_sorted.index)]])

            headers = df_final.columns.tolist()  # Obter os cabeçalhos
            duplicates_list = duplicatas.values.tolist()

            # Atualiza a tabela com o DataFrame final
            table.setRowCount(df_final.shape[0])  # Ajusta o número de linhas da tabela
            # Definir cor de fundo com transparência (simulação)
            transparent_color = QColor(255, 52, 52)  # Transparência não suportada diretamente
            transparent_color.setAlphaF(0.25)  # Define a transparência

            for row in range(df_final.shape[0]):
                for col in range(df_final.shape[1]):
                    item = QTableWidgetItem(str(df_final.iloc[row, col]))
                    table.setItem(row, col, item)
                    # Marcar linhas duplicadas em vermelho
                    if df_final.iloc[row][coluna_para_verificar] in duplicatas[coluna_para_verificar].values:
                        item.setBackground(transparent_color)  # Vermelho claro

            ui.txt_output_logs.setPlainText(f"Duplicatas encontradas na coluna '{coluna_para_verificar}' e ordenadas no início da tabela.")
            return duplicates_list, headers
        else:
            ui.txt_output_logs.setPlainText(f"Nenhuma duplicata encontrada na coluna '{coluna_para_verificar}'.")
            return [], headers

    except Exception as e:
        ui.txt_output_logs.setPlainText(f"Erro ao buscar dados duplicados: {e}")
        erros.show_error_popup("Erro!", f"Erro ao tentar processar o arquivo: {e}\n\nEsse erro pode acontecer quando não foi possível encontrar\ndados duplicados na coluna selecionada.\n\nSelecione outra coluna e tente novamente, se o erro persistir\npode ser que não haja dados duplicados na sua tabela.")
        return [], []