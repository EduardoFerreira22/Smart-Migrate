import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
from dbfread import DBF

class DBFViewer(QMainWindow):
    def __init__(self, dbf_file_path, encoding='latin1'):
        super().__init__()
        
        self.setWindowTitle("DBF Viewer")
        self.setGeometry(100, 100, 800, 600)

        # Ler o arquivo DBF com a codificação especificada
        table = DBF(dbf_file_path, encoding=encoding)

        # Criar um widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Criar um layout
        layout = QVBoxLayout(central_widget)

        # Criar uma tabela
        self.table_widget = QTableWidget()
        layout.addWidget(self.table_widget)

        # Preencher a tabela com os dados do DBF
        self.populate_table(table)

    def populate_table(self, table):
        # Obter os nomes das colunas
        field_names = table.field_names

        # Configurar a tabela
        self.table_widget.setColumnCount(len(field_names))
        self.table_widget.setHorizontalHeaderLabels(field_names)

        # Adicionar os dados à tabela
        for row_index, record in enumerate(table):
            self.table_widget.insertRow(row_index)
            for col_index, field_name in enumerate(field_names):
                self.table_widget.setItem(row_index, col_index, QTableWidgetItem(str(record[field_name])))

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Substitua 'caminho_para_seu_arquivo.dbf' pelo caminho para o seu arquivo .DBF
    dbf_file_path = 'PRODUTOS.dbf'
    
    # Substitua 'latin1' pela codificação correta se necessário
    viewer = DBFViewer(dbf_file_path, encoding='latin1')
    viewer.show()

    sys.exit(app.exec())
