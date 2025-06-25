from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import (
    QIcon,
    QFont,
    QColor,
    QStandardItem,
    QStandardItemModel,
    QCursor,
)
from PySide6 import QtCore
from PySide6.QtWidgets import (
    QApplication,
    QMessageBox,
    QFileDialog,
    QMenu,
    QMenu,
    QToolButton,
    QTableWidgetItem,
)
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
import time

ui = app_instance.get_ui_instance()


def save_csv(parent:None):
    ui = app_instance.get_ui_instance()
    # Caixa de diálogo para o usuário escolher o formato do arquivo
    formatos = "CSV Files (*.csv);;Excel Files (*.xlsx);;All Files (*)"
    file_path, selected_filter = QFileDialog.getSaveFileName(
        None, "Salvar Relatório", "relatorio_notas", formatos
    )

    # Verifica se um caminho foi selecionado
    if not file_path:
        QMessageBox.warning(
            None, "Atenção", "Nenhum diretório selecionado. O relatório não foi salvo."
        )
        return

    try:
        # Obtém o modelo associado ao QTreeView
        model = ui.tableWidget_xml_list.model()
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
            with open(file_path, mode="w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file, delimiter=";")

                # Escreve os cabeçalhos da tabela
                headers = [
                    model.headerData(col, Qt.Horizontal) for col in range(column_count)
                ]
                writer.writerow(headers)

                # Escreve os dados da tabela
                for row in range(row_count):
                    row_data = [
                        (
                            model.data(model.index(row, col))
                            if model.index(row, col).isValid()
                            else ""
                        )
                        for col in range(column_count)
                    ]
                    writer.writerow(row_data)

            QMessageBox.information(
                None, "Sucesso", f"Relatório CSV salvo com sucesso em {file_path}"
            )

        elif selected_filter == "Excel Files (*.xlsx)":
            # Adiciona a extensão .xlsx se o usuário não a colocou
            if not file_path.endswith(".xlsx"):
                file_path += ".xlsx"

            # Salva como XLSX
            wb = Workbook()
            ws = wb.active
            ws.title = "Relatório de Notas"

            # Escreve os cabeçalhos da tabela
            headers = [
                model.headerData(col, Qt.Horizontal) for col in range(column_count)
            ]
            ws.append(headers)

            # Escreve os dados da tabela
            for row in range(row_count):
                row_data = [
                    (
                        model.data(model.index(row, col))
                        if model.index(row, col).isValid()
                        else ""
                    )
                    for col in range(column_count)
                ]
                ws.append(row_data)

            # Salva o arquivo XLSX
            wb.save(file_path)
            QMessageBox.information(
                None, "Sucesso", f"Relatório XLSX salvo com sucesso em {file_path}"
            )

    except Exception as e:
        import traceback

        print(f"Erro ao exportar o relatório: {e}")
        print(traceback.format_exc())
        QMessageBox.critical(
            None, "Erro", f"Ocorreu um erro ao salvar o relatório: {e}"
        )


def save_pdf(parent:None ):
    ui = app_instance.get_ui_instance()
    current_datetime = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    data = datetime.datetime.now().strftime("%d-%m-%Y")
    print(data)
    file_path, _ = QFileDialog.getSaveFileName(
        None,
        "Salvar Relatório PDF",
        f"Relatorio_notas-{data}.pdf",
        "PDF Files (*.pdf);;All Files (*)",
    )

    if not file_path:
        QMessageBox.warning(
            "Atenção", "Nenhum diretório selecionado. O relatório não foi salvo."
        )
        return

    try:
        print(f"Salvando PDF em: {file_path}")

        logo_path = "ui/icons/logo_smartMigrate.png"

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
            ("CHAVE", 655),
        ]

        def draw_headers(y_pos):
            c.setFont("Helvetica-Bold", 9)
            for header, x_pos in headers:
                c.drawString(x_pos, y_pos - 10, header)

        logo_width, logo_height = 110, 20
        c.drawImage(
            logo_path,
            10,
            height - 25,
            width=logo_width,
            height=logo_height,
            mask="auto",
        )

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

        model = ui.tableWidget_xml_list.model()
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

                    c.drawImage(
                        logo_path,
                        10,
                        height - 25,
                        width=logo_width,
                        height=logo_height,
                        mask="auto",
                    )
                    c.setFont("Helvetica-Bold", 12)
                    c.drawString(10, height - 40, "Relatório de Notas Fiscais")
                    c.setFont("Helvetica", 10)
                    c.drawString(10, height - 55, f"Data e Hora: {current_datetime}")
                    draw_headers(y_pos)
                    c.rect(
                        10, y_pos - row_height, width - 20, row_height, stroke=1, fill=0
                    )
                    y_pos -= row_height
                    c.setFont("Helvetica", 8)
                    c.drawString(width - 55, 20, f"Página {page_num}")

        c.setFont("Helvetica", 8)
        c.drawString(width - 55, 20, f"Página {page_num}")
        c.save()

        QMessageBox.information(
            ui, "Sucesso", f"Relatório PDF salvo com sucesso em {file_path}"
        )

    except Exception as e:
        import traceback

        print("Erro ao exportar para PDF:")
        print(traceback.format_exc())
        QMessageBox.critical(
            ui,
            "Erro",
            f"Ocorreu um erro ao salvar o relatório PDF: {e}",
            QMessageBox.Ok,
        )


