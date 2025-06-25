# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainEcpUfA.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractSpinBox, QApplication, QCheckBox,
    QComboBox, QDateEdit, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPlainTextEdit, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTabWidget, QTableWidget, QTableWidgetItem, QTreeView,
    QVBoxLayout, QWidget)
from ui import icon_rc

class Ui_PrincipalWindow(object):
    def setupUi(self, PrincipalWindow):
        if not PrincipalWindow.objectName():
            PrincipalWindow.setObjectName(u"PrincipalWindow")
        PrincipalWindow.setEnabled(True)
        PrincipalWindow.resize(1400, 800)
        PrincipalWindow.setMinimumSize(QSize(1400, 800))
        PrincipalWindow.setMaximumSize(QSize(1400, 800))
        PrincipalWindow.setStyleSheet(u"#PrincipalWindow QFrame{\n"
"	background-color: rgb(242, 242, 242);\n"
"\n"
"}\n"
"\n"
"\n"
"#centralwidget  {\n"
"	\n"
"	\n"
"	border: 1px solid rgba(109, 109, 109, 0.30);\n"
"	 border-top-left-radius: 5px;\n"
"    border-top-right-radius: 5px;\n"
"    border-bottom-left-radius: 5px;\n"
"    border-bottom-right-radius: 5px;\n"
"}\n"
"\n"
"#tabWidgetFiscal_contabil{\n"
"	border:none;\n"
"}\n"
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
"	border: none;"
                        "\n"
"	background-color: rgb(226, 226, 226);\n"
"}\n"
"\n"
"#btn_minimize:hover{\n"
"	border: none;\n"
"	background-color: rgb(226, 226, 226);\n"
"}\n"
"\n"
"#btn_executar_pesquisas{\n"
"	border:none;\n"
"}\n"
"\n"
"\n"
"#table_principal{	\n"
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
"      background-color: #c8c8c8;\n"
"		border: 1px solid rgba(217, 217, 217, 0.80);\n"
"	font: 700 11pt \"Times New Roman\";\n"
"       \n"
"	color: rgb(0, 0, 0);\n"
"\n"
""
                        "}\n"
"\n"
"\n"
"    QScrollBar:vertical {\n"
"        border: none;\n"
"        background: #F0F0F0; /* Cor de fundo da barra de rolagem */\n"
"        width: 12px;\n"
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
"    QScrollBar::add-page:vertical, QScro"
                        "llBar::sub-page:vertical {\n"
"        background: none;\n"
"    }\n"
"\n"
"    QScrollBar:horizontal {\n"
"        border: none;\n"
"        background: #F0F0F0; /* Cor de fundo da barra de rolagem */\n"
"        height: 12px;\n"
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
"        back"
                        "ground: none;\n"
"    }\n"
"\n"
"    QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"        background: none;\n"
"    }\n"
"\n"
"\n"
"#btn_closeFrm_lateral{\n"
"        background-color: #c42b1c;\n"
"        border-radius: 9px;\n"
"        min-width: 20px;\n"
"        min-height: 20px;\n"
"        max-width: 20px;\n"
"        max-height: 20px;\n"
"\n"
"    }\n"
"\n"
"#btn_closeFrm_cliente{\n"
"        background-color: #c42b1c;\n"
"        border-radius: 9px;\n"
"        min-width: 20px;\n"
"        min-height: 20px;\n"
"        max-width: 20px;\n"
"        max-height: 20px;\n"
"}\n"
"\n"
"#btn_closeFrm_contabilidade{\n"
"        background-color: #c42b1c;\n"
"        border-radius: 9px;\n"
"        min-width: 20px;\n"
"        min-height: 20px;\n"
"        max-width: 20px;\n"
"        max-height: 20px;\n"
"}\n"
"\n"
"\n"
"\n"
"#frm_functions_table_principal QPushButton{\n"
"	border: none;\n"
"\n"
"}\n"
"\n"
"#frm_functions_table_principal QPushButton:hover{\n"
"	border: none;\n"
"	back"
                        "ground-color: rgba(226, 226, 226, 0.20);\n"
"	border: 1px solid rgba(109, 109, 109, 0.30);\n"
"    border-top-left-radius: 5px;\n"
"    border-top-right-radius: 5px;\n"
"    border-bottom-left-radius: 5px;\n"
"    border-bottom-right-radius: 5px;\n"
"}\n"
"\n"
"#frm_setas_titulo QPushButton{\n"
"	border: none;\n"
"}\n"
"\n"
"#frm_setas_titulo QPushButton:hover{\n"
"	border: none;\n"
"}\n"
"\n"
"#lb_titulos_tabelas{\n"
"	\n"
"	font: 700 16pt \"Arial\";\n"
"	qproperty-alignment: AlignCenter;\n"
"}")
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
        self.btn_importar_file.setGeometry(QRect(10, 10, 150, 35))
        self.btn_importar_file.setMinimumSize(QSize(150, 35))
        self.btn_importar_file.setMaximumSize(QSize(150, 35))
        self.btn_importar_file.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/file.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_importar_file.setIcon(icon4)
        self.btn_importar_file.setIconSize(QSize(25, 25))
        self.btn_opcoes_pesquisas = QPushButton(self.frm_buttons_menu)
        self.btn_opcoes_pesquisas.setObjectName(u"btn_opcoes_pesquisas")
        self.btn_opcoes_pesquisas.setGeometry(QRect(170, 10, 150, 35))
        self.btn_opcoes_pesquisas.setMinimumSize(QSize(150, 35))
        self.btn_opcoes_pesquisas.setMaximumSize(QSize(150, 35))
        self.btn_opcoes_pesquisas.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/search.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_opcoes_pesquisas.setIcon(icon5)
        self.btn_opcoes_pesquisas.setIconSize(QSize(25, 25))
        self.btn_opcoes_processamento = QPushButton(self.frm_buttons_menu)
        self.btn_opcoes_processamento.setObjectName(u"btn_opcoes_processamento")
        self.btn_opcoes_processamento.setGeometry(QRect(330, 10, 180, 35))
        self.btn_opcoes_processamento.setMinimumSize(QSize(180, 35))
        self.btn_opcoes_processamento.setMaximumSize(QSize(180, 35))
        self.btn_opcoes_processamento.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/data-processing.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_opcoes_processamento.setIcon(icon6)
        self.btn_opcoes_processamento.setIconSize(QSize(25, 25))
        self.btn_opcoes_conexoes_db = QPushButton(self.frm_buttons_menu)
        self.btn_opcoes_conexoes_db.setObjectName(u"btn_opcoes_conexoes_db")
        self.btn_opcoes_conexoes_db.setGeometry(QRect(520, 10, 150, 35))
        self.btn_opcoes_conexoes_db.setMinimumSize(QSize(150, 35))
        self.btn_opcoes_conexoes_db.setMaximumSize(QSize(150, 35))
        self.btn_opcoes_conexoes_db.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/data.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_opcoes_conexoes_db.setIcon(icon7)
        self.btn_opcoes_conexoes_db.setIconSize(QSize(30, 30))
        self.btn_opcoes_conexoes_db.setAutoDefault(False)
        self.btn_opcoes_contabil = QPushButton(self.frm_buttons_menu)
        self.btn_opcoes_contabil.setObjectName(u"btn_opcoes_contabil")
        self.btn_opcoes_contabil.setGeometry(QRect(680, 10, 150, 35))
        self.btn_opcoes_contabil.setMinimumSize(QSize(150, 35))
        self.btn_opcoes_contabil.setMaximumSize(QSize(150, 35))
        self.btn_opcoes_contabil.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/account.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_opcoes_contabil.setIcon(icon8)
        self.btn_opcoes_contabil.setIconSize(QSize(30, 30))
        self.btn_opcoes_contabil.setAutoDefault(False)

        self.verticalLayout_2.addWidget(self.frm_buttons_menu)

        self.frm_layout_geral = QFrame(self.frame)
        self.frm_layout_geral.setObjectName(u"frm_layout_geral")
        self.frm_layout_geral.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_layout_geral.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frm_layout_geral)
        self.gridLayout.setSpacing(2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, -1, -1, 5)
        self.frame_opcoes_busca_processamento = QFrame(self.frm_layout_geral)
        self.frame_opcoes_busca_processamento.setObjectName(u"frame_opcoes_busca_processamento")
        self.frame_opcoes_busca_processamento.setMinimumSize(QSize(0, 0))
        self.frame_opcoes_busca_processamento.setMaximumSize(QSize(16777215, 16777215))
        self.frame_opcoes_busca_processamento.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_opcoes_busca_processamento.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_opcoes_busca_processamento)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.page_opcoes_busca = QFrame(self.frame_opcoes_busca_processamento)
        self.page_opcoes_busca.setObjectName(u"page_opcoes_busca")
        self.page_opcoes_busca.setMinimumSize(QSize(0, 120))
        self.page_opcoes_busca.setMaximumSize(QSize(16777215, 120))
        self.page_opcoes_busca.setFrameShape(QFrame.Shape.StyledPanel)
        self.page_opcoes_busca.setFrameShadow(QFrame.Shadow.Raised)
        self.layoutWidget = QWidget(self.page_opcoes_busca)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 341, 101))
        self.gridLayout_3 = QGridLayout(self.layoutWidget)
        self.gridLayout_3.setSpacing(2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btn_executar_pesquisas = QPushButton(self.layoutWidget)
        self.btn_executar_pesquisas.setObjectName(u"btn_executar_pesquisas")
        self.btn_executar_pesquisas.setMinimumSize(QSize(30, 30))
        self.btn_executar_pesquisas.setMaximumSize(QSize(16777215, 30))
        self.btn_executar_pesquisas.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/btn_buscar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_executar_pesquisas.setIcon(icon9)
        self.btn_executar_pesquisas.setIconSize(QSize(18, 18))

        self.gridLayout_3.addWidget(self.btn_executar_pesquisas, 0, 1, 1, 1, Qt.AlignmentFlag.AlignLeft)

        self.combo_opcoes_busca = QComboBox(self.layoutWidget)
        self.combo_opcoes_busca.addItem("")
        self.combo_opcoes_busca.addItem("")
        self.combo_opcoes_busca.addItem("")
        self.combo_opcoes_busca.addItem("")
        self.combo_opcoes_busca.addItem("")
        self.combo_opcoes_busca.setObjectName(u"combo_opcoes_busca")
        self.combo_opcoes_busca.setMinimumSize(QSize(0, 30))
        self.combo_opcoes_busca.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_3.addWidget(self.combo_opcoes_busca, 0, 0, 1, 1)

        self.btn_extrair_duplicados = QPushButton(self.layoutWidget)
        self.btn_extrair_duplicados.setObjectName(u"btn_extrair_duplicados")
        self.btn_extrair_duplicados.setMinimumSize(QSize(0, 30))
        self.btn_extrair_duplicados.setMaximumSize(QSize(16777215, 30))
        self.btn_extrair_duplicados.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_3.addWidget(self.btn_extrair_duplicados, 2, 1, 1, 1)

        self.txt_op_busca1 = QLineEdit(self.layoutWidget)
        self.txt_op_busca1.setObjectName(u"txt_op_busca1")
        self.txt_op_busca1.setMinimumSize(QSize(0, 30))
        self.txt_op_busca1.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_3.addWidget(self.txt_op_busca1, 2, 0, 1, 1)

        self.comboBox_opcoes_de_busca2 = QComboBox(self.layoutWidget)
        self.comboBox_opcoes_de_busca2.setObjectName(u"comboBox_opcoes_de_busca2")
        self.comboBox_opcoes_de_busca2.setMinimumSize(QSize(0, 30))
        self.comboBox_opcoes_de_busca2.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_3.addWidget(self.comboBox_opcoes_de_busca2, 1, 0, 1, 1)


        self.verticalLayout_6.addWidget(self.page_opcoes_busca)

        self.page_opcoes_processamento = QFrame(self.frame_opcoes_busca_processamento)
        self.page_opcoes_processamento.setObjectName(u"page_opcoes_processamento")
        self.page_opcoes_processamento.setEnabled(True)
        self.page_opcoes_processamento.setMinimumSize(QSize(0, 120))
        self.page_opcoes_processamento.setMaximumSize(QSize(16777215, 120))
        self.page_opcoes_processamento.setFrameShape(QFrame.Shape.StyledPanel)
        self.page_opcoes_processamento.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.page_opcoes_processamento)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.frm_processamento1 = QFrame(self.page_opcoes_processamento)
        self.frm_processamento1.setObjectName(u"frm_processamento1")
        self.frm_processamento1.setMinimumSize(QSize(300, 0))
        self.frm_processamento1.setMaximumSize(QSize(300, 16777215))
        self.frm_processamento1.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_processamento1.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frm_processamento1)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.comboBox = QComboBox(self.frm_processamento1)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(0, 30))
        self.comboBox.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_4.addWidget(self.comboBox)

        self.btn_executar_processamento = QPushButton(self.frm_processamento1)
        self.btn_executar_processamento.setObjectName(u"btn_executar_processamento")
        self.btn_executar_processamento.setMinimumSize(QSize(0, 30))
        self.btn_executar_processamento.setMaximumSize(QSize(16777215, 30))
        self.btn_executar_processamento.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.btn_executar_processamento, 0, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout_5.addWidget(self.frm_processamento1)

        self.frm_processamento2 = QFrame(self.page_opcoes_processamento)
        self.frm_processamento2.setObjectName(u"frm_processamento2")
        self.frm_processamento2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_processamento2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.frm_processamento2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.bt_retirar_combo1 = QPushButton(self.frm_processamento2)
        self.bt_retirar_combo1.setObjectName(u"bt_retirar_combo1")
        self.bt_retirar_combo1.setMinimumSize(QSize(0, 35))
        self.bt_retirar_combo1.setMaximumSize(QSize(16777215, 35))
        self.bt_retirar_combo1.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon10 = QIcon()
        icon10.addFile(u":/icons/icons/minus (1).png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_retirar_combo1.setIcon(icon10)
        self.bt_retirar_combo1.setIconSize(QSize(25, 25))

        self.gridLayout_2.addWidget(self.bt_retirar_combo1, 2, 5, 1, 1)

        self.txt_coluna_processamento2 = QLineEdit(self.frm_processamento2)
        self.txt_coluna_processamento2.setObjectName(u"txt_coluna_processamento2")
        self.txt_coluna_processamento2.setMinimumSize(QSize(180, 30))
        self.txt_coluna_processamento2.setMaximumSize(QSize(180, 30))

        self.gridLayout_2.addWidget(self.txt_coluna_processamento2, 2, 3, 1, 1)

        self.bt_retirar_combo = QPushButton(self.frm_processamento2)
        self.bt_retirar_combo.setObjectName(u"bt_retirar_combo")
        self.bt_retirar_combo.setMinimumSize(QSize(0, 35))
        self.bt_retirar_combo.setMaximumSize(QSize(16777215, 35))
        self.bt_retirar_combo.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.bt_retirar_combo.setIcon(icon10)
        self.bt_retirar_combo.setIconSize(QSize(25, 25))

        self.gridLayout_2.addWidget(self.bt_retirar_combo, 2, 2, 1, 1)

        self.txt_coluna_processamento1 = QLineEdit(self.frm_processamento2)
        self.txt_coluna_processamento1.setObjectName(u"txt_coluna_processamento1")
        self.txt_coluna_processamento1.setMinimumSize(QSize(180, 30))
        self.txt_coluna_processamento1.setMaximumSize(QSize(180, 30))

        self.gridLayout_2.addWidget(self.txt_coluna_processamento1, 2, 0, 1, 1)

        self.cbx_coluna_processamento1 = QComboBox(self.frm_processamento2)
        self.cbx_coluna_processamento1.setObjectName(u"cbx_coluna_processamento1")
        self.cbx_coluna_processamento1.setMinimumSize(QSize(180, 30))
        self.cbx_coluna_processamento1.setMaximumSize(QSize(180, 30))

        self.gridLayout_2.addWidget(self.cbx_coluna_processamento1, 0, 0, 1, 1)

        self.bt_add_combo = QPushButton(self.frm_processamento2)
        self.bt_add_combo.setObjectName(u"bt_add_combo")
        self.bt_add_combo.setMinimumSize(QSize(0, 35))
        self.bt_add_combo.setMaximumSize(QSize(16777215, 35))
        self.bt_add_combo.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon11 = QIcon()
        icon11.addFile(u":/icons/icons/more.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_add_combo.setIcon(icon11)
        self.bt_add_combo.setIconSize(QSize(25, 25))

        self.gridLayout_2.addWidget(self.bt_add_combo, 2, 1, 1, 1)

        self.cbx_coluna_processamento2 = QComboBox(self.frm_processamento2)
        self.cbx_coluna_processamento2.setObjectName(u"cbx_coluna_processamento2")
        self.cbx_coluna_processamento2.setMinimumSize(QSize(180, 30))
        self.cbx_coluna_processamento2.setMaximumSize(QSize(180, 30))

        self.gridLayout_2.addWidget(self.cbx_coluna_processamento2, 0, 3, 1, 1)

        self.cbx_coluna_processamento3 = QComboBox(self.frm_processamento2)
        self.cbx_coluna_processamento3.setObjectName(u"cbx_coluna_processamento3")
        self.cbx_coluna_processamento3.setMinimumSize(QSize(180, 30))
        self.cbx_coluna_processamento3.setMaximumSize(QSize(180, 30))

        self.gridLayout_2.addWidget(self.cbx_coluna_processamento3, 0, 6, 1, 1)

        self.txt_coluna_processamento3 = QLineEdit(self.frm_processamento2)
        self.txt_coluna_processamento3.setObjectName(u"txt_coluna_processamento3")
        self.txt_coluna_processamento3.setMinimumSize(QSize(180, 30))
        self.txt_coluna_processamento3.setMaximumSize(QSize(180, 30))

        self.gridLayout_2.addWidget(self.txt_coluna_processamento3, 2, 6, 1, 1)

        self.bt_add_combo2 = QPushButton(self.frm_processamento2)
        self.bt_add_combo2.setObjectName(u"bt_add_combo2")
        self.bt_add_combo2.setMinimumSize(QSize(0, 35))
        self.bt_add_combo2.setMaximumSize(QSize(16777215, 35))
        self.bt_add_combo2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.bt_add_combo2.setIcon(icon11)
        self.bt_add_combo2.setIconSize(QSize(25, 25))

        self.gridLayout_2.addWidget(self.bt_add_combo2, 2, 4, 1, 1)

        self.txt_coluna_processamento3.raise_()
        self.txt_coluna_processamento2.raise_()
        self.cbx_coluna_processamento1.raise_()
        self.bt_add_combo.raise_()
        self.txt_coluna_processamento1.raise_()
        self.bt_add_combo2.raise_()
        self.cbx_coluna_processamento3.raise_()
        self.cbx_coluna_processamento2.raise_()
        self.bt_retirar_combo1.raise_()
        self.bt_retirar_combo.raise_()

        self.horizontalLayout_5.addWidget(self.frm_processamento2)


        self.verticalLayout_6.addWidget(self.page_opcoes_processamento)


        self.gridLayout.addWidget(self.frame_opcoes_busca_processamento, 0, 0, 1, 1)

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
        self.btn_voltar_pagina.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon12 = QIcon()
        icon12.addFile(u":/icons/icons/voltar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_voltar_pagina.setIcon(icon12)
        self.btn_voltar_pagina.setIconSize(QSize(20, 20))

        self.horizontalLayout_4.addWidget(self.btn_voltar_pagina, 0, Qt.AlignmentFlag.AlignLeft)

        self.lb_titulos_tabelas = QLabel(self.frm_setas_titulo)
        self.lb_titulos_tabelas.setObjectName(u"lb_titulos_tabelas")

        self.horizontalLayout_4.addWidget(self.lb_titulos_tabelas)

        self.btn_proxima_pagina = QPushButton(self.frm_setas_titulo)
        self.btn_proxima_pagina.setObjectName(u"btn_proxima_pagina")
        self.btn_proxima_pagina.setMinimumSize(QSize(0, 30))
        self.btn_proxima_pagina.setMaximumSize(QSize(16777215, 30))
        self.btn_proxima_pagina.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon13 = QIcon()
        icon13.addFile(u":/icons/icons/proxima.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_proxima_pagina.setIcon(icon13)
        self.btn_proxima_pagina.setIconSize(QSize(20, 20))

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
        self.frm_functions_table_principal.setMinimumSize(QSize(0, 50))
        self.frm_functions_table_principal.setMaximumSize(QSize(16777215, 50))
        self.frm_functions_table_principal.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_functions_table_principal.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frm_functions_table_principal)
        self.horizontalLayout_3.setSpacing(2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(2, 2, 2, 2)
        self.btn_desfazer = QPushButton(self.frm_functions_table_principal)
        self.btn_desfazer.setObjectName(u"btn_desfazer")
        self.btn_desfazer.setMinimumSize(QSize(40, 40))
        self.btn_desfazer.setMaximumSize(QSize(40, 40))
        icon14 = QIcon()
        icon14.addFile(u":/icons/icons/arrow.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_desfazer.setIcon(icon14)
        self.btn_desfazer.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.btn_desfazer, 0, Qt.AlignmentFlag.AlignLeft)

        self.line_2 = QFrame(self.frm_functions_table_principal)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_3.addWidget(self.line_2, 0, Qt.AlignmentFlag.AlignLeft)

        self.bt_salvar_dados_tabela_principal = QPushButton(self.frm_functions_table_principal)
        self.bt_salvar_dados_tabela_principal.setObjectName(u"bt_salvar_dados_tabela_principal")
        self.bt_salvar_dados_tabela_principal.setMinimumSize(QSize(40, 40))
        self.bt_salvar_dados_tabela_principal.setMaximumSize(QSize(40, 40))
        self.bt_salvar_dados_tabela_principal.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.bt_salvar_dados_tabela_principal.setStyleSheet(u"")
        icon15 = QIcon()
        icon15.addFile(u":/icons/icons/save-as.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_salvar_dados_tabela_principal.setIcon(icon15)
        self.bt_salvar_dados_tabela_principal.setIconSize(QSize(25, 25))

        self.horizontalLayout_3.addWidget(self.bt_salvar_dados_tabela_principal)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.bt_reprocesar_csv = QPushButton(self.frm_functions_table_principal)
        self.bt_reprocesar_csv.setObjectName(u"bt_reprocesar_csv")
        self.bt_reprocesar_csv.setMinimumSize(QSize(40, 40))
        self.bt_reprocesar_csv.setMaximumSize(QSize(40, 40))
        self.bt_reprocesar_csv.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon16 = QIcon()
        icon16.addFile(u":/icons/icons/refresh.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_reprocesar_csv.setIcon(icon16)
        self.bt_reprocesar_csv.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.bt_reprocesar_csv)


        self.verticalLayout_5.addWidget(self.frm_functions_table_principal)

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
        self.page_duplicados = QWidget()
        self.page_duplicados.setObjectName(u"page_duplicados")
        self.verticalLayout_9 = QVBoxLayout(self.page_duplicados)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frm_functions_table_duplicados = QFrame(self.page_duplicados)
        self.frm_functions_table_duplicados.setObjectName(u"frm_functions_table_duplicados")
        self.frm_functions_table_duplicados.setMinimumSize(QSize(0, 50))
        self.frm_functions_table_duplicados.setMaximumSize(QSize(16777215, 50))
        self.frm_functions_table_duplicados.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_functions_table_duplicados.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_9.addWidget(self.frm_functions_table_duplicados)

        self.table_duplicados = QTableWidget(self.page_duplicados)
        self.table_duplicados.setObjectName(u"table_duplicados")

        self.verticalLayout_9.addWidget(self.table_duplicados)

        self.stackedWidget_tables.addWidget(self.page_duplicados)
        self.page_contabil_fiscal = QWidget()
        self.page_contabil_fiscal.setObjectName(u"page_contabil_fiscal")
        self.verticalLayout_10 = QVBoxLayout(self.page_contabil_fiscal)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.tabWidgetFiscal_contabil = QTabWidget(self.page_contabil_fiscal)
        self.tabWidgetFiscal_contabil.setObjectName(u"tabWidgetFiscal_contabil")
        self.tabWidgetFiscal_contabil.setTabPosition(QTabWidget.TabPosition.North)
        self.tabWidgetFiscal_contabil.setTabShape(QTabWidget.TabShape.Rounded)
        self.tabWidgetFiscal_contabil.setElideMode(Qt.TextElideMode.ElideLeft)
        self.tabWidgetFiscal_contabil.setDocumentMode(False)
        self.tabWidgetFiscal_contabil.setTabsClosable(False)
        self.tabWidgetFiscal_contabil.setMovable(False)
        self.tabWidgetFiscal_contabil.setTabBarAutoHide(False)
        self.tab_clientes = QWidget()
        self.tab_clientes.setObjectName(u"tab_clientes")
        self.horizontalLayout_2 = QHBoxLayout(self.tab_clientes)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frm_table_cliente = QFrame(self.tab_clientes)
        self.frm_table_cliente.setObjectName(u"frm_table_cliente")
        self.frm_table_cliente.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_table_cliente.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frm_table_cliente)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frm_filtros_cliente = QFrame(self.frm_table_cliente)
        self.frm_filtros_cliente.setObjectName(u"frm_filtros_cliente")
        self.frm_filtros_cliente.setMinimumSize(QSize(0, 50))
        self.frm_filtros_cliente.setMaximumSize(QSize(16777215, 50))
        self.frm_filtros_cliente.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_filtros_cliente.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frm_filtros_cliente)
        self.horizontalLayout_13.setSpacing(2)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(5, 2, 5, 2)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.txt_buscar_cliente = QLineEdit(self.frm_filtros_cliente)
        self.txt_buscar_cliente.setObjectName(u"txt_buscar_cliente")
        self.txt_buscar_cliente.setMinimumSize(QSize(300, 30))
        self.txt_buscar_cliente.setMaximumSize(QSize(300, 30))
        self.txt_buscar_cliente.setFrame(True)

        self.horizontalLayout_7.addWidget(self.txt_buscar_cliente, 0, Qt.AlignmentFlag.AlignLeft)

        self.btn_busca_avancada_cliente = QPushButton(self.frm_filtros_cliente)
        self.btn_busca_avancada_cliente.setObjectName(u"btn_busca_avancada_cliente")
        self.btn_busca_avancada_cliente.setMinimumSize(QSize(100, 30))
        self.btn_busca_avancada_cliente.setMaximumSize(QSize(100, 30))

        self.horizontalLayout_7.addWidget(self.btn_busca_avancada_cliente, 0, Qt.AlignmentFlag.AlignLeft)


        self.horizontalLayout_13.addLayout(self.horizontalLayout_7)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_3)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.data_filtro_inicio_cliente = QDateEdit(self.frm_filtros_cliente)
        self.data_filtro_inicio_cliente.setObjectName(u"data_filtro_inicio_cliente")
        self.data_filtro_inicio_cliente.setMinimumSize(QSize(100, 0))
        self.data_filtro_inicio_cliente.setMaximumSize(QSize(100, 16777215))
        self.data_filtro_inicio_cliente.setFrame(False)
        self.data_filtro_inicio_cliente.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.data_filtro_inicio_cliente.setReadOnly(False)
        self.data_filtro_inicio_cliente.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.data_filtro_inicio_cliente.setMinimumDateTime(QDateTime(QDate(1752, 9, 16), QTime(0, 0, 0)))
        self.data_filtro_inicio_cliente.setCalendarPopup(True)
        self.data_filtro_inicio_cliente.setTimeSpec(Qt.TimeSpec.LocalTime)

        self.horizontalLayout_11.addWidget(self.data_filtro_inicio_cliente)

        self.data_filtro_fim_cliente = QDateEdit(self.frm_filtros_cliente)
        self.data_filtro_fim_cliente.setObjectName(u"data_filtro_fim_cliente")
        self.data_filtro_fim_cliente.setMinimumSize(QSize(100, 0))
        self.data_filtro_fim_cliente.setMaximumSize(QSize(100, 16777215))
        self.data_filtro_fim_cliente.setWrapping(False)
        self.data_filtro_fim_cliente.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.data_filtro_fim_cliente.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.data_filtro_fim_cliente.setCalendarPopup(True)

        self.horizontalLayout_11.addWidget(self.data_filtro_fim_cliente)


        self.horizontalLayout_13.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.combo_filtro_statusEnvio = QComboBox(self.frm_filtros_cliente)
        self.combo_filtro_statusEnvio.setObjectName(u"combo_filtro_statusEnvio")
        self.combo_filtro_statusEnvio.setMinimumSize(QSize(120, 0))
        self.combo_filtro_statusEnvio.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_12.addWidget(self.combo_filtro_statusEnvio)

        self.combo_filtro_contador = QComboBox(self.frm_filtros_cliente)
        self.combo_filtro_contador.setObjectName(u"combo_filtro_contador")
        self.combo_filtro_contador.setMinimumSize(QSize(120, 0))
        self.combo_filtro_contador.setMaximumSize(QSize(120, 16777215))
        self.combo_filtro_contador.setDuplicatesEnabled(False)

        self.horizontalLayout_12.addWidget(self.combo_filtro_contador)

        self.btn_novo_cliente = QPushButton(self.frm_filtros_cliente)
        self.btn_novo_cliente.setObjectName(u"btn_novo_cliente")
        self.btn_novo_cliente.setMinimumSize(QSize(120, 30))
        self.btn_novo_cliente.setMaximumSize(QSize(120, 30))

        self.horizontalLayout_12.addWidget(self.btn_novo_cliente)


        self.horizontalLayout_13.addLayout(self.horizontalLayout_12)


        self.verticalLayout_11.addWidget(self.frm_filtros_cliente)

        self.table_clientes = QTableWidget(self.frm_table_cliente)
        if (self.table_clientes.columnCount() < 13):
            self.table_clientes.setColumnCount(13)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_clientes.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_clientes.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_clientes.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table_clientes.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table_clientes.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table_clientes.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.table_clientes.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.table_clientes.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.table_clientes.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.table_clientes.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.table_clientes.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.table_clientes.setHorizontalHeaderItem(11, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.table_clientes.setHorizontalHeaderItem(12, __qtablewidgetitem12)
        self.table_clientes.setObjectName(u"table_clientes")
        self.table_clientes.verticalHeader().setVisible(False)

        self.verticalLayout_11.addWidget(self.table_clientes)


        self.horizontalLayout_2.addWidget(self.frm_table_cliente)

        self.frm_cadastro_cliente = QFrame(self.tab_clientes)
        self.frm_cadastro_cliente.setObjectName(u"frm_cadastro_cliente")
        self.frm_cadastro_cliente.setMinimumSize(QSize(320, 0))
        self.frm_cadastro_cliente.setMaximumSize(QSize(320, 16777215))
        self.frm_cadastro_cliente.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_cadastro_cliente.setFrameShadow(QFrame.Shadow.Raised)
        self.layoutWidget1 = QWidget(self.frm_cadastro_cliente)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 0, 301, 451))
        self.verticalLayout_12 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_12.setSpacing(6)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frm_btn_close_cliente = QFrame(self.layoutWidget1)
        self.frm_btn_close_cliente.setObjectName(u"frm_btn_close_cliente")
        self.frm_btn_close_cliente.setMinimumSize(QSize(0, 30))
        self.frm_btn_close_cliente.setMaximumSize(QSize(16777215, 30))
        self.frm_btn_close_cliente.setFrameShape(QFrame.Shape.NoFrame)
        self.frm_btn_close_cliente.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frm_btn_close_cliente)
        self.verticalLayout_13.setSpacing(2)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(2, 2, 2, 2)
        self.btn_closeFrm_cliente = QPushButton(self.frm_btn_close_cliente)
        self.btn_closeFrm_cliente.setObjectName(u"btn_closeFrm_cliente")
        self.btn_closeFrm_cliente.setMinimumSize(QSize(20, 20))
        self.btn_closeFrm_cliente.setMaximumSize(QSize(20, 20))
        self.btn_closeFrm_cliente.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_closeFrm_cliente.setIcon(icon3)
        self.btn_closeFrm_cliente.setIconSize(QSize(7, 7))

        self.verticalLayout_13.addWidget(self.btn_closeFrm_cliente, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_12.addWidget(self.frm_btn_close_cliente)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.btn_situacao_cliente = QCheckBox(self.layoutWidget1)
        self.btn_situacao_cliente.setObjectName(u"btn_situacao_cliente")
        self.btn_situacao_cliente.setMaximumSize(QSize(60, 16777215))
        self.btn_situacao_cliente.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_6.addWidget(self.btn_situacao_cliente, 0, Qt.AlignmentFlag.AlignRight)

        self.combo_status_envio_arquivos_cliente = QComboBox(self.layoutWidget1)
        self.combo_status_envio_arquivos_cliente.addItem("")
        self.combo_status_envio_arquivos_cliente.addItem("")
        self.combo_status_envio_arquivos_cliente.addItem("")
        self.combo_status_envio_arquivos_cliente.addItem("")
        self.combo_status_envio_arquivos_cliente.addItem("")
        self.combo_status_envio_arquivos_cliente.setObjectName(u"combo_status_envio_arquivos_cliente")
        self.combo_status_envio_arquivos_cliente.setMinimumSize(QSize(140, 30))
        self.combo_status_envio_arquivos_cliente.setMaximumSize(QSize(140, 30))

        self.horizontalLayout_6.addWidget(self.combo_status_envio_arquivos_cliente, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_12.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.txt_id_cliente = QLineEdit(self.layoutWidget1)
        self.txt_id_cliente.setObjectName(u"txt_id_cliente")
        self.txt_id_cliente.setMinimumSize(QSize(50, 30))
        self.txt_id_cliente.setMaximumSize(QSize(50, 30))

        self.horizontalLayout_17.addWidget(self.txt_id_cliente, 0, Qt.AlignmentFlag.AlignLeft)

        self.txt_cnpj_cliente = QLineEdit(self.layoutWidget1)
        self.txt_cnpj_cliente.setObjectName(u"txt_cnpj_cliente")
        self.txt_cnpj_cliente.setMinimumSize(QSize(200, 30))
        self.txt_cnpj_cliente.setMaximumSize(QSize(200, 30))

        self.horizontalLayout_17.addWidget(self.txt_cnpj_cliente, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_12.addLayout(self.horizontalLayout_17)

        self.txt_nome_cliente = QLineEdit(self.layoutWidget1)
        self.txt_nome_cliente.setObjectName(u"txt_nome_cliente")
        self.txt_nome_cliente.setMinimumSize(QSize(0, 30))
        self.txt_nome_cliente.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_12.addWidget(self.txt_nome_cliente)

        self.txt_razao_social_cliente = QLineEdit(self.layoutWidget1)
        self.txt_razao_social_cliente.setObjectName(u"txt_razao_social_cliente")
        self.txt_razao_social_cliente.setMinimumSize(QSize(0, 30))
        self.txt_razao_social_cliente.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_12.addWidget(self.txt_razao_social_cliente)

        self.txt_email_cliente = QLineEdit(self.layoutWidget1)
        self.txt_email_cliente.setObjectName(u"txt_email_cliente")
        self.txt_email_cliente.setMinimumSize(QSize(0, 30))
        self.txt_email_cliente.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_12.addWidget(self.txt_email_cliente)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.combo_contador = QComboBox(self.layoutWidget1)
        self.combo_contador.setObjectName(u"combo_contador")
        self.combo_contador.setMinimumSize(QSize(200, 30))
        self.combo_contador.setMaximumSize(QSize(200, 30))

        self.horizontalLayout_8.addWidget(self.combo_contador)

        self.btn_novo_contador = QPushButton(self.layoutWidget1)
        self.btn_novo_contador.setObjectName(u"btn_novo_contador")
        self.btn_novo_contador.setMinimumSize(QSize(30, 30))
        self.btn_novo_contador.setMaximumSize(QSize(30, 30))
        self.btn_novo_contador.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_novo_contador.setIcon(icon11)
        self.btn_novo_contador.setIconSize(QSize(18, 18))

        self.horizontalLayout_8.addWidget(self.btn_novo_contador, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_12.addLayout(self.horizontalLayout_8)

        self.combo_sistema_cliente = QComboBox(self.layoutWidget1)
        self.combo_sistema_cliente.addItem("")
        self.combo_sistema_cliente.addItem("")
        self.combo_sistema_cliente.addItem("")
        self.combo_sistema_cliente.addItem("")
        self.combo_sistema_cliente.addItem("")
        self.combo_sistema_cliente.addItem("")
        self.combo_sistema_cliente.setObjectName(u"combo_sistema_cliente")
        self.combo_sistema_cliente.setMinimumSize(QSize(0, 30))
        self.combo_sistema_cliente.setMaximumSize(QSize(16777215, 30))
        self.combo_sistema_cliente.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)

        self.verticalLayout_12.addWidget(self.combo_sistema_cliente)

        self.txt_link_sistema_cliente = QLineEdit(self.layoutWidget1)
        self.txt_link_sistema_cliente.setObjectName(u"txt_link_sistema_cliente")
        self.txt_link_sistema_cliente.setMinimumSize(QSize(0, 30))
        self.txt_link_sistema_cliente.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_12.addWidget(self.txt_link_sistema_cliente)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.txt_user_cliente_sistema = QLineEdit(self.layoutWidget1)
        self.txt_user_cliente_sistema.setObjectName(u"txt_user_cliente_sistema")
        self.txt_user_cliente_sistema.setMinimumSize(QSize(0, 30))
        self.txt_user_cliente_sistema.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_9.addWidget(self.txt_user_cliente_sistema)

        self.txt_password_cliente_sistema = QLineEdit(self.layoutWidget1)
        self.txt_password_cliente_sistema.setObjectName(u"txt_password_cliente_sistema")
        self.txt_password_cliente_sistema.setMinimumSize(QSize(0, 30))
        self.txt_password_cliente_sistema.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_9.addWidget(self.txt_password_cliente_sistema)


        self.verticalLayout_12.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.btn_atualizar_cliente = QPushButton(self.layoutWidget1)
        self.btn_atualizar_cliente.setObjectName(u"btn_atualizar_cliente")
        self.btn_atualizar_cliente.setMinimumSize(QSize(0, 30))
        self.btn_atualizar_cliente.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_10.addWidget(self.btn_atualizar_cliente)

        self.btn_salvar_cliente = QPushButton(self.layoutWidget1)
        self.btn_salvar_cliente.setObjectName(u"btn_salvar_cliente")
        self.btn_salvar_cliente.setMinimumSize(QSize(0, 30))
        self.btn_salvar_cliente.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_10.addWidget(self.btn_salvar_cliente)


        self.verticalLayout_12.addLayout(self.horizontalLayout_10)


        self.horizontalLayout_2.addWidget(self.frm_cadastro_cliente)

        self.tabWidgetFiscal_contabil.addTab(self.tab_clientes, "")
        self.tab_contabilidades = QWidget()
        self.tab_contabilidades.setObjectName(u"tab_contabilidades")
        self.horizontalLayout_35 = QHBoxLayout(self.tab_contabilidades)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.frm_table_contabilidade = QFrame(self.tab_contabilidades)
        self.frm_table_contabilidade.setObjectName(u"frm_table_contabilidade")
        self.frm_table_contabilidade.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_table_contabilidade.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frm_table_contabilidade)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.frm_filtros_contabilidade = QFrame(self.frm_table_contabilidade)
        self.frm_filtros_contabilidade.setObjectName(u"frm_filtros_contabilidade")
        self.frm_filtros_contabilidade.setMinimumSize(QSize(0, 50))
        self.frm_filtros_contabilidade.setMaximumSize(QSize(16777215, 50))
        self.frm_filtros_contabilidade.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_filtros_contabilidade.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_36 = QHBoxLayout(self.frm_filtros_contabilidade)
        self.horizontalLayout_36.setSpacing(2)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(5, 2, 5, 2)
        self.horizontalLayout_37 = QHBoxLayout()
        self.horizontalLayout_37.setSpacing(0)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.txt_buscar_contabilidade = QLineEdit(self.frm_filtros_contabilidade)
        self.txt_buscar_contabilidade.setObjectName(u"txt_buscar_contabilidade")
        self.txt_buscar_contabilidade.setMinimumSize(QSize(300, 30))
        self.txt_buscar_contabilidade.setMaximumSize(QSize(300, 30))
        self.txt_buscar_contabilidade.setFrame(True)

        self.horizontalLayout_37.addWidget(self.txt_buscar_contabilidade, 0, Qt.AlignmentFlag.AlignLeft)


        self.horizontalLayout_36.addLayout(self.horizontalLayout_37)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_36.addItem(self.horizontalSpacer_6)

        self.horizontalLayout_38 = QHBoxLayout()
        self.horizontalLayout_38.setSpacing(0)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")

        self.horizontalLayout_36.addLayout(self.horizontalLayout_38)

        self.btn_nova_contabilidade = QPushButton(self.frm_filtros_contabilidade)
        self.btn_nova_contabilidade.setObjectName(u"btn_nova_contabilidade")
        self.btn_nova_contabilidade.setMinimumSize(QSize(130, 30))
        self.btn_nova_contabilidade.setMaximumSize(QSize(130, 30))

        self.horizontalLayout_36.addWidget(self.btn_nova_contabilidade)

        self.horizontalLayout_39 = QHBoxLayout()
        self.horizontalLayout_39.setSpacing(0)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")

        self.horizontalLayout_36.addLayout(self.horizontalLayout_39)


        self.verticalLayout_22.addWidget(self.frm_filtros_contabilidade)

        self.table_contabilidade = QTableWidget(self.frm_table_contabilidade)
        if (self.table_contabilidade.columnCount() < 8):
            self.table_contabilidade.setColumnCount(8)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.table_contabilidade.setHorizontalHeaderItem(0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.table_contabilidade.setHorizontalHeaderItem(1, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.table_contabilidade.setHorizontalHeaderItem(2, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.table_contabilidade.setHorizontalHeaderItem(3, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.table_contabilidade.setHorizontalHeaderItem(4, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.table_contabilidade.setHorizontalHeaderItem(5, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.table_contabilidade.setHorizontalHeaderItem(6, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.table_contabilidade.setHorizontalHeaderItem(7, __qtablewidgetitem20)
        self.table_contabilidade.setObjectName(u"table_contabilidade")
        self.table_contabilidade.horizontalHeader().setMinimumSectionSize(100)
        self.table_contabilidade.horizontalHeader().setDefaultSectionSize(120)
        self.table_contabilidade.verticalHeader().setVisible(False)

        self.verticalLayout_22.addWidget(self.table_contabilidade)


        self.horizontalLayout_35.addWidget(self.frm_table_contabilidade)

        self.frm_cadastro_contabilidade = QFrame(self.tab_contabilidades)
        self.frm_cadastro_contabilidade.setObjectName(u"frm_cadastro_contabilidade")
        self.frm_cadastro_contabilidade.setMinimumSize(QSize(300, 0))
        self.frm_cadastro_contabilidade.setMaximumSize(QSize(300, 16777215))
        self.frm_cadastro_contabilidade.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_cadastro_contabilidade.setFrameShadow(QFrame.Shadow.Raised)
        self.layoutWidget2 = QWidget(self.frm_cadastro_contabilidade)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(10, 10, 281, 291))
        self.verticalLayout_16 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frm_btn_close_contabilidade = QFrame(self.layoutWidget2)
        self.frm_btn_close_contabilidade.setObjectName(u"frm_btn_close_contabilidade")
        self.frm_btn_close_contabilidade.setMinimumSize(QSize(0, 30))
        self.frm_btn_close_contabilidade.setMaximumSize(QSize(16777215, 30))
        self.frm_btn_close_contabilidade.setFrameShape(QFrame.Shape.NoFrame)
        self.frm_btn_close_contabilidade.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frm_btn_close_contabilidade)
        self.verticalLayout_21.setSpacing(2)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(2, 2, 2, 2)
        self.btn_closeFrm_contabilidade = QPushButton(self.frm_btn_close_contabilidade)
        self.btn_closeFrm_contabilidade.setObjectName(u"btn_closeFrm_contabilidade")
        self.btn_closeFrm_contabilidade.setMinimumSize(QSize(20, 20))
        self.btn_closeFrm_contabilidade.setMaximumSize(QSize(20, 20))
        self.btn_closeFrm_contabilidade.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_closeFrm_contabilidade.setIcon(icon3)
        self.btn_closeFrm_contabilidade.setIconSize(QSize(7, 7))

        self.verticalLayout_21.addWidget(self.btn_closeFrm_contabilidade, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_16.addWidget(self.frm_btn_close_contabilidade)

        self.btn_situacao_contabilidade = QCheckBox(self.layoutWidget2)
        self.btn_situacao_contabilidade.setObjectName(u"btn_situacao_contabilidade")
        self.btn_situacao_contabilidade.setMaximumSize(QSize(60, 16777215))
        self.btn_situacao_contabilidade.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_16.addWidget(self.btn_situacao_contabilidade)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.txt_id_contabilidade = QLineEdit(self.layoutWidget2)
        self.txt_id_contabilidade.setObjectName(u"txt_id_contabilidade")
        self.txt_id_contabilidade.setMinimumSize(QSize(50, 30))
        self.txt_id_contabilidade.setMaximumSize(QSize(50, 30))

        self.horizontalLayout_16.addWidget(self.txt_id_contabilidade, 0, Qt.AlignmentFlag.AlignLeft)

        self.txt_cnpj_contabilidade = QLineEdit(self.layoutWidget2)
        self.txt_cnpj_contabilidade.setObjectName(u"txt_cnpj_contabilidade")
        self.txt_cnpj_contabilidade.setMinimumSize(QSize(200, 30))
        self.txt_cnpj_contabilidade.setMaximumSize(QSize(200, 30))

        self.horizontalLayout_16.addWidget(self.txt_cnpj_contabilidade)


        self.verticalLayout_16.addLayout(self.horizontalLayout_16)

        self.txt_nome_contabilidade = QLineEdit(self.layoutWidget2)
        self.txt_nome_contabilidade.setObjectName(u"txt_nome_contabilidade")
        self.txt_nome_contabilidade.setMinimumSize(QSize(0, 30))
        self.txt_nome_contabilidade.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_16.addWidget(self.txt_nome_contabilidade)

        self.txt_razao_social_contabilidade = QLineEdit(self.layoutWidget2)
        self.txt_razao_social_contabilidade.setObjectName(u"txt_razao_social_contabilidade")
        self.txt_razao_social_contabilidade.setMinimumSize(QSize(0, 30))
        self.txt_razao_social_contabilidade.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_16.addWidget(self.txt_razao_social_contabilidade)

        self.txt_email_contabilidade = QLineEdit(self.layoutWidget2)
        self.txt_email_contabilidade.setObjectName(u"txt_email_contabilidade")
        self.txt_email_contabilidade.setMinimumSize(QSize(0, 30))
        self.txt_email_contabilidade.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_16.addWidget(self.txt_email_contabilidade)

        self.txt_telefone_contabilidade_2 = QLineEdit(self.layoutWidget2)
        self.txt_telefone_contabilidade_2.setObjectName(u"txt_telefone_contabilidade_2")
        self.txt_telefone_contabilidade_2.setMinimumSize(QSize(0, 30))
        self.txt_telefone_contabilidade_2.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_16.addWidget(self.txt_telefone_contabilidade_2)

        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setSpacing(0)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.btn_atualizar_contabilidade = QPushButton(self.layoutWidget2)
        self.btn_atualizar_contabilidade.setObjectName(u"btn_atualizar_contabilidade")
        self.btn_atualizar_contabilidade.setMinimumSize(QSize(0, 30))
        self.btn_atualizar_contabilidade.setMaximumSize(QSize(16777215, 30))
        self.btn_atualizar_contabilidade.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_34.addWidget(self.btn_atualizar_contabilidade)

        self.btn_salvar_contabilidade = QPushButton(self.layoutWidget2)
        self.btn_salvar_contabilidade.setObjectName(u"btn_salvar_contabilidade")
        self.btn_salvar_contabilidade.setMinimumSize(QSize(0, 30))
        self.btn_salvar_contabilidade.setMaximumSize(QSize(16777215, 30))
        self.btn_salvar_contabilidade.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_34.addWidget(self.btn_salvar_contabilidade)


        self.verticalLayout_16.addLayout(self.horizontalLayout_34)


        self.horizontalLayout_35.addWidget(self.frm_cadastro_contabilidade)

        self.tabWidgetFiscal_contabil.addTab(self.tab_contabilidades, "")
        self.tab_xml = QWidget()
        self.tab_xml.setObjectName(u"tab_xml")
        self.verticalLayout_25 = QVBoxLayout(self.tab_xml)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.frm_geral_xml = QFrame(self.tab_xml)
        self.frm_geral_xml.setObjectName(u"frm_geral_xml")
        self.frm_geral_xml.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_geral_xml.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frm_geral_xml)
        self.verticalLayout_23.setSpacing(1)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.frm_top_xml = QFrame(self.frm_geral_xml)
        self.frm_top_xml.setObjectName(u"frm_top_xml")
        self.frm_top_xml.setMinimumSize(QSize(0, 60))
        self.frm_top_xml.setMaximumSize(QSize(16777215, 60))
        self.frm_top_xml.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_top_xml.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frm_top_xml)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.btn_path_xml = QPushButton(self.frm_top_xml)
        self.btn_path_xml.setObjectName(u"btn_path_xml")
        self.btn_path_xml.setMinimumSize(QSize(40, 30))
        self.btn_path_xml.setMaximumSize(QSize(40, 30))
        self.btn_path_xml.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_path_xml.setIcon(icon4)
        self.btn_path_xml.setIconSize(QSize(20, 20))

        self.horizontalLayout_15.addWidget(self.btn_path_xml, 0, Qt.AlignmentFlag.AlignBottom)

        self.txt_pesquisa_table_xml = QLineEdit(self.frm_top_xml)
        self.txt_pesquisa_table_xml.setObjectName(u"txt_pesquisa_table_xml")
        self.txt_pesquisa_table_xml.setMinimumSize(QSize(300, 30))
        self.txt_pesquisa_table_xml.setMaximumSize(QSize(300, 30))

        self.horizontalLayout_15.addWidget(self.txt_pesquisa_table_xml, 0, Qt.AlignmentFlag.AlignBottom)

        self.line_5 = QFrame(self.frm_top_xml)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.Shape.VLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_15.addWidget(self.line_5)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_4)

        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_4 = QLabel(self.frm_top_xml)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_17.addWidget(self.label_4, 0, Qt.AlignmentFlag.AlignBottom)

        self.combo_opcoes_relatorios_xml = QComboBox(self.frm_top_xml)
        self.combo_opcoes_relatorios_xml.addItem("")
        self.combo_opcoes_relatorios_xml.addItem("")
        self.combo_opcoes_relatorios_xml.addItem("")
        self.combo_opcoes_relatorios_xml.setObjectName(u"combo_opcoes_relatorios_xml")
        self.combo_opcoes_relatorios_xml.setMinimumSize(QSize(150, 25))
        self.combo_opcoes_relatorios_xml.setMaximumSize(QSize(150, 25))

        self.verticalLayout_17.addWidget(self.combo_opcoes_relatorios_xml)


        self.horizontalLayout_15.addLayout(self.verticalLayout_17)

        self.btn_salvar_relatorio_xml = QPushButton(self.frm_top_xml)
        self.btn_salvar_relatorio_xml.setObjectName(u"btn_salvar_relatorio_xml")
        self.btn_salvar_relatorio_xml.setMinimumSize(QSize(0, 30))
        self.btn_salvar_relatorio_xml.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_15.addWidget(self.btn_salvar_relatorio_xml, 0, Qt.AlignmentFlag.AlignBottom)

        self.line_4 = QFrame(self.frm_top_xml)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.Shape.VLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_15.addWidget(self.line_4)

        self.bt_limpa_tab_xml = QPushButton(self.frm_top_xml)
        self.bt_limpa_tab_xml.setObjectName(u"bt_limpa_tab_xml")
        self.bt_limpa_tab_xml.setMinimumSize(QSize(0, 30))
        self.bt_limpa_tab_xml.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_15.addWidget(self.bt_limpa_tab_xml, 0, Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignBottom)


        self.verticalLayout_23.addWidget(self.frm_top_xml)

        self.frm_center_xml = QFrame(self.frm_geral_xml)
        self.frm_center_xml.setObjectName(u"frm_center_xml")
        self.frm_center_xml.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_center_xml.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frm_center_xml)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.tableWidget_xml_list = QTreeView(self.frm_center_xml)
        self.tableWidget_xml_list.setObjectName(u"tableWidget_xml_list")
        self.tableWidget_xml_list.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)

        self.verticalLayout_26.addWidget(self.tableWidget_xml_list)


        self.verticalLayout_23.addWidget(self.frm_center_xml)

        self.frm_botton_xml = QFrame(self.frm_geral_xml)
        self.frm_botton_xml.setObjectName(u"frm_botton_xml")
        self.frm_botton_xml.setMinimumSize(QSize(0, 65))
        self.frm_botton_xml.setMaximumSize(QSize(16777215, 65))
        self.frm_botton_xml.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_botton_xml.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_41 = QHBoxLayout(self.frm_botton_xml)
        self.horizontalLayout_41.setSpacing(2)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.horizontalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.frm_botton_xml)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(300, 0))
        self.frame_4.setMaximumSize(QSize(300, 16777215))
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_4)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.label_qtda_xmls = QPlainTextEdit(self.frame_4)
        self.label_qtda_xmls.setObjectName(u"label_qtda_xmls")

        self.verticalLayout_18.addWidget(self.label_qtda_xmls)


        self.horizontalLayout_41.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frm_botton_xml)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_43 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalSpacer_10 = QSpacerItem(113, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_43.addItem(self.horizontalSpacer_10)

        self.horizontalLayout_42 = QHBoxLayout()
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.verticalLayout_27 = QVBoxLayout()
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.label_9 = QLabel(self.frame_5)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(110, 0))
        self.label_9.setMaximumSize(QSize(110, 16777215))

        self.verticalLayout_27.addWidget(self.label_9)

        self.txt_icms_xml = QLineEdit(self.frame_5)
        self.txt_icms_xml.setObjectName(u"txt_icms_xml")
        self.txt_icms_xml.setMinimumSize(QSize(110, 25))
        self.txt_icms_xml.setMaximumSize(QSize(110, 25))

        self.verticalLayout_27.addWidget(self.txt_icms_xml)


        self.horizontalLayout_42.addLayout(self.verticalLayout_27)

        self.verticalLayout_28 = QVBoxLayout()
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.label_10 = QLabel(self.frame_5)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(110, 0))
        self.label_10.setMaximumSize(QSize(110, 16777215))

        self.verticalLayout_28.addWidget(self.label_10)

        self.txt_pis_xml = QLineEdit(self.frame_5)
        self.txt_pis_xml.setObjectName(u"txt_pis_xml")
        self.txt_pis_xml.setMinimumSize(QSize(110, 25))
        self.txt_pis_xml.setMaximumSize(QSize(110, 25))

        self.verticalLayout_28.addWidget(self.txt_pis_xml)


        self.horizontalLayout_42.addLayout(self.verticalLayout_28)

        self.verticalLayout_29 = QVBoxLayout()
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.label_11 = QLabel(self.frame_5)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(110, 0))
        self.label_11.setMaximumSize(QSize(110, 16777215))

        self.verticalLayout_29.addWidget(self.label_11)

        self.txt_confins_xml = QLineEdit(self.frame_5)
        self.txt_confins_xml.setObjectName(u"txt_confins_xml")
        self.txt_confins_xml.setMinimumSize(QSize(110, 25))
        self.txt_confins_xml.setMaximumSize(QSize(110, 25))

        self.verticalLayout_29.addWidget(self.txt_confins_xml)


        self.horizontalLayout_42.addLayout(self.verticalLayout_29)

        self.verticalLayout_30 = QVBoxLayout()
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.label_12 = QLabel(self.frame_5)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(110, 0))
        self.label_12.setMaximumSize(QSize(110, 16777215))

        self.verticalLayout_30.addWidget(self.label_12)

        self.txt_ipi_xml = QLineEdit(self.frame_5)
        self.txt_ipi_xml.setObjectName(u"txt_ipi_xml")
        self.txt_ipi_xml.setMinimumSize(QSize(110, 25))
        self.txt_ipi_xml.setMaximumSize(QSize(110, 25))

        self.verticalLayout_30.addWidget(self.txt_ipi_xml)


        self.horizontalLayout_42.addLayout(self.verticalLayout_30)

        self.verticalLayout_31 = QVBoxLayout()
        self.verticalLayout_31.setSpacing(0)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.label_13 = QLabel(self.frame_5)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(110, 0))
        self.label_13.setMaximumSize(QSize(110, 16777215))

        self.verticalLayout_31.addWidget(self.label_13)

        self.txt_totalNF_xml = QLineEdit(self.frame_5)
        self.txt_totalNF_xml.setObjectName(u"txt_totalNF_xml")
        self.txt_totalNF_xml.setMinimumSize(QSize(110, 25))
        self.txt_totalNF_xml.setMaximumSize(QSize(110, 25))

        self.verticalLayout_31.addWidget(self.txt_totalNF_xml)


        self.horizontalLayout_42.addLayout(self.verticalLayout_31)


        self.horizontalLayout_43.addLayout(self.horizontalLayout_42)


        self.horizontalLayout_41.addWidget(self.frame_5)


        self.verticalLayout_23.addWidget(self.frm_botton_xml)


        self.verticalLayout_25.addWidget(self.frm_geral_xml)

        self.tabWidgetFiscal_contabil.addTab(self.tab_xml, "")
        self.tab_importar_exportar = QWidget()
        self.tab_importar_exportar.setObjectName(u"tab_importar_exportar")
        self.verticalLayout_14 = QVBoxLayout(self.tab_importar_exportar)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.groupBox = QGroupBox(self.tab_importar_exportar)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.txt_output_import = QPlainTextEdit(self.groupBox)
        self.txt_output_import.setObjectName(u"txt_output_import")
        self.txt_output_import.setGeometry(QRect(20, 190, 611, 91))
        self.txt_output_import.setFrameShadow(QFrame.Shadow.Raised)
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 170, 141, 16))
        self.line = QFrame(self.groupBox)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(630, 10, 20, 291))
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.radioBtn_importar_fiscal_contabil = QRadioButton(self.groupBox)
        self.radioBtn_importar_fiscal_contabil.setObjectName(u"radioBtn_importar_fiscal_contabil")
        self.radioBtn_importar_fiscal_contabil.setGeometry(QRect(20, 60, 92, 20))
        self.radioBtn_importar_fiscal_contabil.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.radioBtn_exportar_fiscal_contabil = QRadioButton(self.groupBox)
        self.radioBtn_exportar_fiscal_contabil.setObjectName(u"radioBtn_exportar_fiscal_contabil")
        self.radioBtn_exportar_fiscal_contabil.setGeometry(QRect(110, 60, 92, 20))
        self.radioBtn_exportar_fiscal_contabil.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.line_3 = QFrame(self.groupBox)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(10, 80, 621, 16))
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(650, 20, 361, 261))
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.label_3.setWordWrap(True)
        self.label_3.setMargin(5)
        self.label_3.setIndent(0)
        self.layoutWidget3 = QWidget(self.groupBox)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(12, 92, 621, 61))
        self.verticalLayout_15 = QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.layoutWidget3)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_15.addWidget(self.label_2)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.txt_path_importar_exportar = QLineEdit(self.layoutWidget3)
        self.txt_path_importar_exportar.setObjectName(u"txt_path_importar_exportar")
        self.txt_path_importar_exportar.setMinimumSize(QSize(0, 30))
        self.txt_path_importar_exportar.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_14.addWidget(self.txt_path_importar_exportar)

        self.btn_path_import = QPushButton(self.layoutWidget3)
        self.btn_path_import.setObjectName(u"btn_path_import")
        self.btn_path_import.setMinimumSize(QSize(0, 35))
        self.btn_path_import.setMaximumSize(QSize(35, 30))
        self.btn_path_import.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_path_import.setIcon(icon4)
        self.btn_path_import.setIconSize(QSize(20, 20))

        self.horizontalLayout_14.addWidget(self.btn_path_import)

        self.btn_importar_cliente_contabil = QPushButton(self.layoutWidget3)
        self.btn_importar_cliente_contabil.setObjectName(u"btn_importar_cliente_contabil")
        self.btn_importar_cliente_contabil.setMinimumSize(QSize(0, 30))
        self.btn_importar_cliente_contabil.setMaximumSize(QSize(16777215, 30))
        self.btn_importar_cliente_contabil.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_14.addWidget(self.btn_importar_cliente_contabil)


        self.verticalLayout_15.addLayout(self.horizontalLayout_14)

        self.comboTipo_import_export_fiscal_contabil = QComboBox(self.groupBox)
        self.comboTipo_import_export_fiscal_contabil.addItem("")
        self.comboTipo_import_export_fiscal_contabil.addItem("")
        self.comboTipo_import_export_fiscal_contabil.addItem("")
        self.comboTipo_import_export_fiscal_contabil.addItem("")
        self.comboTipo_import_export_fiscal_contabil.addItem("")
        self.comboTipo_import_export_fiscal_contabil.setObjectName(u"comboTipo_import_export_fiscal_contabil")
        self.comboTipo_import_export_fiscal_contabil.setGeometry(QRect(470, 50, 161, 30))
        self.comboTipo_import_export_fiscal_contabil.setMinimumSize(QSize(0, 30))
        self.comboTipo_import_export_fiscal_contabil.setMaximumSize(QSize(16777215, 30))
        self.comboTipo_import_export_fiscal_contabil.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_14.addWidget(self.groupBox)

        self.tabWidgetFiscal_contabil.addTab(self.tab_importar_exportar, "")

        self.verticalLayout_10.addWidget(self.tabWidgetFiscal_contabil)

        self.stackedWidget_tables.addWidget(self.page_contabil_fiscal)

        self.verticalLayout_3.addWidget(self.stackedWidget_tables)


        self.gridLayout.addWidget(self.frm_geral_tables, 3, 0, 1, 1)

        self.frm_lateral_functions = QFrame(self.frm_layout_geral)
        self.frm_lateral_functions.setObjectName(u"frm_lateral_functions")
        self.frm_lateral_functions.setEnabled(True)
        self.frm_lateral_functions.setMinimumSize(QSize(300, 0))
        self.frm_lateral_functions.setMaximumSize(QSize(300, 16777215))
        self.frm_lateral_functions.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_lateral_functions.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frm_lateral_functions)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frm_lateral_functions)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 30))
        self.frame_3.setMaximumSize(QSize(16777215, 30))
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(2, 2, 2, 2)
        self.btn_closeFrm_lateral = QPushButton(self.frame_3)
        self.btn_closeFrm_lateral.setObjectName(u"btn_closeFrm_lateral")
        self.btn_closeFrm_lateral.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_closeFrm_lateral.setIcon(icon3)
        self.btn_closeFrm_lateral.setIconSize(QSize(7, 7))

        self.verticalLayout_8.addWidget(self.btn_closeFrm_lateral, 0, Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignVCenter)


        self.verticalLayout_7.addWidget(self.frame_3)

        self.frame_2 = QFrame(self.frm_lateral_functions)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_7.addWidget(self.frame_2)


        self.gridLayout.addWidget(self.frm_lateral_functions, 0, 1, 5, 1)

        self.frm_setas_titulo.raise_()
        self.frm_bottom_bar.raise_()
        self.frm_geral_tables.raise_()
        self.frm_lateral_functions.raise_()
        self.frame_opcoes_busca_processamento.raise_()

        self.verticalLayout_2.addWidget(self.frm_layout_geral)


        self.verticalLayout.addWidget(self.frame)

        PrincipalWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.btn_minimize, self.btn_maximize)
        QWidget.setTabOrder(self.btn_maximize, self.btn_close_window)
        QWidget.setTabOrder(self.btn_close_window, self.pushButton)
        QWidget.setTabOrder(self.pushButton, self.btn_opcoes_pesquisas)
        QWidget.setTabOrder(self.btn_opcoes_pesquisas, self.btn_opcoes_processamento)
        QWidget.setTabOrder(self.btn_opcoes_processamento, self.btn_opcoes_conexoes_db)
        QWidget.setTabOrder(self.btn_opcoes_conexoes_db, self.btn_opcoes_contabil)
        QWidget.setTabOrder(self.btn_opcoes_contabil, self.btn_closeFrm_lateral)
        QWidget.setTabOrder(self.btn_closeFrm_lateral, self.btn_voltar_pagina)
        QWidget.setTabOrder(self.btn_voltar_pagina, self.btn_proxima_pagina)
        QWidget.setTabOrder(self.btn_proxima_pagina, self.btn_executar_pesquisas)
        QWidget.setTabOrder(self.btn_executar_pesquisas, self.combo_opcoes_busca)
        QWidget.setTabOrder(self.combo_opcoes_busca, self.btn_extrair_duplicados)
        QWidget.setTabOrder(self.btn_extrair_duplicados, self.txt_op_busca1)
        QWidget.setTabOrder(self.txt_op_busca1, self.comboBox_opcoes_de_busca2)
        QWidget.setTabOrder(self.comboBox_opcoes_de_busca2, self.comboBox)
        QWidget.setTabOrder(self.comboBox, self.btn_executar_processamento)
        QWidget.setTabOrder(self.btn_executar_processamento, self.bt_retirar_combo1)
        QWidget.setTabOrder(self.bt_retirar_combo1, self.txt_coluna_processamento2)
        QWidget.setTabOrder(self.txt_coluna_processamento2, self.bt_retirar_combo)
        QWidget.setTabOrder(self.bt_retirar_combo, self.txt_coluna_processamento1)
        QWidget.setTabOrder(self.txt_coluna_processamento1, self.cbx_coluna_processamento1)
        QWidget.setTabOrder(self.cbx_coluna_processamento1, self.bt_add_combo)
        QWidget.setTabOrder(self.bt_add_combo, self.cbx_coluna_processamento2)
        QWidget.setTabOrder(self.cbx_coluna_processamento2, self.cbx_coluna_processamento3)
        QWidget.setTabOrder(self.cbx_coluna_processamento3, self.txt_coluna_processamento3)
        QWidget.setTabOrder(self.txt_coluna_processamento3, self.bt_add_combo2)
        QWidget.setTabOrder(self.bt_add_combo2, self.btn_desfazer)
        QWidget.setTabOrder(self.btn_desfazer, self.bt_salvar_dados_tabela_principal)
        QWidget.setTabOrder(self.bt_salvar_dados_tabela_principal, self.bt_reprocesar_csv)
        QWidget.setTabOrder(self.bt_reprocesar_csv, self.table_principal)
        QWidget.setTabOrder(self.table_principal, self.table_duplicados)
        QWidget.setTabOrder(self.table_duplicados, self.tabWidgetFiscal_contabil)
        QWidget.setTabOrder(self.tabWidgetFiscal_contabil, self.btn_importar_file)
        QWidget.setTabOrder(self.btn_importar_file, self.btn_busca_avancada_cliente)
        QWidget.setTabOrder(self.btn_busca_avancada_cliente, self.data_filtro_inicio_cliente)
        QWidget.setTabOrder(self.data_filtro_inicio_cliente, self.data_filtro_fim_cliente)
        QWidget.setTabOrder(self.data_filtro_fim_cliente, self.combo_filtro_statusEnvio)
        QWidget.setTabOrder(self.combo_filtro_statusEnvio, self.combo_filtro_contador)
        QWidget.setTabOrder(self.combo_filtro_contador, self.table_clientes)
        QWidget.setTabOrder(self.table_clientes, self.btn_closeFrm_cliente)
        QWidget.setTabOrder(self.btn_closeFrm_cliente, self.btn_situacao_cliente)
        QWidget.setTabOrder(self.btn_situacao_cliente, self.combo_status_envio_arquivos_cliente)
        QWidget.setTabOrder(self.combo_status_envio_arquivos_cliente, self.txt_cnpj_cliente)
        QWidget.setTabOrder(self.txt_cnpj_cliente, self.txt_nome_cliente)
        QWidget.setTabOrder(self.txt_nome_cliente, self.txt_razao_social_cliente)
        QWidget.setTabOrder(self.txt_razao_social_cliente, self.txt_email_cliente)
        QWidget.setTabOrder(self.txt_email_cliente, self.combo_contador)
        QWidget.setTabOrder(self.combo_contador, self.btn_novo_contador)
        QWidget.setTabOrder(self.btn_novo_contador, self.combo_sistema_cliente)
        QWidget.setTabOrder(self.combo_sistema_cliente, self.txt_link_sistema_cliente)
        QWidget.setTabOrder(self.txt_link_sistema_cliente, self.txt_user_cliente_sistema)
        QWidget.setTabOrder(self.txt_user_cliente_sistema, self.txt_password_cliente_sistema)
        QWidget.setTabOrder(self.txt_password_cliente_sistema, self.btn_atualizar_cliente)
        QWidget.setTabOrder(self.btn_atualizar_cliente, self.btn_salvar_cliente)
        QWidget.setTabOrder(self.btn_salvar_cliente, self.txt_output_import)
        QWidget.setTabOrder(self.txt_output_import, self.txt_path_importar_exportar)
        QWidget.setTabOrder(self.txt_path_importar_exportar, self.btn_path_import)
        QWidget.setTabOrder(self.btn_path_import, self.btn_importar_cliente_contabil)
        QWidget.setTabOrder(self.btn_importar_cliente_contabil, self.comboTipo_import_export_fiscal_contabil)
        QWidget.setTabOrder(self.comboTipo_import_export_fiscal_contabil, self.radioBtn_importar_fiscal_contabil)
        QWidget.setTabOrder(self.radioBtn_importar_fiscal_contabil, self.radioBtn_exportar_fiscal_contabil)
        QWidget.setTabOrder(self.radioBtn_exportar_fiscal_contabil, self.txt_buscar_cliente)
        QWidget.setTabOrder(self.txt_buscar_cliente, self.btn_closeFrm_contabilidade)
        QWidget.setTabOrder(self.btn_closeFrm_contabilidade, self.btn_situacao_contabilidade)
        QWidget.setTabOrder(self.btn_situacao_contabilidade, self.txt_nome_contabilidade)
        QWidget.setTabOrder(self.txt_nome_contabilidade, self.txt_razao_social_contabilidade)
        QWidget.setTabOrder(self.txt_razao_social_contabilidade, self.txt_email_contabilidade)
        QWidget.setTabOrder(self.txt_email_contabilidade, self.btn_atualizar_contabilidade)
        QWidget.setTabOrder(self.btn_atualizar_contabilidade, self.btn_salvar_contabilidade)
        QWidget.setTabOrder(self.btn_salvar_contabilidade, self.txt_buscar_contabilidade)
        QWidget.setTabOrder(self.txt_buscar_contabilidade, self.table_contabilidade)
        QWidget.setTabOrder(self.table_contabilidade, self.txt_telefone_contabilidade_2)

        self.retranslateUi(PrincipalWindow)

        self.stackedWidget_tables.setCurrentIndex(2)
        self.tabWidgetFiscal_contabil.setCurrentIndex(2)


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
        self.btn_opcoes_contabil.setText(QCoreApplication.translate("PrincipalWindow", u"Contabilidades", None))
#if QT_CONFIG(shortcut)
        self.btn_opcoes_contabil.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.btn_executar_pesquisas.setText("")
        self.combo_opcoes_busca.setItemText(0, QCoreApplication.translate("PrincipalWindow", u"Op\u00e7\u00f5es de buscas", None))
        self.combo_opcoes_busca.setItemText(1, QCoreApplication.translate("PrincipalWindow", u"Buscar por NCM", None))
        self.combo_opcoes_busca.setItemText(2, QCoreApplication.translate("PrincipalWindow", u"NCM Inv\u00e1lido", None))
        self.combo_opcoes_busca.setItemText(3, QCoreApplication.translate("PrincipalWindow", u"Tudo que cont\u00e9m", None))
        self.combo_opcoes_busca.setItemText(4, QCoreApplication.translate("PrincipalWindow", u"Duplicados", None))

        self.btn_extrair_duplicados.setText(QCoreApplication.translate("PrincipalWindow", u"Extrair", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("PrincipalWindow", u"Op\u00e7\u00f5es de processamento", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("PrincipalWindow", u"Buscar e Substituir caracteres especiais", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("PrincipalWindow", u"Buscar valores negativos e mudar para zero", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("PrincipalWindow", u"Filtrar e copiar linhas que cont\u00e9m. Separar para tabela ao lado.", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("PrincipalWindow", u"Formatar c\u00f3digos de barras", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("PrincipalWindow", u"Formatar CPF e CNPJ", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("PrincipalWindow", u"Substituir NCM", None))
        self.comboBox.setItemText(7, QCoreApplication.translate("PrincipalWindow", u"Se Coluna A cont\u00e9m, Coluna B recebe.", None))
        self.comboBox.setItemText(8, QCoreApplication.translate("PrincipalWindow", u"Tudo que cont\u00e9m mude para", None))
        self.comboBox.setItemText(9, QCoreApplication.translate("PrincipalWindow", u"Transformar em min\u00fasculas A-a", None))
        self.comboBox.setItemText(10, QCoreApplication.translate("PrincipalWindow", u"Transformar em mai\u00fascula a-A", None))

        self.btn_executar_processamento.setText(QCoreApplication.translate("PrincipalWindow", u"Executar", None))
        self.bt_retirar_combo1.setText("")
        self.bt_retirar_combo.setText("")
        self.bt_add_combo.setText("")
        self.bt_add_combo2.setText("")
        self.btn_voltar_pagina.setText("")
        self.lb_titulos_tabelas.setText(QCoreApplication.translate("PrincipalWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.btn_proxima_pagina.setText("")
        self.btn_desfazer.setText("")
#if QT_CONFIG(tooltip)
        self.bt_salvar_dados_tabela_principal.setToolTip(QCoreApplication.translate("PrincipalWindow", u"<html><head/><body><p><span style=\" font-size:8pt; color:#4b3ff1;\">Exportar .csv</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.bt_salvar_dados_tabela_principal.setText("")
        self.bt_reprocesar_csv.setText("")
        self.txt_buscar_cliente.setPlaceholderText(QCoreApplication.translate("PrincipalWindow", u"Buscar: c\u00f3digo, nome, cnpj", None))
        self.btn_busca_avancada_cliente.setText(QCoreApplication.translate("PrincipalWindow", u"Busca Avan\u00e7ada", None))
        self.data_filtro_inicio_cliente.setSpecialValueText(QCoreApplication.translate("PrincipalWindow", u"Data inicio", None))
        self.data_filtro_fim_cliente.setSpecialValueText(QCoreApplication.translate("PrincipalWindow", u"Data fim", None))
        self.combo_filtro_statusEnvio.setPlaceholderText(QCoreApplication.translate("PrincipalWindow", u"Status envio", None))
        self.combo_filtro_contador.setPlaceholderText(QCoreApplication.translate("PrincipalWindow", u"Contabilidade", None))
        self.btn_novo_cliente.setText(QCoreApplication.translate("PrincipalWindow", u"Novo Cliente", None))
        ___qtablewidgetitem = self.table_clientes.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("PrincipalWindow", u"ID", None));
        ___qtablewidgetitem1 = self.table_clientes.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("PrincipalWindow", u"Status", None));
        ___qtablewidgetitem2 = self.table_clientes.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("PrincipalWindow", u"CNPJ", None));
        ___qtablewidgetitem3 = self.table_clientes.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("PrincipalWindow", u"Nome", None));
        ___qtablewidgetitem4 = self.table_clientes.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("PrincipalWindow", u"Raz\u00e3o Social", None));
        ___qtablewidgetitem5 = self.table_clientes.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("PrincipalWindow", u"E-mail", None));
        ___qtablewidgetitem6 = self.table_clientes.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("PrincipalWindow", u"Contabilidade", None));
        ___qtablewidgetitem7 = self.table_clientes.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("PrincipalWindow", u"Sistema", None));
        ___qtablewidgetitem8 = self.table_clientes.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("PrincipalWindow", u"Link", None));
        ___qtablewidgetitem9 = self.table_clientes.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("PrincipalWindow", u"Usu\u00e1rio", None));
        ___qtablewidgetitem10 = self.table_clientes.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("PrincipalWindow", u"Senha", None));
        ___qtablewidgetitem11 = self.table_clientes.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("PrincipalWindow", u"Data Ult. Envio", None));
        ___qtablewidgetitem12 = self.table_clientes.horizontalHeaderItem(12)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("PrincipalWindow", u"A\u00e7\u00f5es", None));
        self.btn_closeFrm_cliente.setText("")
        self.btn_situacao_cliente.setText(QCoreApplication.translate("PrincipalWindow", u"Ativo", None))
        self.combo_status_envio_arquivos_cliente.setItemText(0, QCoreApplication.translate("PrincipalWindow", u"Status envio", None))
        self.combo_status_envio_arquivos_cliente.setItemText(1, QCoreApplication.translate("PrincipalWindow", u"Enviado", None))
        self.combo_status_envio_arquivos_cliente.setItemText(2, QCoreApplication.translate("PrincipalWindow", u"N\u00e3o Enviado", None))
        self.combo_status_envio_arquivos_cliente.setItemText(3, QCoreApplication.translate("PrincipalWindow", u"Erro na gera\u00e7\u00e3o", None))
        self.combo_status_envio_arquivos_cliente.setItemText(4, QCoreApplication.translate("PrincipalWindow", u"N\u00e3o fez Venda", None))

        self.txt_cnpj_cliente.setPlaceholderText(QCoreApplication.translate("PrincipalWindow", u"CNPJ", None))
        self.txt_nome_cliente.setPlaceholderText(QCoreApplication.translate("PrincipalWindow", u"Nome", None))
        self.txt_razao_social_cliente.setPlaceholderText(QCoreApplication.translate("PrincipalWindow", u"Raz\u00e3o Social", None))
        self.txt_email_cliente.setPlaceholderText(QCoreApplication.translate("PrincipalWindow", u"E-mail", None))
        self.combo_contador.setPlaceholderText(QCoreApplication.translate("PrincipalWindow", u"Contador", None))
        self.btn_novo_contador.setText("")
        self.combo_sistema_cliente.setItemText(0, QCoreApplication.translate("PrincipalWindow", u"Sistema de Gest\u00e3o", None))
        self.combo_sistema_cliente.setItemText(1, QCoreApplication.translate("PrincipalWindow", u"Hiper", None))
        self.combo_sistema_cliente.setItemText(2, QCoreApplication.translate("PrincipalWindow", u"Vr System", None))
        self.combo_sistema_cliente.setItemText(3, QCoreApplication.translate("PrincipalWindow", u"Digisat", None))
        self.combo_sistema_cliente.setItemText(4, QCoreApplication.translate("PrincipalWindow", u"Velo", None))
        self.combo_sistema_cliente.setItemText(5, QCoreApplication.translate("PrincipalWindow", u"STI3", None))

        self.combo_sistema_cliente.setCurrentText("")
        self.combo_sistema_cliente.setPlaceholderText(QCoreApplication.translate("PrincipalWindow", u"Sistema de Gest\u00e3o", None))
        self.txt_link_sistema_cliente.setPlaceholderText(QCoreApplication.translate("PrincipalWindow", u"Link Sistema", None))
        self.txt_user_cliente_sistema.setPlaceholderText(QCoreApplication.translate("PrincipalWindow", u"User", None))
        self.txt_password_cliente_sistema.setPlaceholderText(QCoreApplication.translate("PrincipalWindow", u"Password", None))
        self.btn_atualizar_cliente.setText(QCoreApplication.translate("PrincipalWindow", u"Atualizar", None))
        self.btn_salvar_cliente.setText(QCoreApplication.translate("PrincipalWindow", u"Novo", None))
        self.tabWidgetFiscal_contabil.setTabText(self.tabWidgetFiscal_contabil.indexOf(self.tab_clientes), QCoreApplication.translate("PrincipalWindow", u"Clientes", None))
        self.txt_buscar_contabilidade.setPlaceholderText(QCoreApplication.translate("PrincipalWindow", u"Buscar: c\u00f3digo, nome, cnpj", None))
        self.btn_nova_contabilidade.setText(QCoreApplication.translate("PrincipalWindow", u"Nova Contabilidade", None))
        ___qtablewidgetitem13 = self.table_contabilidade.horizontalHeaderItem(0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("PrincipalWindow", u"ID", None));
        ___qtablewidgetitem14 = self.table_contabilidade.horizontalHeaderItem(1)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("PrincipalWindow", u"Status", None));
        ___qtablewidgetitem15 = self.table_contabilidade.horizontalHeaderItem(2)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("PrincipalWindow", u"Nome", None));
        ___qtablewidgetitem16 = self.table_contabilidade.horizontalHeaderItem(3)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("PrincipalWindow", u"Raz\u00e3o Social", None));
        ___qtablewidgetitem17 = self.table_contabilidade.horizontalHeaderItem(4)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("PrincipalWindow", u"CNPJ", None));
        ___qtablewidgetitem18 = self.table_contabilidade.horizontalHeaderItem(5)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("PrincipalWindow", u"E-mail", None));
        ___qtablewidgetitem19 = self.table_contabilidade.horizontalHeaderItem(6)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("PrincipalWindow", u"Telefone", None));
        ___qtablewidgetitem20 = self.table_contabilidade.horizontalHeaderItem(7)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("PrincipalWindow", u"A\u00e7\u00f5es", None));
        self.btn_closeFrm_contabilidade.setText("")
        self.btn_situacao_contabilidade.setText(QCoreApplication.translate("PrincipalWindow", u"Ativo", None))
        self.txt_cnpj_contabilidade.setPlaceholderText(QCoreApplication.translate("PrincipalWindow", u"CNPJ", None))
        self.txt_nome_contabilidade.setPlaceholderText(QCoreApplication.translate("PrincipalWindow", u"Nome", None))
        self.txt_razao_social_contabilidade.setPlaceholderText(QCoreApplication.translate("PrincipalWindow", u"Raz\u00e3o Social", None))
        self.txt_email_contabilidade.setPlaceholderText(QCoreApplication.translate("PrincipalWindow", u"E-mail", None))
        self.txt_telefone_contabilidade_2.setPlaceholderText(QCoreApplication.translate("PrincipalWindow", u"Telefone", None))
        self.btn_atualizar_contabilidade.setText(QCoreApplication.translate("PrincipalWindow", u"Atualizar", None))
        self.btn_salvar_contabilidade.setText(QCoreApplication.translate("PrincipalWindow", u"Novo", None))
        self.tabWidgetFiscal_contabil.setTabText(self.tabWidgetFiscal_contabil.indexOf(self.tab_contabilidades), QCoreApplication.translate("PrincipalWindow", u"Contabilidades", None))
        self.btn_path_xml.setText("")
        self.txt_pesquisa_table_xml.setPlaceholderText(QCoreApplication.translate("PrincipalWindow", u"N\u00ba NFe, Chave, CNPJ", None))
        self.label_4.setText(QCoreApplication.translate("PrincipalWindow", u"Relat\u00f3rios", None))
        self.combo_opcoes_relatorios_xml.setItemText(0, "")
        self.combo_opcoes_relatorios_xml.setItemText(1, QCoreApplication.translate("PrincipalWindow", u"Exportar em CSV", None))
        self.combo_opcoes_relatorios_xml.setItemText(2, QCoreApplication.translate("PrincipalWindow", u"Exportar em PDF", None))

        self.btn_salvar_relatorio_xml.setText(QCoreApplication.translate("PrincipalWindow", u"Salvar", None))
        self.bt_limpa_tab_xml.setText(QCoreApplication.translate("PrincipalWindow", u"Limpar", None))
        self.label_9.setText(QCoreApplication.translate("PrincipalWindow", u"ICMS", None))
        self.label_10.setText(QCoreApplication.translate("PrincipalWindow", u"PIS", None))
        self.label_11.setText(QCoreApplication.translate("PrincipalWindow", u"COFINS", None))
        self.label_12.setText(QCoreApplication.translate("PrincipalWindow", u"IPI", None))
        self.label_13.setText(QCoreApplication.translate("PrincipalWindow", u"Total NF", None))
        self.tabWidgetFiscal_contabil.setTabText(self.tabWidgetFiscal_contabil.indexOf(self.tab_xml), QCoreApplication.translate("PrincipalWindow", u"XML", None))
        self.groupBox.setTitle(QCoreApplication.translate("PrincipalWindow", u"Importar/Exportar", None))
        self.label.setText(QCoreApplication.translate("PrincipalWindow", u"Sa\u00edda import de dados:", None))
        self.radioBtn_importar_fiscal_contabil.setText(QCoreApplication.translate("PrincipalWindow", u"Importar?", None))
        self.radioBtn_exportar_fiscal_contabil.setText(QCoreApplication.translate("PrincipalWindow", u"Exportar?", None))
        self.label_3.setText(QCoreApplication.translate("PrincipalWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Importar: </span>\u00c9 poss\u00edvel importar clientes e contabilidades de forma f\u00e1cil seguindo o modelo de arquivo para importa\u00e7\u00e3o.</p><p><span style=\" font-weight:700;\">Exportar: </span>Permite que o usu\u00e1rio exporte dados como <span style=\" font-weight:700;\">clientes, contabilidades </span>e relat\u00f3rios como <span style=\" font-weight:700;\">Totais de NFE, Totais de NFCE, </span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("PrincipalWindow", u"Caminho do arquivo:", None))
        self.btn_path_import.setText("")
        self.btn_importar_cliente_contabil.setText(QCoreApplication.translate("PrincipalWindow", u"Excutar", None))
        self.comboTipo_import_export_fiscal_contabil.setItemText(0, QCoreApplication.translate("PrincipalWindow", u"Tipo", None))
        self.comboTipo_import_export_fiscal_contabil.setItemText(1, QCoreApplication.translate("PrincipalWindow", u"Clientes", None))
        self.comboTipo_import_export_fiscal_contabil.setItemText(2, QCoreApplication.translate("PrincipalWindow", u"Contabilidades", None))
        self.comboTipo_import_export_fiscal_contabil.setItemText(3, QCoreApplication.translate("PrincipalWindow", u"Relat\u00f3rio Totais NFE", None))
        self.comboTipo_import_export_fiscal_contabil.setItemText(4, QCoreApplication.translate("PrincipalWindow", u"Relat\u00f3rio Totais NFCE", None))

        self.tabWidgetFiscal_contabil.setTabText(self.tabWidgetFiscal_contabil.indexOf(self.tab_importar_exportar), QCoreApplication.translate("PrincipalWindow", u"Importar/Exportar", None))
        self.btn_closeFrm_lateral.setText("")
    # retranslateUi

