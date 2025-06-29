import asyncio
from PySide6.QtCore import QCoreApplication,QUrl,QTimer,Qt, QEvent,QObject
from PySide6.QtGui import QGuiApplication, QIcon,QFont,QColor,QDesktopServices, QKeyEvent, QCursor
from PySide6 import QtCore
from PySide6.QtWidgets import (QApplication,QMainWindow, QScrollArea, QHBoxLayout,QMessageBox,QProgressBar,QDialog, QVBoxLayout, QPushButton,QTableWidgetItem,QFileDialog,QMenu, QWidgetAction,
                                    QPlainTextEdit, QPushButton, QVBoxLayout, QWidget, QSystemTrayIcon, QMenu)

import sqlite3
from ui.ui_main import Ui_PrincipalWindow
from components.progress_bar import CSVLoaderThread, ProgressBarWindow
import ui.app_instance as app_instance
from components import controladores as i
from components import objetos as obj
from functions import functions_csv as f_csv
from xml_functions.table import XmlTable, TablesClienteContabil
from xml_functions.relatorios import save_csv, save_pdf
import bcrypt
import base64
import sys
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SCHEMA_PATH = os.path.join(BASE_DIR, "dados", "SQL", "schema.txt")
DB_PATH = os.path.join(BASE_DIR, "dados", "current", "shar", "current", "sqlite_db.db")
# Função para ler o arquivo schema.txt
# def read_tables():
#     base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
#     schema_path = os.path.join(base_path, "dados", "SQL", "schema.txt")
#     with open(schema_path, "r", encoding='utf-8') as file:
#         return file.read().strip()
        

class WindowPrincipal(QMainWindow, Ui_PrincipalWindow):
    def __init__(self):
        super(WindowPrincipal, self).__init__()
        self.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)#Remove a barra padrão
        self.old_pos = None  # Variável para armazenar a posição do mouse
        self.full_size_window()
        app_instance.set_ui_instance(self)
        self.show_frames = i.FramesControler()
        self.tb_xml = XmlTable(directory=None)
        self.tab_c = TablesClienteContabil(parent=self)
        self.visibilidade_objetos()
        self.lb_titulos_tabelas.setText("Importe um arquivo .csv")
        # self.login(username="admin", password="smart_admin_migrate")
        # self.setComboBox()
        # self.table_cliente()
        self.setupWindow_xml()



    """    
    def setComboBox(self):
        data = self.sqlite.select_contabilidade()
        self.combo_contador.clear()
        for row in data:
            id_contador, ativo, cnpj, nome, razao_social, email, phone = row
            self.combo_contador.addItem(nome)
            self.combo_contador.setItemData(self.combo_contador.count() - 1, id_contador)
        if self.combo_contador.count() > 0:
            self.combo_contador.setCurrentIndex(0)"""

    def get_selected_contador_id(self):
        current_index = self.combo_contador.currentIndex()
        if current_index >= 0:
            return self.combo_contador.itemData(current_index)
        return None
        
    def visibilidade_objetos(self):
        self.btn_opcoes_pesquisas.setEnabled(False)
        self.btn_opcoes_processamento.setEnabled(False)
        self.show_frames.showFrames(status=False)


        # Obtendo o tamanho da tela corretamente no PySide6
    
    def full_size_window(self):
        screen = QGuiApplication.primaryScreen().geometry()
        self.setGeometry(0, 0, screen.width(), screen.height())
        self.setup_buttons()
        

    #Funções que permitem arrastar a tela //////////////////////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        """Armazena a posição do clique inicial ao pressionar o botão esquerdo do mouse."""
        if event.button() == Qt.LeftButton:
            self.old_pos = event.globalPos()

    def mouseMoveEvent(self, event):
        """Move a janela com base na posição do mouse."""
        if self.old_pos is not None:
            delta = event.globalPos() - self.old_pos
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.old_pos = event.globalPos()

    def mouseReleaseEvent(self, event):
        """Libera o movimento ao soltar o botão do mouse."""
        if event.button() == Qt.LeftButton:
            self.old_pos = None       
    #///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    def setup_buttons(self):
        # Estado da Janela (Maximizada ou não)
        self.isMaximized = False  
        # Conectar os botões às funções
        self.btn_minimize.clicked.connect(self.minimize_window)
        
        self.btn_maximize.clicked.connect(self.maximize_restore_window)
        
        self.btn_close_window.clicked.connect(self.close_window)
        self.btn_importar_file.clicked.connect(self.buscar_csv)
        self.btn_opcoes_pesquisas.clicked.connect(lambda: self.mostrar_opcoes('pesquisar'))
        self.btn_opcoes_processamento.clicked.connect(lambda: self.mostrar_opcoes('processar'))

        self.btn_opcoes_conexoes_db.clicked.connect(i.FramesControler.showFrm_lateral)
        self.btn_closeFrm_lateral.clicked.connect(i.FramesControler.closeFrm_lateral)

        self.btn_opcoes_contabil.clicked.connect(i.contabil_fiscal)

        self.btn_closeFrm_cliente.clicked.connect(i.FramesControler.closeFrm_lateral_cliente)
        self.btn_closeFrm_contabilidade.clicked.connect(i.FramesControler.closeFrm_lateral_contabilidade)

        self.btn_proxima_pagina.clicked.connect(i.mudar_proxima_pag)
        self.btn_voltar_pagina.clicked.connect(i.mudar_pag_anterior)

        self.btn_novo_cliente.clicked.connect(self.button_novo_cliente)
        self.btn_nova_contabilidade.clicked.connect(self.button_nova_contabilidade)
        self.btn_salvar_contabilidade.clicked.connect(self.create_contabilidade)
        self.btn_salvar_cliente.clicked.connect(self.create_clientes)



    def setupWindow_xml(self):
       
        self.btn_path_xml.clicked.connect(self.buscar_xml)
        self.bt_limpa_tab_xml.clicked.connect(lambda checked=False: self.tb_xml.clear_xml())
        # self.txt_pesquisa_table_xml.textChanged.connect(self.tb_xml.filter_table_xml)
        self.tableWidget_xml_list.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tableWidget_xml_list.customContextMenuRequested.connect(self.tb_xml.show_context_menu_mde)
        self.btn_salvar_relatorio_xml.clicked.connect(self._salvar_relatorios_xml)

    def _salvar_relatorios_xml(self):
        opcoes = self.combo_opcoes_relatorios_xml.currentText()
        print(opcoes)
        if opcoes == "Exportar em CSV":
            save_csv(self)
        elif opcoes == "Exportar em PDF":
            save_pdf(self)
        else:
            QMessageBox.warning(
                None,
                "Atenção!",
                "É necessário selecionar uma das opções."
            )

    def buscar_xml(self):
        xml_path = obj.path_xml()
        if xml_path:
            self.progress_window = ProgressBarWindow(xml_path, parent=self)
            self.progress_window.thread.data_loaded.connect(lambda data: self.on_xml_loaded(xml_path))
            self.progress_window.show()

    #carrega e processa os xml's
    def on_xml_loaded(self, xml_path):
        if xml_path:
            self.tb_xml.directory = xml_path
            self.tb_xml.processing_xmls()
        self.progress_window.close()         

    # Método buscar_csv ajustado
    def buscar_csv(self):
        path_file = obj.search_file()
        if path_file:
            # Cria e exibe a janela de progresso
            self.progress_window = ProgressBarWindow(path_file, parent=self)  # Passa self como parent
            self.progress_window.thread.data_loaded.connect(self.on_csv_loaded)
            self.progress_window.show()
            self.stackedWidget_tables.setCurrentWidget(self.page_principal)
            self.lb_titulos_tabelas.setText("Manipulação de Dados")
            
    def on_csv_loaded(self, data):
        """Callback executado quando os dados do CSV são carregados"""
        if data:          
                # Chama a função combosHeader
            # i.combosHeader(data=data, combo=self.combo_colunas_1, table=self.table_principal)
            f_csv.load_data_InTable(table=self.table_principal, data=data)
            self.btn_opcoes_pesquisas.setEnabled(True)
            self.btn_opcoes_processamento.setEnabled(True)
            self.frm_functions_table_principal.setVisible(True)
        self.progress_window.close()

    def mostrar_opcoes(self, acao):
        if acao == "pesquisar":
            self.show_frames.frames[0].setVisible(True)
            self.stackedWidget_tables.setCurrentWidget(self.page_principal)
            self.page_opcoes_processamento.setVisible(False)
            self.page_opcoes_busca.setVisible(True)
            
        elif acao == "processar":
            self.show_frames.frames[0].setVisible(True)
            self.stackedWidget_tables.setCurrentWidget(self.page_principal)
            self.page_opcoes_processamento.setVisible(True)
            self.page_opcoes_busca.setVisible(False)

        elif acao == "contabil":
            self.show_frames.frames[0].setVisible(False)

    def minimize_window(self):
        """Minimiza a janela."""
        self.showMinimized()

    def maximize_restore_window(self):
        """Alterna entre maximizar e restaurar o tamanho original da janela."""
        if self.isMaximized:
            self.showNormal()  # Restaura o tamanho original
            self.full_size_window()
            self.isMaximized = False
        else:
            self.showMaximized()  # Maximiza a janela
            # self.resize(1400, 800)
            self.isMaximized = True

    def close_window(self):
        """Fecha a janela."""
        self.close()


    def create_initial_data(self):
        try:
            user = 'admin'
            password = 'smart_admin_migrate'
            hashed_bytes = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            hashed_str = hashed_bytes.decode('utf-8')
            cursor = self.sqlite.connect_db()
            if cursor:
                # Inserir papéis na tabela roles
                roles = ['superadmin', 'admin', 'user']
                for role in roles:
                    cursor.execute(
                        "INSERT INTO roles (name) VALUES (?)",
                        (role,)
                    )
                # Inserir usuário admin na tabela users com role_id = 1 (superadmin)
                cursor.execute(
                    "INSERT INTO users (username, password_hash, role_id) VALUES (?, ?, ?)",
                    (user, hashed_str, 1)
                )
                self.sqlite.commit()

        except Exception as e:
            print(f"Erro create_initial_data: {e}")

    def login(self, username, password):
        cursor = self.sqlite.connect_db()
        if cursor:
            cursor.execute("SELECT password_hash FROM users WHERE username = ?", (username,))
            result = cursor.fetchone()
            print(result)
            self.sqlite.close()
            if result:
                # Converter o hash armazenado (string em maiúsculas) para bytes
                hashed_bytes = result[0].encode('utf-8')
                print(f"Login: {hashed_bytes}")
                print(f"login do {username} realizado com sucesso!")
                return bcrypt.checkpw(password.encode('utf-8'), hashed_bytes)
        return False

    def create_contabilidade(self):
        user = 1
        data = (
            self.txt_cnpj_contabilidade.text(),
            self.txt_nome_contabilidade.text(),
            self.txt_razao_social_contabilidade.text(),
            self.txt_email_contabilidade.text(),
            self.txt_telefone_contabilidade_2.text(),
            user
        )
        self.sqlite.post_contabilidade(data=data)

    def create_clientes(self):
        id_contador = self.get_selected_contador_id()
        print(id_contador)
        if id_contador is None:
            raise ValueError("Nenhum contador selecionado no QComboBox")
        
        user = 1
        data = (
            self.txt_nome_cliente.text(),
            self.txt_razao_social_cliente.text(),
            self.txt_cnpj_cliente.text(),
            self.txt_email_cliente.text(),
            id_contador,
            self.combo_sistema_cliente.currentText(),
            self.txt_link_sistema_cliente.text(),
            self.txt_user_cliente_sistema.text(),
            self.txt_password_cliente_sistema.text(),
            user
        )
        try:
            self.sqlite.post_cliente(data)
            i.clean_txt_cliente()
            print(f"Cliente cadastrado com sucesso: {data}")
            # Recarregar a tabela
            self.table_cliente()
        except sqlite3.OperationalError as e:
            print(f"Erro ao cadastrar cliente: {e}")
            raise

    """
    def table_cliente(self):
            data = self.sqlite.select_cliente()
            self.tab_c.table_cliente_contabilidade(
                table=self.table_clientes,
                data=data,
                action=self.tab_c.show_edit_frame  # Passar a função show_edit_frame
            )"""

    def button_novo_cliente(self):
        self.frm_cadastro_cliente.setVisible(True)

    def button_nova_contabilidade(self):
        self.frm_cadastro_contabilidade.setVisible(True)



if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)  # Crie a instância de QApplication
    window = WindowPrincipal()
    window.show()
    sys.exit(app.exec())  # Execute o loop de eventos e finalize o programa corretamente