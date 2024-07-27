from PySide6.QtCore import QCoreApplication,QUrl,QTimer,Qt
from PySide6.QtGui import QIcon,QFont,QColor,QDesktopServices
from PySide6 import QtCore
from PySide6.QtWidgets import (QApplication,QMainWindow,QMessageBox,QProgressBar,QDialog, QVBoxLayout, QPushButton,QTableWidgetItem,QFileDialog,QMenu, QWidgetAction,
                               QPlainTextEdit, QPushButton, QVBoxLayout, QWidget, QSystemTrayIcon, QMenu)

from gui.ui_ui_main import Ui_MainWindow
import gui.app_instance as app_instance
from conections.db_conect import conectar_ao_sql_server, conectar_ao_MySQL, conectar_ao_PostgreSQL

import csv

class WindowPrincipal(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(WindowPrincipal, self).__init__()
        self.setupUi(self)
        app_instance.set_ui_instance(self)  # Configure a instância
        self.setWindowTitle("Tech Tools")


        #ocultos tabs
        self.widget_right.setVisible(False)
        self.tabs_lateral_right.setVisible(False)
        self.frame_func_duplicados.setVisible(False)
        self.frame_10.setVisible(False) #frame dos botões de dados duplicados
        self.label_3.setVisible(False)

        
        self.tab_lista_tabelas_db.setVisible(False)
        self.bt_buscar_sqlite.setVisible(False)
        self.txt_port_data_base.setVisible(False)

        #buttons
        self.bt_conexoes_banco_dados.clicked.connect(self.show_conections)
        self.combo_data_base_list.currentIndexChanged.connect(self.select_datas)

        #Buttons Menu
        self.bt_buscar_csv.clicked.connect(self.buscar_csv)
        self.bt_buscar_sqlite.clicked.connect(self.buscar_file_sqlite)
        self.bt_conectar_data_base.clicked.connect(self.conect_data)
    

    #MOSTRA UM POPUP DE NOTIFICAÇÃO DE ERRO 
    def show_error_popup(self, title, message):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setIcon(QMessageBox.Warning)
        msg.exec()

    def show_conections(self):
        self.widget_right.setVisible(True)
        self.tabs_lateral_right.setVisible(True)
        self.tab_lista_tabelas_db.setVisible(True)
        self.bt_mostra_dados_tabelas.setVisible(False)
        self.label_4.setVisible(False)

    def show_tab_dados_duplicados(self):
        self.frame_func_duplicados.setVisible(True)
        self.frame_10.setVisible(True) #frame dos botões de dados duplicados
        self.label_3.setVisible(True)

    def buscar_arquivo(self):
        selected_data = self.combo_data_base_list.currentText()
        self.txt_output_logs.setPlainText("Buscando novo arquivo.")
        #Abre um diálogo de seleção de arquivos
        if selected_data == 'SQLite':
            # Abre um diálogo de seleção de arquivo
            file_dialog = QFileDialog()
            file_dialog.setFileMode(QFileDialog.ExistingFile)
            file_dialog.setNameFilter("Banco de Dados SQLite (*.db *.sqlite *.sqlite3);;Todos os Arquivos (*)")

        else:
            file_dialog = QFileDialog()
            file_dialog.setFileMode(QFileDialog.ExistingFile)
            file_dialog.setNameFilter("Arquivo CSV UTF-8 (*.csv);;CSV separado por vírgula (*.csv)")

        if file_dialog.exec():
            #Obtém o caminho do arquivo selecionado
            file = file_dialog.selectedFiles()[0]
            
            # Carrega o arquivo CSV na tabela
            # self.load_csv_to_table(selected_file, self.table_principal)
            return file
        
    def buscar_csv(self):
        buscar = self.buscar_arquivo()
        self.load_csv_to_table(buscar, self.table_principal)
        self.txt_output_logs.setPlainText(f"Caminho do arquivo selecionado:{buscar}")

    def buscar_file_sqlite(self):
        buscar = self.buscar_arquivo()
        self.txt_servidor_data_base.setText(buscar)
        self.txt_output_logs.setPlainText(f"Caminho do arquivo selecionado:{buscar}")
        self.bt_buscar_sqlite.setVisible(False)
        self.bt_conectar_data_base.setVisible(True)

    def load_csv_to_table(self, file_path, table):
        try:
            with open(file_path, newline='', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile, delimiter=';')
                all_data = list(reader)
        except UnicodeDecodeError:
            with open(file_path, newline='', encoding='latin1', errors='replace') as csvfile:
                reader = csv.reader(csvfile, delimiter=';')
                all_data = list(reader)

        if all_data:
            headers = all_data[0]
            rows = all_data[1:]
            
            table.setColumnCount(len(headers))
            table.setRowCount(len(rows))
            table.setHorizontalHeaderLabels(headers)
            
            for row_idx, row_data in enumerate(rows):
                for col_idx, col_data in enumerate(row_data):
                    table.setItem(row_idx, col_idx, QTableWidgetItem(col_data))

    #SELECIONA A OPÇÃO DE CONEXÃO DE BANCO DE DADOS NO COMBOBOX DA PÁGINA CONEXÕES
    def select_datas(self):

        selected_data = self.combo_data_base_list.currentText()

        # Verifica se a opção selecionada é 'Firebird'
        if selected_data == 'SQLite':
            # Se for 'Firebird', torna os elementos visíveis
            self.txt_output_logs.setPlainText("Opção SQLite selecionado com sucesso!")
            self.bt_conectar_data_base.setVisible(False)
            self.bt_buscar_sqlite.setVisible(True)
            self.txt_user_data_base.setVisible(False)
            self.txt_password_data_base.setVisible(False)
            self.txt_data_base_name.setVisible(False)
            self.txt_port_data_base.setVisible(False)

        else:
            # Caso contrário, torna os elementos invisíveis
            self.bt_buscar_sqlite.setVisible(True)
            self.bt_conectar_data_base.setVisible(False)

        if selected_data == 'PostgreSQL':
            self.txt_output_logs.setPlainText("Opção PostgreSQL selecionado com sucesso!")
            self.bt_conectar_data_base.setVisible(True)
            self.bt_buscar_sqlite.setVisible(False)
            self.txt_user_data_base.setVisible(True)
            self.txt_password_data_base.setVisible(True)
            self.txt_data_base_name.setVisible(True)
            self.txt_port_data_base.setVisible(True)


        elif selected_data == 'MySQL':
            self.txt_output_logs.setPlainText("Opção MySQL selecionado com sucesso!")
            self.bt_conectar_data_base.setVisible(True)
            self.bt_buscar_sqlite.setVisible(False)
            self.txt_user_data_base.setVisible(True)
            self.txt_password_data_base.setVisible(True)
            self.txt_data_base_name.setVisible(True)
            self.txt_port_data_base.setVisible(True)

        elif selected_data == 'SQL Server':
            self.txt_output_logs.setPlainText("Opção SQL Server selecionado com sucesso!")
            self.bt_conectar_data_base.setVisible(True)
            self.bt_buscar_sqlite.setVisible(False)
            self.txt_user_data_base.setVisible(True)
            self.txt_password_data_base.setVisible(True)
            self.txt_data_base_name.setVisible(True)
            self.txt_port_data_base.setVisible(False)

    def conect_data(self):
        selected_data = self.combo_data_base_list.currentText()

        if self.bt_conectar_data_base and selected_data == 'SQL Server':
            conectar_ao_sql_server()

        elif self.bt_conectar_data_base and selected_data == 'MySQL':
            conectar_ao_MySQL()

        elif self.bt_conectar_data_base and selected_data == 'PostgreSQL':
            conectar_ao_PostgreSQL()
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)  # Crie a instância de QApplication
    window = WindowPrincipal()
    window.show()
    sys.exit(app.exec())  # Execute o loop de eventos e finalize o programa corretamente

