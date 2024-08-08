# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main - CopiaFSVIWj.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPlainTextEdit, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QTableWidget,
    QTableWidgetItem, QTreeView, QVBoxLayout, QWidget)
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1717, 1008)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(10, 7, 10, 5)
        self.widget_right = QWidget(self.widget)
        self.widget_right.setObjectName(u"widget_right")
        self.widget_right.setMinimumSize(QSize(400, 0))
        self.widget_right.setMaximumSize(QSize(400, 16777215))
        self.widget_right.setStyleSheet(u"#widget_right{\n"
"	background-color: rgba(217, 217, 217, 0.35);\n"
"	border-right: 1px solid rgb(109, 109, 109);\n"
"	border-left: 1px solid rgba(217, 217, 217, 0.80);\n"
"	border-top: 1px solid rgba(217, 217, 217, 0.80);\n"
"	border-bottom: 1px solid rgb(109, 109, 109);\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    padding: 10px;\n"
" \n"
"}")
        self.gridLayout_6 = QGridLayout(self.widget_right)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(2, 2, 2, 2)
        self.tabs_lateral_right = QStackedWidget(self.widget_right)
        self.tabs_lateral_right.setObjectName(u"tabs_lateral_right")
        self.tabs_lateral_right.setMinimumSize(QSize(0, 0))
        self.tabs_lateral_right.setMaximumSize(QSize(16777215, 16777215))
        self.page_conections = QWidget()
        self.page_conections.setObjectName(u"page_conections")
        self.verticalLayout = QVBoxLayout(self.page_conections)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.page_conections)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 180))
        self.frame.setMaximumSize(QSize(16777215, 180))
        self.frame.setStyleSheet(u"QFrame{\n"
"background-color: rgba(255, 255, 255, 0.80);\n"
"}\n"
"\n"
"QLineEdit{\n"
"	font: 700 8pt \"Segoe UI\";\n"
"	color:rgb(120, 120, 120);\n"
"	border: 1px solid rgba(109, 109, 109, 0.60);\n"
"    border-top-left-radius: 5px;\n"
"    border-top-right-radius: 5px;\n"
"    border-bottom-left-radius: 5px;\n"
"    border-bottom-right-radius: 5px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"\n"
"background-color: rgba(195, 205, 255, 0.40)\n"
"}\n"
"\n"
"QComboBox{\n"
"	\n"
"	font: 700 8pt \"Segoe UI\";\n"
"	color:rgb(120, 120, 120);\n"
"	border: 1px solid rgba(109, 109, 109, 0.60);\n"
"    border-top-left-radius: 5px;\n"
"    border-top-right-radius: 5px;\n"
"    border-bottom-left-radius: 5px;\n"
"    border-bottom-right-radius: 5px;\n"
"}\n"
"\n"
"QComboBox:hover{\n"
"background-color: rgba(195, 205, 255, 0.40)\n"
"}\n"
"\n"
"QPushButton{\n"
"	\n"
"    border-top-left-radius: 5px;\n"
"    border-top-right-radius: 5px;\n"
"    border-bottom-left-radius: 5px;\n"
"    border-bottom-right-radius: 5px;\n"
"	border-rig"
                        "ht: 1px solid rgb(109, 109, 109);\n"
"	border-left: 1px solid rgba(217, 217, 217, 0.80);\n"
"	border-top: 1px solid rgba(217, 217, 217, 0.80);\n"
"	border-bottom: 1px solid rgb(109, 109, 109);\n"
"	font: 700 8pt \"Segoe UI\";\n"
"	color:rgb(120, 120, 120);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(195, 205, 255)\n"
"}")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.txt_servidor_data_base = QLineEdit(self.frame)
        self.txt_servidor_data_base.setObjectName(u"txt_servidor_data_base")
        self.txt_servidor_data_base.setGeometry(QRect(10, 60, 231, 30))
        self.txt_servidor_data_base.setMinimumSize(QSize(0, 30))
        self.txt_servidor_data_base.setMaximumSize(QSize(16777215, 30))
        self.txt_data_base_name = QLineEdit(self.frame)
        self.txt_data_base_name.setObjectName(u"txt_data_base_name")
        self.txt_data_base_name.setGeometry(QRect(10, 140, 101, 30))
        self.txt_data_base_name.setMinimumSize(QSize(0, 30))
        self.txt_data_base_name.setMaximumSize(QSize(16777215, 30))
        self.txt_data_base_name.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.txt_port_data_base = QLineEdit(self.frame)
        self.txt_port_data_base.setObjectName(u"txt_port_data_base")
        self.txt_port_data_base.setGeometry(QRect(140, 140, 101, 30))
        self.txt_port_data_base.setMinimumSize(QSize(0, 30))
        self.txt_port_data_base.setMaximumSize(QSize(16777215, 30))
        self.txt_port_data_base.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.combo_data_base_list = QComboBox(self.frame)
        self.combo_data_base_list.addItem("")
        self.combo_data_base_list.addItem("")
        self.combo_data_base_list.addItem("")
        self.combo_data_base_list.addItem("")
        self.combo_data_base_list.addItem("")
        self.combo_data_base_list.addItem("")
        self.combo_data_base_list.addItem("")
        self.combo_data_base_list.addItem("")
        self.combo_data_base_list.setObjectName(u"combo_data_base_list")
        self.combo_data_base_list.setGeometry(QRect(10, 10, 161, 30))
        self.combo_data_base_list.setMinimumSize(QSize(0, 30))
        self.combo_data_base_list.setMaximumSize(QSize(16777215, 30))
        self.txt_user_data_base = QLineEdit(self.frame)
        self.txt_user_data_base.setObjectName(u"txt_user_data_base")
        self.txt_user_data_base.setGeometry(QRect(10, 100, 101, 30))
        self.txt_user_data_base.setMinimumSize(QSize(0, 30))
        self.txt_user_data_base.setMaximumSize(QSize(16777215, 30))
        self.txt_user_data_base.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.txt_password_data_base = QLineEdit(self.frame)
        self.txt_password_data_base.setObjectName(u"txt_password_data_base")
        self.txt_password_data_base.setGeometry(QRect(140, 100, 101, 30))
        self.txt_password_data_base.setMinimumSize(QSize(0, 30))
        self.txt_password_data_base.setMaximumSize(QSize(16777215, 30))
        self.txt_password_data_base.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.titulo_conexoes = QLabel(self.frame)
        self.titulo_conexoes.setObjectName(u"titulo_conexoes")
        self.titulo_conexoes.setGeometry(QRect(180, 10, 181, 21))
        self.bt_conectar_data_base = QPushButton(self.frame)
        self.bt_conectar_data_base.setObjectName(u"bt_conectar_data_base")
        self.bt_conectar_data_base.setGeometry(QRect(250, 60, 110, 30))
        self.bt_conectar_data_base.setMinimumSize(QSize(110, 30))
        self.bt_conectar_data_base.setMaximumSize(QSize(110, 30))
        self.bt_conectar_data_base.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.bt_buscar_sqlite = QPushButton(self.frame)
        self.bt_buscar_sqlite.setObjectName(u"bt_buscar_sqlite")
        self.bt_buscar_sqlite.setGeometry(QRect(250, 60, 110, 30))
        self.bt_buscar_sqlite.setMinimumSize(QSize(110, 30))
        self.bt_buscar_sqlite.setMaximumSize(QSize(110, 30))
        self.bt_buscar_sqlite.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.bt_buscar_sqlite.raise_()
        self.txt_servidor_data_base.raise_()
        self.txt_data_base_name.raise_()
        self.txt_port_data_base.raise_()
        self.combo_data_base_list.raise_()
        self.txt_user_data_base.raise_()
        self.txt_password_data_base.raise_()
        self.titulo_conexoes.raise_()
        self.bt_conectar_data_base.raise_()

        self.verticalLayout.addWidget(self.frame)

        self.frame_3 = QFrame(self.page_conections)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setEnabled(True)
        self.frame_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_12 = QGridLayout(self.frame_3)
        self.gridLayout_12.setSpacing(3)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.treeView_lista_tabelas = QTreeView(self.frame_3)
        self.treeView_lista_tabelas.setObjectName(u"treeView_lista_tabelas")
        self.treeView_lista_tabelas.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.treeView_lista_tabelas.setStyleSheet(u"QTreeView{\n"
"\n"
"	font: 11pt \"Segoe UI\";\n"
"	\n"
"	color: rgb(75, 63, 241);\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-right: 1px solid rgba(217, 217, 217, 0.80);\n"
"	border-left: 1px solid rgba(217, 217, 217, 0.80);\n"
"	border-top: 1px solid rgba(217, 217, 217, 0.80);\n"
"	border-bottom: 1px solid rgba(217, 217, 217, 0.80);\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    padding: 10px;\n"
"\n"
"}\n"
"\n"
"QTreeView:hover{\n"
"	background-color: rgba(195, 205, 255, 0.25);\n"
"}\n"
"\n"
" QHeaderView::section {\n"
"      background-color: #4b3ff1;\n"
"		border: 1px solid rgba(217, 217, 217, 0.80);\n"
"	font: 700 11pt \"Times New Roman\";\n"
"       color: white;\n"
"\n"
"\n"
"}")
        self.treeView_lista_tabelas.setInputMethodHints(Qt.InputMethodHint.ImhNone)
        self.treeView_lista_tabelas.setEditTriggers(QAbstractItemView.EditTrigger.AllEditTriggers)
        self.treeView_lista_tabelas.setTabKeyNavigation(True)
        self.treeView_lista_tabelas.setAlternatingRowColors(True)
        self.treeView_lista_tabelas.setIconSize(QSize(30, 30))
        self.treeView_lista_tabelas.setAnimated(True)
        self.treeView_lista_tabelas.setHeaderHidden(True)
        self.treeView_lista_tabelas.header().setVisible(False)
        self.treeView_lista_tabelas.header().setMinimumSectionSize(100)

        self.gridLayout_12.addWidget(self.treeView_lista_tabelas, 4, 0, 1, 1)

        self.frame_9 = QFrame(self.frame_3)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setEnabled(True)
        self.frame_9.setMinimumSize(QSize(0, 30))
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_15 = QGridLayout(self.frame_9)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setHorizontalSpacing(6)
        self.gridLayout_15.setContentsMargins(4, 2, 4, 3)
        self.bt_mostra_dados_tabelas = QPushButton(self.frame_9)
        self.bt_mostra_dados_tabelas.setObjectName(u"bt_mostra_dados_tabelas")
        self.bt_mostra_dados_tabelas.setMinimumSize(QSize(120, 35))
        self.bt_mostra_dados_tabelas.setMaximumSize(QSize(120, 35))
        self.bt_mostra_dados_tabelas.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.bt_mostra_dados_tabelas.setStyleSheet(u"QPushButton{\n"
"	background-color: rgba(241, 242, 246, 0.50);\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"	border-right: 1px solid rgb(109, 109, 109);\n"
"	border-left: 1px solid rgba(217, 217, 217, 0.80);\n"
"	border-top: 1px solid rgba(217, 217, 217, 0.80);\n"
"	border-bottom: 1px solid rgb(109, 109, 109);\n"
"	font: 800 9pt \"Segoe UI\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(195, 205, 255)\n"
"}")

        self.gridLayout_15.addWidget(self.bt_mostra_dados_tabelas, 0, 1, 1, 1, Qt.AlignmentFlag.AlignBottom)

        self.label_4 = QLabel(self.frame_9)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_15.addWidget(self.label_4, 0, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)


        self.gridLayout_12.addWidget(self.frame_9, 5, 0, 1, 1)

        self.frame_pesquisa_tabelas = QFrame(self.frame_3)
        self.frame_pesquisa_tabelas.setObjectName(u"frame_pesquisa_tabelas")
        self.frame_pesquisa_tabelas.setMinimumSize(QSize(0, 40))
        self.frame_pesquisa_tabelas.setMaximumSize(QSize(16777215, 40))
        self.frame_pesquisa_tabelas.setStyleSheet(u"QFrame{\n"
"\n"
"	font: 11pt \"Segoe UI\";\n"
"	\n"
"	color: rgb(75, 63, 241);\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-right: 1px solid rgba(217, 217, 217, 0.80);\n"
"	border-left: 1px solid rgba(217, 217, 217, 0.80);\n"
"	border-top: 1px solid rgba(217, 217, 217, 0.80);\n"
"	border-bottom: 1px solid rgba(217, 217, 217, 0.80);\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    padding: 10px;\n"
"\n"
"}\n"
"\n"
"QLineEdit{\n"
"	font: 700 8pt \"Segoe UI\";\n"
"	color:rgb(120, 120, 120);\n"
"	border: 1px solid rgba(109, 109, 109, 0.60);\n"
"    border-top-left-radius: 5px;\n"
"    border-top-right-radius: 5px;\n"
"    border-bottom-left-radius: 5px;\n"
"    border-bottom-right-radius: 5px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"\n"
"background-color: rgba(195, 205, 255, 0.40)\n"
"}\n"
"")
        self.frame_pesquisa_tabelas.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_pesquisa_tabelas.setFrameShadow(QFrame.Shadow.Raised)
        self.txt_pesquisar_tabela = QLineEdit(self.frame_pesquisa_tabelas)
        self.txt_pesquisar_tabela.setObjectName(u"txt_pesquisar_tabela")
        self.txt_pesquisar_tabela.setGeometry(QRect(0, 0, 374, 38))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_pesquisar_tabela.sizePolicy().hasHeightForWidth())
        self.txt_pesquisar_tabela.setSizePolicy(sizePolicy)
        self.txt_pesquisar_tabela.setMinimumSize(QSize(374, 38))
        self.txt_pesquisar_tabela.setMaximumSize(QSize(374, 38))
        self.txt_pesquisar_tabela.setStyleSheet(u"")
        self.txt_pesquisar_tabela.setCursorPosition(0)

        self.gridLayout_12.addWidget(self.frame_pesquisa_tabelas, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.frame_3)

        self.tabs_lateral_right.addWidget(self.page_conections)
        self.page_duplicados = QWidget()
        self.page_duplicados.setObjectName(u"page_duplicados")
        self.verticalLayout_2 = QVBoxLayout(self.page_duplicados)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_func_duplicados = QFrame(self.page_duplicados)
        self.frame_func_duplicados.setObjectName(u"frame_func_duplicados")
        self.frame_func_duplicados.setMinimumSize(QSize(0, 60))
        self.frame_func_duplicados.setMaximumSize(QSize(16777215, 100))
        self.frame_func_duplicados.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_func_duplicados.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_func_duplicados.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_func_duplicados)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(1, 1, 1, 1)
        self.frame_7 = QFrame(self.frame_func_duplicados)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_7)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_2 = QLabel(self.frame_7)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_5.addWidget(self.label_2)

        self.label_3 = QLabel(self.frame_7)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_5.addWidget(self.label_3)


        self.verticalLayout_4.addWidget(self.frame_7)


        self.verticalLayout_2.addWidget(self.frame_func_duplicados)

        self.frame_tabelas_duplicadas = QFrame(self.page_duplicados)
        self.frame_tabelas_duplicadas.setObjectName(u"frame_tabelas_duplicadas")
        self.frame_tabelas_duplicadas.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_tabelas_duplicadas.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_tabelas_duplicadas.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_13 = QGridLayout(self.frame_tabelas_duplicadas)
        self.gridLayout_13.setSpacing(2)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setContentsMargins(0, 0, 0, 0)
        self.table_duplicados = QTableWidget(self.frame_tabelas_duplicadas)
        self.table_duplicados.setObjectName(u"table_duplicados")
        self.table_duplicados.setStyleSheet(u"QTableWidget{\n"
"	\n"
"	\n"
"	font: 8pt \"Segoe UI\";\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-right: 1px solid rgba(217, 217, 217, 0.80);\n"
"	border-left: 1px solid rgba(217, 217, 217, 0.80);\n"
"	border-top: 1px solid rgba(217, 217, 217, 0.80);\n"
"	border-bottom: 1px solid rgba(217, 217, 217, 0.80);\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    padding: 10px;\n"
"\n"
"}\n"
"\n"
"QTableView:hover{\n"
"	background-color: rgba(195, 205, 255, 0.25);\n"
"}\n"
" QHeaderView::section {\n"
"      background-color: #4b3ff1;\n"
"		border: 1px solid rgba(217, 217, 217, 0.80);\n"
"	font: 700 11pt \"Times New Roman\";\n"
"       color: white;\n"
"\n"
"\n"
"}\n"
"\n"
"\n"
"    QScrollBar:vertical {\n"
"        border: none;\n"
"        background: #F0F0F0; /* Cor de fundo da barra de rolagem */\n"
"        width: 8px;\n"
"        margin: 0px 0px 0px 0px;\n"
"    }\n"
"\n"
"    QScrol"
                        "lBar::handle:vertical {\n"
"        background-color: rgb(195, 205, 255); /* Cor da \"pegada\" da barra de rolagem */\n"
"        min-height: 20px;\n"
"        border-radius: 4px;\n"
"    }\n"
"\n"
"    QScrollBar::add-line:vertical {\n"
"        border: none;\n"
"        background: #CACACA;\n"
"        height: 14px;\n"
"        subcontrol-position: bottom;\n"
"        subcontrol-origin: margin;\n"
"    }\n"
"\n"
"    QScrollBar::sub-line:vertical {\n"
"        border: none;\n"
"        background: #CACACA;\n"
"        height: 14px;\n"
"        subcontrol-position: top;\n"
"        subcontrol-origin: margin;\n"
"    }\n"
"\n"
"    QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"        background: none;\n"
"    }\n"
"\n"
"    QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"        background: none;\n"
"    }\n"
"\n"
"    QScrollBar:horizontal {\n"
"        border: none;\n"
"        background: #F0F0F0; /* Cor de fundo da barra de rolagem */\n"
"        height: 8px;\n"
""
                        "        margin: 0px 0px 0px 0px;\n"
"    }\n"
"\n"
"    QScrollBar::handle:horizontal {\n"
"        background-color: rgb(195, 205, 255); /* Cor da \"pegada\" da barra de rolagem */\n"
"        min-width: 20px;\n"
"        border-radius: 4px;\n"
"    }\n"
"\n"
"    QScrollBar::add-line:horizontal {\n"
"        border: none;\n"
"        background: #CACACA;\n"
"        width: 14px;\n"
"        subcontrol-position: right;\n"
"        subcontrol-origin: margin;\n"
"    }\n"
"\n"
"    QScrollBar::sub-line:horizontal {\n"
"        border: none;\n"
"        background: #CACACA;\n"
"        width: 14px;\n"
"        subcontrol-position: left;\n"
"        subcontrol-origin: margin;\n"
"    }\n"
"\n"
"    QScrollBar::left-arrow:horizontal, QScrollBar::right-arrow:horizontal {\n"
"        background: none;\n"
"    }\n"
"\n"
"    QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"        background: none;\n"
"    }")
        self.table_duplicados.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table_duplicados.verticalHeader().setVisible(False)

        self.gridLayout_13.addWidget(self.table_duplicados, 3, 0, 1, 1)

        self.frame_10 = QFrame(self.frame_tabelas_duplicadas)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(0, 35))
        self.frame_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.bt_exportar_duplicados = QPushButton(self.frame_10)
        self.bt_exportar_duplicados.setObjectName(u"bt_exportar_duplicados")
        self.bt_exportar_duplicados.setMinimumSize(QSize(40, 35))
        self.bt_exportar_duplicados.setMaximumSize(QSize(40, 35))
        self.bt_exportar_duplicados.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.bt_exportar_duplicados.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgba(51, 221, 51, 0.25);\n"
"	border-right: 1px solid rgb(109, 109, 109);\n"
"	border-left: 1px solid rgba(217, 217, 217, 0.80);\n"
"	border-top: 1px solid rgba(217, 217, 217, 0.80);\n"
"	border-bottom: 1px solid rgb(109, 109, 109);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/img/save_data.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_exportar_duplicados.setIcon(icon)
        self.bt_exportar_duplicados.setIconSize(QSize(30, 30))

        self.horizontalLayout_3.addWidget(self.bt_exportar_duplicados, 0, Qt.AlignmentFlag.AlignLeft)

        self.bt_deletar_duplicados = QPushButton(self.frame_10)
        self.bt_deletar_duplicados.setObjectName(u"bt_deletar_duplicados")
        self.bt_deletar_duplicados.setMinimumSize(QSize(40, 35))
        self.bt_deletar_duplicados.setMaximumSize(QSize(40, 35))
        self.bt_deletar_duplicados.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.bt_deletar_duplicados.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgba(255, 52, 52, 0.25);\n"
"	border-right: 1px solid rgb(109, 109, 109);\n"
"	border-left: 1px solid rgba(217, 217, 217, 0.80);\n"
"	border-top: 1px solid rgba(217, 217, 217, 0.80);\n"
"	border-bottom: 1px solid rgb(109, 109, 109);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/img/delete_duplicados.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_deletar_duplicados.setIcon(icon1)
        self.bt_deletar_duplicados.setIconSize(QSize(30, 30))

        self.horizontalLayout_3.addWidget(self.bt_deletar_duplicados)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.gridLayout_13.addWidget(self.frame_10, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.frame_tabelas_duplicadas)

        self.tabs_lateral_right.addWidget(self.page_duplicados)
        self.page_systems = QWidget()
        self.page_systems.setObjectName(u"page_systems")
        self.verticalLayout_6 = QVBoxLayout(self.page_systems)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_titulo_systems = QFrame(self.page_systems)
        self.frame_titulo_systems.setObjectName(u"frame_titulo_systems")
        self.frame_titulo_systems.setMinimumSize(QSize(0, 30))
        self.frame_titulo_systems.setMaximumSize(QSize(16777215, 30))
        self.frame_titulo_systems.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_titulo_systems.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_28 = QGridLayout(self.frame_titulo_systems)
        self.gridLayout_28.setSpacing(0)
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.gridLayout_28.setContentsMargins(5, 0, 0, 0)
        self.label_11 = QLabel(self.frame_titulo_systems)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_28.addWidget(self.label_11, 0, 0, 1, 1)


        self.verticalLayout_6.addWidget(self.frame_titulo_systems)

        self.frame_table_list_systems_query = QFrame(self.page_systems)
        self.frame_table_list_systems_query.setObjectName(u"frame_table_list_systems_query")
        self.frame_table_list_systems_query.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_table_list_systems_query.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_27 = QGridLayout(self.frame_table_list_systems_query)
        self.gridLayout_27.setSpacing(0)
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.gridLayout_27.setContentsMargins(0, 0, 0, 0)
        self.table_list_querys_systems = QTreeView(self.frame_table_list_systems_query)
        self.table_list_querys_systems.setObjectName(u"table_list_querys_systems")
        self.table_list_querys_systems.setFrameShape(QFrame.Shape.StyledPanel)

        self.gridLayout_27.addWidget(self.table_list_querys_systems, 1, 0, 1, 1)

        self.frame_buttons_systems = QFrame(self.frame_table_list_systems_query)
        self.frame_buttons_systems.setObjectName(u"frame_buttons_systems")
        self.frame_buttons_systems.setMinimumSize(QSize(0, 50))
        self.frame_buttons_systems.setMaximumSize(QSize(16777215, 50))
        self.frame_buttons_systems.setStyleSheet(u"QComboBox{\n"
"	\n"
"	font: 700 8pt \"Segoe UI\";\n"
"	color:rgb(120, 120, 120);\n"
"	border: 1px solid rgba(109, 109, 109, 0.60);\n"
"    border-top-left-radius: 5px;\n"
"    border-top-right-radius: 5px;\n"
"    border-bottom-left-radius: 5px;\n"
"    border-bottom-right-radius: 5px;\n"
"}\n"
"\n"
"QComboBox:hover{\n"
"background-color: rgba(195, 205, 255, 0.40)\n"
"}\n"
"\n"
"#bt_execut_query_system{\n"
"	border:none;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"	font: 700 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"#bt_execut_query_system:hover{\n"
"	background-color: rgba(51, 221, 51, 0.25);\n"
"	color:#00ab0e;\n"
"	font: 700 10pt \"Segoe UI\";\n"
"}")
        self.frame_buttons_systems.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_buttons_systems.setFrameShadow(QFrame.Shadow.Raised)
        self.combo_list_systems = QComboBox(self.frame_buttons_systems)
        self.combo_list_systems.setObjectName(u"combo_list_systems")
        self.combo_list_systems.setGeometry(QRect(10, 11, 151, 31))
        self.bt_execut_query_system = QPushButton(self.frame_buttons_systems)
        self.bt_execut_query_system.setObjectName(u"bt_execut_query_system")
        self.bt_execut_query_system.setGeometry(QRect(320, 10, 50, 30))
        self.bt_execut_query_system.setMinimumSize(QSize(50, 30))
        self.bt_execut_query_system.setMaximumSize(QSize(50, 30))
        self.bt_execut_query_system.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/img/play.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_execut_query_system.setIcon(icon2)

        self.gridLayout_27.addWidget(self.frame_buttons_systems, 0, 0, 1, 1)


        self.verticalLayout_6.addWidget(self.frame_table_list_systems_query)

        self.tabs_lateral_right.addWidget(self.page_systems)
        self.page_terminal_sql = QWidget()
        self.page_terminal_sql.setObjectName(u"page_terminal_sql")
        self.verticalLayout_3 = QVBoxLayout(self.page_terminal_sql)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_query_meio = QFrame(self.page_terminal_sql)
        self.frame_query_meio.setObjectName(u"frame_query_meio")
        self.frame_query_meio.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_query_meio.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_11 = QGridLayout(self.frame_query_meio)
        self.gridLayout_11.setSpacing(0)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.txt_terminal_query = QPlainTextEdit(self.frame_query_meio)
        self.txt_terminal_query.setObjectName(u"txt_terminal_query")

        self.gridLayout_11.addWidget(self.txt_terminal_query, 1, 0, 1, 1)

        self.frame_2 = QFrame(self.frame_query_meio)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 40))
        self.frame_2.setMaximumSize(QSize(16777215, 40))
        self.frame_2.setStyleSheet(u"#bt_executar_query{\n"
"	border:none;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"	font: 700 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"#bt_executar_query:hover{\n"
"	background-color: rgba(51, 221, 51, 0.25);\n"
"	color:#00ab0e;\n"
"	font: 700 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"#bt_buscar_file_query{\n"
"border:none;\n"
"}\n"
"\n"
"#bt_buscar_file_query:hover{\n"
"	background-color: rgb(195, 205, 255);\n"
"    border-top-left-radius: 10px;\n"
"    border-top-right-radius: 10px;\n"
"    border-bottom-left-radius: 10px;\n"
"    border-bottom-right-radius: 10px;\n"
"\n"
"}")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.bt_buscar_file_query = QPushButton(self.frame_2)
        self.bt_buscar_file_query.setObjectName(u"bt_buscar_file_query")
        self.bt_buscar_file_query.setGeometry(QRect(3, 5, 50, 30))
        self.bt_buscar_file_query.setMinimumSize(QSize(50, 30))
        self.bt_buscar_file_query.setMaximumSize(QSize(50, 30))
        self.bt_buscar_file_query.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/img/folder.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_buscar_file_query.setIcon(icon3)
        self.bt_buscar_file_query.setIconSize(QSize(25, 25))
        self.bt_executar_query = QPushButton(self.frame_2)
        self.bt_executar_query.setObjectName(u"bt_executar_query")
        self.bt_executar_query.setGeometry(QRect(60, 5, 50, 30))
        self.bt_executar_query.setMinimumSize(QSize(50, 30))
        self.bt_executar_query.setMaximumSize(QSize(50, 30))
        self.bt_executar_query.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.bt_executar_query.setIcon(icon2)

        self.gridLayout_11.addWidget(self.frame_2, 0, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.frame_query_meio)

        self.frame_query_baixo = QFrame(self.page_terminal_sql)
        self.frame_query_baixo.setObjectName(u"frame_query_baixo")
        self.frame_query_baixo.setMinimumSize(QSize(0, 150))
        self.frame_query_baixo.setMaximumSize(QSize(16777215, 150))
        self.frame_query_baixo.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_query_baixo.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_10 = QGridLayout(self.frame_query_baixo)
        self.gridLayout_10.setSpacing(0)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.txt_output_query = QPlainTextEdit(self.frame_query_baixo)
        self.txt_output_query.setObjectName(u"txt_output_query")
        self.txt_output_query.setFrameShape(QFrame.Shape.NoFrame)

        self.gridLayout_10.addWidget(self.txt_output_query, 0, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.frame_query_baixo)

        self.tabs_lateral_right.addWidget(self.page_terminal_sql)

        self.gridLayout_6.addWidget(self.tabs_lateral_right, 1, 0, 1, 1)

        self.frame_buttons_rigt = QFrame(self.widget_right)
        self.frame_buttons_rigt.setObjectName(u"frame_buttons_rigt")
        self.frame_buttons_rigt.setMinimumSize(QSize(0, 40))
        self.frame_buttons_rigt.setMaximumSize(QSize(16777215, 40))
        self.frame_buttons_rigt.setCursor(QCursor(Qt.CursorShape.IBeamCursor))
        self.frame_buttons_rigt.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(195, 205, 255);\n"
"    border-top-left-radius: 10px;\n"
"    border-top-right-radius: 10px;\n"
"    border-bottom-left-radius: 10px;\n"
"    border-bottom-right-radius: 10px;\n"
"\n"
"}")
        self.frame_buttons_rigt.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_buttons_rigt.setFrameShadow(QFrame.Shadow.Raised)
        self.bt_conections = QPushButton(self.frame_buttons_rigt)
        self.bt_conections.setObjectName(u"bt_conections")
        self.bt_conections.setGeometry(QRect(10, 2, 70, 35))
        self.bt_conections.setMinimumSize(QSize(70, 35))
        self.bt_conections.setMaximumSize(QSize(70, 35))
        self.bt_conections.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/icons/img/conexoes2.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_conections.setIcon(icon4)
        self.bt_conections.setIconSize(QSize(25, 25))
        self.bt_terminal_sql = QPushButton(self.frame_buttons_rigt)
        self.bt_terminal_sql.setObjectName(u"bt_terminal_sql")
        self.bt_terminal_sql.setGeometry(QRect(110, 2, 70, 35))
        self.bt_terminal_sql.setMinimumSize(QSize(70, 35))
        self.bt_terminal_sql.setMaximumSize(QSize(70, 35))
        self.bt_terminal_sql.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/icons/img/querys.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_terminal_sql.setIcon(icon5)
        self.bt_terminal_sql.setIconSize(QSize(25, 25))
        self.bt_systems = QPushButton(self.frame_buttons_rigt)
        self.bt_systems.setObjectName(u"bt_systems")
        self.bt_systems.setGeometry(QRect(207, 2, 70, 35))
        self.bt_systems.setMinimumSize(QSize(70, 35))
        self.bt_systems.setMaximumSize(QSize(70, 35))
        self.bt_systems.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon6 = QIcon()
        icon6.addFile(u":/icons/img/systems.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_systems.setIcon(icon6)
        self.bt_systems.setIconSize(QSize(25, 25))
        self.bt_duplicados = QPushButton(self.frame_buttons_rigt)
        self.bt_duplicados.setObjectName(u"bt_duplicados")
        self.bt_duplicados.setGeometry(QRect(299, 2, 70, 35))
        self.bt_duplicados.setMinimumSize(QSize(70, 35))
        self.bt_duplicados.setMaximumSize(QSize(70, 35))
        self.bt_duplicados.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon7 = QIcon()
        icon7.addFile(u":/icons/img/duplicado2.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_duplicados.setIcon(icon7)
        self.bt_duplicados.setIconSize(QSize(25, 25))

        self.gridLayout_6.addWidget(self.frame_buttons_rigt, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.widget_right, 1, 1, 2, 1)

        self.widget_functions_table = QWidget(self.widget)
        self.widget_functions_table.setObjectName(u"widget_functions_table")
        self.widget_functions_table.setMinimumSize(QSize(0, 170))
        self.widget_functions_table.setMaximumSize(QSize(16777215, 200))
        self.widget_functions_table.setStyleSheet(u"#widget_functions_table{\n"
"	background-color: rgba(217, 217, 217, 0.35);\n"
"	border-right: 1px solid rgb(109, 109, 109);\n"
"	border-left: 1px solid rgba(217, 217, 217, 0.80);\n"
"	border-top: 1px solid rgba(217, 217, 217, 0.80);\n"
"	border-bottom: 1px solid rgb(109, 109, 109);\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    padding: 10px;\n"
"\n"
"}")
        self.gridLayout_4 = QGridLayout(self.widget_functions_table)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(8, 8, 8, 8)
        self.stackedWidget_opcoes = QStackedWidget(self.widget_functions_table)
        self.stackedWidget_opcoes.setObjectName(u"stackedWidget_opcoes")
        self.stackedWidget_opcoes.setStyleSheet(u"QStackedWidget{\n"
"	border-right: 1px solid rgba(217, 217, 217, 0.80);\n"
"	border-left: 1px solid rgba(217, 217, 217, 0.80);\n"
"	border-top: 1px solid rgba(217, 217, 217, 0.80);\n"
"	border-bottom: 1px solid rgba(217, 217, 217, 0.80);\n"
"	background-color: rgb(255, 255, 255);\n"
"    border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"   \n"
"}")
        self.page_opcoes_busca = QWidget()
        self.page_opcoes_busca.setObjectName(u"page_opcoes_busca")
        self.frame_analise_inteligente = QFrame(self.page_opcoes_busca)
        self.frame_analise_inteligente.setObjectName(u"frame_analise_inteligente")
        self.frame_analise_inteligente.setGeometry(QRect(515, 9, 800, 160))
        sizePolicy.setHeightForWidth(self.frame_analise_inteligente.sizePolicy().hasHeightForWidth())
        self.frame_analise_inteligente.setSizePolicy(sizePolicy)
        self.frame_analise_inteligente.setMinimumSize(QSize(800, 160))
        self.frame_analise_inteligente.setMaximumSize(QSize(800, 160))
        self.frame_analise_inteligente.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_analise_inteligente.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_analise_inteligente)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.frame_analise_inteligente)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 50))
        self.frame_4.setMaximumSize(QSize(16777215, 50))
        self.frame_4.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_17 = QGridLayout(self.frame_4)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.label_titulo_analise_inteligente = QLabel(self.frame_4)
        self.label_titulo_analise_inteligente.setObjectName(u"label_titulo_analise_inteligente")
        self.label_titulo_analise_inteligente.setStyleSheet(u"font: 700 14pt \"Segoe UI\";\n"
"color: rgb(72, 41, 249);\n"
"qproperty-alignment: 'AlignCenter';")
        self.label_titulo_analise_inteligente.setIndent(6)

        self.gridLayout_17.addWidget(self.label_titulo_analise_inteligente, 0, 0, 1, 1)


        self.verticalLayout_11.addWidget(self.frame_4)

        self.frame_6 = QFrame(self.frame_analise_inteligente)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(0, 115))
        self.frame_6.setMaximumSize(QSize(16777215, 115))
        self.frame_6.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_6)
        self.gridLayout_5.setSpacing(2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(2, 28, 2, 0)
        self.frame_qtda_linhas = QFrame(self.frame_6)
        self.frame_qtda_linhas.setObjectName(u"frame_qtda_linhas")
        self.frame_qtda_linhas.setMinimumSize(QSize(185, 80))
        self.frame_qtda_linhas.setMaximumSize(QSize(185, 80))
        self.frame_qtda_linhas.setStyleSheet(u"#titulo_1{\n"
"	\n"
"	\n"
"	font: 700 10pt \"Segoe UI\";\n"
"	color: rgb(72, 41, 249);\n"
"}\n"
"\n"
"#quantidade_linhas_tabela{\n"
"	\n"
"	font: 700 17pt \"Segoe UI\";\n"
"	color: rgb(72, 41, 249);\n"
"qproperty-alignment: 'AlignCenter';\n"
"}")
        self.frame_qtda_linhas.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_qtda_linhas.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_qtda_linhas)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.titulo_1 = QLabel(self.frame_qtda_linhas)
        self.titulo_1.setObjectName(u"titulo_1")

        self.verticalLayout_10.addWidget(self.titulo_1)

        self.quantidade_linhas_tabela = QLabel(self.frame_qtda_linhas)
        self.quantidade_linhas_tabela.setObjectName(u"quantidade_linhas_tabela")

        self.verticalLayout_10.addWidget(self.quantidade_linhas_tabela)


        self.gridLayout_5.addWidget(self.frame_qtda_linhas, 0, 0, 1, 1)

        self.frame_qtda_duplicados = QFrame(self.frame_6)
        self.frame_qtda_duplicados.setObjectName(u"frame_qtda_duplicados")
        self.frame_qtda_duplicados.setMinimumSize(QSize(185, 80))
        self.frame_qtda_duplicados.setMaximumSize(QSize(185, 80))
        self.frame_qtda_duplicados.setStyleSheet(u"#titulo_4{\n"
"	\n"
"	\n"
"	font: 700 10pt \"Segoe UI\";\n"
"	color: rgb(72, 41, 249);\n"
"}\n"
"\n"
"#quantidade_linhas_duplicadas{\n"
"	\n"
"	font: 700 17pt \"Segoe UI\";\n"
"	color: rgb(72, 41, 249);\n"
"qproperty-alignment: 'AlignCenter';\n"
"}")
        self.frame_qtda_duplicados.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_qtda_duplicados.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_qtda_duplicados)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.titulo_4 = QLabel(self.frame_qtda_duplicados)
        self.titulo_4.setObjectName(u"titulo_4")

        self.verticalLayout_9.addWidget(self.titulo_4)

        self.quantidade_linhas_duplicadas = QLabel(self.frame_qtda_duplicados)
        self.quantidade_linhas_duplicadas.setObjectName(u"quantidade_linhas_duplicadas")

        self.verticalLayout_9.addWidget(self.quantidade_linhas_duplicadas)


        self.gridLayout_5.addWidget(self.frame_qtda_duplicados, 0, 1, 1, 1)

        self.frame_qtda_cod_barras = QFrame(self.frame_6)
        self.frame_qtda_cod_barras.setObjectName(u"frame_qtda_cod_barras")
        self.frame_qtda_cod_barras.setMinimumSize(QSize(185, 80))
        self.frame_qtda_cod_barras.setMaximumSize(QSize(185, 80))
        self.frame_qtda_cod_barras.setStyleSheet(u"#titulo_2{\n"
"	\n"
"	\n"
"	font: 700 10pt \"Segoe UI\";\n"
"	color: rgb(72, 41, 249);\n"
"}\n"
"\n"
"#quantidade_cod_barras{\n"
"	\n"
"	font: 700 17pt \"Segoe UI\";\n"
"	color: rgb(72, 41, 249);\n"
"	qproperty-alignment: 'AlignCenter';\n"
"}")
        self.frame_qtda_cod_barras.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_qtda_cod_barras.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_qtda_cod_barras)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.titulo_2 = QLabel(self.frame_qtda_cod_barras)
        self.titulo_2.setObjectName(u"titulo_2")

        self.verticalLayout_7.addWidget(self.titulo_2)

        self.quantidade_cod_barras = QLabel(self.frame_qtda_cod_barras)
        self.quantidade_cod_barras.setObjectName(u"quantidade_cod_barras")

        self.verticalLayout_7.addWidget(self.quantidade_cod_barras)


        self.gridLayout_5.addWidget(self.frame_qtda_cod_barras, 0, 2, 1, 1)

        self.frame_qtda_caracteres_especiais = QFrame(self.frame_6)
        self.frame_qtda_caracteres_especiais.setObjectName(u"frame_qtda_caracteres_especiais")
        self.frame_qtda_caracteres_especiais.setMinimumSize(QSize(185, 80))
        self.frame_qtda_caracteres_especiais.setMaximumSize(QSize(185, 80))
        self.frame_qtda_caracteres_especiais.setStyleSheet(u"#titulo_3{\n"
"	\n"
"	\n"
"	font: 700 10pt \"Segoe UI\";\n"
"	color: rgb(72, 41, 249);\n"
"}\n"
"\n"
"#quantidade_caracteres_especiais{\n"
"	\n"
"	font: 700 17pt \"Segoe UI\";\n"
"	color: rgb(72, 41, 249);\n"
"	qproperty-alignment: 'AlignCenter';\n"
"}")
        self.frame_qtda_caracteres_especiais.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_qtda_caracteres_especiais.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_qtda_caracteres_especiais)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.titulo_3 = QLabel(self.frame_qtda_caracteres_especiais)
        self.titulo_3.setObjectName(u"titulo_3")

        self.verticalLayout_8.addWidget(self.titulo_3)

        self.quantidade_caracteres_especiais = QLabel(self.frame_qtda_caracteres_especiais)
        self.quantidade_caracteres_especiais.setObjectName(u"quantidade_caracteres_especiais")

        self.verticalLayout_8.addWidget(self.quantidade_caracteres_especiais)


        self.gridLayout_5.addWidget(self.frame_qtda_caracteres_especiais, 0, 3, 1, 1)


        self.verticalLayout_11.addWidget(self.frame_6)

        self.frame_op_busca = QFrame(self.page_opcoes_busca)
        self.frame_op_busca.setObjectName(u"frame_op_busca")
        self.frame_op_busca.setGeometry(QRect(9, 9, 500, 164))
        self.frame_op_busca.setMinimumSize(QSize(500, 0))
        self.frame_op_busca.setMaximumSize(QSize(500, 16777215))
        self.frame_op_busca.setStyleSheet(u"QFrame{\n"
"background-color: rgba(255, 255, 255, 0.80);\n"
"}\n"
"\n"
"QLineEdit{\n"
"	font: 700 8pt \"Segoe UI\";\n"
"	color:rgb(120, 120, 120);\n"
"	border: 1px solid rgba(109, 109, 109, 0.60);\n"
"    border-top-left-radius: 5px;\n"
"    border-top-right-radius: 5px;\n"
"    border-bottom-left-radius: 5px;\n"
"    border-bottom-right-radius: 5px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"\n"
"background-color: rgba(195, 205, 255, 0.40)\n"
"}\n"
"\n"
"QComboBox{\n"
"	\n"
"	font: 700 8pt \"Segoe UI\";\n"
"	color:rgb(120, 120, 120);\n"
"	border: 1px solid rgba(109, 109, 109, 0.60);\n"
"    border-top-left-radius: 5px;\n"
"    border-top-right-radius: 5px;\n"
"    border-bottom-left-radius: 5px;\n"
"    border-bottom-right-radius: 5px;\n"
"}\n"
"\n"
"QComboBox:hover{\n"
"background-color: rgba(195, 205, 255, 0.40)\n"
"}\n"
"\n"
"QPushButton{\n"
"	\n"
"    border-top-left-radius: 5px;\n"
"    border-top-right-radius: 5px;\n"
"    border-bottom-left-radius: 5px;\n"
"    border-bottom-right-radius: 5px;\n"
"	border-rig"
                        "ht: 1px solid rgb(109, 109, 109);\n"
"	border-left: 1px solid rgba(217, 217, 217, 0.80);\n"
"	border-top: 1px solid rgba(217, 217, 217, 0.80);\n"
"	border-bottom: 1px solid rgb(109, 109, 109);\n"
"	font: 700 8pt \"Segoe UI\";\n"
"	color:rgb(120, 120, 120);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(195, 205, 255)\n"
"}")
        self.frame_op_busca.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_op_busca.setFrameShadow(QFrame.Shadow.Raised)
        self.comboBox_opcoes_busca = QComboBox(self.frame_op_busca)
        self.comboBox_opcoes_busca.addItem("")
        self.comboBox_opcoes_busca.addItem("")
        self.comboBox_opcoes_busca.addItem("")
        self.comboBox_opcoes_busca.addItem("")
        self.comboBox_opcoes_busca.addItem("")
        self.comboBox_opcoes_busca.addItem("")
        self.comboBox_opcoes_busca.setObjectName(u"comboBox_opcoes_busca")
        self.comboBox_opcoes_busca.setGeometry(QRect(100, 30, 261, 31))
        self.txt_opcoes_busca = QLineEdit(self.frame_op_busca)
        self.txt_opcoes_busca.setObjectName(u"txt_opcoes_busca")
        self.txt_opcoes_busca.setGeometry(QRect(100, 100, 181, 31))
        self.txt_opcoes_busca.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.txt_opcoes_busca.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.bt_buscar_op_busca = QPushButton(self.frame_op_busca)
        self.bt_buscar_op_busca.setObjectName(u"bt_buscar_op_busca")
        self.bt_buscar_op_busca.setGeometry(QRect(380, 30, 101, 31))
        self.bt_buscar_op_busca.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.combo1_colunas_opcoes_busca = QComboBox(self.frame_op_busca)
        self.combo1_colunas_opcoes_busca.setObjectName(u"combo1_colunas_opcoes_busca")
        self.combo1_colunas_opcoes_busca.setGeometry(QRect(100, 100, 261, 31))
        self.bt_extrair_duplicados = QPushButton(self.frame_op_busca)
        self.bt_extrair_duplicados.setObjectName(u"bt_extrair_duplicados")
        self.bt_extrair_duplicados.setGeometry(QRect(380, 100, 101, 31))
        self.bt_extrair_duplicados.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.stackedWidget_opcoes.addWidget(self.page_opcoes_busca)
        self.page_opcoes_processamento = QWidget()
        self.page_opcoes_processamento.setObjectName(u"page_opcoes_processamento")
        self.frame_opcoes_processamento = QFrame(self.page_opcoes_processamento)
        self.frame_opcoes_processamento.setObjectName(u"frame_opcoes_processamento")
        self.frame_opcoes_processamento.setGeometry(QRect(9, 9, 1307, 164))
        self.frame_opcoes_processamento.setMinimumSize(QSize(0, 0))
        self.frame_opcoes_processamento.setMaximumSize(QSize(16777215, 16777215))
        self.frame_opcoes_processamento.setStyleSheet(u"QFrame{\n"
"background-color: rgba(255, 255, 255, 0.80);\n"
"}\n"
"\n"
"QLineEdit{\n"
"	font: 700 8pt \"Segoe UI\";\n"
"	color:rgb(120, 120, 120);\n"
"	border: 1px solid rgba(109, 109, 109, 0.60);\n"
"    border-top-left-radius: 5px;\n"
"    border-top-right-radius: 5px;\n"
"    border-bottom-left-radius: 5px;\n"
"    border-bottom-right-radius: 5px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"\n"
"background-color: rgba(195, 205, 255, 0.40)\n"
"}\n"
"\n"
"QComboBox{\n"
"	\n"
"	font: 700 8pt \"Segoe UI\";\n"
"	color:rgb(120, 120, 120);\n"
"	border: 1px solid rgba(109, 109, 109, 0.60);\n"
"    border-top-left-radius: 5px;\n"
"    border-top-right-radius: 5px;\n"
"    border-bottom-left-radius: 5px;\n"
"    border-bottom-right-radius: 5px;\n"
"}\n"
"\n"
"QComboBox:hover{\n"
"background-color: rgba(195, 205, 255, 0.40)\n"
"}\n"
"\n"
"QPushButton{\n"
"	\n"
"    border-top-left-radius: 5px;\n"
"    border-top-right-radius: 5px;\n"
"    border-bottom-left-radius: 5px;\n"
"    border-bottom-right-radius: 5px;\n"
"	border-rig"
                        "ht: 1px solid rgb(109, 109, 109);\n"
"	border-left: 1px solid rgba(217, 217, 217, 0.80);\n"
"	border-top: 1px solid rgba(217, 217, 217, 0.80);\n"
"	border-bottom: 1px solid rgb(109, 109, 109);\n"
"	font: 700 8pt \"Segoe UI\";\n"
"	color:rgb(120, 120, 120);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(195, 205, 255)\n"
"}\n"
"\n"
"#bt_retirar_opcoes2{\n"
"	font: 700 10pt \"Segoe UI\";\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"	border-right: 1px solid rgb(109, 109, 109);\n"
"	border-left: 1px solid rgba(217, 217, 217, 0.80);\n"
"	border-top: 1px solid rgba(217, 217, 217, 0.80);\n"
"	border-bottom: 1px solid rgb(109, 109, 109);\n"
"}\n"
"\n"
"#bt_retirar_opcoes2:hover{\n"
"	background-color: rgba(255, 52, 52, 0.25);\n"
"	border-right: 1px solid rgb(109, 109, 109);\n"
"	border-left: 1px solid rgba(217, 217, 217, 0.80);\n"
"	border-top: 1px solid rgba(217, 217, 217, 0.80);\n"
"	borde"
                        "r-bottom: 1px solid rgb(109, 109, 109);\n"
"}\n"
"\n"
"#bt_retirar_opcoes3{\n"
"	font: 700 10pt \"Segoe UI\";\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"	border-right: 1px solid rgb(109, 109, 109);\n"
"	border-left: 1px solid rgba(217, 217, 217, 0.80);\n"
"	border-top: 1px solid rgba(217, 217, 217, 0.80);\n"
"	border-bottom: 1px solid rgb(109, 109, 109);\n"
"}\n"
"\n"
"#bt_retirar_opcoes3:hover{\n"
"	background-color: rgba(255, 52, 52, 0.25);\n"
"	border-right: 1px solid rgb(109, 109, 109);\n"
"	border-left: 1px solid rgba(217, 217, 217, 0.80);\n"
"	border-top: 1px solid rgba(217, 217, 217, 0.80);\n"
"	border-bottom: 1px solid rgb(109, 109, 109);\n"
"}\n"
"\n"
"\n"
"#bt_add_opcoes2{\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"	border-right: 1px solid rgb(109, 109, 109);\n"
"	border"
                        "-left: 1px solid rgba(217, 217, 217, 0.80);\n"
"	border-top: 1px solid rgba(217, 217, 217, 0.80);\n"
"	border-bottom: 1px solid rgb(109, 109, 109);\n"
"	font: 700 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"#bt_add_opcoes2:hover{\n"
"	background-color: rgba(51, 221, 51, 0.25);\n"
"}\n"
"\n"
"#bt_add_opcoes3{\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"	border-right: 1px solid rgb(109, 109, 109);\n"
"	border-left: 1px solid rgba(217, 217, 217, 0.80);\n"
"	border-top: 1px solid rgba(217, 217, 217, 0.80);\n"
"	border-bottom: 1px solid rgb(109, 109, 109);\n"
"	font: 700 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"#bt_add_opcoes3:hover{\n"
"	background-color: rgba(51, 221, 51, 0.25);\n"
"}")
        self.frame_opcoes_processamento.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_opcoes_processamento.setFrameShadow(QFrame.Shadow.Raised)
        self.combo_opcoes_processamento = QComboBox(self.frame_opcoes_processamento)
        self.combo_opcoes_processamento.addItem("")
        self.combo_opcoes_processamento.addItem("")
        self.combo_opcoes_processamento.addItem("")
        self.combo_opcoes_processamento.addItem("")
        self.combo_opcoes_processamento.addItem("")
        self.combo_opcoes_processamento.addItem("")
        self.combo_opcoes_processamento.addItem("")
        self.combo_opcoes_processamento.addItem("")
        self.combo_opcoes_processamento.addItem("")
        self.combo_opcoes_processamento.addItem("")
        self.combo_opcoes_processamento.addItem("")
        self.combo_opcoes_processamento.setObjectName(u"combo_opcoes_processamento")
        self.combo_opcoes_processamento.setGeometry(QRect(30, 10, 441, 31))
        self.combo_opcoes_processamento.setEditable(False)
        self.txt_opcao1_processamento = QLineEdit(self.frame_opcoes_processamento)
        self.txt_opcao1_processamento.setObjectName(u"txt_opcao1_processamento")
        self.txt_opcao1_processamento.setGeometry(QRect(30, 110, 181, 31))
        self.txt_opcao1_processamento.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.txt_opcao2_processamento = QLineEdit(self.frame_opcoes_processamento)
        self.txt_opcao2_processamento.setObjectName(u"txt_opcao2_processamento")
        self.txt_opcao2_processamento.setGeometry(QRect(290, 110, 181, 31))
        self.txt_opcao2_processamento.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.combo1_colunas_processamento = QComboBox(self.frame_opcoes_processamento)
        self.combo1_colunas_processamento.setObjectName(u"combo1_colunas_processamento")
        self.combo1_colunas_processamento.setGeometry(QRect(30, 60, 181, 31))
        self.combo2_colunas_processamento = QComboBox(self.frame_opcoes_processamento)
        self.combo2_colunas_processamento.setObjectName(u"combo2_colunas_processamento")
        self.combo2_colunas_processamento.setGeometry(QRect(290, 60, 181, 31))
        self.bt_setas1 = QPushButton(self.frame_opcoes_processamento)
        self.bt_setas1.setObjectName(u"bt_setas1")
        self.bt_setas1.setGeometry(QRect(220, 110, 60, 31))
        self.bt_setas1.setMinimumSize(QSize(60, 31))
        self.bt_setas1.setMaximumSize(QSize(60, 31))
        self.bt_setas1.setStyleSheet(u"border:none;")
        icon8 = QIcon()
        icon8.addFile(u":/icons/img/setas1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_setas1.setIcon(icon8)
        self.bt_setas1.setIconSize(QSize(40, 28))
        self.txt_opcao3_processamento = QLineEdit(self.frame_opcoes_processamento)
        self.txt_opcao3_processamento.setObjectName(u"txt_opcao3_processamento")
        self.txt_opcao3_processamento.setGeometry(QRect(550, 110, 181, 31))
        self.txt_opcao3_processamento.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.combo3_colunas_processamento = QComboBox(self.frame_opcoes_processamento)
        self.combo3_colunas_processamento.setObjectName(u"combo3_colunas_processamento")
        self.combo3_colunas_processamento.setGeometry(QRect(550, 60, 181, 31))
        self.txt_opcao4_processamento = QLineEdit(self.frame_opcoes_processamento)
        self.txt_opcao4_processamento.setObjectName(u"txt_opcao4_processamento")
        self.txt_opcao4_processamento.setGeometry(QRect(810, 110, 181, 31))
        self.txt_opcao4_processamento.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.combo4_colunas_processamento = QComboBox(self.frame_opcoes_processamento)
        self.combo4_colunas_processamento.setObjectName(u"combo4_colunas_processamento")
        self.combo4_colunas_processamento.setGeometry(QRect(810, 60, 181, 31))
        self.bt_setas2 = QPushButton(self.frame_opcoes_processamento)
        self.bt_setas2.setObjectName(u"bt_setas2")
        self.bt_setas2.setGeometry(QRect(480, 110, 60, 31))
        self.bt_setas2.setMinimumSize(QSize(60, 31))
        self.bt_setas2.setMaximumSize(QSize(60, 31))
        self.bt_setas2.setStyleSheet(u"border:none;")
        self.bt_setas2.setIcon(icon8)
        self.bt_setas2.setIconSize(QSize(40, 28))
        self.bt_setas3 = QPushButton(self.frame_opcoes_processamento)
        self.bt_setas3.setObjectName(u"bt_setas3")
        self.bt_setas3.setGeometry(QRect(740, 110, 60, 31))
        self.bt_setas3.setMinimumSize(QSize(60, 31))
        self.bt_setas3.setMaximumSize(QSize(60, 31))
        self.bt_setas3.setStyleSheet(u"border:none;")
        self.bt_setas3.setIcon(icon8)
        self.bt_setas3.setIconSize(QSize(40, 28))
        self.bt_processamento_de_para = QPushButton(self.frame_opcoes_processamento)
        self.bt_processamento_de_para.setObjectName(u"bt_processamento_de_para")
        self.bt_processamento_de_para.setGeometry(QRect(500, 10, 81, 31))
        self.bt_processamento_de_para.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.bt_add_opcoes2 = QPushButton(self.frame_opcoes_processamento)
        self.bt_add_opcoes2.setObjectName(u"bt_add_opcoes2")
        self.bt_add_opcoes2.setGeometry(QRect(480, 110, 60, 31))
        self.bt_add_opcoes2.setMinimumSize(QSize(60, 31))
        self.bt_add_opcoes2.setMaximumSize(QSize(60, 31))
        self.bt_add_opcoes2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.bt_add_opcoes2.setStyleSheet(u"border:none;")
        icon9 = QIcon()
        icon9.addFile(u":/icons/img/more.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_add_opcoes2.setIcon(icon9)
        self.bt_add_opcoes2.setIconSize(QSize(40, 25))
        self.bt_add_opcoes3 = QPushButton(self.frame_opcoes_processamento)
        self.bt_add_opcoes3.setObjectName(u"bt_add_opcoes3")
        self.bt_add_opcoes3.setGeometry(QRect(740, 110, 60, 31))
        self.bt_add_opcoes3.setMinimumSize(QSize(60, 31))
        self.bt_add_opcoes3.setMaximumSize(QSize(60, 31))
        self.bt_add_opcoes3.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.bt_add_opcoes3.setStyleSheet(u"border:none;")
        self.bt_add_opcoes3.setIcon(icon9)
        self.bt_add_opcoes3.setIconSize(QSize(40, 25))
        self.bt_retirar_opcoes3 = QPushButton(self.frame_opcoes_processamento)
        self.bt_retirar_opcoes3.setObjectName(u"bt_retirar_opcoes3")
        self.bt_retirar_opcoes3.setGeometry(QRect(740, 60, 60, 31))
        self.bt_retirar_opcoes3.setMinimumSize(QSize(60, 31))
        self.bt_retirar_opcoes3.setMaximumSize(QSize(60, 31))
        self.bt_retirar_opcoes3.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.bt_retirar_opcoes3.setStyleSheet(u"border:none;")
        icon10 = QIcon()
        icon10.addFile(u":/icons/img/minus.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_retirar_opcoes3.setIcon(icon10)
        self.bt_retirar_opcoes3.setIconSize(QSize(40, 25))
        self.bt_retirar_opcoes2 = QPushButton(self.frame_opcoes_processamento)
        self.bt_retirar_opcoes2.setObjectName(u"bt_retirar_opcoes2")
        self.bt_retirar_opcoes2.setGeometry(QRect(480, 60, 60, 31))
        self.bt_retirar_opcoes2.setMinimumSize(QSize(60, 31))
        self.bt_retirar_opcoes2.setMaximumSize(QSize(60, 31))
        self.bt_retirar_opcoes2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.bt_retirar_opcoes2.setStyleSheet(u"border:none;")
        self.bt_retirar_opcoes2.setIcon(icon10)
        self.bt_retirar_opcoes2.setIconSize(QSize(40, 25))
        self.combo_opcoes_processamento.raise_()
        self.txt_opcao1_processamento.raise_()
        self.txt_opcao2_processamento.raise_()
        self.combo1_colunas_processamento.raise_()
        self.combo2_colunas_processamento.raise_()
        self.bt_setas1.raise_()
        self.txt_opcao3_processamento.raise_()
        self.combo3_colunas_processamento.raise_()
        self.txt_opcao4_processamento.raise_()
        self.combo4_colunas_processamento.raise_()
        self.bt_setas2.raise_()
        self.bt_setas3.raise_()
        self.bt_processamento_de_para.raise_()
        self.bt_add_opcoes3.raise_()
        self.bt_retirar_opcoes3.raise_()
        self.bt_retirar_opcoes2.raise_()
        self.bt_add_opcoes2.raise_()
        self.stackedWidget_opcoes.addWidget(self.page_opcoes_processamento)

        self.gridLayout_4.addWidget(self.stackedWidget_opcoes, 1, 0, 1, 1)


        self.gridLayout_2.addWidget(self.widget_functions_table, 1, 0, 1, 1)

        self.widget_table_principal = QWidget(self.widget)
        self.widget_table_principal.setObjectName(u"widget_table_principal")
        self.gridLayout_3 = QGridLayout(self.widget_table_principal)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_table_principal = QFrame(self.widget_table_principal)
        self.frame_table_principal.setObjectName(u"frame_table_principal")
        self.frame_table_principal.setStyleSheet(u"#frame_table_principal{\n"
"                \n"
"	background-color: rgba(217, 217, 217, 0.35);\n"
"	border-right: 1px solid rgb(109, 109, 109);\n"
"	border-left: 1px solid rgba(217, 217, 217, 0.80);\n"
"	border-top: 1px solid rgba(217, 217, 217, 0.80);\n"
"	border-bottom: 1px solid rgb(109, 109, 109);\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    padding: 10px;\n"
"}")
        self.frame_table_principal.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_table_principal.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_8 = QGridLayout(self.frame_table_principal)
        self.gridLayout_8.setSpacing(0)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.txt_output_logs = QPlainTextEdit(self.frame_table_principal)
        self.txt_output_logs.setObjectName(u"txt_output_logs")
        self.txt_output_logs.setMaximumSize(QSize(16777215, 30))
        self.txt_output_logs.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.gridLayout_8.addWidget(self.txt_output_logs, 5, 1, 1, 1)

        self.frame_bts_top_table = QFrame(self.frame_table_principal)
        self.frame_bts_top_table.setObjectName(u"frame_bts_top_table")
        self.frame_bts_top_table.setMinimumSize(QSize(0, 50))
        self.frame_bts_top_table.setMaximumSize(QSize(16777215, 50))
        self.frame_bts_top_table.setStyleSheet(u"QFrame{\n"
"\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-right: 1px solid rgba(217, 217, 217, 0.80);\n"
"	border-left: 1px solid rgba(217, 217, 217, 0.80);\n"
"	border-top: 1px solid rgba(217, 217, 217, 0.80);\n"
"	border-bottom: 1px solid rgba(217, 217, 217, 0.80);\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    padding: 10px;\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
"border:none;\n"
"}")
        self.frame_bts_top_table.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_bts_top_table.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_bts_top_table)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 1, 0)
        self.bt_desfazer = QPushButton(self.frame_bts_top_table)
        self.bt_desfazer.setObjectName(u"bt_desfazer")
        self.bt_desfazer.setMinimumSize(QSize(40, 35))
        self.bt_desfazer.setMaximumSize(QSize(40, 35))
        self.bt_desfazer.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"	\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"/*\n"
"	border-right: 1px solid rgb(109, 109, 109);\n"
"	border-left: 1px solid rgba(217, 217, 217, 0.80);\n"
"	border-top: 1px solid rgba(217, 217, 217, 0.80);\n"
"	border-bottom: 1px solid rgb(109, 109, 109);\n"
"	font: 700 10pt \"Segoe UI\";\n"
"*/\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgba(51, 221, 51, 0.25);\n"
"	border-right: 1px solid rgb(109, 109, 109);\n"
"	border-left: 1px solid rgba(217, 217, 217, 0.80);\n"
"	border-top: 1px solid rgba(217, 217, 217, 0.80);\n"
"	border-bottom: 1px solid rgb(109, 109, 109);\n"
"}")
        icon11 = QIcon()
        icon11.addFile(u":/icons/img/desfazer.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_desfazer.setIcon(icon11)
        self.bt_desfazer.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.bt_desfazer, 0, Qt.AlignmentFlag.AlignLeft)

        self.bt_salvar_dados_tabela_principal = QPushButton(self.frame_bts_top_table)
        self.bt_salvar_dados_tabela_principal.setObjectName(u"bt_salvar_dados_tabela_principal")
        self.bt_salvar_dados_tabela_principal.setMinimumSize(QSize(40, 35))
        self.bt_salvar_dados_tabela_principal.setMaximumSize(QSize(40, 35))
        self.bt_salvar_dados_tabela_principal.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.bt_salvar_dados_tabela_principal.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"	\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"/*\n"
"	border-right: 1px solid rgb(109, 109, 109);\n"
"	border-left: 1px solid rgba(217, 217, 217, 0.80);\n"
"	border-top: 1px solid rgba(217, 217, 217, 0.80);\n"
"	border-bottom: 1px solid rgb(109, 109, 109);\n"
"	font: 700 10pt \"Segoe UI\";\n"
"*/\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgba(51, 221, 51, 0.25);\n"
"	border-right: 1px solid rgb(109, 109, 109);\n"
"	border-left: 1px solid rgba(217, 217, 217, 0.80);\n"
"	border-top: 1px solid rgba(217, 217, 217, 0.80);\n"
"	border-bottom: 1px solid rgb(109, 109, 109);\n"
"}")
        self.bt_salvar_dados_tabela_principal.setIcon(icon)
        self.bt_salvar_dados_tabela_principal.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.bt_salvar_dados_tabela_principal)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.bt_reprocesar_csv = QPushButton(self.frame_bts_top_table)
        self.bt_reprocesar_csv.setObjectName(u"bt_reprocesar_csv")
        self.bt_reprocesar_csv.setMinimumSize(QSize(40, 35))
        self.bt_reprocesar_csv.setMaximumSize(QSize(40, 35))
        self.bt_reprocesar_csv.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.bt_reprocesar_csv.setStyleSheet(u"QPushButton{\n"
"	\n"
"	font: 700 9pt \"Segoe UI\";\n"
"	\n"
"	color: rgb(170, 0, 255);\n"
"	border:none;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgba(51, 221, 51, 0.25);\n"
"	border-right: 1px solid rgb(109, 109, 109);\n"
"	border-left: 1px solid rgba(217, 217, 217, 0.80);\n"
"	border-top: 1px solid rgba(217, 217, 217, 0.80);\n"
"	border-bottom: 1px solid rgb(109, 109, 109);\n"
"}")
        icon12 = QIcon()
        icon12.addFile(u":/icons/img/reset.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_reprocesar_csv.setIcon(icon12)
        self.bt_reprocesar_csv.setIconSize(QSize(26, 26))

        self.horizontalLayout.addWidget(self.bt_reprocesar_csv)


        self.gridLayout_8.addWidget(self.frame_bts_top_table, 1, 1, 1, 2, Qt.AlignmentFlag.AlignBottom)

        self.table_principal = QTableWidget(self.frame_table_principal)
        self.table_principal.setObjectName(u"table_principal")
        self.table_principal.setStyleSheet(u"#table_principal{\n"
"	\n"
"	\n"
"	font: 8pt \"Segoe UI\";\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-right: 1px solid rgba(217, 217, 217, 0.80);\n"
"	border-left: 1px solid rgba(217, 217, 217, 0.80);\n"
"	border-top: 1px solid rgba(217, 217, 217, 0.80);\n"
"	border-bottom: 1px solid rgba(217, 217, 217, 0.80);\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    padding: 10px;\n"
"\n"
"}\n"
"\n"
"/*#table_principal:hover{\n"
"	background-color: rgba(195, 205, 255, 0.25);\n"
"}*/\n"
" QHeaderView::section {\n"
"      background-color: #4b3ff1;\n"
"		border: 1px solid rgba(217, 217, 217, 0.80);\n"
"	font: 700 11pt \"Times New Roman\";\n"
"       color: white;\n"
"\n"
"\n"
"}\n"
"\n"
"\n"
"    QScrollBar:vertical {\n"
"        border: none;\n"
"        background: #F0F0F0; /* Cor de fundo da barra de rolagem */\n"
"        width: 8px;\n"
"        margin: 0px 0px 0px 0px;\n"
"    }\n"
"\n"
""
                        "    QScrollBar::handle:vertical {\n"
"        background-color: rgb(195, 205, 255); /* Cor da \"pegada\" da barra de rolagem */\n"
"        min-height: 20px;\n"
"        border-radius: 4px;\n"
"    }\n"
"\n"
"    QScrollBar::add-line:vertical {\n"
"        border: none;\n"
"        background: #CACACA;\n"
"        height: 14px;\n"
"        subcontrol-position: bottom;\n"
"        subcontrol-origin: margin;\n"
"    }\n"
"\n"
"    QScrollBar::sub-line:vertical {\n"
"        border: none;\n"
"        background: #CACACA;\n"
"        height: 14px;\n"
"        subcontrol-position: top;\n"
"        subcontrol-origin: margin;\n"
"    }\n"
"\n"
"    QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"        background: none;\n"
"    }\n"
"\n"
"    QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"        background: none;\n"
"    }\n"
"\n"
"    QScrollBar:horizontal {\n"
"        border: none;\n"
"        background: #F0F0F0; /* Cor de fundo da barra de rolagem */\n"
"        height:"
                        " 8px;\n"
"        margin: 0px 0px 0px 0px;\n"
"    }\n"
"\n"
"    QScrollBar::handle:horizontal {\n"
"        background-color: rgb(195, 205, 255); /* Cor da \"pegada\" da barra de rolagem */\n"
"        min-width: 20px;\n"
"        border-radius: 4px;\n"
"    }\n"
"\n"
"    QScrollBar::add-line:horizontal {\n"
"        border: none;\n"
"        background: #CACACA;\n"
"        width: 14px;\n"
"        subcontrol-position: right;\n"
"        subcontrol-origin: margin;\n"
"    }\n"
"\n"
"    QScrollBar::sub-line:horizontal {\n"
"        border: none;\n"
"        background: #CACACA;\n"
"        width: 14px;\n"
"        subcontrol-position: left;\n"
"        subcontrol-origin: margin;\n"
"    }\n"
"\n"
"    QScrollBar::left-arrow:horizontal, QScrollBar::right-arrow:horizontal {\n"
"        background: none;\n"
"    }\n"
"\n"
"    QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"        background: none;\n"
"    }")
        self.table_principal.setFrameShape(QFrame.Shape.StyledPanel)
        self.table_principal.setFrameShadow(QFrame.Shadow.Sunken)
        self.table_principal.setLineWidth(1)
        self.table_principal.setEditTriggers(QAbstractItemView.EditTrigger.AllEditTriggers)
        self.table_principal.setDragEnabled(True)
        self.table_principal.setDragDropMode(QAbstractItemView.DragDropMode.InternalMove)
        self.table_principal.setAlternatingRowColors(True)
        self.table_principal.setSelectionMode(QAbstractItemView.SelectionMode.ContiguousSelection)
        self.table_principal.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.table_principal.setIconSize(QSize(30, 30))
        self.table_principal.setSortingEnabled(False)
        self.table_principal.horizontalHeader().setProperty("showSortIndicator", True)
        self.table_principal.verticalHeader().setVisible(False)

        self.gridLayout_8.addWidget(self.table_principal, 2, 0, 1, 3)


        self.gridLayout_3.addWidget(self.frame_table_principal, 1, 0, 1, 1)


        self.gridLayout_2.addWidget(self.widget_table_principal, 2, 0, 1, 1)


        self.gridLayout.addWidget(self.widget, 1, 0, 1, 1)

        self.widget_menu = QWidget(self.centralwidget)
        self.widget_menu.setObjectName(u"widget_menu")
        self.widget_menu.setMinimumSize(QSize(0, 80))
        self.widget_menu.setMaximumSize(QSize(16777215, 80))
        self.widget_menu.setStyleSheet(u"#widget_menu{\n"
"	background-color: rgba(217, 217, 217, 0.35);\n"
"	border-right: 1px solid rgba(217, 217, 217, 0.80);\n"
"	border-left: 1px solid rgba(217, 217, 217, 0.80);\n"
"	border-bottom: 1px solid rgba(217, 217, 217, 0.80);\n"
"    border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    padding: 10px;\n"
"}")
        self.gridLayout_7 = QGridLayout(self.widget_menu)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(3, 0, 3, 5)
        self.frame_5 = QFrame(self.widget_menu)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"#frame_5{\n"
"	border-right: 1px solid rgba(217, 217, 217, 0.80);\n"
"	border-left: 1px solid rgba(217, 217, 217, 0.80);\n"
"	border-top: 1px solid rgba(217, 217, 217, 0.80);\n"
"	border-bottom: 1px solid rgba(217, 217, 217, 0.80);\n"
"	background-color: rgb(255, 255, 255);\n"
"    border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"   \n"
"}\n"
"\n"
"\n"
"")
        self.frame_5.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Shadow.Plain)
        self.gridLayout_9 = QGridLayout(self.frame_5)
        self.gridLayout_9.setSpacing(0)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, -1, 0)
        self.frame_11 = QFrame(self.frame_5)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(300, 0))
        self.frame_11.setMaximumSize(QSize(350, 16777215))
        self.frame_11.setStyleSheet(u"")
        self.frame_11.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_14 = QGridLayout(self.frame_11)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.pushButton_2 = QPushButton(self.frame_11)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(250, 0))
        self.pushButton_2.setMaximumSize(QSize(250, 16777215))
        self.pushButton_2.setStyleSheet(u"border:none;")
        icon13 = QIcon()
        icon13.addFile(u":/icons/img/logo_smartMigrate.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_2.setIcon(icon13)
        self.pushButton_2.setIconSize(QSize(200, 100))

        self.gridLayout_14.addWidget(self.pushButton_2, 0, 2, 1, 1)


        self.gridLayout_9.addWidget(self.frame_11, 0, 0, 1, 1, Qt.AlignmentFlag.AlignLeft)

        self.frame_butons_menu = QFrame(self.frame_5)
        self.frame_butons_menu.setObjectName(u"frame_butons_menu")
        self.frame_butons_menu.setStyleSheet(u"")
        self.frame_butons_menu.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_butons_menu.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_butons_menu)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.frame_butons_menu)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(600, 60))
        self.frame_8.setMaximumSize(QSize(600, 60))
        self.frame_8.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(195, 205, 255);\n"
"    border-top-left-radius: 10px;\n"
"    border-top-right-radius: 10px;\n"
"    border-bottom-left-radius: 10px;\n"
"    border-bottom-right-radius: 10px;\n"
"\n"
"}\n"
"\n"
"\n"
"")
        self.frame_8.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.bt_buscar_csv = QPushButton(self.frame_8)
        self.bt_buscar_csv.setObjectName(u"bt_buscar_csv")
        self.bt_buscar_csv.setGeometry(QRect(0, 9, 80, 50))
        self.bt_buscar_csv.setMinimumSize(QSize(80, 50))
        self.bt_buscar_csv.setMaximumSize(QSize(80, 50))
        self.bt_buscar_csv.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.bt_buscar_csv.setToolTipDuration(0)
        self.bt_buscar_csv.setIcon(icon3)
        self.bt_buscar_csv.setIconSize(QSize(40, 40))
        self.bt_conexoes_banco_dados = QPushButton(self.frame_8)
        self.bt_conexoes_banco_dados.setObjectName(u"bt_conexoes_banco_dados")
        self.bt_conexoes_banco_dados.setGeometry(QRect(100, 9, 80, 50))
        self.bt_conexoes_banco_dados.setMinimumSize(QSize(80, 50))
        self.bt_conexoes_banco_dados.setMaximumSize(QSize(50, 60))
        self.bt_conexoes_banco_dados.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.bt_conexoes_banco_dados.setToolTipDuration(0)
        icon14 = QIcon()
        icon14.addFile(u":/icons/img/data_bases.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_conexoes_banco_dados.setIcon(icon14)
        self.bt_conexoes_banco_dados.setIconSize(QSize(40, 40))
        self.bt_pesquisar_dados = QPushButton(self.frame_8)
        self.bt_pesquisar_dados.setObjectName(u"bt_pesquisar_dados")
        self.bt_pesquisar_dados.setGeometry(QRect(200, 9, 80, 50))
        self.bt_pesquisar_dados.setMinimumSize(QSize(80, 50))
        self.bt_pesquisar_dados.setMaximumSize(QSize(80, 50))
        self.bt_pesquisar_dados.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon15 = QIcon()
        icon15.addFile(u":/icons/img/search-data.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_pesquisar_dados.setIcon(icon15)
        self.bt_pesquisar_dados.setIconSize(QSize(40, 40))
        self.bt_processamento_dados = QPushButton(self.frame_8)
        self.bt_processamento_dados.setObjectName(u"bt_processamento_dados")
        self.bt_processamento_dados.setGeometry(QRect(300, 9, 80, 50))
        self.bt_processamento_dados.setMinimumSize(QSize(80, 50))
        self.bt_processamento_dados.setMaximumSize(QSize(80, 50))
        self.bt_processamento_dados.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.bt_processamento_dados.setToolTipDuration(0)
        icon16 = QIcon()
        icon16.addFile(u":/icons/img/data-processing.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_processamento_dados.setIcon(icon16)
        self.bt_processamento_dados.setIconSize(QSize(40, 40))

        self.horizontalLayout_2.addWidget(self.frame_8, 0, Qt.AlignmentFlag.AlignLeft)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.gridLayout_9.addWidget(self.frame_butons_menu, 0, 1, 1, 1)


        self.gridLayout_7.addWidget(self.frame_5, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.widget_menu, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabs_lateral_right.setCurrentIndex(0)
        self.stackedWidget_opcoes.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.txt_servidor_data_base.setInputMask("")
        self.txt_servidor_data_base.setText("")
        self.txt_servidor_data_base.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Servidor\\inst\u00e2ncia", None))
        self.txt_data_base_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"data base", None))
        self.txt_port_data_base.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Porta", None))
        self.combo_data_base_list.setItemText(0, QCoreApplication.translate("MainWindow", u"SQL Server", None))
        self.combo_data_base_list.setItemText(1, QCoreApplication.translate("MainWindow", u"MySQL", None))
        self.combo_data_base_list.setItemText(2, QCoreApplication.translate("MainWindow", u"PostgreSQL", None))
        self.combo_data_base_list.setItemText(3, QCoreApplication.translate("MainWindow", u"SQLite", None))
        self.combo_data_base_list.setItemText(4, QCoreApplication.translate("MainWindow", u"Firebird", None))
        self.combo_data_base_list.setItemText(5, QCoreApplication.translate("MainWindow", u"Firebird arquivos .DBF", None))
        self.combo_data_base_list.setItemText(6, QCoreApplication.translate("MainWindow", u"Hiper", None))
        self.combo_data_base_list.setItemText(7, QCoreApplication.translate("MainWindow", u"Etrade", None))

        self.txt_user_data_base.setPlaceholderText(QCoreApplication.translate("MainWindow", u"User", None))
        self.txt_password_data_base.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.titulo_conexoes.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:8pt; font-weight:700; color:#4b3ff1;\">Conecte-se a um bando de dados</span></p></body></html>", None))
        self.bt_conectar_data_base.setText(QCoreApplication.translate("MainWindow", u"Conectar", None))
        self.bt_buscar_sqlite.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
#if QT_CONFIG(accessibility)
        self.treeView_lista_tabelas.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"3", None))
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(tooltip)
        self.bt_mostra_dados_tabelas.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt; color:#4b3ff1;\">Ver dados da tabelas</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.bt_mostra_dados_tabelas.setText(QCoreApplication.translate("MainWindow", u"Mostrar Tabela", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Clique para mostrar os dados da tabela</p></body></html>", None))
        self.txt_pesquisar_tabela.setPlaceholderText(QCoreApplication.translate("MainWindow", u"  Pesquisar por tabela", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:700;\">DADOS DUPLICADOS</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Para lidar com os dados duplicados selecione uma das op\u00e7\u00f5es.</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.bt_exportar_duplicados.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt; color:#4b3ff1;\">Exportar duplicados</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.bt_exportar_duplicados.setText("")
#if QT_CONFIG(tooltip)
        self.bt_deletar_duplicados.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#4b3ff1;\">Deletar duplicados</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.bt_deletar_duplicados.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:8pt; font-weight:700; color:#4b3ff1;\">Lista de Sistemas catalogados.</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.bt_execut_query_system.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt; color:#00ab0e;\">Executar Script</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.bt_execut_query_system.setText("")
#if QT_CONFIG(tooltip)
        self.bt_buscar_file_query.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt; color:#4829f9;\">Buscar Script</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.bt_buscar_file_query.setText("")
#if QT_CONFIG(tooltip)
        self.bt_executar_query.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt; color:#00ab0e;\">Executar Query</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.bt_executar_query.setText("")
#if QT_CONFIG(tooltip)
        self.bt_conections.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt; color:#4b3ff1;\">Data Base Conect</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.bt_conections.setText("")
#if QT_CONFIG(tooltip)
        self.bt_terminal_sql.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt; color:#4b3ff1;\">Terminal SQL</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.bt_terminal_sql.setText("")
#if QT_CONFIG(tooltip)
        self.bt_systems.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt; color:#4b3ff1;\">Sistemas Catalogados</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.bt_systems.setText("")
#if QT_CONFIG(tooltip)
        self.bt_duplicados.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt; color:#4b3ff1;\">Dados Duplicados</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.bt_duplicados.setText("")
        self.label_titulo_analise_inteligente.setText("")
        self.titulo_1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:700; color:#4829f9;\">Qtda. Linhas</span></p></body></html>", None))
        self.quantidade_linhas_tabela.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.titulo_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Linhas Duplicadas</p></body></html>", None))
        self.quantidade_linhas_duplicadas.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.titulo_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">C\u00f3d. de barras Duplicados</p></body></html>", None))
        self.quantidade_cod_barras.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.titulo_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#4829f9;\">Caracteres Especiais</span></p></body></html>", None))
        self.quantidade_caracteres_especiais.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.comboBox_opcoes_busca.setItemText(0, QCoreApplication.translate("MainWindow", u"Op\u00e7\u00f5es de busca", None))
        self.comboBox_opcoes_busca.setItemText(1, QCoreApplication.translate("MainWindow", u"Analise inteligente", None))
        self.comboBox_opcoes_busca.setItemText(2, QCoreApplication.translate("MainWindow", u"Buscar por NCM", None))
        self.comboBox_opcoes_busca.setItemText(3, QCoreApplication.translate("MainWindow", u"NCM Inv\u00e1lido", None))
        self.comboBox_opcoes_busca.setItemText(4, QCoreApplication.translate("MainWindow", u"Tudo que cont\u00e9m", None))
        self.comboBox_opcoes_busca.setItemText(5, QCoreApplication.translate("MainWindow", u"Duplicados", None))

        self.bt_buscar_op_busca.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.combo1_colunas_opcoes_busca.setCurrentText("")
        self.combo1_colunas_opcoes_busca.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Selecione a coluna que desejada analizar", None))
        self.bt_extrair_duplicados.setText(QCoreApplication.translate("MainWindow", u"Extrair", None))
        self.combo_opcoes_processamento.setItemText(0, QCoreApplication.translate("MainWindow", u"Op\u00e7\u00f5es de Processamento", None))
        self.combo_opcoes_processamento.setItemText(1, QCoreApplication.translate("MainWindow", u"Buscar valores negativos e mudar para zero", None))
        self.combo_opcoes_processamento.setItemText(2, QCoreApplication.translate("MainWindow", u"Filtrar por coluna e copiar todas a linhas que contenham", None))
        self.combo_opcoes_processamento.setItemText(3, QCoreApplication.translate("MainWindow", u"Formatar colunas com valores do tipo moeda", None))
        self.combo_opcoes_processamento.setItemText(4, QCoreApplication.translate("MainWindow", u"Formatar c\u00f3digos de barras", None))
        self.combo_opcoes_processamento.setItemText(5, QCoreApplication.translate("MainWindow", u"Formatar n\u00famero de telefone", None))
        self.combo_opcoes_processamento.setItemText(6, QCoreApplication.translate("MainWindow", u"Formatar CPF", None))
        self.combo_opcoes_processamento.setItemText(7, QCoreApplication.translate("MainWindow", u"Formatar CNPJ", None))
        self.combo_opcoes_processamento.setItemText(8, QCoreApplication.translate("MainWindow", u"Substituir NCM", None))
        self.combo_opcoes_processamento.setItemText(9, QCoreApplication.translate("MainWindow", u"Se Coluna A cont\u00e9m, Coluna B recebe...", None))
        self.combo_opcoes_processamento.setItemText(10, QCoreApplication.translate("MainWindow", u"Tudo que cont\u00e9m mude para", None))

        self.combo1_colunas_processamento.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Selecione uma Coluna", None))
        self.combo2_colunas_processamento.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Selecione uma Coluna", None))
        self.bt_setas1.setText("")
        self.combo3_colunas_processamento.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Selecione uma Coluna", None))
        self.combo4_colunas_processamento.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Selecione uma Coluna", None))
        self.bt_setas2.setText("")
        self.bt_setas3.setText("")
        self.bt_processamento_de_para.setText(QCoreApplication.translate("MainWindow", u"Executar", None))
        self.bt_add_opcoes2.setText("")
        self.bt_add_opcoes3.setText("")
        self.bt_retirar_opcoes3.setText("")
        self.bt_retirar_opcoes2.setText("")
#if QT_CONFIG(tooltip)
        self.bt_desfazer.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt; color:#4b3ff1;\">Desfazer</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.bt_desfazer.setText("")
#if QT_CONFIG(tooltip)
        self.bt_salvar_dados_tabela_principal.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt; color:#4b3ff1;\">Exportar dados</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.bt_salvar_dados_tabela_principal.setText("")
#if QT_CONFIG(tooltip)
        self.bt_reprocesar_csv.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt; color:#4b3ff1;\">Reprocessar</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.bt_reprocesar_csv.setText("")
        self.pushButton_2.setText("")
#if QT_CONFIG(tooltip)
        self.bt_buscar_csv.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt; color:#4b3ff1;\">Arquivo</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.bt_buscar_csv.setText("")
#if QT_CONFIG(tooltip)
        self.bt_conexoes_banco_dados.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt; color:#4b3ff1;\">Data Bases</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.bt_conexoes_banco_dados.setText("")
#if QT_CONFIG(tooltip)
        self.bt_pesquisar_dados.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt; color:#4b3ff1;\">Filtros de pesquisas</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.bt_pesquisar_dados.setText("")
#if QT_CONFIG(tooltip)
        self.bt_processamento_dados.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt; color:#4b3ff1;\">Altera\u00e7\u00f5es</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.bt_processamento_dados.setText("")
    # retranslateUi

