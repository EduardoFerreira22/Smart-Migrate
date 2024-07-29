from PySide6.QtCore import QCoreApplication,QUrl,QTimer,Qt
from PySide6.QtGui import QIcon,QFont,QColor,QDesktopServices
from PySide6 import QtCore
from PySide6.QtWidgets import (QApplication,QMainWindow,QMessageBox,QProgressBar,QDialog, QVBoxLayout, QPushButton,QTableWidgetItem,QFileDialog,QMenu, QWidgetAction,
                               QPlainTextEdit, QPushButton, QVBoxLayout, QWidget, QSystemTrayIcon, QMenu)

from gui.ui_ui_main import Ui_MainWindow
import gui.app_instance as app_instance

from conections.db_conect import conectar_ao_sql_server, conectar_ao_MySQL, conectar_ao_PostgreSQL, populate_tree_view_with_tables_and_columns, tables_SqlServer, tables_MySQL, tables_PostgreSQL, tables_SQLite3, close_connections
from files_csv.csv_functions import save_data_to_csv,analise_inteligente

import csv

class WindowPrincipal(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(WindowPrincipal, self).__init__()
        self.setupUi(self)
        app_instance.set_ui_instance(self)  # Configure a instância
        self.setWindowTitle("Smart Migrate")


        #ocultos tabs
        self.widget_right.setVisible(False)
        self.tabs_lateral_right.setVisible(False)
        self.frame_func_duplicados.setVisible(False)
        self.frame_10.setVisible(False) #frame dos botões de dados duplicados
        self.label_3.setVisible(False)
        self.bt_salvar_dados_tabela_principal.setVisible(False)


        self.bt_buscar_sqlite.setVisible(False)
        self.txt_port_data_base.setVisible(False)

        #buttons
        
        self.combo_data_base_list.currentIndexChanged.connect(self.select_datas)
        self.bt_mostra_dados_tabelas.clicked.connect(self.show_table_data)
        self.bt_salvar_dados_tabela_principal.clicked.connect(save_data_to_csv)
        self.txt_pesquisar_tabela.textChanged.connect(self.filter_and_update_tree_view)


        #Buttons Menu
        self.bt_buscar_sqlite.clicked.connect(self.buscar_file_sqlite)
        self.bt_conectar_data_base.clicked.connect(self.conect_data)

        #botões menu bar
        self.bt_pesquisar_dados.setVisible(False)
        self.bt_processamento_dados.setVisible(False)

        #Botões barra lateral (Conexões, Sistemas, Scripts)
        self.bt_terminal_sql.setVisible(False)
        self.bt_systems.setVisible(False)
        self.bt_duplicados.setVisible(False)

        #opções de busca e processamento
        self.widget_functions_table.setVisible(False)
        #opções de Busca
        self.page_opcoes_busca.setVisible(False)
        self.page_buscar_ncm.setVisible(False)
        self.page_ncm_invalido.setVisible(False)
        self.page_op_busca_dados_duplicados.setVisible(False)
        self.page_tudo_que_contem.setVisible(False)
        self.txt_opcoes_busca.setVisible(False)
        self.bt_buscar_op_busca.setVisible(False)
        

        #Opções de Processamento
        self.page_opcoes_processamento.setVisible(False)
        self.page_colunaA_colunaB_recebe.setVisible(False)
        self.page_extrair_duplicados.setVisible(False)
        self.page_filtrar_coluna_linhas_contem.setVisible(False)
        self.page_substituir_ncm.setVisible(False)
        self.txt_opcao1_processamento.setVisible(False)
        self.txt_opcao2_processamento.setVisible(False)
        self.combo1_colunas_processamento.setVisible(False)
        self.combo2_colunas_processamento.setVisible(False)
        self.bt_processamento_de_para.setVisible(False)
        self.bt_extrair_duplicados.setVisible(False)
 
        self.setup_connections()
        self.setup_execut_opcoes()

    #MOSTRA UM POPUP DE NOTIFICAÇÃO DE ERRO 
    def show_error_popup(self, title, message):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setIcon(QMessageBox.Warning)
        msg.exec()

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

        if self.table_principal.rowCount() > 0 or self.table_principal.columnCount() > 0 or self.widget_right.isVisible():
            reply = QMessageBox.question(self, 'Salvar Dados', 
                                         "A tabela contém dados. Deseja salvar antes de continuar?",
                                         QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel,
                                         QMessageBox.Cancel)
            if reply == QMessageBox.Yes:
                self.widget_right.setVisible(False)
                self.limpar_tabela_principal()  # Limpa a tabela após salvar
                close_connections()
                buscar = self.buscar_arquivo()
                self.load_csv_to_table(buscar, self.table_principal)
                self.txt_output_logs.setPlainText(f"Caminho do arquivo selecionado: {buscar}")
            elif reply == QMessageBox.No:
                self.widget_right.setVisible(False)
                self.limpar_tabela_principal()  # Limpa a tabela
                close_connections()
                buscar = self.buscar_arquivo()
                self.load_csv_to_table(buscar, self.table_principal)
                self.txt_output_logs.setPlainText(f"Caminho do arquivo selecionado: {buscar}")
        else:
            self.widget_right.setVisible(False)
            close_connections()
            buscar = self.buscar_arquivo()  # Abre o diálogo de arquivo se a tabela estiver vazia
            self.load_csv_to_table(buscar, self.table_principal)
            self.txt_output_logs.setPlainText(f"Caminho do arquivo selecionado: {buscar}")

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
                self.txt_output_logs.setPlainText("Planilha processada com encondig: UTF-8")
        except UnicodeDecodeError:
            with open(file_path, newline='', encoding='latin1', errors='replace') as csvfile:
                reader = csv.reader(csvfile, delimiter=';')
                all_data = list(reader)
                self.txt_output_logs.setPlainText("Planilha processada com encondig: Latin1")

        self.load_data_table(data=all_data,table=table)
        self.bt_pesquisar_dados.setVisible(True)
        self.bt_processamento_dados.setVisible(True)

    def load_data_table(self, data, table):
        all_data = data
        if all_data:
            headers = all_data[0]
            rows = all_data[1:]
            
            table.setColumnCount(len(headers))
            table.setRowCount(len(rows))
            table.setHorizontalHeaderLabels(headers)
            
            for row_idx, row_data in enumerate(rows):
                for col_idx, col_data in enumerate(row_data):
                    # Converte col_data para string, se não for uma string já
                    col_data_str = str(col_data) if col_data is not None else ""
                    table.setItem(row_idx, col_idx, QTableWidgetItem(col_data_str))

            
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

    #lista todos os bancos de dados - OBS: adptar para usar em todos SGBDS
    """
    def list_DataBases(self):
        try:
            self.conn1.cursor.execute("SELECT name FROM sys.databases WHERE database_id > 4")
            databases = [database[0] for database in self.conn1.cursor.fetchall()]
            print(databases)
            return databases
        except Exception as err:
            self.log.logs(name_file=self.file_name,path=self.path_logs,msg=f"Erro ao conectar ao SQL Server: {err}")
            print("Erro ao conectar ao SQL Server:", err)
            return []
    """
    def query_table_list(self, table):
        selected_data = self.combo_data_base_list.currentText()
        conn = self.get_current_connection()

        try:
            if selected_data == 'SQL Server' and conn:
                query_value = f"""SELECT * FROM [{table}]"""
                conn.cursor.execute(query_value)
                resp = conn.cursor.fetchall()
                column_names = [column[0] for column in conn.cursor.description]
            
            elif selected_data == 'MySQL' and conn:
                query_value = f"""SELECT * FROM {table};"""
                conn.cursor.execute(query_value)
                resp = conn.cursor.fetchall()
                column_names = conn.cursor.column_names
            
            elif selected_data == 'PostgreSQL' and conn:
                query_value = f"""SELECT * FROM {table};"""
                conn.cursor.execute(query_value)
                resp = conn.cursor.fetchall()
                column_names = [desc[0] for desc in conn.cursor.description]
            
            elif selected_data == 'SQLite' and conn:
                query_value = f"SELECT * FROM {table};"
                conn.cursor.execute(query_value)
                resp = conn.cursor.fetchall()
                column_names = [column[0] for column in conn.cursor.description]
            
            else:
                self.show_error_popup("Erro", "Nenhuma conexão ativa encontrada.")
                return None, None

            return resp, column_names

        except Exception as e:
            self.show_error_popup("Erro", str(e))
            print(e)
            return None, None
  
    def get_current_connection(self):
        selected_data = self.combo_data_base_list.currentText()
        if selected_data == 'SQL Server':
            return conectar_ao_sql_server()
        elif selected_data == 'MySQL':
            return conectar_ao_MySQL()
        elif selected_data == 'PostgreSQL':
            return conectar_ao_PostgreSQL()
        else:
            return None

    def show_table_data(self):
        selected_table = self.treeView_lista_tabelas.currentIndex().data()
        if selected_table:
            data, headers = self.query_table_list(selected_table)
            if data and headers:
                self.load_data_table([headers] + data, self.table_principal)
                self.bt_salvar_dados_tabela_principal.setVisible(True)
            else:
                self.show_error_popup("Erro", "Não foi possível carregar os dados da tabela.")
        else:
            self.show_error_popup("Erro", "Nenhuma tabela selecionada.")

    #Filtra pesquisa por tabela
    def filter_and_update_tree_view(self):
        conn = self.get_current_connection()
        search_text = self.txt_pesquisar_tabela.text().lower()

        # Obtenha todas as tabelas disponíveis
        selected_data = self.combo_data_base_list.currentText()
        if selected_data == 'SQL Server':
            tables = tables_SqlServer(conn)  # Obtém a lista de tabelas
        elif selected_data == 'MySQL':
            tables = tables_MySQL(conn)
        elif selected_data == 'PostgreSQL':
            tables = tables_PostgreSQL(conn)
        elif selected_data == 'SQLite':
            tables = tables_SQLite3(conn)
        else:
            tables = []

        filtered_tables = [table for table in tables if search_text in table[0].lower()]

        # Atualize a treeView_lista_tabelas
        populate_tree_view_with_tables_and_columns(filtered_tables, conn)

    def setup_execut_opcoes(self):
        self.comboBox_opcoes_busca.currentIndexChanged.connect(lambda: self.executa_fucoes_Opcoes('Analise inteligente'))
    # conecta função de opções dos botões
    def setup_connections(self):
        # Conecte os sinais de clique dos botões à função mostrar_opcoes
        self.bt_pesquisar_dados.clicked.connect(lambda: self.mostrar_opcoes("pesquisar"))
        self.bt_processamento_dados.clicked.connect(lambda: self.mostrar_opcoes("processar"))
        self.bt_conexoes_banco_dados.clicked.connect(lambda: self.mostrar_opcoes("conexoes"))
        self.bt_buscar_csv.clicked.connect(self.buscar_csv)

    def limpar_tabela_principal(self):
        self.table_principal.clear()  # Limpa o conteúdo da tabela
        self.table_principal.setRowCount(0)  # Redefine o número de linhas para zero
        self.table_principal.setColumnCount(0)  # Redefine o número de colunas para zero
    
    def mostrar_opcoes(self, acao):
        if acao == "pesquisar":
            self.widget_functions_table.setVisible(True)
            self.page_opcoes_busca.setVisible(True)
            self.page_opcoes_processamento.setVisible(False)
        elif acao == "processar":
            self.widget_functions_table.setVisible(True)
            self.page_opcoes_busca.setVisible(False)
            self.page_opcoes_processamento.setVisible(True)
            self.frame_info_opcoes_processamento.setVisible(False)
        elif acao == "conexoes":
            if self.table_principal.rowCount() > 0:
                reply = QMessageBox.question(self, 'Salvar Dados', 
                                             "A tabela contém dados. Deseja salvar antes de continuar?",
                                             QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel,
                                             QMessageBox.Cancel)
                if reply == QMessageBox.Yes:
                    save_data_to_csv()
                    self.limpar_tabela_principal()  # Limpa a tabela após salvar
                    self.mostrar_conexoes()
                elif reply == QMessageBox.No:
                    self.limpar_tabela_principal()  # Limpa a tabela
                    self.mostrar_conexoes()
            else:
                self.mostrar_conexoes()

    def mostrar_conexoes(self):
        self.widget_functions_table.setVisible(False)
        self.widget_right.setVisible(True)
        self.tabs_lateral_right.setVisible(True)
        self.bt_mostra_dados_tabelas.setVisible(False)
        self.label_4.setVisible(False)
        if self.table_principal is not None:
            self.bt_salvar_dados_tabela_principal.clicked.connect(save_data_to_csv)
    
    def executa_fucoes_Opcoes(self, acao):
        
        #OPÇÕES DE BUSCA
        if acao == 'Analise inteligente':
            self.txt_analise_inteligente_output.setVisible(True)
            analise_inteligente()
        elif acao == 'Buscar por NCM':
            ...
        elif acao == 'NCM Inválido':
            ...
        elif acao == 'Tudo que contém':
            ...
        elif acao == 'Duplicados':
            ...

        # OPÇÕES DE PROCESSAMENTO
        elif acao == 'Substituir NCM':
            ...
        elif acao == 'Tudo que contém mude para':
            ...
        elif acao == 'Se Coluna A contém, Coluna B recebe...':
            ...
        elif acao == 'Filtrar por coluna e copiar todas a linhas que contenham':
            ...
        elif acao == 'Extrair dados duplicados da tabela':
            ...



if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)  # Crie a instância de QApplication
    window = WindowPrincipal()
    window.show()
    sys.exit(app.exec())  # Execute o loop de eventos e finalize o programa corretamente

