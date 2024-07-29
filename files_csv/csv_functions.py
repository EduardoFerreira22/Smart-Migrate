from PySide6.QtWidgets import (QApplication,QMainWindow,QMessageBox,QTableWidgetItem,QFileDialog)
from configs.erros import Erros
import csv

import gui.app_instance as app_instance # Importe o módulo que você criou


from PySide6.QtWidgets import QFileDialog
import csv
import gui.app_instance as app_instance  # Importe o módulo que você criou
from configs.erros import Erros
import re

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