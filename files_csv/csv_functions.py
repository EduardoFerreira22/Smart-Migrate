from PySide6.QtWidgets import (QApplication,QMainWindow,QMessageBox,QTableWidgetItem,QFileDialog)
from PySide6.QtGui import QIcon,QFont,QColor,QDesktopServices
from configs.erros import Erros
import csv
import pandas as pd
import chardet

import gui.app_instance as app_instance 
from PySide6.QtWidgets import QFileDialog
import csv
from configs.erros import Erros
from configs.encoders import detectar_encoding
import re
from collections import defaultdict

#COMBO OPTIONS
def combo_Columns(head):
    ui = app_instance.get_ui_instance()
    ui.combo1_colunas_processamento.addItems(head)
    ui.combo2_colunas_processamento.addItems(head)
    ui.combo3_colunas_processamento.addItems(head)
    ui.combo4_colunas_processamento.addItems(head)
    ui.combo1_colunas_opcoes_busca.addItems(head)

def save_data_to_csv(file_path,table):
    error = Erros()
    ui = app_instance.get_ui_instance()


    if file_path:
        try:
            with open(file_path, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file, delimiter=';')
                headers = [table.horizontalHeaderItem(i).text() for i in range(table.columnCount())]
                writer.writerow(headers)
                for row in range(table.rowCount()):
                    row_data = [table.item(row, col).text() if table.item(row, col) else '' for col in range(table.columnCount())]
                    writer.writerow(row_data)
            ui.txt_output_logs.setPlainText(f"Dados salvos com sucesso em: {file_path}")
        except Exception as e:
            error.show_error_popup("Erro ao salvar o arquivo", str(e))
            print(e)

def analise_inteligente():
    ui = app_instance.get_ui_instance()
    # Identifica as colunas relevantes
    colunas_relevantes = [
        'codigo', 'código', 'cod. barras', 'código de barras', 'cod_barras', 'codigo_barras',
        'nome', 'descricao', 'descrição', 'nome_produto', 'nome_cliente', 'nome do produto',
        'nome do cliente', 'nome_fornecedor', 'nome do fornecedor', 'codigo', 'cod', 'id_produto', 
        'id_cliente', 'cod_produto', 'cod_cliente', 'cod_fornecedor', 'id_fornecedor', 'id_conta', 
        'cod_conta', 'codigo_cliente', 'codigo_produto', 'codigo_fornecedor', 'codigo_conta', 
        'Nome_fantasia', 'Razao social', 'CPF_CNPJ_CLIENTE'
    ]
    
    if ui.table_principal is None:
        ui.label_titulo_analise_inteligente.setText("Nenhuma tabela carregada para análise.")
        return
    
    num_linhas = ui.table_principal.rowCount()
    if num_linhas == 0:
        ui.label_titulo_analise_inteligente.setText("A tabela está vazia.")
        return
    
    # Obtém os nomes das colunas
    colunas = [ui.table_principal.horizontalHeaderItem(i).text() for i in range(ui.table_principal.columnCount())]

    # Identifica as colunas relevantes presentes na tabela
    colunas_identificadas = [col for col in colunas if col.lower() in [c.lower() for c in colunas_relevantes]]

    if not colunas_identificadas:
        ui.label_titulo_analise_inteligente.setText("Nenhuma coluna relevante encontrada na tabela.")
        return
    
    # Análise de duplicatas e caracteres especiais
    duplicatas = {}
    duplicatas_codigo_barras = {}
    caracteres_especiais = set()

    for row in range(num_linhas):
        linha = [ui.table_principal.item(row, col).text() for col in range(ui.table_principal.columnCount())]
        chave = tuple(linha[i] for i in range(ui.table_principal.columnCount()) if colunas[i] in colunas_identificadas)
        
        # Análise geral de duplicatas
        if chave:
            duplicatas[chave] = duplicatas.get(chave, 0) + 1
        
        # Análise específica para a coluna de código de barras
        for col in colunas_identificadas:
            if col.lower() in ['codigo_barras', 'codigo de barras', 'cod_barras', 'barcode']:
                valor_codigo_barras = linha[colunas.index(col)]
                if valor_codigo_barras:
                    duplicatas_codigo_barras[valor_codigo_barras] = duplicatas_codigo_barras.get(valor_codigo_barras, 0) + 1

        for valor in linha:
            caracteres_especiais.update(re.findall(r'\W', valor))

    # Contabilizar duplicatas e caracteres especiais
    num_duplicatas = sum(1 for count in duplicatas.values() if count > 1)
    num_duplicatas_codigo_barras = sum(1 for count in duplicatas_codigo_barras.values() if count > 1)
    num_caracteres_especiais = len(caracteres_especiais)

    # Atualizar os labels com os resultados
    ui.quantidade_linhas_tabela.setText(str(num_linhas))
    ui.quantidade_linhas_duplicadas.setText(str(num_duplicatas))
    ui.quantidade_cod_barras.setText(str(num_duplicatas_codigo_barras))
    ui.quantidade_caracteres_especiais.setText(str(num_caracteres_especiais))
    
    # Atualizar o label principal com um resumo
    ui.label_titulo_analise_inteligente.setText("Análise inteligente concluída com sucesso.")

def valores_negativos(path_csv, coluna):
    encoding = detectar_encoding(path_csv=path_csv)
    ui = app_instance.get_ui_instance()
    coluna = coluna

    try:
        # Carregar o CSV
        df = pd.read_csv(path_csv, delimiter=';', encoding=encoding)

        # Identificar e alterar os valores negativos para 0
        df.loc[df[coluna] < 0, coluna] = 0

        # Salvar o CSV atualizado
        df.to_csv(path_csv, index=False, sep=';', encoding='latin1')
        print("Valores negativos substituídos por 0 com sucesso.")
        ui.txt_output_logs.setPlainText("Todos os dados negativos foram removidos com sucesso!")


    except Exception as e:
        print(f"Erro: {e}")
        ui.txt_output_logs.setPlainText(f"Erro ao processar valores negativos: {e}")


def find_and_load_duplicates(data, headers):
    # Column names to search for duplicates
    columns_to_check = [
        'codigo', 'código', 'cod. barras', 'código de barras', 'cod_barras', 'codigo_barras',
        'nome', 'descricao', 'descrição', 'nome_produto', 'nome_cliente', 'nome do produto',
        'nome do cliente', 'nome_fornecedor', 'nome do fornecedor', 'codigo', 'cod', 'id_produto', 
        'id_cliente', 'cod_produto', 'cod_cliente', 'cod_fornecedor', 'id_fornecedor', 'id_conta', 
        'cod_conta', 'codigo_cliente', 'codigo_produto', 'codigo_fornecedor', 'codigo_conta', 
        'Nome_fantasia', 'Razao social', 'CPF_CNPJ_CLIENTE'
    ]

    # Normalize headers
    header_map = {header.lower().strip(): header for header in headers}

    # Find column indices to check
    indices_to_check = [index for index, header in enumerate(headers)
                        if header.lower().strip() in map(str.lower, columns_to_check)]

    # Create a dictionary to store seen values and their rows
    seen = defaultdict(list)
    duplicates = []

    for row in data:
        key = tuple(row[index] for index in indices_to_check)
        seen[key].append(row)

    for rows in seen.values():
        if len(rows) > 1:
            duplicates.extend(rows)  # Add all duplicates to the list

    # Load duplicates into table_duplicados
    load_duplicates_to_table(duplicates, headers)
    
    return duplicates

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
