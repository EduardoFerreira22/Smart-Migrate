# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'progressamkqCZ.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QProgressBar,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_ProgressBar(object):
    def setupUi(self, ProgressBar):
        if not ProgressBar.objectName():
            ProgressBar.setObjectName(u"ProgressBar")
        ProgressBar.resize(488, 69)
        ProgressBar.setMinimumSize(QSize(0, 0))
        ProgressBar.setMaximumSize(QSize(16777215, 16777215))
        ProgressBar.setStyleSheet(u"QLabel{\n"
"	\n"
"	font: 8pt \"Verdana\";\n"
"	color: rgb(39, 0, 118);\n"
"}\n"
"\n"
"QProgressBar {\n"
"        border: 1px solid #555;\n"
"        border-radius: 5px;\n"
"        background-color: #FFFFFF;\n"
"        text-align: center;\n"
"    }\n"
"    QProgressBar::chunk {\n"
"		\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #4b3ff1, stop:1 #4b3ff1);\n"
"        border-radius: 3px;\n"
"    }\n"
"\n"
"")
        self.verticalLayout = QVBoxLayout(ProgressBar)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frm_botton_progress = QFrame(ProgressBar)
        self.frm_botton_progress.setObjectName(u"frm_botton_progress")
        font = QFont()
        font.setBold(True)
        self.frm_botton_progress.setFont(font)
        self.frm_botton_progress.setFrameShape(QFrame.Shape.NoFrame)
        self.frm_botton_progress.setFrameShadow(QFrame.Shadow.Raised)
        self.progressBar = QProgressBar(self.frm_botton_progress)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(10, 20, 465, 20))
        self.progressBar.setMinimumSize(QSize(0, 20))
        self.progressBar.setMaximumSize(QSize(16777215, 20))
        self.progressBar.setFont(font)
        self.progressBar.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.progressBar.setValue(1)
        self.progressBar.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)
        self.progressBar.setTextVisible(True)
        self.progressBar.setOrientation(Qt.Orientation.Horizontal)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QProgressBar.Direction.BottomToTop)
        self.lb_informacoes_progress = QLabel(self.frm_botton_progress)
        self.lb_informacoes_progress.setObjectName(u"lb_informacoes_progress")
        self.lb_informacoes_progress.setGeometry(QRect(10, 30, 465, 35))
        self.lb_informacoes_progress.setMargin(10)

        self.verticalLayout.addWidget(self.frm_botton_progress)


        self.retranslateUi(ProgressBar)

        QMetaObject.connectSlotsByName(ProgressBar)
    # setupUi

    def retranslateUi(self, ProgressBar):
        ProgressBar.setWindowTitle(QCoreApplication.translate("ProgressBar", u"Form", None))
        self.progressBar.setFormat(QCoreApplication.translate("ProgressBar", u"%p%", None))
        self.lb_informacoes_progress.setText(QCoreApplication.translate("ProgressBar", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
    # retranslateUi

