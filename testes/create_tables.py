import sys
import os
import unittest
import time

# Adicionar o diretório raiz ao sys.path para imports absolutos
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from dados.models import SQLiteConnect

class TestSQLiteConnect(unittest.TestCase):
    def setUp(self):
        # Configurar o banco de teste
        self.sqlite = SQLiteConnect("test.db")
        try:
            with open("dados/SQL/schema.txt", "r", encoding="utf-8") as f:
                self.queries = f.read()
        except FileNotFoundError:
            self.fail("Arquivo schema.txt não encontrado em dados/SQL/schema.txt")

    def test_create_tables(self):
        # Testar a criação da tabela 'clients'
        self.sqlite.create_tables(path=self.queries)
        cursor = self.sqlite.connect_db()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='clients'")
        result = cursor.fetchone()
        self.assertIsNotNone(result, "Tabela 'clients' não foi criada")
        self.sqlite.close()

    def test_create_tables_all(self):
        # Testar se todas as tabelas esperadas foram criadas
        self.sqlite.create_tables(path=self.queries)
        cursor = self.sqlite.connect_db()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = [t[0] for t in cursor.fetchall()]
        expected_tables = ['roles', 'users', 'permissions', 'role_permissions', 'licenses', 'clients']
        for table in expected_tables:
            self.assertIn(table, tables, f"Tabela '{table}' não foi criada")
        self.sqlite.close()

    def tearDown(self):
        # Fechar a conexão e tentar remover o banco de teste
        self.sqlite.close()
        # Aguardar um momento para o Windows liberar o arquivo
        for _ in range(5):  # Tentar até 5 vezes
            try:
                if os.path.exists("test.db"):
                    os.remove("test.db")
                break
            except PermissionError:
                time.sleep(0.1)  # Aguardar 100ms antes de tentar novamente
            except FileNotFoundError:
                break

if __name__ == "__main__":
    unittest.main()