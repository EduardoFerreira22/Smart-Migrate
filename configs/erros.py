from PySide6.QtWidgets import (QApplication,QMainWindow,QMessageBox,QTableWidgetItem,QFileDialog)


class Erros():

    #MOSTRA UM POPUP DE NOTIFICAÇÃO DE ERRO 
    def show_error_popup(self, title, message):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setIcon(QMessageBox.Warning)
        msg.exec()
    
    def msg_popup(self,resp,msg1,msg2,**kwargs):
            msg1 = msg1
            msg2 = msg2
            if resp == 'OK':
                self.label_conectando.setVisible(False)
                self.label_conectado.setVisible(True)
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setWindowTitle("Sucesso!")
                msg.setText(f"{msg1}")
                msg.exec()
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setWindowTitle("Erro")
                msg.setText(f"{msg2}")
                msg.exec()