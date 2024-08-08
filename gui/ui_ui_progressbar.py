# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_progressbartSahRF.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QPlainTextEdit, QProgressBar, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_ProgressBar(object):
    def setupUi(self, ProgressBar):
        if not ProgressBar.objectName():
            ProgressBar.setObjectName(u"ProgressBar")
        ProgressBar.setEnabled(True)
        ProgressBar.resize(483, 155)
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DriveHarddisk))
        ProgressBar.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(ProgressBar)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_titulo_progressBar = QLabel(ProgressBar)
        self.label_titulo_progressBar.setObjectName(u"label_titulo_progressBar")

        self.verticalLayout.addWidget(self.label_titulo_progressBar, 0, Qt.AlignmentFlag.AlignHCenter)

        self.frame_progressBar = QFrame(ProgressBar)
        self.frame_progressBar.setObjectName(u"frame_progressBar")
        self.frame_progressBar.setMinimumSize(QSize(0, 30))
        self.frame_progressBar.setMaximumSize(QSize(16777215, 30))
        self.frame_progressBar.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_progressBar.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_progressBar)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.progressBar = QProgressBar(self.frame_progressBar)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMinimumSize(QSize(400, 30))
        self.progressBar.setMaximumSize(QSize(400, 30))
        self.progressBar.setStyleSheet(u"background-color: rgb(170, 0, 255);")
        self.progressBar.setValue(0)
        self.progressBar.setOrientation(Qt.Orientation.Horizontal)
        self.progressBar.setTextDirection(QProgressBar.Direction.TopToBottom)

        self.verticalLayout_2.addWidget(self.progressBar, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)


        self.verticalLayout.addWidget(self.frame_progressBar)

        self.frame_logs_progressBar = QFrame(ProgressBar)
        self.frame_logs_progressBar.setObjectName(u"frame_logs_progressBar")
        self.frame_logs_progressBar.setMinimumSize(QSize(0, 85))
        self.frame_logs_progressBar.setMaximumSize(QSize(16777215, 85))
        self.frame_logs_progressBar.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_logs_progressBar.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frame_logs_progressBar)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(2, 2, 2, 2)
        self.bt_cancelar_progress = QPushButton(self.frame_logs_progressBar)
        self.bt_cancelar_progress.setObjectName(u"bt_cancelar_progress")
        self.bt_cancelar_progress.setMinimumSize(QSize(100, 0))
        self.bt_cancelar_progress.setMaximumSize(QSize(100, 16777215))
        self.bt_cancelar_progress.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.bt_cancelar_progress.setAutoFillBackground(False)

        self.gridLayout.addWidget(self.bt_cancelar_progress, 0, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.outPut_logs_progressBar = QPlainTextEdit(self.frame_logs_progressBar)
        self.outPut_logs_progressBar.setObjectName(u"outPut_logs_progressBar")
        self.outPut_logs_progressBar.setMinimumSize(QSize(0, 60))
        self.outPut_logs_progressBar.setMaximumSize(QSize(16777215, 60))
        self.outPut_logs_progressBar.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.gridLayout.addWidget(self.outPut_logs_progressBar, 2, 0, 1, 1)


        self.verticalLayout.addWidget(self.frame_logs_progressBar)


        self.retranslateUi(ProgressBar)

        QMetaObject.connectSlotsByName(ProgressBar)
    # setupUi

    def retranslateUi(self, ProgressBar):
        ProgressBar.setWindowTitle(QCoreApplication.translate("ProgressBar", u"Carregando...", None))
        self.label_titulo_progressBar.setText(QCoreApplication.translate("ProgressBar", u"Processarndo o arquivo .csv porfavor aguarde...", None))
        self.progressBar.setFormat(QCoreApplication.translate("ProgressBar", u"%p%", None))
        self.bt_cancelar_progress.setText(QCoreApplication.translate("ProgressBar", u"Cancelar", None))
    # retranslateUi

