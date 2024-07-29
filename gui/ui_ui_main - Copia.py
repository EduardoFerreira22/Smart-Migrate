# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main - CopiadniXHz.ui'
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
        MainWindow.resize(1787, 1024)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
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
"QPushButton{\n"
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
        self.frame_5.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Shadow.Plain)
        self.gridLayout_9 = QGridLayout(self.frame_5)
        self.gridLayout_9.setSpacing(0)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, -1, 0)
        self.frame_butons_menu = QFrame(self.frame_5)
        self.frame_butons_menu.setObjectName(u"frame_butons_menu")
        self.frame_butons_menu.setStyleSheet(u"")
        self.frame_butons_menu.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_butons_menu.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_butons_menu)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_9.addWidget(self.frame_butons_menu, 0, 3, 1, 1)

        self.frame_8 = QFrame(self.frame_5)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(600, 60))
        self.frame_8.setMaximumSize(QSize(600, 60))
        self.frame_8.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_8)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, 2, 0)
        self.bt_buscar_csv = QPushButton(self.frame_8)
        self.bt_buscar_csv.setObjectName(u"bt_buscar_csv")
        self.bt_buscar_csv.setMinimumSize(QSize(80, 50))
        self.bt_buscar_csv.setMaximumSize(QSize(80, 50))
        self.bt_buscar_csv.setToolTipDuration(0)
        icon = QIcon()
        icon.addFile(u":/icons/img/folder.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_buscar_csv.setIcon(icon)
        self.bt_buscar_csv.setIconSize(QSize(40, 40))

        self.horizontalLayout.addWidget(self.bt_buscar_csv)

        self.bt_conexoes_banco_dados = QPushButton(self.frame_8)
        self.bt_conexoes_banco_dados.setObjectName(u"bt_conexoes_banco_dados")
        self.bt_conexoes_banco_dados.setMinimumSize(QSize(80, 50))
        self.bt_conexoes_banco_dados.setMaximumSize(QSize(50, 60))
        self.bt_conexoes_banco_dados.setToolTipDuration(0)
        icon1 = QIcon()
        icon1.addFile(u":/icons/img/data_bases.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_conexoes_banco_dados.setIcon(icon1)
        self.bt_conexoes_banco_dados.setIconSize(QSize(40, 40))

        self.horizontalLayout.addWidget(self.bt_conexoes_banco_dados)

        self.bt_pesquisar_dados = QPushButton(self.frame_8)
        self.bt_pesquisar_dados.setObjectName(u"bt_pesquisar_dados")
        self.bt_pesquisar_dados.setMinimumSize(QSize(80, 50))
        self.bt_pesquisar_dados.setMaximumSize(QSize(80, 50))
        icon2 = QIcon()
        icon2.addFile(u":/icons/img/search-data.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_pesquisar_dados.setIcon(icon2)
        self.bt_pesquisar_dados.setIconSize(QSize(40, 40))

        self.horizontalLayout.addWidget(self.bt_pesquisar_dados)

        self.bt_processamento_dados = QPushButton(self.frame_8)
        self.bt_processamento_dados.setObjectName(u"bt_processamento_dados")
        self.bt_processamento_dados.setMinimumSize(QSize(80, 50))
        self.bt_processamento_dados.setMaximumSize(QSize(80, 50))
        self.bt_processamento_dados.setToolTipDuration(0)
        icon3 = QIcon()
        icon3.addFile(u":/icons/img/data-processing.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_processamento_dados.setIcon(icon3)
        self.bt_processamento_dados.setIconSize(QSize(40, 40))

        self.horizontalLayout.addWidget(self.bt_processamento_dados)


        self.gridLayout_9.addWidget(self.frame_8, 0, 2, 1, 1)

        self.frame_11 = QFrame(self.frame_5)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(300, 0))
        self.frame_11.setMaximumSize(QSize(350, 16777215))
        self.frame_11.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_14 = QGridLayout(self.frame_11)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.pushButton_2 = QPushButton(self.frame_11)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(250, 0))
        self.pushButton_2.setMaximumSize(QSize(250, 16777215))
        self.pushButton_2.setStyleSheet(u"border:none;")
        icon4 = QIcon()
        icon4.addFile(u":/icons/img/logo_smartMigrate.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_2.setIcon(icon4)
        self.pushButton_2.setIconSize(QSize(200, 100))

        self.gridLayout_14.addWidget(self.pushButton_2, 0, 2, 1, 1)


        self.gridLayout_9.addWidget(self.frame_11, 0, 0, 1, 1, Qt.AlignmentFlag.AlignLeft)

        self.horizontalSpacer = QSpacerItem(150, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer, 0, 1, 1, 1)


        self.gridLayout_7.addWidget(self.frame_5, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.widget_menu, 0, 0, 1, 1)

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
        self.combo_data_base_list.setObjectName(u"combo_data_base_list")
        self.combo_data_base_list.setGeometry(QRect(240, 10, 121, 30))
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
        self.titulo_conexoes.setGeometry(QRect(10, 10, 181, 21))
        self.bt_conectar_data_base = QPushButton(self.frame)
        self.bt_conectar_data_base.setObjectName(u"bt_conectar_data_base")
        self.bt_conectar_data_base.setGeometry(QRect(250, 60, 110, 30))
        self.bt_conectar_data_base.setMinimumSize(QSize(110, 30))
        self.bt_conectar_data_base.setMaximumSize(QSize(110, 30))
        self.bt_buscar_sqlite = QPushButton(self.frame)
        self.bt_buscar_sqlite.setObjectName(u"bt_buscar_sqlite")
        self.bt_buscar_sqlite.setGeometry(QRect(250, 60, 110, 30))
        self.bt_buscar_sqlite.setMinimumSize(QSize(110, 30))
        self.bt_buscar_sqlite.setMaximumSize(QSize(110, 30))

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
        self.treeView_lista_tabelas.setTabKeyNavigation(True)
        self.treeView_lista_tabelas.setAnimated(True)
        self.treeView_lista_tabelas.header().setVisible(False)

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
        self.frame_10 = QFrame(self.frame_tabelas_duplicadas)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(0, 35))
        self.frame_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_16 = QGridLayout(self.frame_10)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_16.setContentsMargins(5, 2, 5, 2)
        self.bt_exportar_duplicados = QPushButton(self.frame_10)
        self.bt_exportar_duplicados.setObjectName(u"bt_exportar_duplicados")
        self.bt_exportar_duplicados.setMinimumSize(QSize(120, 35))
        self.bt_exportar_duplicados.setMaximumSize(QSize(120, 35))
        self.bt_exportar_duplicados.setStyleSheet(u"QPushButton{\n"
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
"QPushButton:hover{\n"
"	background-color: rgba(51, 221, 51, 0.25);\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/icons/img/save_data.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_exportar_duplicados.setIcon(icon5)
        self.bt_exportar_duplicados.setIconSize(QSize(30, 30))

        self.gridLayout_16.addWidget(self.bt_exportar_duplicados, 0, 0, 1, 1, Qt.AlignmentFlag.AlignLeft)

        self.bt_deletar_duplicados = QPushButton(self.frame_10)
        self.bt_deletar_duplicados.setObjectName(u"bt_deletar_duplicados")
        self.bt_deletar_duplicados.setMinimumSize(QSize(120, 35))
        self.bt_deletar_duplicados.setMaximumSize(QSize(120, 35))
        self.bt_deletar_duplicados.setStyleSheet(u"QPushButton{\n"
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
"QPushButton:hover{\n"
"	background-color: rgba(255, 52, 52, 0.25);\n"
"	border-right: 1px solid rgb(109, 109, 109);\n"
"	border-left: 1px solid rgba(217, 217, 217, 0.80);\n"
"	border-top: 1px solid rgba(217, 217, 217, 0.80);\n"
"	border-bottom: 1px solid rgb(109, 109, 109);\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/icons/img/delete.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_deletar_duplicados.setIcon(icon6)
        self.bt_deletar_duplicados.setIconSize(QSize(30, 30))

        self.gridLayout_16.addWidget(self.bt_deletar_duplicados, 0, 1, 1, 1)


        self.gridLayout_13.addWidget(self.frame_10, 5, 0, 1, 1)

        self.table_duplicados = QTableWidget(self.frame_tabelas_duplicadas)
        self.table_duplicados.setObjectName(u"table_duplicados")

        self.gridLayout_13.addWidget(self.table_duplicados, 3, 0, 1, 1)

        self.label_3 = QLabel(self.frame_tabelas_duplicadas)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_13.addWidget(self.label_3, 4, 0, 1, 1)


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
        icon7 = QIcon()
        icon7.addFile(u":/icons/img/play.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_execut_query_system.setIcon(icon7)

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
        self.bt_buscar_file_query.setIcon(icon)
        self.bt_buscar_file_query.setIconSize(QSize(25, 25))
        self.bt_executar_query = QPushButton(self.frame_2)
        self.bt_executar_query.setObjectName(u"bt_executar_query")
        self.bt_executar_query.setGeometry(QRect(60, 5, 50, 30))
        self.bt_executar_query.setMinimumSize(QSize(50, 30))
        self.bt_executar_query.setMaximumSize(QSize(50, 30))
        self.bt_executar_query.setIcon(icon7)

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
        self.frame_buttons_rigt.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_buttons_rigt.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_buttons_rigt)
        self.horizontalLayout_5.setSpacing(1)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(2, 1, 2, 1)
        self.bt_conections = QPushButton(self.frame_buttons_rigt)
        self.bt_conections.setObjectName(u"bt_conections")
        self.bt_conections.setMinimumSize(QSize(70, 35))
        self.bt_conections.setMaximumSize(QSize(70, 35))
        icon8 = QIcon()
        icon8.addFile(u":/icons/img/conexoes2.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_conections.setIcon(icon8)
        self.bt_conections.setIconSize(QSize(25, 25))

        self.horizontalLayout_5.addWidget(self.bt_conections)

        self.bt_terminal_sql = QPushButton(self.frame_buttons_rigt)
        self.bt_terminal_sql.setObjectName(u"bt_terminal_sql")
        self.bt_terminal_sql.setMinimumSize(QSize(70, 35))
        self.bt_terminal_sql.setMaximumSize(QSize(70, 35))
        icon9 = QIcon()
        icon9.addFile(u":/icons/img/querys.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_terminal_sql.setIcon(icon9)
        self.bt_terminal_sql.setIconSize(QSize(25, 25))

        self.horizontalLayout_5.addWidget(self.bt_terminal_sql)

        self.bt_systems = QPushButton(self.frame_buttons_rigt)
        self.bt_systems.setObjectName(u"bt_systems")
        self.bt_systems.setMinimumSize(QSize(70, 35))
        self.bt_systems.setMaximumSize(QSize(70, 35))
        icon10 = QIcon()
        icon10.addFile(u":/icons/img/systems.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_systems.setIcon(icon10)
        self.bt_systems.setIconSize(QSize(25, 25))

        self.horizontalLayout_5.addWidget(self.bt_systems)

        self.bt_duplicados = QPushButton(self.frame_buttons_rigt)
        self.bt_duplicados.setObjectName(u"bt_duplicados")
        self.bt_duplicados.setMinimumSize(QSize(70, 35))
        self.bt_duplicados.setMaximumSize(QSize(70, 35))
        icon11 = QIcon()
        icon11.addFile(u":/icons/img/duplicado2.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_duplicados.setIcon(icon11)
        self.bt_duplicados.setIconSize(QSize(25, 25))

        self.horizontalLayout_5.addWidget(self.bt_duplicados)


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
        self.stackedWidget = QStackedWidget(self.widget_functions_table)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"QStackedWidget{\n"
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
        self.horizontalLayout_3 = QHBoxLayout(self.page_opcoes_busca)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame_op_busca = QFrame(self.page_opcoes_busca)
        self.frame_op_busca.setObjectName(u"frame_op_busca")
        self.frame_op_busca.setMinimumSize(QSize(450, 0))
        self.frame_op_busca.setMaximumSize(QSize(450, 16777215))
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
        self.comboBox_opcoes_busca.setGeometry(QRect(120, 20, 181, 31))
        self.txt_opcoes_busca = QLineEdit(self.frame_op_busca)
        self.txt_opcoes_busca.setObjectName(u"txt_opcoes_busca")
        self.txt_opcoes_busca.setGeometry(QRect(120, 80, 181, 31))
        self.bt_buscar_op_busca = QPushButton(self.frame_op_busca)
        self.bt_buscar_op_busca.setObjectName(u"bt_buscar_op_busca")
        self.bt_buscar_op_busca.setGeometry(QRect(320, 80, 101, 31))

        self.horizontalLayout_3.addWidget(self.frame_op_busca)

        self.stackedWidget_sobre_func_op_buscas = QStackedWidget(self.page_opcoes_busca)
        self.stackedWidget_sobre_func_op_buscas.setObjectName(u"stackedWidget_sobre_func_op_buscas")
        self.stackedWidget_sobre_func_op_buscas.setMinimumSize(QSize(0, 0))
        self.stackedWidget_sobre_func_op_buscas.setMaximumSize(QSize(16777215, 16777215))
        self.page_buscar_ncm = QWidget()
        self.page_buscar_ncm.setObjectName(u"page_buscar_ncm")
        self.gridLayout_17 = QGridLayout(self.page_buscar_ncm)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.label_sobre_op_busca = QLabel(self.page_buscar_ncm)
        self.label_sobre_op_busca.setObjectName(u"label_sobre_op_busca")
        self.label_sobre_op_busca.setMinimumSize(QSize(450, 0))
        self.label_sobre_op_busca.setMaximumSize(QSize(450, 16777215))
        self.label_sobre_op_busca.setMargin(1)

        self.gridLayout_17.addWidget(self.label_sobre_op_busca, 0, 0, 1, 1)

        self.stackedWidget_sobre_func_op_buscas.addWidget(self.page_buscar_ncm)
        self.page_analise_inteligente = QWidget()
        self.page_analise_inteligente.setObjectName(u"page_analise_inteligente")
        self.gridLayout_25 = QGridLayout(self.page_analise_inteligente)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.txt_output_analise_inteligente = QPlainTextEdit(self.page_analise_inteligente)
        self.txt_output_analise_inteligente.setObjectName(u"txt_output_analise_inteligente")
        self.txt_output_analise_inteligente.setAutoFillBackground(False)
        self.txt_output_analise_inteligente.setStyleSheet(u"QPlainTextEdit{\n"
"	font: 11pt \"Segoe UI\";\n"
"	color:rgb(120, 120, 120);\n"
"	border:none;\n"
"	background-color: rgb(255, 255, 255);\n"
"    border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"}")
        self.txt_output_analise_inteligente.setFrameShape(QFrame.Shape.NoFrame)
        self.txt_output_analise_inteligente.setBackgroundVisible(False)
        self.txt_output_analise_inteligente.setCenterOnScroll(False)

        self.gridLayout_25.addWidget(self.txt_output_analise_inteligente, 0, 0, 1, 1)

        self.stackedWidget_sobre_func_op_buscas.addWidget(self.page_analise_inteligente)
        self.page_ncm_invalido = QWidget()
        self.page_ncm_invalido.setObjectName(u"page_ncm_invalido")
        self.gridLayout_18 = QGridLayout(self.page_ncm_invalido)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.label = QLabel(self.page_ncm_invalido)
        self.label.setObjectName(u"label")
        self.label.setTextFormat(Qt.TextFormat.AutoText)

        self.gridLayout_18.addWidget(self.label, 0, 0, 1, 1)

        self.stackedWidget_sobre_func_op_buscas.addWidget(self.page_ncm_invalido)
        self.page_tudo_que_contem = QWidget()
        self.page_tudo_que_contem.setObjectName(u"page_tudo_que_contem")
        self.gridLayout_19 = QGridLayout(self.page_tudo_que_contem)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.label_5 = QLabel(self.page_tudo_que_contem)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_19.addWidget(self.label_5, 0, 0, 1, 1)

        self.stackedWidget_sobre_func_op_buscas.addWidget(self.page_tudo_que_contem)
        self.page_op_busca_dados_duplicados = QWidget()
        self.page_op_busca_dados_duplicados.setObjectName(u"page_op_busca_dados_duplicados")
        self.gridLayout_20 = QGridLayout(self.page_op_busca_dados_duplicados)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.label_6 = QLabel(self.page_op_busca_dados_duplicados)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_20.addWidget(self.label_6, 0, 0, 1, 1)

        self.stackedWidget_sobre_func_op_buscas.addWidget(self.page_op_busca_dados_duplicados)

        self.horizontalLayout_3.addWidget(self.stackedWidget_sobre_func_op_buscas)

        self.stackedWidget.addWidget(self.page_opcoes_busca)
        self.page_opcoes_processamento = QWidget()
        self.page_opcoes_processamento.setObjectName(u"page_opcoes_processamento")
        self.horizontalLayout_4 = QHBoxLayout(self.page_opcoes_processamento)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.frame_opcoes_processamento = QFrame(self.page_opcoes_processamento)
        self.frame_opcoes_processamento.setObjectName(u"frame_opcoes_processamento")
        self.frame_opcoes_processamento.setMinimumSize(QSize(500, 120))
        self.frame_opcoes_processamento.setMaximumSize(QSize(500, 16777215))
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
        self.combo_opcoes_processamento.setObjectName(u"combo_opcoes_processamento")
        self.combo_opcoes_processamento.setGeometry(QRect(30, 10, 441, 31))
        self.txt_opcao1_processamento = QLineEdit(self.frame_opcoes_processamento)
        self.txt_opcao1_processamento.setObjectName(u"txt_opcao1_processamento")
        self.txt_opcao1_processamento.setGeometry(QRect(30, 110, 181, 31))
        self.txt_opcao2_processamento = QLineEdit(self.frame_opcoes_processamento)
        self.txt_opcao2_processamento.setObjectName(u"txt_opcao2_processamento")
        self.txt_opcao2_processamento.setGeometry(QRect(290, 110, 181, 31))
        self.combo1_colunas_processamento = QComboBox(self.frame_opcoes_processamento)
        self.combo1_colunas_processamento.setObjectName(u"combo1_colunas_processamento")
        self.combo1_colunas_processamento.setGeometry(QRect(30, 60, 181, 31))
        self.combo2_colunas_processamento = QComboBox(self.frame_opcoes_processamento)
        self.combo2_colunas_processamento.setObjectName(u"combo2_colunas_processamento")
        self.combo2_colunas_processamento.setGeometry(QRect(290, 60, 181, 31))
        self.bt_processamento_de_para = QPushButton(self.frame_opcoes_processamento)
        self.bt_processamento_de_para.setObjectName(u"bt_processamento_de_para")
        self.bt_processamento_de_para.setGeometry(QRect(220, 110, 60, 31))
        self.bt_processamento_de_para.setMinimumSize(QSize(60, 31))
        self.bt_processamento_de_para.setMaximumSize(QSize(60, 31))
        self.bt_processamento_de_para.setStyleSheet(u"border:none;")
        icon12 = QIcon()
        icon12.addFile(u":/icons/img/setas1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_processamento_de_para.setIcon(icon12)
        self.bt_processamento_de_para.setIconSize(QSize(40, 28))

        self.horizontalLayout_4.addWidget(self.frame_opcoes_processamento)

        self.frame_info_opcoes_processamento = QFrame(self.page_opcoes_processamento)
        self.frame_info_opcoes_processamento.setObjectName(u"frame_info_opcoes_processamento")
        self.frame_info_opcoes_processamento.setMinimumSize(QSize(0, 0))
        self.frame_info_opcoes_processamento.setMaximumSize(QSize(16777215, 16777215))
        self.frame_info_opcoes_processamento.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_info_opcoes_processamento.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_info_opcoes_processamento)
        self.gridLayout_5.setSpacing(1)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(1, 1, 1, 1)
        self.stackedWidget_op_processamento = QStackedWidget(self.frame_info_opcoes_processamento)
        self.stackedWidget_op_processamento.setObjectName(u"stackedWidget_op_processamento")
        self.page_substituir_ncm = QWidget()
        self.page_substituir_ncm.setObjectName(u"page_substituir_ncm")
        self.gridLayout_21 = QGridLayout(self.page_substituir_ncm)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.label_7 = QLabel(self.page_substituir_ncm)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_21.addWidget(self.label_7, 0, 0, 1, 1)

        self.stackedWidget_op_processamento.addWidget(self.page_substituir_ncm)
        self.page_colunaA_colunaB_recebe = QWidget()
        self.page_colunaA_colunaB_recebe.setObjectName(u"page_colunaA_colunaB_recebe")
        self.gridLayout_22 = QGridLayout(self.page_colunaA_colunaB_recebe)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.label_8 = QLabel(self.page_colunaA_colunaB_recebe)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_22.addWidget(self.label_8, 0, 0, 1, 1)

        self.stackedWidget_op_processamento.addWidget(self.page_colunaA_colunaB_recebe)
        self.page_filtrar_coluna_linhas_contem = QWidget()
        self.page_filtrar_coluna_linhas_contem.setObjectName(u"page_filtrar_coluna_linhas_contem")
        self.gridLayout_23 = QGridLayout(self.page_filtrar_coluna_linhas_contem)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.label_9 = QLabel(self.page_filtrar_coluna_linhas_contem)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_23.addWidget(self.label_9, 0, 0, 1, 1)

        self.stackedWidget_op_processamento.addWidget(self.page_filtrar_coluna_linhas_contem)
        self.page_extrair_duplicados = QWidget()
        self.page_extrair_duplicados.setObjectName(u"page_extrair_duplicados")
        self.gridLayout_24 = QGridLayout(self.page_extrair_duplicados)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.label_10 = QLabel(self.page_extrair_duplicados)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_24.addWidget(self.label_10, 0, 0, 1, 1)

        self.stackedWidget_op_processamento.addWidget(self.page_extrair_duplicados)

        self.gridLayout_5.addWidget(self.stackedWidget_op_processamento, 0, 0, 1, 1)


        self.horizontalLayout_4.addWidget(self.frame_info_opcoes_processamento)

        self.stackedWidget.addWidget(self.page_opcoes_processamento)

        self.gridLayout_4.addWidget(self.stackedWidget, 1, 0, 1, 1)


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
        self.table_principal = QTableWidget(self.frame_table_principal)
        self.table_principal.setObjectName(u"table_principal")
        self.table_principal.setStyleSheet(u"QTableWidget{\n"
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
"}")
        self.table_principal.setFrameShape(QFrame.Shape.StyledPanel)
        self.table_principal.setFrameShadow(QFrame.Shadow.Sunken)
        self.table_principal.setLineWidth(1)
        self.table_principal.setEditTriggers(QAbstractItemView.EditTrigger.AnyKeyPressed|QAbstractItemView.EditTrigger.CurrentChanged|QAbstractItemView.EditTrigger.DoubleClicked|QAbstractItemView.EditTrigger.SelectedClicked)
        self.table_principal.setDragEnabled(True)
        self.table_principal.setAlternatingRowColors(True)
        self.table_principal.setSelectionMode(QAbstractItemView.SelectionMode.ContiguousSelection)
        self.table_principal.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.table_principal.setSortingEnabled(True)
        self.table_principal.verticalHeader().setVisible(False)

        self.gridLayout_8.addWidget(self.table_principal, 1, 0, 1, 3)

        self.txt_output_logs = QPlainTextEdit(self.frame_table_principal)
        self.txt_output_logs.setObjectName(u"txt_output_logs")
        self.txt_output_logs.setMaximumSize(QSize(16777215, 30))
        self.txt_output_logs.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.gridLayout_8.addWidget(self.txt_output_logs, 4, 1, 1, 1)

        self.bt_salvar_dados_tabela_principal = QPushButton(self.frame_table_principal)
        self.bt_salvar_dados_tabela_principal.setObjectName(u"bt_salvar_dados_tabela_principal")
        self.bt_salvar_dados_tabela_principal.setMinimumSize(QSize(120, 35))
        self.bt_salvar_dados_tabela_principal.setMaximumSize(QSize(16777215, 35))
        self.bt_salvar_dados_tabela_principal.setStyleSheet(u"QPushButton{\n"
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
"QPushButton:hover{\n"
"	background-color: rgba(51, 221, 51, 0.25);\n"
"}")
        self.bt_salvar_dados_tabela_principal.setIcon(icon5)
        self.bt_salvar_dados_tabela_principal.setIconSize(QSize(30, 30))

        self.gridLayout_8.addWidget(self.bt_salvar_dados_tabela_principal, 4, 2, 1, 1)


        self.gridLayout_3.addWidget(self.frame_table_principal, 1, 0, 1, 1)


        self.gridLayout_2.addWidget(self.widget_table_principal, 2, 0, 1, 1)


        self.gridLayout.addWidget(self.widget, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabs_lateral_right.setCurrentIndex(2)
        self.stackedWidget.setCurrentIndex(1)
        self.stackedWidget_sobre_func_op_buscas.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
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
        self.pushButton_2.setText("")
        self.txt_servidor_data_base.setInputMask("")
        self.txt_servidor_data_base.setText("")
        self.txt_servidor_data_base.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Servidor\\inst\u00e2ncia", None))
        self.txt_data_base_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"data base", None))
        self.txt_port_data_base.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Porta", None))
        self.combo_data_base_list.setItemText(0, QCoreApplication.translate("MainWindow", u"SQL Server", None))
        self.combo_data_base_list.setItemText(1, QCoreApplication.translate("MainWindow", u"MySQL", None))
        self.combo_data_base_list.setItemText(2, QCoreApplication.translate("MainWindow", u"PostgreSQL", None))
        self.combo_data_base_list.setItemText(3, QCoreApplication.translate("MainWindow", u"SQLite", None))

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
        self.bt_exportar_duplicados.setText(QCoreApplication.translate("MainWindow", u"Exportar", None))
        self.bt_deletar_duplicados.setText(QCoreApplication.translate("MainWindow", u"Deletar", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Para lidar com os dados duplicados selecione uma das op\u00e7\u00f5es a cima.</p></body></html>", None))
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
        self.comboBox_opcoes_busca.setItemText(0, QCoreApplication.translate("MainWindow", u"Op\u00e7\u00f5es de busca", None))
        self.comboBox_opcoes_busca.setItemText(1, QCoreApplication.translate("MainWindow", u"Analise inteligente", None))
        self.comboBox_opcoes_busca.setItemText(2, QCoreApplication.translate("MainWindow", u"Buscar por NCM", None))
        self.comboBox_opcoes_busca.setItemText(3, QCoreApplication.translate("MainWindow", u"NCM Inv\u00e1lido", None))
        self.comboBox_opcoes_busca.setItemText(4, QCoreApplication.translate("MainWindow", u"Tudo que cont\u00e9m", None))
        self.comboBox_opcoes_busca.setItemText(5, QCoreApplication.translate("MainWindow", u"Duplicados", None))

        self.bt_buscar_op_busca.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.label_sobre_op_busca.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><h4 style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt; font-weight:700;\">Fun\u00e7\u00e3o: Buscar NCM</span></h4><p><span style=\" font-size:6pt;\">Essa fun\u00e7\u00e3o permite ao usu\u00e1rio buscar um NCM espec\u00edfico digitado por ele. A tabela ser\u00e1 atualizada para mostrar apenas os resultados que correspondem ao NCM digitado.</span></p><p><span style=\" font-size:6pt; font-weight:700;\">Passos:</span></p><p><span style=\" font-size:6pt;\">1: Digite o NCM desejado no campo de busca.</span></p><p><span style=\" font-size:6pt;\">2: Clique no bot\u00e3o &quot;Buscar NCM&quot;.</span></p><p><span style=\" font-size:6pt;\">3: A tabela ser\u00e1 atualizada para mostrar os resultados que correspondem ao NCM digitado.</span></p></body></html>", None))
        self.txt_output_analise_inteligente.setPlainText("")
        self.txt_output_analise_inteligente.setPlaceholderText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><h4 style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt; font-weight:700;\">Fun\u00e7\u00e3o: NCM Inv\u00e1lido</span></h4><p><span style=\" font-size:6pt;\">Essa fun\u00e7\u00e3o busca por todos os NCMs que est\u00e3o vencidos na tabela. Isso \u00e9 \u00fatil para identificar rapidamente itens que precisam de atualiza\u00e7\u00e3o.</span></p><p><span style=\" font-size:6pt; font-weight:700;\">Passos:</span></p><p><span style=\" font-size:6pt;\">1: Clique no bot\u00e3o &quot;NCM Inv\u00e1lido&quot;.</span></p><p><span style=\" font-size:6pt;\">2: A tabela ser\u00e1 atualizada para mostrar todos os NCMs que est\u00e3o vencidos.</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><h4 style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt; font-weight:700;\">Fun\u00e7\u00e3o: Tudo que Cont\u00e9m</span></h4><p><span style=\" font-size:6pt;\">Essa fun\u00e7\u00e3o permite ao usu\u00e1rio fazer uma busca na tabela para encontrar itens que contenham o texto digitado ou itens similares.</span></p><p><span style=\" font-size:6pt; font-weight:700;\">Passos:</span></p><p><span style=\" font-size:6pt;\">1: Digite o texto desejado no campo de busca.</span></p><p><span style=\" font-size:6pt;\">2: Clique no bot\u00e3o &quot;Tudo que Cont\u00e9m&quot;.</span></p><p><span style=\" font-size:6pt;\">3: A tabela ser\u00e1 atualizada para mostrar os resultados que cont\u00eam o texto digitado ou itens similares.</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><h4 align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt; font-weight:700;\">Fun\u00e7\u00e3o: Dados Duplicados</span></h4><p align=\"justify\"><span style=\" font-size:6pt;\">Essa fun\u00e7\u00e3o atualiza a tabela para marcar todas as linhas que s\u00e3o iguais, levando em conta colunas como descri\u00e7\u00e3o, </span></p><p align=\"justify\"><span style=\" font-size:6pt;\">c\u00f3digo interno, c\u00f3digo de barras, etc. As linhas duplicadasser\u00e3o destacadas em vermelho para facilitar a identifica\u00e7\u00e3o.</span></p><p align=\"justify\"><span style=\" font-size:6pt; font-weight:700;\">Passos:</span></p><p align=\"justify\"><span style=\" font-size:6pt;\">1: Clique no bot\u00e3o &quot;Dados Duplicados&quot;. 2: A tabela ser\u00e1 atualizada e todas as linhas </span></p><p align=\"justify\"><span style=\" font-size:6pt;\">duplicadas ser\u00e3o destacadas em vermelho.</"
                        "span></p></body></html>", None))
        self.combo_opcoes_processamento.setItemText(0, QCoreApplication.translate("MainWindow", u"Op\u00e7\u00f5es de Processamento", None))
        self.combo_opcoes_processamento.setItemText(1, QCoreApplication.translate("MainWindow", u"Substituir NCM", None))
        self.combo_opcoes_processamento.setItemText(2, QCoreApplication.translate("MainWindow", u"Tudo que cont\u00e9m mude para.", None))
        self.combo_opcoes_processamento.setItemText(3, QCoreApplication.translate("MainWindow", u"Se Coluna A cont\u00e9m, Coluna B recebe...", None))
        self.combo_opcoes_processamento.setItemText(4, QCoreApplication.translate("MainWindow", u"Filtrar por coluna e copiar todas a linhas que contenham", None))
        self.combo_opcoes_processamento.setItemText(5, QCoreApplication.translate("MainWindow", u"Extrair dados duplicados da tabela", None))

        self.bt_processamento_de_para.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><h4 style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt; font-weight:700;\">Fun\u00e7\u00e3o: Substituir NCM</span></h4><p><span style=\" font-size:6pt;\">Essa fun\u00e7\u00e3o verifica o NCM digitado no primeiro campo e substitui o NCM encontrado na tabela por outro digitado no segundo campo.</span></p><p><span style=\" font-size:6pt; font-weight:700;\">Passos:</span></p><p><span style=\" font-size:6pt; font-weight:700;\">1</span><span style=\" font-size:6pt;\">: Digite o NCM a ser substitu\u00eddo no primeiro campo. </span><span style=\" font-size:6pt; font-weight:700;\">2:</span><span style=\" font-size:6pt;\"> Digite o novo NCM no segundo campo.</span></p><p><span style=\" font-size:6pt; font-weight:700;\">3:</span><span style=\" font-size:6pt;\"> Clique no bot\u00e3o &quot;Substituir NCM&quot;.</span><span style=\" font-size:6pt; font-weight:700;\"> 4:</span><span style=\" font-size:6pt;\"> "
                        "A tabela ser\u00e1 atualizada com as substitui\u00e7\u00f5es.</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><h4 style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:7pt; font-weight:700;\">Fun\u00e7\u00e3o: Se Coluna A cont\u00e9m, Coluna B recebe</span></h4><p><span style=\" font-size:6pt;\">Essa fun\u00e7\u00e3o verifica se a coluna selecionada no ComboBox 1 cont\u00e9m o dado digitado e, se sim, substitui os valores na </span></p><p><span style=\" font-size:6pt;\">coluna selecionada no ComboBox 2.</span></p><p><span style=\" font-size:6pt; font-weight:700;\">1: </span><span style=\" font-size:6pt;\">Selecione a coluna a ser verificada no ComboBox 1. </span><span style=\" font-size:6pt; font-weight:700;\">2: </span><span style=\" font-size:6pt;\">Digite o dado a ser verificado no primeiro campo. </span></p><p><span style=\" font-size:6pt; font-weight:700;\">3: </span><span style=\" font-size:6pt;\">Selecione a coluna a ser alterada no ComboBox 2. </span><span style=\" font-size:6pt; font-weight:700;\">4: "
                        "</span><span style=\" font-size:6pt;\">Digite o novo valor no segundo campo.</span></p><p><span style=\" font-size:6pt; font-weight:700;\">5: </span><span style=\" font-size:6pt;\">Clique no bot\u00e3o &quot;Se Coluna A cont\u00e9m, Coluna B recebe&quot;. </span><span style=\" font-size:6pt; font-weight:700;\">6: </span><span style=\" font-size:6pt;\">A tabela ser\u00e1 atualizada com as altera\u00e7\u00f5es.</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:7pt; font-weight:700;\">Fun\u00e7\u00e3o: Filtrar por Coluna e Copiar Todas as Linhas que Contenham</span></p><p><span style=\" font-size:6pt;\">Essa fun\u00e7\u00e3o filtra os dados da tabela com base na coluna e no texto digitados, </span></p><p><span style=\" font-size:6pt;\">e permite ao usu\u00e1rio salvar o resultado em CSV.</span></p><p><span style=\" font-size:6pt; font-weight:700;\">1: </span><span style=\" font-size:6pt;\">Selecione a coluna a ser filtrada no ComboBox 1. </span><span style=\" font-size:6pt; font-weight:700;\">2: </span><span style=\" font-size:6pt;\">Digite o texto a ser filtrado no primeiro campo.</span></p><p><span style=\" font-size:6pt; font-weight:700;\">3: </span><span style=\" font-size:6pt;\">Selecione a coluna a ser alterada no ComboBox 2. </span><span style=\" font-size:6pt; font-weight:700;\">4: </span><span style=\" font-size:6pt;\">Digite o novo valor no segundo campo.</span></p><p><span style=\" font-size:6pt; font-weight:7"
                        "00;\">5: </span><span style=\" font-size:6pt;\">Clique no bot\u00e3o &quot;Filtrar por Coluna e Copiar Todas as Linhas que Contenham&quot;.</span></p><p><span style=\" font-size:6pt; font-weight:700;\">6: </span><span style=\" font-size:6pt;\">A tabela ser\u00e1 atualizada com os dados filtrados, e voc\u00ea pode salvar o resultado em CSV.</span></p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><h4 style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt; font-weight:700;\">Fun\u00e7\u00e3o: Extrair Dados Duplicados da Tabela</span></h4><p><span style=\" font-size:6pt;\">Essa funcionalidade verifica todas as linhas com dados iguais, levando em considera\u00e7\u00e3o colunas como descri\u00e7\u00e3o e c\u00f3digo, marca esses dados em vermelho e permite ao usu\u00e1rio extrair os dados repetidos para uma nova tabela.</span></p><p><span style=\" font-size:6pt; font-weight:700;\">Passos:</span></p><p><span style=\" font-size:6pt; font-weight:700;\">1: </span><span style=\" font-size:6pt;\">Clique no bot\u00e3o &quot;Extrair Dados Duplicados&quot;. </span><span style=\" font-size:6pt; font-weight:700;\">2 </span><span style=\" font-size:6pt;\">A tabela ser\u00e1 atualizada com as linhas duplicadas marcadas em vermelho.</span></p><p><span style=\" font-size:6pt; font-weight:700;\">3: </span><span"
                        " style=\" font-size:6pt;\">Clique no bot\u00e3o &quot;Extrair e Salvar&quot;. </span><span style=\" font-size:6pt; font-weight:700;\">4: </span><span style=\" font-size:6pt;\">Os dados duplicados ser\u00e3o salvos em uma nova tabela, permitindo um </span></p><p><span style=\" font-size:6pt;\">processamento mais f\u00e1cil.</span></p></body></html>", None))
        self.bt_salvar_dados_tabela_principal.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
    # retranslateUi

