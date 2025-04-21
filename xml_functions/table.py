from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QIcon,QFont,QColor, QStandardItem, QStandardItemModel, QCursor
from PySide6 import QtCore
from PySide6.QtWidgets import (QApplication,QMessageBox,QFileDialog,QMenu,QMenu, QToolButton, QTableWidgetItem)
import ui.app_instance as app_instance
from brazilfiscalreport.danfe import Danfe
from reportlab.lib.pagesizes import landscape, A4
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader  # Para manipular a imagem
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import ParseError
import locale
from openpyxl import Workbook
from datetime import datetime
import datetime  # Para obter a data e hora atuais
import os
import csv

# Configurar o locale para formato brasileiro
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

def format_value(symbol, value, cnpj_format=False):
    """
    Formata valores monetários ou CNPJ.
    """
    try:
        if cnpj_format:
            return f"{value[:2]}.{value[2:5]}.{value[5:8]}/{value[8:12]}-{value[12:]}"
        elif isinstance(value, (int, float)):
            return f"{symbol} {locale.currency(value, grouping=True, symbol=None)}"
        elif isinstance(value, str):
            # Remove caracteres monetários (R$, espaços, pontos de milhar) e substitui vírgula por ponto
            cleaned_value = value.replace('R$', '').replace(' ', '').replace('.', '').replace(',', '.').strip()
            try:
                float_value = float(cleaned_value)
                return f"{symbol} {locale.currency(float_value, grouping=True, symbol=None)}"
            except ValueError:
                return value  # Retorna a string original se não for um número válido
        else:
            return str(value)  # Retorna como string para valores não numéricos
    except Exception as e:
        print(f"Erro ao formatar o valor '{value}': {e}")
        return str(value)  # Retorna valor original como string em caso de erro


def format_all_values(symbol, values, cnpj_indices=None):
    """
    Formata uma lista de valores.
    - `symbol`: Símbolo para valores monetários.
    - `values`: Lista ou tupla de valores a serem formatados.
    - `cnpj_indices`: Índices dos valores que são CNPJ.
    """
    formatted = []
    cnpj_indices = cnpj_indices or []  # Índices que precisam de formatação de CNPJ
    for i, value in enumerate(values):
        if i in cnpj_indices:
            formatted.append(format_value(symbol, value, cnpj_format=True))

        else:
            formatted.append(format_value(symbol, value))
    return formatted

class XmlTable:
    def __init__(self, directory):
        super(XmlTable, self).__init__()
        self.ui = app_instance.get_ui_instance()
        self.directory = directory
    # CONTA QUANTOS XML'S HÁ NA PASTA SELECIONADA
    def count_files(self,directory):
            total_files = sum(1 for arquivo in os.listdir(directory) if arquivo.endswith('.xml'))
            print(total_files)
            return total_files

    def processing_xmls(self):
        if not hasattr(self, 'directory') or not self.directory:
            print("Nenhum diretório selecionado. A busca foi cancelada.")
            return

        # Obtém a referência para o QTreeView
        tree_view = self.ui.tableWidget_xml_list

        # Cria um QStandardItemModel e configura para o QTreeView
        model = QStandardItemModel()
        tree_view.setModel(model)

        #linhas pai --------------------------------------------------------------------------------------------------
        # Define as colunas do modelo para a linha principal (Nota Fiscal)
        model.setHorizontalHeaderLabels([
            'Emitente', 'CNPJ', 'Número NF', 'Modelo NFE', 'ICMS', 
            'PIS', 'COFINS', 'IPI', 'Total NF', 'Chave NFE', 'Natureza Operação', '', '', '', '', '', ''
        ])

        # Variáveis totais
        total_geral = 0
        total_icms = 0
        total_pis = 0
        total_cofins = 0
        total_ipi = 0
        num_nf_list = []

        NAMESPACE = '{http://www.portalfiscal.inf.br/nfe}'

        for nome_arquivo in os.listdir(self.directory):
            if nome_arquivo.endswith('.xml'):
                xml_path = os.path.join(self.directory, nome_arquivo)

                try:
                    tree = ET.parse(xml_path)
                    root = tree.getroot()

                    # Obtém os valores necessários da nota fiscal
                    emitente = root.find(f'.//{NAMESPACE}emit/{NAMESPACE}xNome')
                    cnpj = root.find(f'.//{NAMESPACE}emit/{NAMESPACE}CNPJ')
                    num_nf = root.find(f'.//{NAMESPACE}ide/{NAMESPACE}nNF')
                    modelo_nfe = root.find(f'.//{NAMESPACE}ide/{NAMESPACE}mod')
                    icms = root.find(f'.//{NAMESPACE}total/{NAMESPACE}ICMSTot/{NAMESPACE}vICMS')
                    pis = root.find(f'.//{NAMESPACE}total/{NAMESPACE}ICMSTot/{NAMESPACE}vPIS')
                    cofins = root.find(f'.//{NAMESPACE}total/{NAMESPACE}ICMSTot/{NAMESPACE}vCOFINS')
                    ipi = root.find(f'.//{NAMESPACE}total/{NAMESPACE}ICMSTot/{NAMESPACE}vIPI')
                    total_nf = root.find(f'.//{NAMESPACE}total/{NAMESPACE}ICMSTot/{NAMESPACE}vNF')
                    chave_nfe = root.find(f'.//{NAMESPACE}protNFe/{NAMESPACE}infProt/{NAMESPACE}chNFe')
                    natureza_op = root.find(f'.//{NAMESPACE}ide/{NAMESPACE}natOp')

                    # Extração com verificação de None
                    emitente = emitente.text if emitente is not None else "N/A"
                    cnpj = cnpj.text if cnpj is not None else ""
                    num_nf = int(num_nf.text) if num_nf is not None else None
                    modelo_nfe = int(modelo_nfe.text) if modelo_nfe is not None else None
                    icms = float(icms.text) if icms is not None else 0.0
                    pis = float(pis.text) if pis is not None else 0.0
                    cofins = float(cofins.text) if cofins is not None else 0.0
                    ipi = float(ipi.text) if ipi is not None else 0.0
                    total_nf = float(total_nf.text) if total_nf is not None else 0.0
                    chave_nfe = chave_nfe.text if chave_nfe is not None else "N/A"
                    natureza_op = natureza_op.text if natureza_op is not None else "N/A"

                    # Formata os valores da nota fiscal
                    cnpj_formatted = format_value('', cnpj, cnpj_format=True)
                    icms_formatted = format_value('R$', icms)
                    pis_formatted = format_value('R$', pis)
                    cofins_formatted = format_value('R$', cofins)
                    ipi_formatted = format_value('R$', ipi)
                    total_nf_formatted = format_value('R$', total_nf)

                    nf_icon = QIcon("ui/images/plus.png")
                    # Adiciona a linha principal (nota fiscal)
                    emitente_item = QStandardItem(nf_icon, emitente)
                    cnpj_item = QStandardItem(cnpj_formatted)
                    num_nf_item = QStandardItem(str(num_nf) if num_nf is not None else "N/A")
                    modelo_nfe_item = QStandardItem(str(modelo_nfe) if modelo_nfe is not None else "N/A")
                    icms_item = QStandardItem(icms_formatted)
                    pis_item = QStandardItem(pis_formatted)
                    cofins_item = QStandardItem(cofins_formatted)
                    ipi_item = QStandardItem(ipi_formatted)
                    total_nf_item = QStandardItem(total_nf_formatted)
                    chave_nfe_item = QStandardItem(chave_nfe)
                    natureza_op_item = QStandardItem(natureza_op)

                    # Linha principal no modelo
                    row = [emitente_item, cnpj_item, num_nf_item, modelo_nfe_item, icms_item, pis_item, cofins_item, ipi_item, total_nf_item, chave_nfe_item, natureza_op_item]
                    model.appendRow(row)
                    #linhas pai --------------------------------------------------------------------------------------------------
                    # linhas filhas -----------------------------------------------------------------------------------------------------------------------------------------------------
                    # Obter o item principal (nota fiscal) onde os produtos serão adicionados como filhos
                    parent_item = model.item(model.rowCount() - 1)  # Última linha no modelo (linha principal da nota fiscal)

                    # Adiciona os cabeçalhos personalizados para as linhas filhas (produtos)
                    header_produtos = [
                        QStandardItem("Cód."), 
                        QStandardItem("Produto"), 
                        QStandardItem("CFOP"),
                        QStandardItem("NCM"), 
                        QStandardItem("CSOSN"), 
                        QStandardItem("UN"), 
                        QStandardItem("QUANT."), 
                        QStandardItem("V.Unitário"), 
                        QStandardItem("V.Total"), 
                        QStandardItem("CST ICMS"), 
                        QStandardItem("V.ICMS"), 
                        QStandardItem("CST IPI"), 
                        QStandardItem("V.IPI"), 
                        QStandardItem("CST PIS"), 
                        QStandardItem("V.PIS"), 
                        QStandardItem("V.COFINS"),
                        QStandardItem("T.TRIBUTOS")
                    ]

                    # Estiliza os cabeçalhos das linhas filhas (opcional)
                    for header_item in header_produtos:
                        header_item.setBackground(QColor(200, 200, 200))  # Cor de fundo cinza claro
                        header_item.setFont(QFont("Arial", 10, QFont.Bold))  # Fonte em negrito
                        header_item.setEditable(False)  # Impede edição do cabeçalho

                    # Adiciona os cabeçalhos como primeira linha filha
                    parent_item.appendRow(header_produtos)

                    # Obter os produtos e adicionar como linhas filhas
                    produtos = root.findall(f'.//{NAMESPACE}det')

                    for produto in produtos:
                        cod_prod = produto.find(f'.//{NAMESPACE}cProd')
                        descricao_produto = produto.find(f'.//{NAMESPACE}xProd')
                        ncm = produto.find(f'.//{NAMESPACE}NCM')
                        csosn = produto.find(f'.//{NAMESPACE}CSOSN')
                        cfop_produto = produto.find(f'.//{NAMESPACE}CFOP')
                        unidade = produto.find(f'.//{NAMESPACE}uCom')
                        qtda = produto.find(f'.//{NAMESPACE}qCom')
                        v_unit = produto.find(f'.//{NAMESPACE}vUnTrib')
                        v_total = produto.find(f'.//{NAMESPACE}vProd')
                        v_icms = produto.find(f'.//{NAMESPACE}ICMS/{NAMESPACE}vICMS')
                        cst_ipi = produto.find(f'.//{NAMESPACE}IPI/{NAMESPACE}IPITrib/{NAMESPACE}CST')
                        v_ipi = produto.find(f'.//{NAMESPACE}IPI/{NAMESPACE}IPITrib/{NAMESPACE}vIPI')
                        cst_pis = produto.find(f'.//{NAMESPACE}PIS/{NAMESPACE}PISOutr/{NAMESPACE}CST')
                        v_pis = produto.find(f'.//{NAMESPACE}PIS/{NAMESPACE}PISOutr/{NAMESPACE}vPIS')
                        v_cofins = produto.find(f'.//{NAMESPACE}COFINS/{NAMESPACE}COFINSOutr/{NAMESPACE}vCOFINS')
                        total_trib = produto.find(f'.//{NAMESPACE}imposto/{NAMESPACE}vTotTrib')


                        # Inicializa os valores padrão
                        cod_prod = cod_prod.text if cod_prod is not None else "N/A"
                        descricao_produto = descricao_produto.text if descricao_produto is not None else "N/A"
                        ncm = ncm.text if ncm is not None else "N/A"
                        csosn = csosn.text if csosn is not None else "N/A"
                        cfop_produto = cfop_produto.text if cfop_produto is not None else "N/A"
                        unidade = unidade.text if unidade is not None else "N/A"
                        qtda = qtda.text if qtda is not None else "0.000"
                        v_unit = v_unit.text if v_unit is not None else "R$0,00"
                        v_total = v_total.text if v_total is not None else "R$0,00"
                        v_icms = v_icms.text if v_icms is not None else "R$0,00"
                        cst_ipi = cst_ipi.text if cst_ipi is not None else "N/A"
                        v_ipi = v_ipi.text if v_ipi is not None else "R$0,00"
                        cst_pis = cst_pis.text if cst_pis is not None else "N/A"
                        v_pis = v_pis.text if v_pis is not None else "R$0,00"
                        v_cofins = v_cofins.text if v_cofins is not None else "R$0,00"
                        total_trib = total_trib.text if total_trib is not None else "R$0,00"
                        ncm_formatado = f"{ncm[4:]}.{ncm[4:6]}.{ncm[6:]}"
                        qtda_formatado = f"{float(qtda):.3f}"
                        # Verifica as possíveis tags de ICMS para encontrar CST dinamicamente
                        cst_icms = "N/A"  # Valor padrão caso nenhum CST seja encontrado
                        icms_node = produto.find(f'.//{NAMESPACE}ICMS')
                        if icms_node is not None:
                            for child in icms_node:
                                cst_tag = child.find(f'.//{NAMESPACE}CST')
                                if cst_tag is not None:
                                    cst_icms = cst_tag.text
                                    print(cst_icms)
                                    break  # Para no primeiro CST encontrado
                        icon_produto = QIcon('ui/images/product_icon.png')
                        # Cria os itens para as linhas filhas
                        codigo_prod = QStandardItem(icon_produto, cod_prod)
                        produto_item = QStandardItem(descricao_produto)
                        ncm_item = QStandardItem(ncm_formatado)
                        cfop_item = QStandardItem(cfop_produto)
                        csosn_item = QStandardItem(csosn)
                        unidade_item = QStandardItem(unidade)
                        qtda_item = QStandardItem(qtda_formatado)
                        v_unit_item = QStandardItem(v_unit)
                        v_total_item = QStandardItem(v_total)
                        cst_item = QStandardItem(cst_icms)
                        v_icms_item = QStandardItem(v_icms)
                        cst_ipi_item = QStandardItem(cst_ipi)
                        v_ipi_item = QStandardItem(v_ipi)
                        cst_pis_item = QStandardItem(cst_pis)
                        v_pis_item = QStandardItem(v_pis)
                        v_cofins_item = QStandardItem(v_cofins)
                        v_trib_item = QStandardItem(total_trib)

                        # Valores extraídos do XML
                        values = [
                            v_unit_item,
                            v_unit,
                            v_total,
                            v_icms,
                            v_ipi,
                            v_pis,
                            v_cofins,
                            total_trib
                        ]

                        # Formatar os valores
                        formatted_values = format_all_values(symbol='R$', values=values)

                        # Criar os itens da tabela usando os valores formatados                        # Criar os itens da tabela usando os valores formatados
                        v_unit_item = QStandardItem(formatted_values[0])
                        v_total_item = QStandardItem(formatted_values[1])
                        v_icms_item = QStandardItem(formatted_values[2])
                        v_ipi_item = QStandardItem(formatted_values[3])
                        v_pis_item = QStandardItem(formatted_values[4])
                        v_cofins_item = QStandardItem(formatted_values[5])
                        v_trib_item = QStandardItem(formatted_values[6])

                        # Criar a linha do produto
                        produto_row = [
                            codigo_prod,
                            produto_item,
                            cfop_item,
                            ncm_item,
                            csosn_item,
                            unidade_item,
                            qtda_item,
                            v_unit_item,
                            v_total_item,
                            cst_item,
                            v_icms_item,
                            cst_ipi_item,
                            v_ipi_item,
                            cst_pis_item,
                            v_pis_item,
                            v_cofins_item,
                            v_trib_item
                        ]

                        # Adicionar a linha como filha da linha principal
                        parent_item.appendRow(produto_row)

                    # linhas filhas -----------------------------------------------------------------------------------------------------------------------------------------------------

                    # Soma dos valores da nota fiscal
                    total_icms += icms
                    total_pis += pis
                    total_cofins += cofins
                    total_ipi += ipi
                    total_geral += total_nf

                except ET.ParseError as e:
                    print(f"Erro ao processar o arquivo XML '{xml_path}': {e}")
                except Exception as e:
                    print(f"Erro desconhecido ao processar o arquivo XML '{xml_path}': {e}")

        # Atualiza os totais no UI
        try:

            self.ui.txt_icms_xml.setText(format_value('R$', total_icms))
            self.ui.txt_pis_xml.setText(format_value('R$', total_pis))
            self.ui.txt_confins_xml.setText(format_value('R$', total_cofins))
            self.ui.txt_ipi_xml.setText(format_value('R$', total_ipi))
            self.ui.txt_totalNF_xml.setText(format_value('R$', total_geral))
        except Exception as e:
            print(f"Erro ao atualizar os campos: {e}")
        
        try:
            quebra_sequencias = self.quebra_sequencias(num_nf_list)
            # self.ui.label_qtda_xmls.setPlainText(str(len(num_nf_list)))
        except Exception as e:
            print(f"Nenhuma quebra de sequência identificada. {e}")


    #Apaga tudo que está impresso na tabela e inputs
    def clear_xml(self):
        # Limpa o modelo associado ao QTreeView
        if isinstance(self.ui.tableWidget_xml_list.model(), QStandardItemModel):
            self.ui.tableWidget_xml_list.model().clear()
        self.ui.txt_icms_xml.clear()
        self.ui.txt_pis_xml.clear()
        self.ui.txt_confins_xml.clear()
        self.ui.txt_ipi_xml.clear()
        self.ui.txt_totalNF_xml.clear()
        # self.ui.txt_totalTrib_xml.clear()

    # Função auxiliar para encontrar o XML com a chave da nota
    def encontrar_xml(self, chave_nota):
   
        if not hasattr(self, 'directory') or not self.directory:
            QMessageBox.warning(self, "Atenção", "Por favor, selecione o diretório dos XMLs primeiro.")
            return None
        
        # Busca pelo arquivo com a chave da nota na pasta dos XMLs
        for filename in os.listdir(self.directory):
            if chave_nota in filename and filename.endswith('.xml'):
                return os.path.join(self.directory, filename)
        
        return None

    def copiar_chave(self, chave_nota):
        """"Copia a chave da nota para o clipboard"""
        try:
            clipboard = QApplication.clipboard()
            clipboard.setText(chave_nota)
            QMessageBox.information(self, "Sucesso!", "Chave copiada!")

        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Ocorreu um erro ao copiar a chave: {e}")

    def gerar_danfe(self, chave_nota):
        caminho_xml = self.encontrar_xml(chave_nota)
        
        if not caminho_xml:
            QMessageBox.critical(self, "Erro", f"XML não encontrado para a chave: {chave_nota}")
            return

        try:
            with open(caminho_xml, 'r', encoding='utf-8') as file:
                xml_content = file.read()
                
            danfe = Danfe(xml=xml_content)  # Inicializa a geração do DANFE
            
            # Abre o diálogo de "Salvar Como" para salvar o DANFE em PDF
            file_path, _ = QFileDialog.getSaveFileName(
                None,                # Janela principal
                "Salvar DANFE",     # Título do diálogo
                f"Danfe_{chave_nota}", #Título do documento
                ""                  # Caminho padrão inicial (pode ser vazio)
                "PDF Files (*.pdf);;All Files (*)"  # Filtros de arquivo
            )

            # Verifica se um caminho foi selecionado
            if file_path:
                danfe.output(file_path)  # Salva o DANFE em PDF no local especificado
                QMessageBox.information(self, "Sucesso!", f"DANFE salvo com sucesso em {file_path}")
            else:
                QMessageBox.warning(self, "Atenção!", "Nenhum diretório selecionado. Não foi possível salvar o DANFE.")

        except Exception as e:
            print(e)
            QMessageBox.critical(self, "Erro", f"Ocorreu um erro ao gerar o DANFE: {e}")

    def show_context_menu_mde(self, position):
        context_menu_stylesheet = """
                                    QMenu {
                                        background-color:#264495;  /* Cor de fundo do menu */
                                        color: #ffffff;  /* Cor do texto */
                                        font: 700 10pt "Segoe UI";
                                        border: 2px solid #000000;  /* Cor da borda */
                                    }

                                    QMenu::item {
                                        background-color: transparent;
                                        padding: 8px 24px;  /* Espaçamento do item */
                                    }

                                    QMenu::item:selected {
                                        background-color: #5a5a5a;  /* Cor de fundo quando o item está selecionado */
                                    }
                                    """
        # Obtém o índice do item onde o clique ocorreu
        index = self.ui.tableWidget_xml_list.indexAt(position)

        if index.isValid():
            # Encontra o item na coluna 9, independentemente da coluna em que o clique ocorreu
            item = self.ui.tableWidget_xml_list.model().item(index.row(), 9)  # Coluna 9

            if item:
                chave_nota = item.text()  # Obtém o texto da chave da nota
                menu = QMenu(self.ui.tableWidget_xml_list)
                menu.setStyleSheet(context_menu_stylesheet)
                
                # Adiciona ações ao menu
                menu.addAction("Copiar Chave").triggered.connect(lambda: self.copiar_chave(chave_nota))
                menu.addAction("Imprimir DANFE").triggered.connect(lambda: self.gerar_danfe(chave_nota))
                
                # Exibe o menu no local do clique
                menu.exec(self.ui.tableWidget_xml_list.viewport().mapToGlobal(position))
            else:
                print("A célula clicada está vazia ou não existe")
        else:
            print("Índice inválido. Não foi clicado em um item válido.")

    def save_csv(self):
        # Caixa de diálogo para o usuário escolher o formato do arquivo
        formatos = "CSV Files (*.csv);;Excel Files (*.xlsx);;All Files (*)"
        file_path, selected_filter = QFileDialog.getSaveFileName(
            None,
            "Salvar Relatório",
            "relatorio_notas",
            formatos
        )

        # Verifica se um caminho foi selecionado
        if not file_path:
            QMessageBox.warning(None, "Atenção", "Nenhum diretório selecionado. O relatório não foi salvo.")
            return

        try:
            # Obtém o modelo associado ao QTreeView
            model = self.ui.tableWidget_xml_list.model()
            if model is None:
                QMessageBox.critical(None, "Erro", "Nenhum dado encontrado para salvar.")
                return

            row_count = model.rowCount()
            column_count = model.columnCount()

            if selected_filter == "CSV Files (*.csv)":
                # Adiciona a extensão .csv se o usuário não a colocou
                if not file_path.endswith(".csv"):
                    file_path += ".csv"

                # Salva como CSV
                with open(file_path, mode='w', newline='', encoding='utf-8') as file:
                    writer = csv.writer(file, delimiter=';')

                    # Escreve os cabeçalhos da tabela
                    headers = [model.headerData(col, Qt.Horizontal) for col in range(column_count)]
                    writer.writerow(headers)

                    # Escreve os dados da tabela
                    for row in range(row_count):
                        row_data = [
                            model.data(model.index(row, col)) if model.index(row, col).isValid() else ""
                            for col in range(column_count)
                        ]
                        writer.writerow(row_data)

                QMessageBox.information(None, "Sucesso", f"Relatório CSV salvo com sucesso em {file_path}")

            elif selected_filter == "Excel Files (*.xlsx)":
                # Adiciona a extensão .xlsx se o usuário não a colocou
                if not file_path.endswith(".xlsx"):
                    file_path += ".xlsx"

                # Salva como XLSX
                wb = Workbook()
                ws = wb.active
                ws.title = "Relatório de Notas"

                # Escreve os cabeçalhos da tabela
                headers = [model.headerData(col, Qt.Horizontal) for col in range(column_count)]
                ws.append(headers)

                # Escreve os dados da tabela
                for row in range(row_count):
                    row_data = [
                        model.data(model.index(row, col)) if model.index(row, col).isValid() else ""
                        for col in range(column_count)
                    ]
                    ws.append(row_data)

                # Salva o arquivo XLSX
                wb.save(file_path)
                QMessageBox.information(None, "Sucesso", f"Relatório XLSX salvo com sucesso em {file_path}")

        except Exception as e:
            import traceback
            print(f"Erro ao exportar o relatório: {e}")
            print(traceback.format_exc())
            QMessageBox.critical(None, "Erro", f"Ocorreu um erro ao salvar o relatório: {e}")

    def save_pdf(self):
        current_datetime = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        data = datetime.datetime.now().strftime("%d-%m-%Y")
        print(data)
        file_path, _ = QFileDialog.getSaveFileName(
            None,
            "Salvar Relatório PDF",
            f"Relatorio_notas-{data}.pdf",
            "PDF Files (*.pdf);;All Files (*)"
        )

        if not file_path:
            QMessageBox.warning(self, "Atenção", "Nenhum diretório selecionado. O relatório não foi salvo.")
            return

        try:
            print(f"Salvando PDF em: {file_path}")
            
            logo_path = "gui/img/logo_smartMigrate.png"

            c = canvas.Canvas(file_path, pagesize=landscape(A4))
            width, height = landscape(A4)

            headers = [
                ("EMITENTE", 15),
                ("CNPJ", 190),
                ("Nº", 270),
                ("Modelo", 315),
                ("ICMS", 370),
                ("PIS", 425),
                ("COFINS", 480),
                ("IPI", 535),
                ("TOTAL NF", 590),
                ("CHAVE", 655)
            ]

            def draw_headers(y_pos):
                c.setFont("Helvetica-Bold", 9)
                for header, x_pos in headers:
                    c.drawString(x_pos, y_pos - 10, header)

            logo_width, logo_height = 110, 20
            c.drawImage(logo_path, 10, height - 25, width=logo_width, height=logo_height, mask='auto')

            c.setFont("Helvetica-Bold", 12)
            c.drawString(10, height - 40, "Relatório de Notas Fiscais")
            c.setFont("Helvetica", 10)
            c.drawString(10, height - 55, f"Data e Hora: {current_datetime}")

            y_pos = height - 70
            row_height = 15

            draw_headers(y_pos)
            c.setLineWidth(0.5)
            c.setStrokeColorRGB(0, 0, 0)
            c.rect(10, y_pos - row_height, width - 20, row_height, stroke=1, fill=0)
            y_pos -= row_height

            page_num = 1

            model = self.ui.tableWidget_xml_list.model()
            if model is not None:
                for row in range(model.rowCount()):
                    c.setFont("Helvetica", 7)
                    for col, (header, x_pos) in enumerate(headers):
                        index = model.index(row, col)
                        text = model.data(index) if index.isValid() else ""
                        c.drawString(x_pos, y_pos - 10, text)

                    c.rect(10, y_pos - row_height, width - 20, row_height, stroke=1, fill=0)
                    y_pos -= row_height

                    if y_pos < 40:
                        c.showPage()
                        page_num += 1
                        y_pos = height - 65

                        c.drawImage(logo_path, 10, height - 25, width=logo_width, height=logo_height, mask='auto')
                        c.setFont("Helvetica-Bold", 12)
                        c.drawString(10, height - 40, "Relatório de Notas Fiscais")
                        c.setFont("Helvetica", 10)
                        c.drawString(10, height - 55, f"Data e Hora: {current_datetime}")
                        draw_headers(y_pos)
                        c.rect(10, y_pos - row_height, width - 20, row_height, stroke=1, fill=0)
                        y_pos -= row_height
                        c.setFont("Helvetica", 8)
                        c.drawString(width - 55, 20, f"Página {page_num}")

            c.setFont("Helvetica", 8)
            c.drawString(width - 55, 20, f"Página {page_num}")
            c.save()

            QMessageBox.information(self.ui, "Sucesso", f"Relatório PDF salvo com sucesso em {file_path}")

        except Exception as e:
            import traceback
            print("Erro ao exportar para PDF:")
            print(traceback.format_exc())
            QMessageBox.critical(
                self.ui,
                "Erro",
                f"Ocorreu um erro ao salvar o relatório PDF: {e}",
                QMessageBox.Ok
            )

    def quebra_sequencias(self,sequencias):
        lista = []
        for i in range(len(sequencias) - 1):
            if sequencias[i + 1] != sequencias[i] + 1:
                faltando = range(sequencias[i] + 1, sequencias[i + 1])
                lista.extend(faltando)
        return lista

    def filter_table_xml(self):
            # Obtém o texto da pesquisa
            pesquisa = self.ui.txt_pesquisa_table_xml.text().lower().strip()

            # Obtém o modelo do QTreeView
            model = self.ui.tableWidget_xml_list.model()
            if not model:
                return  # Sai se não houver modelo

            def search_in_item(item, pesquisa):
                """Função auxiliar para verificar se o item contém o texto de pesquisa"""
                if item and item.text():
                    return pesquisa in item.text().lower()
                return False

            def search_in_row(row, pesquisa, parent_index=None):
                """Função auxiliar para verificar se uma linha (ou suas filhas) contém a pesquisa"""
                row_match = False
                row_count = model.rowCount(parent_index) if parent_index is not None else model.rowCount()
                col_count = model.columnCount(parent_index) if parent_index is not None else model.columnCount()

                for col in range(col_count):
                    if parent_index is None:
                        item = model.item(row, col)
                    else:
                        item_index = model.index(row, col, parent_index)
                        item = model.itemFromIndex(item_index)
                    if search_in_item(item, pesquisa):
                        return True

                for child_row in range(row_count):
                    child_index = model.index(child_row, 0, parent_index) if parent_index is not None else model.index(child_row, 0)
                    child_item = model.itemFromIndex(child_index)
                    if child_item and search_in_row(child_row, pesquisa, child_index):
                        return True

                return False

            for row in range(model.rowCount()):
                row_match = search_in_row(row, pesquisa, parent_index=None)
                self.ui.tableWidget_xml_list.setRowHidden(row, not row_match, model.index(row, 0))



class TablesClienteContabil:
    def __init__(self, parent=None):
        self.parent = parent  # Referência ao WindowPrincipal
        self.current_row = -1
        # Caminho base para o diretório do projeto
        self.base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        self.icon_path = os.path.join(self.base_path, "ui", "icons", "edit.png")
        print(self.icon_path)

    def tool_button(self, table, action):
            for row in range(table.rowCount()):
                button = QToolButton()
                # Carregar e verificar o ícone
                icon = QIcon(self.icon_path)
                if icon.isNull():
                    print(f"Erro: Não foi possível carregar o ícone em {self.icon_path}")
                button.setIcon(icon)
                button.setMinimumSize(QSize(30, 30))
                button.setMaximumSize(QSize(30, 30))
                button.setIconSize(QSize(20, 20))  # Tamanho do ícone
                button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
                button.setText("")  # Manter texto, ou use "" para apenas ícone
                button.setToolTip("Editar cliente")  # Dica ao passar o mouse
                button.clicked.connect(lambda checked, r=row: action(r))
                table.setCellWidget(row, table.columnCount() - 1, button)

    def table_cliente_contabilidade(self, table, data, action):
        if data:
            table.setRowCount(len(data))
            action_col = table.columnCount() - 1

            for row_idx, row_data in enumerate(data):
                for col_idx, col_data in enumerate(row_data):
                    if col_idx < action_col:
                        table.setItem(row_idx, col_idx, QTableWidgetItem(str(col_data)))
            
            # Chamar tool_button uma vez, após preencher todas as linhas
            self.tool_button(table=table, action=action)

    def show_edit_frame(self, row):
            """Exibe o frame de cadastro preenchido com os dados da linha selecionada"""
            self.current_row = row
            # Exibir o frame frm_cadastro_cliente
            self.parent.frm_cadastro_cliente.setVisible(True)

            # Preencher os campos do frame com os dados da linha
            headers = [self.parent.table_clientes.horizontalHeaderItem(col).text().lower() 
                    for col in range(self.parent.table_clientes.columnCount() - 1)]
            for col in range(len(headers)):
                item = self.parent.table_clientes.item(row, col)
                value = item.text() if item else ""
                
                # Mapear cabeçalhos para campos do frm_cadastro_cliente
                if headers[col] == "nome":
                    self.parent.txt_nome_cliente.setText(value)
                elif headers[col] == "razao social":
                    self.parent.txt_razao_social_cliente.setText(value)
                elif headers[col] == "cnpj":
                    self.parent.txt_cnpj_cliente.setText(value)
                elif headers[col] == "email":
                    self.parent.txt_email_cliente.setText(value)
                elif headers[col] == "id_contador":
                    # Selecionar o contador correspondente no combo_contador
                    id_contador = int(value) if value.isdigit() else 0
                    for i in range(self.parent.combo_contador.count()):
                        if self.parent.combo_contador.itemData(i) == id_contador:
                            self.parent.combo_contador.setCurrentIndex(i)
                            break
                elif headers[col] == "sistema":
                    self.parent.combo_sistema_cliente.setCurrentText(value)
                elif headers[col] == "link_sistema":
                    self.parent.txt_link_sistema_cliente.setText(value)
                elif headers[col] == "user_sistema":
                    self.parent.txt_user_cliente_sistema.setText(value)
                elif headers[col] == "senha_sistema":
                    self.parent.txt_password_cliente_sistema.setText(value)