# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainbhYEMM.ui'
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
    QSizePolicy, QSpacerItem, QTabWidget, QTableWidget,
    QTableWidgetItem, QTreeView, QVBoxLayout, QWidget)
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1444, 1032)
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
        self.widget_barra_inferior = QWidget(self.widget)
        self.widget_barra_inferior.setObjectName(u"widget_barra_inferior")
        self.widget_barra_inferior.setMinimumSize(QSize(0, 25))
        self.widget_barra_inferior.setMaximumSize(QSize(16777215, 25))
        self.gridLayout_5 = QGridLayout(self.widget_barra_inferior)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.widget_barra_inferior)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(2, 0, 1, 0)
        self.txt_output_logs = QPlainTextEdit(self.frame_2)
        self.txt_output_logs.setObjectName(u"txt_output_logs")

        self.verticalLayout.addWidget(self.txt_output_logs)


        self.gridLayout_5.addWidget(self.frame_2, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.widget_barra_inferior, 3, 0, 1, 2)

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

        self.gridLayout_8.addWidget(self.table_principal, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frame_table_principal, 1, 0, 1, 1)


        self.gridLayout_2.addWidget(self.widget_table_principal, 2, 0, 1, 1)

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
        self.frame_functions_table = QFrame(self.widget_functions_table)
        self.frame_functions_table.setObjectName(u"frame_functions_table")
        self.frame_functions_table.setMinimumSize(QSize(0, 0))
        self.frame_functions_table.setMaximumSize(QSize(16777215, 16777215))
        self.frame_functions_table.setToolTipDuration(0)
        self.frame_functions_table.setStyleSheet(u"#frame_functions_table{\n"
"\n"
"\n"
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
"}")
        self.frame_functions_table.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_functions_table.setFrameShadow(QFrame.Shadow.Plain)

        self.gridLayout_4.addWidget(self.frame_functions_table, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.widget_functions_table, 1, 0, 1, 1)

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
        self.tabs_lateral_right = QTabWidget(self.widget_right)
        self.tabs_lateral_right.setObjectName(u"tabs_lateral_right")
        self.tabs_lateral_right.setStyleSheet(u"#tabs_lateral_right{\n"
"	border-right: 1px solid rgba(217, 217, 217, 0.80);\n"
"	border-left: 1px solid rgba(217, 217, 217, 0.80);\n"
"	border-top: 1px solid rgba(217, 217, 217, 0.80);\n"
"	border-bottom: 1px solid rgba(217, 217, 217, 0.80);\n"
"\n"
"}")
        self.tab_lista_tabelas_db = QWidget()
        self.tab_lista_tabelas_db.setObjectName(u"tab_lista_tabelas_db")
        self.tab_lista_tabelas_db.setStyleSheet(u"background-color: rgba(217, 217, 217, 0.35);")
        self.gridLayout_11 = QGridLayout(self.tab_lista_tabelas_db)
        self.gridLayout_11.setSpacing(3)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.tab_lista_tabelas_db)
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
        self.txt_servidor_data_base.setGeometry(QRect(10, 60, 241, 30))
        self.txt_servidor_data_base.setMinimumSize(QSize(0, 30))
        self.txt_servidor_data_base.setMaximumSize(QSize(16777215, 30))
        self.txt_data_base_name = QLineEdit(self.frame)
        self.txt_data_base_name.setObjectName(u"txt_data_base_name")
        self.txt_data_base_name.setGeometry(QRect(10, 140, 113, 30))
        self.txt_data_base_name.setMinimumSize(QSize(0, 30))
        self.txt_data_base_name.setMaximumSize(QSize(16777215, 30))
        self.txt_data_base_name.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.txt_port_data_base = QLineEdit(self.frame)
        self.txt_port_data_base.setObjectName(u"txt_port_data_base")
        self.txt_port_data_base.setGeometry(QRect(140, 140, 113, 30))
        self.txt_port_data_base.setMinimumSize(QSize(0, 30))
        self.txt_port_data_base.setMaximumSize(QSize(16777215, 30))
        self.txt_port_data_base.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.combo_data_base_list = QComboBox(self.frame)
        self.combo_data_base_list.addItem("")
        self.combo_data_base_list.addItem("")
        self.combo_data_base_list.addItem("")
        self.combo_data_base_list.addItem("")
        self.combo_data_base_list.setObjectName(u"combo_data_base_list")
        self.combo_data_base_list.setGeometry(QRect(260, 10, 121, 30))
        self.combo_data_base_list.setMinimumSize(QSize(0, 30))
        self.combo_data_base_list.setMaximumSize(QSize(16777215, 30))
        self.txt_user_data_base = QLineEdit(self.frame)
        self.txt_user_data_base.setObjectName(u"txt_user_data_base")
        self.txt_user_data_base.setGeometry(QRect(10, 100, 113, 30))
        self.txt_user_data_base.setMinimumSize(QSize(0, 30))
        self.txt_user_data_base.setMaximumSize(QSize(16777215, 30))
        self.txt_user_data_base.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.txt_password_data_base = QLineEdit(self.frame)
        self.txt_password_data_base.setObjectName(u"txt_password_data_base")
        self.txt_password_data_base.setGeometry(QRect(140, 100, 113, 30))
        self.txt_password_data_base.setMinimumSize(QSize(0, 30))
        self.txt_password_data_base.setMaximumSize(QSize(16777215, 30))
        self.txt_password_data_base.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.titulo_conexoes = QLabel(self.frame)
        self.titulo_conexoes.setObjectName(u"titulo_conexoes")
        self.titulo_conexoes.setGeometry(QRect(10, 10, 181, 21))
        self.bt_conectar_data_base = QPushButton(self.frame)
        self.bt_conectar_data_base.setObjectName(u"bt_conectar_data_base")
        self.bt_conectar_data_base.setGeometry(QRect(260, 60, 120, 30))
        self.bt_conectar_data_base.setMinimumSize(QSize(120, 30))
        self.bt_conectar_data_base.setMaximumSize(QSize(120, 30))
        self.bt_buscar_sqlite = QPushButton(self.frame)
        self.bt_buscar_sqlite.setObjectName(u"bt_buscar_sqlite")
        self.bt_buscar_sqlite.setGeometry(QRect(260, 60, 120, 30))
        self.bt_buscar_sqlite.setMinimumSize(QSize(120, 30))
        self.bt_buscar_sqlite.setMaximumSize(QSize(120, 30))

        self.gridLayout_11.addWidget(self.frame, 0, 0, 1, 1)

        self.frame_3 = QFrame(self.tab_lista_tabelas_db)
        self.frame_3.setObjectName(u"frame_3")
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
        self.frame_9.setMinimumSize(QSize(0, 30))
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_15 = QGridLayout(self.frame_9)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setHorizontalSpacing(6)
        self.gridLayout_15.setContentsMargins(4, 2, 4, 3)
        self.bt_mostra_dados_tabelas = QPushButton(self.frame_9)
        self.bt_mostra_dados_tabelas.setObjectName(u"bt_mostra_dados_tabelas")
        self.bt_mostra_dados_tabelas.setMinimumSize(QSize(0, 30))
        self.bt_mostra_dados_tabelas.setMaximumSize(QSize(16777215, 30))
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


        self.gridLayout_11.addWidget(self.frame_3, 1, 0, 1, 1)

        self.tabs_lateral_right.addTab(self.tab_lista_tabelas_db, "")
        self.tab_dados_duplicados = QWidget()
        self.tab_dados_duplicados.setObjectName(u"tab_dados_duplicados")
        self.tab_dados_duplicados.setStyleSheet(u"background-color: rgba(217, 217, 217, 0.35);")
        self.gridLayout_10 = QGridLayout(self.tab_dados_duplicados)
        self.gridLayout_10.setSpacing(3)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_func_duplicados = QFrame(self.tab_dados_duplicados)
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


        self.gridLayout_10.addWidget(self.frame_func_duplicados, 1, 0, 1, 1)

        self.frame_tabelas_duplicadas = QFrame(self.tab_dados_duplicados)
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
        self.bt_exportar_duplicados.setMinimumSize(QSize(180, 0))
        self.bt_exportar_duplicados.setMaximumSize(QSize(180, 16777215))
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
        self.bt_exportar_duplicados.setIconSize(QSize(40, 40))

        self.gridLayout_16.addWidget(self.bt_exportar_duplicados, 0, 0, 1, 1, Qt.AlignmentFlag.AlignLeft)

        self.bt_deletar_duplicados = QPushButton(self.frame_10)
        self.bt_deletar_duplicados.setObjectName(u"bt_deletar_duplicados")
        self.bt_deletar_duplicados.setMinimumSize(QSize(180, 30))
        self.bt_deletar_duplicados.setMaximumSize(QSize(180, 16777215))
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
        self.bt_deletar_duplicados.setIconSize(QSize(40, 40))

        self.gridLayout_16.addWidget(self.bt_deletar_duplicados, 0, 1, 1, 1)


        self.gridLayout_13.addWidget(self.frame_10, 5, 0, 1, 1)

        self.tableWidget = QTableWidget(self.frame_tabelas_duplicadas)
        self.tableWidget.setObjectName(u"tableWidget")

        self.gridLayout_13.addWidget(self.tableWidget, 3, 0, 1, 1)

        self.label_3 = QLabel(self.frame_tabelas_duplicadas)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_13.addWidget(self.label_3, 4, 0, 1, 1)


        self.gridLayout_10.addWidget(self.frame_tabelas_duplicadas, 2, 0, 1, 1)

        self.tabs_lateral_right.addTab(self.tab_dados_duplicados, "")

        self.gridLayout_6.addWidget(self.tabs_lateral_right, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.widget_right, 1, 1, 2, 1)


        self.gridLayout.addWidget(self.widget, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabs_lateral_right.setCurrentIndex(0)


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
        self.bt_mostra_dados_tabelas.setText(QCoreApplication.translate("MainWindow", u"Mostrar Dados", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Clique para mostrar os dados da tabela</p></body></html>", None))
        self.tabs_lateral_right.setTabText(self.tabs_lateral_right.indexOf(self.tab_lista_tabelas_db), QCoreApplication.translate("MainWindow", u"Tabelas", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:700;\">DADOS DUPLICADOS</span></p></body></html>", None))
        self.bt_exportar_duplicados.setText(QCoreApplication.translate("MainWindow", u"Exportar", None))
        self.bt_deletar_duplicados.setText(QCoreApplication.translate("MainWindow", u"Deletar", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Para lidar com os dados duplicados selecione uma das op\u00e7\u00f5es a cima.</p></body></html>", None))
        self.tabs_lateral_right.setTabText(self.tabs_lateral_right.indexOf(self.tab_dados_duplicados), QCoreApplication.translate("MainWindow", u"Dados Duplicados", None))
    # retranslateUi

