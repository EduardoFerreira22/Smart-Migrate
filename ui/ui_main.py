# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainVcvoCF.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)
from . import icon_rc

class Ui_PrincipalWindow(object):
    def setupUi(self, PrincipalWindow):
        if not PrincipalWindow.objectName():
            PrincipalWindow.setObjectName(u"PrincipalWindow")
        PrincipalWindow.setEnabled(True)
        PrincipalWindow.resize(1400, 800)
        PrincipalWindow.setMinimumSize(QSize(1400, 800))
        PrincipalWindow.setMaximumSize(QSize(1400, 800))
        PrincipalWindow.setStyleSheet(u"#centralwidget  {\n"
"	border: 1px solid rgba(109, 109, 109, 0.30);\n"
"	 border-top-left-radius: 5px;\n"
"    border-top-right-radius: 5px;\n"
"    border-bottom-left-radius: 5px;\n"
"    border-bottom-right-radius: 5px;\n"
"}\n"
"\n"
"\n"
"\n"
"#frm_menu_bar QPushButton{\n"
"	border: none;\n"
"}\n"
"\n"
"#frm_buttons_menu QPushButton{\n"
"	border:none;\n"
"}\n"
"\n"
"#frm_buttons_menu QPushButton:hover{\n"
"	border:none;\n"
"	font: 700 9pt \"Segoe UI\";\n"
"	background-color: rgba(226, 226, 226, 0.20);\n"
"	border: 1px solid rgba(109, 109, 109, 0.30);\n"
"    border-top-left-radius: 5px;\n"
"    border-top-right-radius: 5px;\n"
"    border-bottom-left-radius: 5px;\n"
"    border-bottom-right-radius: 5px;\n"
"}\n"
"\n"
"#btn_close_window:hover{\n"
"	border: none;\n"
"	background-color: rgb(196, 43, 28);\n"
"}\n"
"\n"
"#btn_maximize:hover{\n"
"	border: none;\n"
"	background-color: rgb(226, 226, 226);\n"
"}\n"
"\n"
"#btn_minimize:hover{\n"
"	border: none;\n"
"	background-color: rgb(226, 226, 226);\n"
"}\n"
"\n"
""
                        "#btn_executar_pesquisas{\n"
"	border:none;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"#table_principal{\n"
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
""
                        "        width: 8px;\n"
"        margin: 0px 0px 0px 0px;\n"
"    }\n"
"\n"
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
"        bac"
                        "kground: #F0F0F0; /* Cor de fundo da barra de rolagem */\n"
"        height: 8px;\n"
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
        self.centralwidget = QWidget(PrincipalWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frm_menu_bar = QFrame(self.frame)
        self.frm_menu_bar.setObjectName(u"frm_menu_bar")
        self.frm_menu_bar.setMinimumSize(QSize(0, 40))
        self.frm_menu_bar.setMaximumSize(QSize(16777215, 40))
        self.frm_menu_bar.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_menu_bar.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frm_menu_bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 2)
        self.pushButton = QPushButton(self.frm_menu_bar)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(160, 40))
        self.pushButton.setMaximumSize(QSize(160, 40))
        icon = QIcon()
        icon.addFile(u":/icons/icons/logo_smartMigrate.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(150, 200))

        self.horizontalLayout.addWidget(self.pushButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_minimize = QPushButton(self.frm_menu_bar)
        self.btn_minimize.setObjectName(u"btn_minimize")
        self.btn_minimize.setMinimumSize(QSize(50, 35))
        self.btn_minimize.setMaximumSize(QSize(50, 35))
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/minus.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_minimize.setIcon(icon1)

        self.horizontalLayout.addWidget(self.btn_minimize)

        self.btn_maximize = QPushButton(self.frm_menu_bar)
        self.btn_maximize.setObjectName(u"btn_maximize")
        self.btn_maximize.setMinimumSize(QSize(50, 35))
        self.btn_maximize.setMaximumSize(QSize(50, 35))
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/maximize.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_maximize.setIcon(icon2)

        self.horizontalLayout.addWidget(self.btn_maximize)

        self.btn_close_window = QPushButton(self.frm_menu_bar)
        self.btn_close_window.setObjectName(u"btn_close_window")
        self.btn_close_window.setMinimumSize(QSize(50, 35))
        self.btn_close_window.setMaximumSize(QSize(50, 35))
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/close.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_close_window.setIcon(icon3)
        self.btn_close_window.setIconSize(QSize(16, 16))

        self.horizontalLayout.addWidget(self.btn_close_window)


        self.verticalLayout_2.addWidget(self.frm_menu_bar)

        self.frm_buttons_menu = QFrame(self.frame)
        self.frm_buttons_menu.setObjectName(u"frm_buttons_menu")
        self.frm_buttons_menu.setMinimumSize(QSize(0, 50))
        self.frm_buttons_menu.setMaximumSize(QSize(16777215, 50))
        self.frm_buttons_menu.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_buttons_menu.setFrameShadow(QFrame.Shadow.Raised)
        self.btn_importar_file = QPushButton(self.frm_buttons_menu)
        self.btn_importar_file.setObjectName(u"btn_importar_file")
        self.btn_importar_file.setGeometry(QRect(50, 10, 150, 35))
        self.btn_importar_file.setMinimumSize(QSize(150, 35))
        self.btn_importar_file.setMaximumSize(QSize(150, 35))
        self.btn_importar_file.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/file.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_importar_file.setIcon(icon4)
        self.btn_importar_file.setIconSize(QSize(25, 25))
        self.btn_opcoes_pesquisas = QPushButton(self.frm_buttons_menu)
        self.btn_opcoes_pesquisas.setObjectName(u"btn_opcoes_pesquisas")
        self.btn_opcoes_pesquisas.setGeometry(QRect(210, 10, 150, 35))
        self.btn_opcoes_pesquisas.setMinimumSize(QSize(150, 35))
        self.btn_opcoes_pesquisas.setMaximumSize(QSize(150, 35))
        self.btn_opcoes_pesquisas.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/search.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_opcoes_pesquisas.setIcon(icon5)
        self.btn_opcoes_pesquisas.setIconSize(QSize(25, 25))
        self.btn_opcoes_processamento = QPushButton(self.frm_buttons_menu)
        self.btn_opcoes_processamento.setObjectName(u"btn_opcoes_processamento")
        self.btn_opcoes_processamento.setGeometry(QRect(370, 10, 180, 35))
        self.btn_opcoes_processamento.setMinimumSize(QSize(180, 35))
        self.btn_opcoes_processamento.setMaximumSize(QSize(180, 35))
        self.btn_opcoes_processamento.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/data-processing.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_opcoes_processamento.setIcon(icon6)
        self.btn_opcoes_processamento.setIconSize(QSize(25, 25))
        self.btn_opcoes_conexoes_db = QPushButton(self.frm_buttons_menu)
        self.btn_opcoes_conexoes_db.setObjectName(u"btn_opcoes_conexoes_db")
        self.btn_opcoes_conexoes_db.setGeometry(QRect(570, 10, 150, 35))
        self.btn_opcoes_conexoes_db.setMinimumSize(QSize(150, 35))
        self.btn_opcoes_conexoes_db.setMaximumSize(QSize(150, 35))
        self.btn_opcoes_conexoes_db.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/data.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_opcoes_conexoes_db.setIcon(icon7)
        self.btn_opcoes_conexoes_db.setIconSize(QSize(35, 35))
        self.btn_opcoes_conexoes_db.setAutoDefault(False)
        self.btn_salvar_geral = QPushButton(self.frm_buttons_menu)
        self.btn_salvar_geral.setObjectName(u"btn_salvar_geral")
        self.btn_salvar_geral.setGeometry(QRect(0, 10, 45, 35))
        self.btn_salvar_geral.setMinimumSize(QSize(45, 35))
        self.btn_salvar_geral.setMaximumSize(QSize(45, 35))
        self.btn_salvar_geral.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/save-as.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_salvar_geral.setIcon(icon8)
        self.btn_salvar_geral.setIconSize(QSize(25, 25))
        self.btn_salvar_geral.setAutoDefault(False)
        self.line = QFrame(self.frm_buttons_menu)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(50, 10, 3, 35))
        self.line.setMinimumSize(QSize(0, 35))
        self.line.setMaximumSize(QSize(16777215, 35))
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_2.addWidget(self.frm_buttons_menu)

        self.frm_layout_geral = QFrame(self.frame)
        self.frm_layout_geral.setObjectName(u"frm_layout_geral")
        self.frm_layout_geral.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_layout_geral.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frm_layout_geral)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(2)
        self.gridLayout.setContentsMargins(-1, -1, -1, 2)
        self.frm_setas_titulo = QFrame(self.frm_layout_geral)
        self.frm_setas_titulo.setObjectName(u"frm_setas_titulo")
        self.frm_setas_titulo.setMinimumSize(QSize(0, 40))
        self.frm_setas_titulo.setMaximumSize(QSize(16777215, 40))
        self.frm_setas_titulo.setFrameShape(QFrame.Shape.NoFrame)
        self.frm_setas_titulo.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frm_setas_titulo)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(2, 0, 2, 0)
        self.btn_voltar_pagina = QPushButton(self.frm_setas_titulo)
        self.btn_voltar_pagina.setObjectName(u"btn_voltar_pagina")
        self.btn_voltar_pagina.setMinimumSize(QSize(0, 30))
        self.btn_voltar_pagina.setMaximumSize(QSize(16777215, 30))
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/voltar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_voltar_pagina.setIcon(icon9)

        self.horizontalLayout_4.addWidget(self.btn_voltar_pagina, 0, Qt.AlignmentFlag.AlignLeft)

        self.lb_titulos_tabelas = QLabel(self.frm_setas_titulo)
        self.lb_titulos_tabelas.setObjectName(u"lb_titulos_tabelas")

        self.horizontalLayout_4.addWidget(self.lb_titulos_tabelas)

        self.btn_proxima_pagina = QPushButton(self.frm_setas_titulo)
        self.btn_proxima_pagina.setObjectName(u"btn_proxima_pagina")
        self.btn_proxima_pagina.setMinimumSize(QSize(0, 30))
        self.btn_proxima_pagina.setMaximumSize(QSize(16777215, 30))
        icon10 = QIcon()
        icon10.addFile(u":/icons/icons/proxima.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_proxima_pagina.setIcon(icon10)

        self.horizontalLayout_4.addWidget(self.btn_proxima_pagina, 0, Qt.AlignmentFlag.AlignRight)


        self.gridLayout.addWidget(self.frm_setas_titulo, 2, 0, 1, 1)

        self.frm_bottom_bar = QFrame(self.frm_layout_geral)
        self.frm_bottom_bar.setObjectName(u"frm_bottom_bar")
        self.frm_bottom_bar.setMinimumSize(QSize(0, 30))
        self.frm_bottom_bar.setMaximumSize(QSize(16777215, 30))
        self.frm_bottom_bar.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_bottom_bar.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout.addWidget(self.frm_bottom_bar, 5, 0, 1, 2)

        self.frm_geral_tables = QFrame(self.frm_layout_geral)
        self.frm_geral_tables.setObjectName(u"frm_geral_tables")
        self.frm_geral_tables.setMinimumSize(QSize(0, 0))
        self.frm_geral_tables.setMaximumSize(QSize(16777215, 16777215))
        self.frm_geral_tables.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_geral_tables.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frm_geral_tables)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget_tables = QStackedWidget(self.frm_geral_tables)
        self.stackedWidget_tables.setObjectName(u"stackedWidget_tables")
        self.stackedWidget_tables.setFrameShape(QFrame.Shape.StyledPanel)
        self.stackedWidget_tables.setFrameShadow(QFrame.Shadow.Raised)
        self.page_principal = QWidget()
        self.page_principal.setObjectName(u"page_principal")
        self.verticalLayout_5 = QVBoxLayout(self.page_principal)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frm_functions_table_principal = QFrame(self.page_principal)
        self.frm_functions_table_principal.setObjectName(u"frm_functions_table_principal")
        self.frm_functions_table_principal.setMinimumSize(QSize(0, 40))
        self.frm_functions_table_principal.setMaximumSize(QSize(16777215, 40))
        self.frm_functions_table_principal.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_functions_table_principal.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_5.addWidget(self.frm_functions_table_principal)

        self.frm_combos_heads = QFrame(self.page_principal)
        self.frm_combos_heads.setObjectName(u"frm_combos_heads")
        self.frm_combos_heads.setMinimumSize(QSize(0, 40))
        self.frm_combos_heads.setMaximumSize(QSize(16777215, 40))
        self.frm_combos_heads.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_combos_heads.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frm_combos_heads)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(5, 2, 5, 2)
        self.bombo_colunas_1 = QComboBox(self.frm_combos_heads)
        self.bombo_colunas_1.setObjectName(u"bombo_colunas_1")
        self.bombo_colunas_1.setMinimumSize(QSize(100, 25))
        self.bombo_colunas_1.setMaximumSize(QSize(100, 25))

        self.horizontalLayout_2.addWidget(self.bombo_colunas_1, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_5.addWidget(self.frm_combos_heads)

        self.table_principal = QTableWidget(self.page_principal)
        self.table_principal.setObjectName(u"table_principal")
        self.table_principal.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table_principal.setDragEnabled(True)
        self.table_principal.setAlternatingRowColors(True)
        self.table_principal.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.table_principal.horizontalHeader().setProperty(u"showSortIndicator", True)
        self.table_principal.verticalHeader().setVisible(False)

        self.verticalLayout_5.addWidget(self.table_principal)

        self.stackedWidget_tables.addWidget(self.page_principal)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget_tables.addWidget(self.page_2)

        self.verticalLayout_3.addWidget(self.stackedWidget_tables)


        self.gridLayout.addWidget(self.frm_geral_tables, 3, 0, 1, 1)

        self.frame_opcoes_busca_processamento = QFrame(self.frm_layout_geral)
        self.frame_opcoes_busca_processamento.setObjectName(u"frame_opcoes_busca_processamento")
        self.frame_opcoes_busca_processamento.setMinimumSize(QSize(0, 120))
        self.frame_opcoes_busca_processamento.setMaximumSize(QSize(16777215, 120))
        self.frame_opcoes_busca_processamento.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_opcoes_busca_processamento.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_opcoes_busca_processamento)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.page_opcoes_busca = QFrame(self.frame_opcoes_busca_processamento)
        self.page_opcoes_busca.setObjectName(u"page_opcoes_busca")
        self.page_opcoes_busca.setFrameShape(QFrame.Shape.StyledPanel)
        self.page_opcoes_busca.setFrameShadow(QFrame.Shadow.Raised)
        self.widget = QWidget(self.page_opcoes_busca)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 10, 341, 101))
        self.gridLayout_3 = QGridLayout(self.widget)
        self.gridLayout_3.setSpacing(2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.txt_op_busca1 = QLineEdit(self.widget)
        self.txt_op_busca1.setObjectName(u"txt_op_busca1")
        self.txt_op_busca1.setMinimumSize(QSize(0, 30))
        self.txt_op_busca1.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_3.addWidget(self.txt_op_busca1, 1, 0, 1, 1)

        self.combo_opcoes_busca = QComboBox(self.widget)
        self.combo_opcoes_busca.setObjectName(u"combo_opcoes_busca")
        self.combo_opcoes_busca.setMinimumSize(QSize(0, 30))
        self.combo_opcoes_busca.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_3.addWidget(self.combo_opcoes_busca, 0, 0, 1, 1)

        self.btn_extrair_duplicados = QPushButton(self.widget)
        self.btn_extrair_duplicados.setObjectName(u"btn_extrair_duplicados")
        self.btn_extrair_duplicados.setMinimumSize(QSize(0, 30))
        self.btn_extrair_duplicados.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_3.addWidget(self.btn_extrair_duplicados, 1, 1, 1, 1)

        self.btn_executar_pesquisas = QPushButton(self.widget)
        self.btn_executar_pesquisas.setObjectName(u"btn_executar_pesquisas")
        self.btn_executar_pesquisas.setMinimumSize(QSize(30, 30))
        self.btn_executar_pesquisas.setMaximumSize(QSize(16777215, 30))
        self.btn_executar_pesquisas.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon11 = QIcon()
        icon11.addFile(u":/icons/icons/btn_buscar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_executar_pesquisas.setIcon(icon11)
        self.btn_executar_pesquisas.setIconSize(QSize(18, 18))

        self.gridLayout_3.addWidget(self.btn_executar_pesquisas, 0, 1, 1, 1, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_6.addWidget(self.page_opcoes_busca)

        self.page_opcoes_processamento = QFrame(self.frame_opcoes_busca_processamento)
        self.page_opcoes_processamento.setObjectName(u"page_opcoes_processamento")
        self.page_opcoes_processamento.setMinimumSize(QSize(0, 120))
        self.page_opcoes_processamento.setMaximumSize(QSize(16777215, 120))
        self.page_opcoes_processamento.setFrameShape(QFrame.Shape.StyledPanel)
        self.page_opcoes_processamento.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.page_opcoes_processamento)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.frm_processamento1 = QFrame(self.page_opcoes_processamento)
        self.frm_processamento1.setObjectName(u"frm_processamento1")
        self.frm_processamento1.setMinimumSize(QSize(200, 0))
        self.frm_processamento1.setMaximumSize(QSize(200, 16777215))
        self.frm_processamento1.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_processamento1.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frm_processamento1)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.comboBox = QComboBox(self.frm_processamento1)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(0, 30))
        self.comboBox.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_4.addWidget(self.comboBox)

        self.btn_executar_processamento = QPushButton(self.frm_processamento1)
        self.btn_executar_processamento.setObjectName(u"btn_executar_processamento")
        self.btn_executar_processamento.setMinimumSize(QSize(0, 30))
        self.btn_executar_processamento.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_4.addWidget(self.btn_executar_processamento, 0, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout_5.addWidget(self.frm_processamento1)

        self.frm_processamento2 = QFrame(self.page_opcoes_processamento)
        self.frm_processamento2.setObjectName(u"frm_processamento2")
        self.frm_processamento2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_processamento2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.frm_processamento2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.cbx_coluna_processamento4 = QComboBox(self.frm_processamento2)
        self.cbx_coluna_processamento4.setObjectName(u"cbx_coluna_processamento4")
        self.cbx_coluna_processamento4.setMinimumSize(QSize(180, 30))
        self.cbx_coluna_processamento4.setMaximumSize(QSize(180, 30))

        self.gridLayout_2.addWidget(self.cbx_coluna_processamento4, 0, 10, 1, 1)

        self.bt_add_combo1 = QPushButton(self.frm_processamento2)
        self.bt_add_combo1.setObjectName(u"bt_add_combo1")
        self.bt_add_combo1.setMinimumSize(QSize(0, 35))
        self.bt_add_combo1.setMaximumSize(QSize(16777215, 35))
        icon12 = QIcon()
        icon12.addFile(u":/icons/icons/more.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_add_combo1.setIcon(icon12)
        self.bt_add_combo1.setIconSize(QSize(25, 25))

        self.gridLayout_2.addWidget(self.bt_add_combo1, 2, 7, 1, 1)

        self.txt_coluna_processamento2 = QLineEdit(self.frm_processamento2)
        self.txt_coluna_processamento2.setObjectName(u"txt_coluna_processamento2")
        self.txt_coluna_processamento2.setMinimumSize(QSize(180, 30))
        self.txt_coluna_processamento2.setMaximumSize(QSize(180, 30))

        self.gridLayout_2.addWidget(self.txt_coluna_processamento2, 2, 2, 1, 1)

        self.bt_seta2 = QPushButton(self.frm_processamento2)
        self.bt_seta2.setObjectName(u"bt_seta2")
        self.bt_seta2.setMinimumSize(QSize(0, 35))
        self.bt_seta2.setMaximumSize(QSize(16777215, 35))
        icon13 = QIcon()
        icon13.addFile(u":/icons/icons/transfer.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_seta2.setIcon(icon13)
        self.bt_seta2.setIconSize(QSize(25, 25))

        self.gridLayout_2.addWidget(self.bt_seta2, 2, 5, 1, 1)

        self.cbx_coluna_processamento1 = QComboBox(self.frm_processamento2)
        self.cbx_coluna_processamento1.setObjectName(u"cbx_coluna_processamento1")
        self.cbx_coluna_processamento1.setMinimumSize(QSize(180, 30))
        self.cbx_coluna_processamento1.setMaximumSize(QSize(180, 30))

        self.gridLayout_2.addWidget(self.cbx_coluna_processamento1, 0, 0, 1, 1)

        self.bt_seta1 = QPushButton(self.frm_processamento2)
        self.bt_seta1.setObjectName(u"bt_seta1")
        self.bt_seta1.setMinimumSize(QSize(0, 35))
        self.bt_seta1.setMaximumSize(QSize(16777215, 35))
        self.bt_seta1.setIcon(icon13)
        self.bt_seta1.setIconSize(QSize(25, 25))

        self.gridLayout_2.addWidget(self.bt_seta1, 2, 1, 1, 1)

        self.txt_coluna_processamento1 = QLineEdit(self.frm_processamento2)
        self.txt_coluna_processamento1.setObjectName(u"txt_coluna_processamento1")
        self.txt_coluna_processamento1.setMinimumSize(QSize(180, 30))
        self.txt_coluna_processamento1.setMaximumSize(QSize(180, 30))

        self.gridLayout_2.addWidget(self.txt_coluna_processamento1, 2, 0, 1, 1)

        self.txt_coluna_processamento4 = QLineEdit(self.frm_processamento2)
        self.txt_coluna_processamento4.setObjectName(u"txt_coluna_processamento4")
        self.txt_coluna_processamento4.setMinimumSize(QSize(180, 30))
        self.txt_coluna_processamento4.setMaximumSize(QSize(180, 30))

        self.gridLayout_2.addWidget(self.txt_coluna_processamento4, 2, 10, 1, 1)

        self.txt_coluna_processamento3 = QLineEdit(self.frm_processamento2)
        self.txt_coluna_processamento3.setObjectName(u"txt_coluna_processamento3")
        self.txt_coluna_processamento3.setMinimumSize(QSize(180, 30))
        self.txt_coluna_processamento3.setMaximumSize(QSize(180, 30))

        self.gridLayout_2.addWidget(self.txt_coluna_processamento3, 2, 6, 1, 1)

        self.bt_add_combo2 = QPushButton(self.frm_processamento2)
        self.bt_add_combo2.setObjectName(u"bt_add_combo2")
        self.bt_add_combo2.setMinimumSize(QSize(0, 35))
        self.bt_add_combo2.setMaximumSize(QSize(16777215, 35))
        self.bt_add_combo2.setIcon(icon12)
        self.bt_add_combo2.setIconSize(QSize(25, 25))

        self.gridLayout_2.addWidget(self.bt_add_combo2, 2, 3, 1, 1)

        self.cbx_coluna_processamento3 = QComboBox(self.frm_processamento2)
        self.cbx_coluna_processamento3.setObjectName(u"cbx_coluna_processamento3")
        self.cbx_coluna_processamento3.setMinimumSize(QSize(180, 30))
        self.cbx_coluna_processamento3.setMaximumSize(QSize(180, 30))

        self.gridLayout_2.addWidget(self.cbx_coluna_processamento3, 0, 6, 1, 1)

        self.cbx_coluna_processamento2 = QComboBox(self.frm_processamento2)
        self.cbx_coluna_processamento2.setObjectName(u"cbx_coluna_processamento2")
        self.cbx_coluna_processamento2.setMinimumSize(QSize(180, 30))
        self.cbx_coluna_processamento2.setMaximumSize(QSize(180, 30))

        self.gridLayout_2.addWidget(self.cbx_coluna_processamento2, 0, 2, 1, 1)

        self.bt_seta3 = QPushButton(self.frm_processamento2)
        self.bt_seta3.setObjectName(u"bt_seta3")
        self.bt_seta3.setMinimumSize(QSize(0, 35))
        self.bt_seta3.setMaximumSize(QSize(16777215, 35))
        self.bt_seta3.setIcon(icon13)
        self.bt_seta3.setIconSize(QSize(25, 25))

        self.gridLayout_2.addWidget(self.bt_seta3, 2, 8, 1, 1)

        self.bt_retirar_combo1 = QPushButton(self.frm_processamento2)
        self.bt_retirar_combo1.setObjectName(u"bt_retirar_combo1")
        self.bt_retirar_combo1.setMinimumSize(QSize(0, 35))
        self.bt_retirar_combo1.setMaximumSize(QSize(16777215, 35))
        icon14 = QIcon()
        icon14.addFile(u":/icons/icons/minus (1).png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_retirar_combo1.setIcon(icon14)
        self.bt_retirar_combo1.setIconSize(QSize(25, 25))

        self.gridLayout_2.addWidget(self.bt_retirar_combo1, 2, 4, 1, 1)

        self.bt_retirar_combo2 = QPushButton(self.frm_processamento2)
        self.bt_retirar_combo2.setObjectName(u"bt_retirar_combo2")
        self.bt_retirar_combo2.setMinimumSize(QSize(0, 35))
        self.bt_retirar_combo2.setMaximumSize(QSize(16777215, 35))
        self.bt_retirar_combo2.setIcon(icon14)
        self.bt_retirar_combo2.setIconSize(QSize(25, 25))

        self.gridLayout_2.addWidget(self.bt_retirar_combo2, 2, 9, 1, 1)


        self.horizontalLayout_5.addWidget(self.frm_processamento2)


        self.verticalLayout_6.addWidget(self.page_opcoes_processamento)


        self.gridLayout.addWidget(self.frame_opcoes_busca_processamento, 0, 0, 1, 1)

        self.frm_lateral_functions = QFrame(self.frm_layout_geral)
        self.frm_lateral_functions.setObjectName(u"frm_lateral_functions")
        self.frm_lateral_functions.setEnabled(True)
        self.frm_lateral_functions.setMinimumSize(QSize(300, 0))
        self.frm_lateral_functions.setMaximumSize(QSize(300, 16777215))
        self.frm_lateral_functions.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_lateral_functions.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout.addWidget(self.frm_lateral_functions, 0, 1, 5, 1)


        self.verticalLayout_2.addWidget(self.frm_layout_geral)


        self.verticalLayout.addWidget(self.frame)

        PrincipalWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(PrincipalWindow)

        self.stackedWidget_tables.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(PrincipalWindow)
    # setupUi

    def retranslateUi(self, PrincipalWindow):
        PrincipalWindow.setWindowTitle(QCoreApplication.translate("PrincipalWindow", u"MainWindow", None))
        self.pushButton.setText("")
        self.btn_minimize.setText("")
        self.btn_maximize.setText("")
        self.btn_close_window.setText("")
        self.btn_importar_file.setText(QCoreApplication.translate("PrincipalWindow", u"Importar arquivo", None))
        self.btn_opcoes_pesquisas.setText(QCoreApplication.translate("PrincipalWindow", u"Op\u00e7\u00f5es de pesquisas", None))
        self.btn_opcoes_processamento.setText(QCoreApplication.translate("PrincipalWindow", u"Op\u00e7\u00f5es de Processamento", None))
        self.btn_opcoes_conexoes_db.setText(QCoreApplication.translate("PrincipalWindow", u"Conex\u00f5es DB", None))
#if QT_CONFIG(shortcut)
        self.btn_opcoes_conexoes_db.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.btn_salvar_geral.setText("")
#if QT_CONFIG(shortcut)
        self.btn_salvar_geral.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.btn_voltar_pagina.setText("")
        self.lb_titulos_tabelas.setText(QCoreApplication.translate("PrincipalWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Tabela Principal</span></p></body></html>", None))
        self.btn_proxima_pagina.setText("")
        self.btn_extrair_duplicados.setText(QCoreApplication.translate("PrincipalWindow", u"Extrair", None))
        self.btn_executar_pesquisas.setText("")
        self.btn_executar_processamento.setText(QCoreApplication.translate("PrincipalWindow", u"Executar", None))
        self.bt_add_combo1.setText("")
        self.bt_seta2.setText("")
        self.bt_seta1.setText("")
        self.bt_add_combo2.setText("")
        self.bt_seta3.setText("")
        self.bt_retirar_combo1.setText("")
        self.bt_retirar_combo2.setText("")
    # retranslateUi

