from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QFrame, QTableWidget)
from PySide6.QtCore import QSize, Qt

import ui.app_instance as app_instance


class FramesControler:
    def __init__(self):
        ui = app_instance.get_ui_instance()


        self.frames = [
            ui.frame_opcoes_busca_processamento,
            ui.frm_lateral_functions,
            ui.frm_functions_table_principal,
            ui.frm_cadastro_cliente,
            ui.frm_cadastro_contabilidade,
            ui.comboBox_opcoes_de_busca2,
            ui.btn_extrair_duplicados,
            ui.data_filtro_inicio_cliente,
            ui.data_filtro_fim_cliente,
            ui.combo_filtro_statusEnvio,
            ui.combo_filtro_contador,
            ui.btn_atualizar_cliente,

            ]

    def showFrames(self, status):
        for f in self.frames:
          f.setVisible(status)

    def showFrm_lateral(self):
        ui = app_instance.get_ui_instance()
        ui.frm_lateral_functions.setVisible(True)

    def closeFrm_lateral(self):
        ui = app_instance.get_ui_instance()
        ui.frm_lateral_functions.setVisible(False)

    def closeFrm_lateral_cliente(self):
        ui = app_instance.get_ui_instance()
        ui.frm_cadastro_cliente.setVisible(False)
    
    def closeFrm_lateral_contabilidade(self):
        ui = app_instance.get_ui_instance()
        ui.frm_cadastro_contabilidade.setVisible(False)

    #Navegando entre as páginas
def atualizar_titulo():
    ui = app_instance.get_ui_instance()
    indictse_atual = ui.stackedWidget_tables.currentIndex()
    if indictse_atual == 0:
        ui.lb_titulos_tabelas.setText("Manipulação de Dados")
    elif indictse_atual == 1:
        ui.lb_titulos_tabelas.setText("Duplicados")
    elif indictse_atual == 2:
        ui.lb_titulos_tabelas.setText("Contábil-Fiscal")

def mudar_pag_anterior():
    ui = app_instance.get_ui_instance()
    indictse_atual = ui.stackedWidget_tables.currentIndex()
    if indictse_atual > 0:
        ui.stackedWidget_tables.setCurrentIndex(indictse_atual - 1)
        print(indictse_atual)
        atualizar_titulo()

def mudar_proxima_pag():
    ui = app_instance.get_ui_instance()
    indictse_atual = ui.stackedWidget_tables.currentIndex()
    if indictse_atual < ui.stackedWidget_tables.count() - 1:
        ui.stackedWidget_tables.setCurrentIndex(indictse_atual + 1)
        print(indictse_atual)
        atualizar_titulo()

def contabil_fiscal():
    ui = app_instance.get_ui_instance()
    ui.stackedWidget_tables.setCurrentWidget(ui.page_contabil_fiscal)
    ui.lb_titulos_tabelas.setText("Contábil-Fiscal")

class Tabelas:
    def __init__(self):
        ...

    def carregarDadosNaTabela(self, data, table, color):
        ...
              

def combosHeader(data, combo, table: QTableWidget):
    ui = app_instance.get_ui_instance()
    print(str(ui))
# Garantir que o layout seja o horizontalLayout_2
# Usar o layout existente
# Usar o layout existente
    layout = ui.horizontalLayout_2
    
    # Depuração
    print(f"Layout type: {type(layout)}")
    print(f"Número de colunas na tabela: {table.columnCount()}")
    
    # Lista para armazenar os combos (começa com o combo existente)
    combos = [combo]
    
    # Extrai as propriedades do combo existente
    min_tamanho = combo.minimumSize()
    max_tamanho = combo.maximumSize()
    nome_base = combo.objectName().replace("_1", "")
    
    # Limpar o layout existente (exceto o combo base) com segurança
    widgets_to_delete = []
    for i in reversed(range(layout.count())):
        item = layout.itemAt(i)
        widget = item.widget() if item else None
        if widget and widget != combo:  # Preserva o combo base
            layout.removeWidget(widget)
            widgets_to_delete.append(widget)
    
    # Deletar os widgets removidos após a iteração
    for widget in widgets_to_delete:
        widget.deleteLater()
    
    # Cria combos adicionais a partir da segunda coluna
    for i in range(1, table.columnCount()):
        print(f"Criando combo para a coluna {i}")
        new_combo = QComboBox(ui.frm_combos_heads)
        new_combo.setObjectName(f"{nome_base}_{i + 1}")
        new_combo.setMinimumSize(min_tamanho)
        new_combo.setMaximumSize(max_tamanho)
        
        # Adiciona o nome da coluna como item inicial
        header = table.horizontalHeaderItem(i)
        if header and header.text():
            new_combo.addItem(header.text())
            print(f"Item adicionado ao combo {new_combo.objectName()}: {header.text()}")
        
        # Adiciona o combo ao layout
        layout.addWidget(new_combo, 0, Qt.AlignmentFlag.AlignLeft)
        combos.append(new_combo)
        print(f"Combo {new_combo.objectName()} adicionado ao layout")
    
    # Adiciona um espaçador ao final
    layout.addStretch(1)
    
    # Configura o combo base com o texto da primeira coluna
    header_0 = table.horizontalHeaderItem(0)
    if header_0 and header_0.text() and combo.count() == 0:
        combo.addItem(header_0.text())
        print(f"Item adicionado ao {combo.objectName()}: {header_0.text()}")
    
    # Armazena os combos na instância
    combos = combos
    print(f"Total de combos criados: {len(combos)}")
    
    # Forçar atualização do scroll area
    ui.scroll_area_combos.update()

def clean_txt_cliente():
    ui = app_instance.get_ui_instance()
    ui.txt_nome_cliente.clear()
    ui.txt_razao_social_cliente.clear()
    ui.txt_cnpj_cliente.clear()
    ui.txt_email_cliente.clear()
    ui.combo_sistema_cliente.clear()
    ui.txt_link_sistema_cliente.clear()
    ui.txt_user_cliente_sistema.clear()
    ui.txt_password_cliente_sistema.clear()