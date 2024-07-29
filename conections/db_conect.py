try:
    import pyodbc
    import mysql.connector
    import sqlite3
    import psycopg2
    import gui.app_instance as app_instance # Importe o módulo que você criou
    from PySide6.QtCore import QCoreApplication
    from PySide6.QtGui import QIcon,QFont,QColor,QStandardItem, QStandardItemModel
    from PySide6 import QtCore
    from PySide6.QtWidgets import (QApplication,QMainWindow,QMessageBox,QTableWidgetItem,QFileDialog)
    import os
    import uuid
    from configs.erros import Erros
except:
    pass

error = Erros()

# Variáveis globais para armazenar conexões
global conn1, conn2, conn3, conn4
conn1 = conn2 = conn3 = conn4 = None

def set_ui_instance(instance):
    global ui_instance
    ui_instance = instance

class Conections_SQLServer():
    def __init__(self):

        self.cursor = None  # Inicializa o atributo cursor
        self.conn = None  # Inicializa a conexão como None
            #LOGS ----------------------------------------------------------------------------------------------------------
            # Obtém o nome do arquivo atual

    def conect_sqlserver(self, server, database, username, password):
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        try:
            self.conn = pyodbc.connect('DRIVER={SQL Server};SERVER=' + self.server +
                                  ';DATABASE=' + self.database + ';UID=' + self.username + ';PWD=' + self.password)
            
            # abre a conexão com o banco de dados
            self.cursor = self.conn.cursor()
            return "OK"
        except Exception as e:
            print(e)
            return "ERRO"

class Conections_MySQL():
    def __init__(self):
        self.conn = None
        self.cursor = None


    def MYSQL(self, host, database, username, password, port):
        try:
            # estabelece a conexão
            self.conn = mysql.connector.connect(
                user=username,
                password=password,
                host=host,
                port=port,
                database=database
            )

            # abre a conexão com o banco de dados
            self.cursor = self.conn.cursor()
            if self.cursor:
                return "OK"

        except Exception as e:
            print(f"Erro de conexão: {str(e)}")
            return "ERRO"

    def query_MySQL(self, value):
        error = Erros()
        try:
            self.cursor.execute(value)
            res = self.cursor.fetchall()
            return res
        except Exception as e:
            error.show_error_popup(str(e))
            print(f'Erro:\n{e}')

class Conections_SQLite3():   
    def __init__(self):
        self.conn = None
        self.cursor = None


    def conectar_sqlite3_db(self, path_db):
        try:
            # Conecta-se ao banco de dados (ou cria um novo se não existir)
            self.conn = sqlite3.connect(path_db)
            self.cursor = self.conn.cursor()
            print("Conexão estabelecida com sucesso.")
            return "OK"
        except Exception as e:
            print("Erro ao conectar à DataBase:", e)
            return "ERRO"
        
        
    def query_SQLite(self, query_value):
        error = Erros()
        try:
            self.cursor.execute(f'{query_value}')
            res = self.cursor.fetchall()
                        # Recupera os nomes das colunas
            column_names = [description[0] for description in self.conn3.cursor.description]
            print(res)
            return column_names,res
        except Exception as e:
          error.show_error_popup(str(e))

class Conections_PostgreSQL():
    def __init__(self):
        self.cursor = None
        self.conn = None

    def postgresql_conect(self, host, database, username, password, port):
        
        try:
            self.conn = psycopg2.connect(dbname=database, user=username, password=password, host=host,port=port)
            self.cursor = self.conn.cursor()
            # abre a conexão com o banco de dados
            self.cursor = self.conn.cursor()
            
            if self.cursor:
                return "OK"

        except Exception as e:
            print(f"Erro de conexão: {str(e)}")
            return "ERRO"
        

# Função para fechar todas as conexões
def close_connections():
    global conn1, conn2, conn3, conn4

    def close_conn(conn):
        if conn is not None:
            try:
                conn.cursor.close()
            except:
                pass
            try:
                conn.close()
            except:
                pass

    close_conn(conn1)
    close_conn(conn2)
    close_conn(conn3)
    close_conn(conn4)

    conn1 = conn2 = conn3 = conn4 = None

# FAZ A CONEXÃO COM O BANCO DE DADOS SQL SERVER
def conectar_ao_sql_server():
        ui = app_instance.get_ui_instance()
        server = ui.txt_servidor_data_base.text()
        database = ui.txt_data_base_name.text()
        user = ui.txt_user_data_base.text()
        password = ui.txt_password_data_base.text()
        if server == '' and database == '' and user == '' and password == '':
            error.show_error_popup("Erro!","É necessário que todos os campos estejam preenchidos.")
            ui.txt_output_logs.setPlainText(f"Erro! dados incompletos.")
        else:
            msg1 = "Conectado com Sucesso!"
            msg2 = f"Não foi possível se conectar ao banco de dados {database}"

            # Instancie a classe Conections_SQLServer com os argumentos necessários
            conn1 = Conections_SQLServer()
            resp = conn1.conect_sqlserver(server, database, user, password)
            
            if resp == 'OK':
                ui.txt_output_logs.setPlainText(f"{msg1}")
                tables_SqlServer(conn1)
                ui.label_4.setVisible(True)
                ui.bt_mostra_dados_tabelas.setVisible(True)
                return conn1
            elif resp == 'ERRO':
                ui.txt_output_logs.setPlainText(f"Erro: {msg2}")
                error.msg_popup(resp,msg1,msg2)
            


#Conectando #############################################################################    
def conectar_ao_MySQL():
            ui = app_instance.get_ui_instance()
            server = ui.txt_servidor_data_base.text()
            database = ui.txt_data_base_name.text()
            user = ui.txt_user_data_base.text()
            password = ui.txt_password_data_base.text()
            port = ui.txt_port_data_base.text()
            if server == '' and database == '' and user == '':
                ui.txt_output_logs.setPlainText(f"Erro! dados incompletos.")
                error.show_error_popup("Erro!","É necessário que todos os campos estejam preenchidos.")

            
            else:
                msg1 = "Conectado com Sucesso!"
                msg2 = f"Não foi possível se conectar ao banco de dados {database}"
                
                if port == '' or port == None:
                    port = '3306'

                conn2 = Conections_MySQL()
                resp = conn2.MYSQL(server, database, user, password, port=port)

                if resp == 'OK':
                    ui.txt_output_logs.setPlainText(f"{msg1}")
                    tables_MySQL(conn2)
                    ui.label_4.setVisible(True)
                    ui.bt_mostra_dados_tabelas.setVisible(True)
                    return conn2
                elif resp == 'ERRO':
                    ui.txt_output_logs.setPlainText(f"Erro: {msg2}")   
                error.msg_popup(resp,msg1,msg2)

def conectar_ao_PostgreSQL():
        ui = app_instance.get_ui_instance()
        server = ui.txt_servidor_data_base.text()
        database = ui.txt_data_base_name.text()
        user = ui.txt_user_data_base.text()
        password = ui.txt_password_data_base.text()
        port = ui.txt_port_data_base.text()


        if server == '' and database == '' and user == '' and password == '':
            error.show_error_popup("Erro!","É necessário que todos os campos estejam preenchidos.")
            ui.txt_output_logs.setPlainText(f"Erro! dados incompletos.")
        else:
            msg1 = "Conectado com Sucesso!"
            msg2 = f"Não foi possível se conectar ao banco de dados {database}"
            if port == '' or port == None:
                port = '5432'
            # Instancie a classe Conections_SQLServer com os argumentos necessários
            conn4 = Conections_PostgreSQL()
            resp =conn4.postgresql_conect(server, database, user, password, port)
            
            if resp == 'OK':
                ui.txt_output_logs.setPlainText(f"{msg1}")
                tables_PostgreSQL(conn4)
                ui.label_4.setVisible(True)
                ui.bt_mostra_dados_tabelas.setVisible(True)
                return conn4
            elif resp == 'ERRO':
                ui.txt_output_logs.setPlainText(f"Erro: {msg2}")

            error.msg_popup(resp,msg1,msg2)

def get_columns_for_table(conn, table_name):
    if conn:
        try:
            query = f"""
                SELECT COLUMN_NAME
                FROM INFORMATION_SCHEMA.COLUMNS
                WHERE TABLE_NAME = '{table_name}'
            """
            conn.cursor.execute(query)
            columns = conn.cursor.fetchall()
            return [column[0] for column in columns]
        except Exception as e:
            print(f"Erro ao buscar colunas: {e}")
            return []
    return []


def populate_tree_view_with_tables_and_columns(tables, conn):
    ui = app_instance.get_ui_instance()
    model = QStandardItemModel()

    for table in tables:
        table_name = table[0]  # Assumindo que `table` é uma tupla e o nome da tabela está na primeira posição
        table_item = QStandardItem(table_name)
        model.appendRow(table_item)

        # Adiciona colunas como subitens
        columns = get_columns_for_table(conn, table_name)
        for column in columns:
            column_item = QStandardItem(column)
            table_item.appendRow(column_item)

    ui.treeView_lista_tabelas.setModel(model)


def tables_SqlServer(conn):
    ui = app_instance.get_ui_instance()
    data = ui.txt_data_base_name.text()
    try:
        conn.cursor.execute(f"""SELECT TABLE_NAME
                                FROM INFORMATION_SCHEMA.TABLES
                                WHERE TABLE_TYPE = 'BASE TABLE' AND TABLE_CATALOG = '{data}'""")
        resp = conn.cursor.fetchall()
        populate_tree_view_with_tables_and_columns(resp, conn)
        return resp
    except Exception as e:
        print(e)
        return []

def tables_MySQL(conn):
    ui = app_instance.get_ui_instance()
    data = ui.txt_data_base_name.text()
    try:
        conn.cursor.execute(f"""SELECT TABLE_NAME
                                FROM INFORMATION_SCHEMA.TABLES
                                WHERE TABLE_TYPE = 'BASE TABLE' AND TABLE_SCHEMA = '{data}'""")
        resp = conn.cursor.fetchall()
        populate_tree_view_with_tables_and_columns(resp, conn)
        return resp
    except Exception as e:
        print(e)
        return []

def tables_PostgreSQL(conn):
    try:
        conn.cursor.execute("""
            SELECT table_name
            FROM information_schema.tables
            WHERE table_schema = 'public' AND table_type = 'BASE TABLE'
        """)
        resp = conn.cursor.fetchall()
        populate_tree_view_with_tables_and_columns(resp, conn)
        return resp
    except psycopg2.Error as e:
        print(f"Erro ao buscar tabelas: {e}")
        return []

def tables_SQLite3(conn):
    try:
        conn.cursor.execute("""SELECT name
                                FROM sqlite_master
                                WHERE type='table'""")
        resp = conn.cursor.fetchall()
        populate_tree_view_with_tables_and_columns(resp, conn)
        return resp
    except Exception as e:
        print(e)
        return []



        
