from PySide6.QtCore import QCoreApplication,QUrl,QTimer,Qt
from PySide6.QtGui import QIcon,QFont,QColor,QDesktopServices
from PySide6 import QtCore
from PySide6.QtWidgets import (QApplication,QMainWindow,QMessageBox,QProgressBar,QDialog, QVBoxLayout, QPushButton,QTableWidgetItem,QFileDialog,QMenu, QWidgetAction,
                               QPlainTextEdit, QPushButton, QVBoxLayout, QWidget, QSystemTrayIcon, QMenu)

from gui.ui_ui_main import Ui_MainWindow
import gui.app_instance as app_instance

from conections.db_conect import View_DBF, conectar_ao_sql_server, conectar_ao_MySQL, conectar_ao_PostgreSQL, conectar_Sqlite3, conectar_ao_Firebird, populate_tree_view_with_tables_and_columns, tables_SqlServer, tables_MySQL, tables_PostgreSQL, tables_SQLite3, tables_Firebird, close_connections
import  files_csv.csv_functions as csv_file
from configs.dictionares import configurar_interface, configurar_busca_interface, configurar_interface_banco_de_dados, adicionar_opcoes, remover_opcoes
import socket
import csv

def get_host_name():
    hostname = socket.gethostname()
    return hostname

class WindowPrincipal(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(WindowPrincipal, self).__init__()
        self.setupUi(self)
        app_instance.set_ui_instance(self)  # Configure a instância
        self.setWindowTitle("Smart Migrate")
        self.nome_computador = get_host_name()
        self.setup_connections()
        self.setup_execut_opcoes()
        self.setup_execut_processamento()



        #ocultos tabs
        self.widget_right.setVisible(False)
        self.tabs_lateral_right.setVisible(False)
        self.bt_salvar_dados_tabela_principal.setVisible(False)
        self.bt_conections.clicked.connect(lambda: self.tabs_lateral_right.setCurrentWidget(self.page_conections))
        self.bt_terminal_sql.clicked.connect(lambda: self.tabs_lateral_right.setCurrentWidget(self.page_terminal_sql))
        self.bt_systems.clicked.connect(lambda: self.tabs_lateral_right.setCurrentWidget(self.page_systems))
        self.bt_duplicados.clicked.connect(lambda: self.tabs_lateral_right.setCurrentWidget(self.page_duplicados))


        self.bt_buscar_sqlite.setVisible(False)
        self.txt_port_data_base.setVisible(False)

        #buttons
        
        self.combo_data_base_list.currentIndexChanged.connect(self.select_datas)
        self.bt_mostra_dados_tabelas.clicked.connect(self.show_table_data)
        self.bt_salvar_dados_tabela_principal.clicked.connect(csv_file.save_data_to_csv)
        self.txt_pesquisar_tabela.textChanged.connect(self.filter_and_update_tree_view)


        # Conecte os botões
        self.bt_add_opcoes2.clicked.connect(adicionar_opcoes)
        self.bt_add_opcoes3.clicked.connect(adicionar_opcoes)
        self.bt_retirar_opcoes2.clicked.connect(remover_opcoes)
        self.bt_retirar_opcoes3.clicked.connect(remover_opcoes)



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
        self.stackedWidget_opcoes.setVisible(False)
        self.widget_functions_table.setVisible(False)

        #opções de Busca
        self.frame_op_busca.setVisible(False)
        self.page_opcoes_busca.setVisible(False)
        self.frame_analise_inteligente.setVisible(False)
        self.txt_analise_inteligente_output.setVisible(False)
        self.txt_opcoes_busca.setVisible(False)
        self.bt_buscar_op_busca.setVisible(False)
        

        #Opções de Processamento
        self.frame_opcoes_processamento.setVisible(False)
        self.page_opcoes_processamento.setVisible(False)
        self.txt_opcao1_processamento.setVisible(False)
        self.txt_opcao2_processamento.setVisible(False)
        self.txt_opcao3_processamento.setVisible(False)
        self.txt_opcao4_processamento.setVisible(False)
        self.combo1_colunas_processamento.setVisible(False)
        self.combo2_colunas_processamento.setVisible(False)
        self.combo3_colunas_processamento.setVisible(False)
        self.combo4_colunas_processamento.setVisible(False)
        self.bt_setas1.setVisible(False)
        self.bt_setas2.setVisible(False)
        self.bt_setas3.setVisible(False)
        self.bt_add_opcoes2.setVisible(False)
        self.bt_add_opcoes3.setVisible(False)
        self.bt_retirar_opcoes2.setVisible(False)
        self.bt_retirar_opcoes3.setVisible(False)
        self.bt_processamento_de_para.setVisible(False)
        self.bt_extrair_duplicados.setVisible(False)
        self.bt_extrair_duplicados.clicked.connect(self.extrair_duplicados)


        
 

    #MOSTRA UM POPUP DE NOTIFICAÇÃO DE ERRO 
    def show_error_popup(self, title, message):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setIcon(QMessageBox.Warning)
        msg.exec()


    def buscar_arquivo(self):
        selected_data = self.combo_data_base_list.currentText()
        self.txt_output_logs.setPlainText("Buscando novo arquivo.")

        # Abre um diálogo de seleção de arquivos
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        
        if selected_data == 'SQLite':
            file_dialog.setNameFilter("Banco de Dados SQLite (*.db *.sqlite *.sqlite3);;Todos os Arquivos (*)")

        elif selected_data == 'Firebird':
            file_dialog.setNameFilter("Banco de Dados Firebird (*.fdb);;Todos os Arquivos (*)")

        elif selected_data == 'Firebird arquivos .DBF':
            file_dialog.setNameFilter("Banco de Dados Firebird (*.dbf);;Todos os Arquivos (*)")

        else:  # Para CSV
            file_dialog.setNameFilter("Arquivo CSV UTF-8 (*.csv);;CSV separado por vírgula (*.csv)")

        if file_dialog.exec():
            # Obtém o caminho do arquivo selecionado
            file = file_dialog.selectedFiles()[0]

            # Retorna o caminho do arquivo selecionado
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
        selected_data = self.combo_data_base_list.currentText()
        if selected_data == 'SQLite':
            self.txt_servidor_data_base.setText(buscar)
            self.txt_output_logs.setPlainText(f"Caminho do arquivo selecionado:{buscar}")
            self.bt_buscar_sqlite.setVisible(False)
            self.bt_conectar_data_base.setVisible(True)

        elif selected_data == 'Firebird arquivos .DBF':
            self.txt_servidor_data_base.setText(buscar)
            self.txt_output_logs.setPlainText(f"Caminho do arquivo selecionado:{buscar}")
            self.bt_buscar_sqlite.setVisible(True)
            self.bt_conectar_data_base.setVisible(False)
            self.limpar_tabela_principal()
            View_DBF()
            self.bt_pesquisar_dados.setVisible(True)
            self.bt_processamento_dados.setVisible(True)

            
        elif selected_data == 'Firebird':
            self.txt_data_base_name.setText(buscar)
            self.txt_user_data_base.setVisible(True)
            self.txt_password_data_base.setVisible(True)
            self.txt_port_data_base.setVisible(True)
            self.txt_output_logs.setPlainText(f"Caminho do arquivo selecionado:{buscar}")
            self.bt_buscar_sqlite.setVisible(False)
            self.bt_conectar_data_base.setVisible(True)



    
    def load_csv_to_table(self, file_path, table):
        try:
            with open(file_path, newline='', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile, delimiter=';')
                self.all_data = list(reader)
                self.txt_output_logs.setPlainText("Planilha processada com encondig: UTF-8")
        except UnicodeDecodeError:
            with open(file_path, newline='', encoding='latin1', errors='replace') as csvfile:
                reader = csv.reader(csvfile, delimiter=';')
                self.all_data = list(reader)
                self.txt_output_logs.setPlainText("Planilha processada com encondig: Latin1")

        self.load_data_table(data=self.all_data,table=table)
        self.bt_pesquisar_dados.setVisible(True)
        self.bt_processamento_dados.setVisible(True)


        headers = self.all_data[0] if self.all_data else []

        # Carregar os dados na tabela
        self.load_data_table(data=self.all_data, table=table)
            # Process and find duplicates

        # Atualizar os combos com os nomes das colunas
        csv_file.combo_Columns(headers)

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


    def extrair_duplicados(self):
            data, headers = csv_file.carregar_dados_da_tabela()
            csv_file.find_and_load_duplicates(data, headers)
            # Mostrar a page de duplicados
            self.widget_right.setVisible(True)
            self.frame_buttons_rigt.setVisible(True)
            self.tabs_lateral_right.setCurrentWidget(self.page_duplicados)
            self.tabs_lateral_right.setVisible(True)  #
            self.bt_duplicados.setVisible(True)
            self.bt_conections.setVisible(False)

    #SELECIONA A OPÇÃO DE CONEXÃO DE BANCO DE DADOS NO COMBOBOX DA PÁGINA CONEXÕES
    def select_datas(self, ):
        selected_data = self.combo_data_base_list.currentText()
        close_connections()
        self.limpar_tabela_principal()

        # Configurações específicas para cada banco de dados
        if selected_data == 'SQLite':
            configurar_interface_banco_de_dados(conectar_visible=False, buscar_sqlite_visible=True, 
                                                user_visible=False, password_visible=False, 
                                                db_name_visible=False, port_visible=False)
            self.txt_output_logs.setPlainText("Opção SQLite selecionada com sucesso!")

        elif selected_data == 'Firebird':
            configurar_interface_banco_de_dados(servidor='localhost', user='SYSDBA', password='masterkey', 
                                                port='3050')
            self.txt_output_logs.setPlainText("Opção Firebird selecionada com sucesso!")

        elif selected_data == 'Firebird arquivos .DBF':
            configurar_interface_banco_de_dados(conectar_visible=False, buscar_sqlite_visible=True, 
                                                user_visible=False, password_visible=False, 
                                                db_name_visible=False, port_visible=False)
            self.txt_output_logs.setPlainText("Opção SQLite selecionada com sucesso!")

        elif selected_data == 'PostgreSQL':
            configurar_interface_banco_de_dados(servidor='localhost',port='5432')
            self.txt_output_logs.setPlainText("Opção PostgreSQL selecionada com sucesso!")

        elif selected_data == 'MySQL':
            configurar_interface_banco_de_dados(servidor='localhost',port='3306')
            self.txt_output_logs.setPlainText("Opção MySQL selecionada com sucesso!")

        elif selected_data == 'SQL Server':
            configurar_interface_banco_de_dados(port_visible=False)
            self.txt_output_logs.setPlainText("Opção SQL Server selecionada com sucesso!")

        elif selected_data == 'Hiper':
            servidor = f"{self.nome_computador}\\Hiper"
            configurar_interface_banco_de_dados(servidor=servidor, user='sa', password='hiper', 
                                                db_name='Hiper', port_visible=False)
            self.txt_output_logs.setPlainText("Opção Hiper selecionada com sucesso!")

        elif selected_data == 'Etrade':
            servidor = f"{self.nome_computador}\\SQL2014"
            configurar_interface_banco_de_dados(servidor=servidor, user='sa', password='senha', 
                                                db_name='Etrade', port_visible=False)
            self.txt_output_logs.setPlainText("Opção Etrade selecionada com sucesso!")
        
        else:
            close_connections()
            self.limpar_tabela_principal()
            # Caso contrário, torna os elementos invisíveis
            self.bt_buscar_sqlite.setVisible(True)
            self.bt_conectar_data_base.setVisible(False)
  
    def conect_data(self):
        selected_data = self.combo_data_base_list.currentText()

        if self.bt_conectar_data_base and selected_data == 'SQL Server':
            conectar_ao_sql_server()

        elif self.bt_conectar_data_base and selected_data == 'Hiper':
            conectar_ao_sql_server()

        elif self.bt_conectar_data_base and selected_data == 'Etrade':
            conectar_ao_sql_server()

        elif self.bt_conectar_data_base and selected_data == 'MySQL':
            conectar_ao_MySQL()

        elif self.bt_conectar_data_base and selected_data == 'PostgreSQL':
            conectar_ao_PostgreSQL()
        
        elif self.bt_conectar_data_base and selected_data == 'Firebird':
            conectar_ao_Firebird()

        elif self.bt_conectar_data_base and selected_data == 'Firebird arquivos .DBF':
            ...

        elif self.bt_conectar_data_base and selected_data == 'SQLite':
            conectar_Sqlite3()

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
            
            elif selected_data == 'Firebird' and conn:    
                query = f"SELECT * FROM {table};"
                conn.cursor.execute(query)
                data = conn.cursor.fetchall()
                column_names = [desc[0].strip() for desc in conn.cursor.description]
                return data, column_names

            
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
        elif selected_data == 'SQLite':
            return conectar_Sqlite3()
        elif selected_data == 'Firebird':
            return conectar_ao_Firebird()
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
        elif selected_data == 'Firebird':
            tables = tables_Firebird(conn)
        else:
            tables = []

        filtered_tables = [table for table in tables if search_text in table[0].lower()]

        # Atualize a treeView_lista_tabelas
        populate_tree_view_with_tables_and_columns(filtered_tables, conn)

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

        self.treeView_lista_tabelas.setModel(None)
    
    def mostrar_opcoes(self, acao):
        if acao == "pesquisar":
            self.widget_functions_table.setVisible(True)
            self.stackedWidget_opcoes.setVisible(True)
            self.page_opcoes_busca.setVisible(True)
            self.frame_op_busca.setVisible(True)
            self.page_opcoes_processamento.setVisible(False)

        elif acao == "processar":
            self.widget_functions_table.setVisible(True)
            self.stackedWidget_opcoes.setVisible(True)
            self.page_opcoes_processamento.setVisible(True)
            self.frame_opcoes_processamento.setVisible(True)
            self.page_opcoes_busca.setVisible(False)

        elif acao == "conexoes":
            if self.table_principal.rowCount() > 0:
                reply = QMessageBox.question(self, 'Salvar Dados', 
                                             "A tabela contém dados. Deseja salvar antes de continuar?",
                                             QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel,
                                             QMessageBox.Cancel)
                if reply == QMessageBox.Yes:
                    csv_file.save_data_to_csv()
                    self.limpar_tabela_principal()  # Limpa a tabela após salvar
                    self.mostrar_conexoes()
                elif reply == QMessageBox.No:
                    self.limpar_tabela_principal()  # Limpa a tabela
                    self.mostrar_conexoes()
            else:
                self.mostrar_conexoes()

    def mostrar_conexoes(self):
            # Mostrar a page de duplicados
            self.widget_right.setVisible(True)
            self.frame_buttons_rigt.setVisible(True)
            self.tabs_lateral_right.setVisible(True)
            self.tabs_lateral_right.setCurrentWidget(self.page_conections)
            self.bt_conections.setVisible(True)
            self.widget_functions_table.setVisible(False)
            if self.table_principal is not None:
                self.bt_salvar_dados_tabela_principal.clicked.connect(csv_file.save_data_to_csv)
    
    def setup_execut_opcoes(self):
        self.comboBox_opcoes_busca.currentIndexChanged.connect(self.executa_fucoes_Opcoes)
        
    def setup_execut_processamento(self):
        self.combo_opcoes_processamento.currentIndexChanged.connect(self.executa_opcoes_processamento)

    def executa_fucoes_Opcoes(self):
        opcao = self.comboBox_opcoes_busca.currentText()
        
        # OPÇÕES DE BUSCA
        if opcao == "Analise inteligente":
            configurar_busca_interface(True, True, False, False)
            csv_file.analise_inteligente()

        elif opcao == "Buscar por NCM":
            configurar_busca_interface(True, False, True, True, "0000.00.00")

        elif opcao == 'NCM Inválido':
            configurar_busca_interface(True, False, False, False)

        elif opcao == 'Tudo que contém':
            configurar_busca_interface(True, False, True, True)

        elif opcao == 'Duplicados':
            configurar_busca_interface(True, False, False, False)

    def executa_opcoes_processamento(self):
        opcao = self.combo_opcoes_processamento.currentText()
        # OPÇÕES DE PROCESSAMENTO
        if opcao == 'Substituir NCM':
            print('Substituir NCM')
            configurar_interface(True, True, False, False, True, False, False, True, True, False, False, 
                                    False, False, False, False, True, False, "De", "Para", "Para", "Para")

        elif opcao == 'Tudo que contém mude para':
            print('Tudo que contém mude para')
            configurar_interface(True, True, False, False, True, False, False, True, True, False, False, 
                                    True, False, False, False, True, False, "De", "Para", "Para", "Para")

        elif opcao == 'Se Coluna A contém, Coluna B recebe...':
            print('Se Coluna A contém, Coluna B recebe...')
            configurar_interface(True, True, False, False, True, False, False, True, True, False, False, 
                                    True, False, False, False, True, False, "De", "Para", "Para", "Para")

        elif opcao == 'Filtrar por coluna e copiar todas a linhas que contenham':
            print('Filtrar por coluna e copiar todas as linhas que contenham')
            configurar_interface(True, False, False, False, False, False, False, True, False, False, False, 
                                    False, False, False, False, True, False, "De", "Para", "Para", "Para")

        elif opcao == 'Extrair dados duplicados da tabela':
            print('Extrair dados duplicados da tabela')
            configurar_interface(False, False, False, False, False, False, False, False, False, False, False, 
                                    False, False, False, False, False, True, "De", "Para", "Para", "Para")


        elif opcao == 'Formatar colunas com valores do tipo moeda':
            print('Formatar colunas com valores do tipo moeda')
            configurar_interface(True, True, False, False, True, False, False, True, True, False, False, 
                                    True, False, False, False, True, False, "De", "Para", "Para", "Para")

        elif opcao == 'Formatar códigos de barras':
            print('Formatar códigos de barras')
            configurar_interface(True, False, False, False, False, False, False, True, False, False, False, 
                                    False, False, False, False, True, False, "", "", "", "")

        elif opcao == 'Formatar número de telefone':
            print('Formatar número de telefone')
            configurar_interface(True, False, False, False, False, False, False, True, False, False, False, 
                                    False, False, False, False, True, False, "(000) 99999-9999", "", "", "")

        elif opcao == 'Formatar CPF':
            print('Formatar CPF')
            configurar_interface(True, False, False, False, False, False, False, True, False, False, False, 
                                    False, False, False, False, True, False, "000.000.000-00", "", "", "")

        elif opcao == 'Formatar CNPJ':
            print('Formatar CNPJ')
            configurar_interface(True, False, False, False, False, False, False, True, False, False, False, 
                                    False, False, False, False, True, False, "00.000.000/0000-00", "", "", "")

        elif opcao == 'Buscar valores negativos e mudar para zero':
            print('Buscar valores negativos e mudar para zero')
            configurar_interface(True, False, False, False, False, False, False, True, False, False, False, 
                                    False, False, False, False, True, False, "", "", "", "")




if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)  # Crie a instância de QApplication
    window = WindowPrincipal()
    window.show()
    sys.exit(app.exec())  # Execute o loop de eventos e finalize o programa corretamente

