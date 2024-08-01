from PySide6.QtWidgets import (QApplication,QMainWindow,QMessageBox,QTableWidgetItem,QFileDialog)
from configs.erros import Erros
import csv

import gui.app_instance as app_instance # Importe o módulo que você criou


from PySide6.QtWidgets import QFileDialog
import csv
import gui.app_instance as app_instance  # Importe o módulo que você criou
from configs.erros import Erros
import re
from collections import defaultdict

#COMBO OPTIONS
def combo_Columns(head):
    ui = app_instance.get_ui_instance()
    ui.combo1_colunas_processamento.addItems(head)
    ui.combo2_colunas_processamento.addItems(head)
    ui.combo3_colunas_processamento.addItems(head)
    ui.combo4_colunas_processamento.addItems(head)

def save_data_to_csv():
    error = Erros()
    ui = app_instance.get_ui_instance()

    file_path, _ = QFileDialog.getSaveFileName(
        ui,
        "Salvar Arquivo CSV",
        "",
        "CSV Files (*.csv);;All Files (*)"
    )

    if file_path:
        try:
            with open(file_path, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file, delimiter=';')
                headers = [ui.table_principal.horizontalHeaderItem(i).text() for i in range(ui.table_principal.columnCount())]
                writer.writerow(headers)
                for row in range(ui.table_principal.rowCount()):
                    row_data = [ui.table_principal.item(row, col).text() if ui.table_principal.item(row, col) else '' for col in range(ui.table_principal.columnCount())]
                    writer.writerow(row_data)
            ui.txt_output_logs.setPlainText(f"Dados salvos com sucesso em: {file_path}")
        except Exception as e:
            error.show_error_popup("Erro ao salvar o arquivo", str(e))
            print(e)

def analise_inteligente():
    ui = app_instance.get_ui_instance()
    # Identifica as colunas relevantes
    colunas_relevantes = [
        'nome', 'Cliente', 'cliente', 'produto', 'nome produto',
        'descricao', 'codigo', 'cod', 'codigo_barras', 'codigo de barras'
    ]
    
    texto_analise = ""
    
    if ui.table_principal is None:
        texto_analise = "Nenhuma tabela carregada para análise."
        ui.txt_analise_inteligente_output.setPlainText(texto_analise)
        return
    
    num_linhas = ui.table_principal.rowCount()
    if num_linhas == 0:
        texto_analise = "A tabela está vazia."
        ui.txt_analise_inteligente_output.setPlainText(texto_analise)
        return
    
    # Obtém os nomes das colunas
    colunas = [ui.table_principal.horizontalHeaderItem(i).text() for i in range(ui.table_principal.columnCount())]

    # Identifica as colunas relevantes presentes na tabela
    colunas_identificadas = [col for col in colunas if col.lower() in [c.lower() for c in colunas_relevantes]]

    if not colunas_identificadas:
        texto_analise = "Nenhuma coluna relevante encontrada na tabela."
        ui.txt_analise_inteligente_output.setPlainText(texto_analise)
        return
    
    # Análise de duplicatas e caracteres especiais
    dados = {}
    caracteres_especiais = set()
    duplicatas = {}
    
    for row in range(num_linhas):
        linha = [ui.table_principal.item(row, col).text() for col in range(ui.table_principal.columnCount())]
        chave = tuple(linha[i] for i in range(ui.table_principal.columnCount()) if colunas[i] in colunas_identificadas)
        if chave:
            if chave in duplicatas:
                duplicatas[chave] += 1
            else:
                duplicatas[chave] = 1
        for valor in linha:
            caracteres_especiais.update(re.findall(r'\W', valor))

    num_linhas_processadas = num_linhas
    num_duplicatas = sum(1 for count in duplicatas.values() if count > 1)
    num_caracteres_especiais = len(caracteres_especiais)
    
    texto_analise += (f"Total de linhas processadas: {num_linhas_processadas}\n"
                      f"Linhas duplicadas encontradas: {num_duplicatas}\n"
                      f"Total de caracteres especiais encontrados: {num_caracteres_especiais}\n")
    
    for chave, count in duplicatas.items():
        if count > 1:
            texto_analise += f"Duplicata: {chave}, Contagem: {count}\n"
    
    ui.txt_analise_inteligente_output.setPlainText(texto_analise)

    #ENCONTRA VALORES NEGATIVOS E MUDA PARA ZERO

def valores_negativos(self):
    self.backup_process_csv()
    coluna = self.combo_column1.currentText()
    try:
        df = pd.read_csv(self.path_csv, delimiter=';', encoding='latin1')

        # Identificar e alterar os valores negativos para 0
        df.loc[df[coluna] < 0, coluna] = 0

        df.to_csv(self.path_csv,index=False, sep=';', encoding='latin1')
        print("Valores negativos substituídos por 0 com sucesso.")
        self.update_label_info("Todos os dados negativos foram removidos com sucesso!")
        self.processar_csv()
    except Exception as e:
        self.log.logs(name_file=self.file_name,path=self.path_logs,msg=f"Erro valores_negativos : Erro ao tentar remover os dados negativos: {e}")
        self.update_label_info(f"Erro ao tentar remover os dados negativos: {e}")
        print(f"Erro: {e}")


def carregar_dados_da_tabela():
    # Função que extrai os dados e cabeçalhos da tabela que você deseja analisar
    # Aqui você precisa adaptar conforme a estrutura da sua interface
    ui = app_instance.get_ui_instance()
    table = ui.table_principal  # Supondo que os dados estejam em `table_principal`
    
    headers = []
    for column in range(table.columnCount()):
        headers.append(table.horizontalHeaderItem(column).text())
    
    data = []
    for row in range(table.rowCount()):
        row_data = []
        for column in range(table.columnCount()):
            item = table.item(row, column)
            row_data.append(item.text() if item else '')
        data.append(row_data)
    
    return data, headers

def find_and_load_duplicates(data, headers):
    # Column names to search for duplicates
    columns_to_check = [
        'codigo', 'código', 'cod. barras', 'código de barras', 'cod_barras', 'codigo_barras',
        'nome', 'descricao', 'descrição', 'nome_produto', 'nome_cliente', 'nome do produto',
        'nome do cliente', 'nome_fornecedor', 'nome do fornecedor'
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

def load_duplicates_to_table(duplicates, headers):
    ui = app_instance.get_ui_instance()
    table = ui.table_duplicados

    # Clear existing data
    table.setRowCount(0)
    table.setColumnCount(len(headers))  # Set column count based on headers

    # Set column headers
    table.setHorizontalHeaderLabels(headers)

    for row_data in duplicates:
        row_position = table.rowCount()
        table.insertRow(row_position)
        for column, value in enumerate(row_data):
            item = QTableWidgetItem(str(value))
            table.setItem(row_position, column, item)