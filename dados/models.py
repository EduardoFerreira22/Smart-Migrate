import sqlite3


class SQLiteConnect():
    def __init__(self, path):
        self.path = path
        self.conn = None
        self.cursor = None

    def connect_db(self):
        try:
            self.conn = sqlite3.connect(self.path)
            self.cursor = self.conn.cursor()
            
            return self.cursor
        except (TypeError, sqlite3.Error) as e:
            print(f"Erro: {e}")

    def commit(self):
        if self.conn:
            self.conn.commit()
        
    def close(self):
        """Fecha a conexão explicitamente"""
        if self.conn:
            self.conn.close()
            self.conn = None
            self.cursor = None
        
    def create_tables(self, queries):
        cursor = self.connect_db()
        try:
            if cursor:
                # Lista de tabelas esperadas
                expected_tables = ['roles', 'users', 'permissions', 'role_permissions', 'licenses', 'clients']
                # Verificar tabelas existentes
                cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
                existing_tables = [row[0] for row in cursor.fetchall()]
                # Verificar se todas as tabelas esperadas já existem
                tables_exist = all(table in existing_tables for table in expected_tables)
                
                if tables_exist:
                    print("Tabelas já criadas!")
                else:
                    cursor.executescript(queries)
                    self.commit()
                    print("Tabelas criadas com sucesso!")
            else:
                print("Erro: Não foi possível obter o cursor para criar tabelas")
        except sqlite3.Error as e:
            print(f"Erro ao criar tabelas: {e}")
        finally:
            self.close()

    def create_data(self):
        ...
    def select_cliente(self):
        pass

    def select_contabilidade(self):
        pass

    def post_cliente(self):
        pass

    def post_contabilidade(self):
        pass

    def put_cliente(self):
        pass

    def put_contabilidade(self):
        pass