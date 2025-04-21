import sqlite3


class SQLiteConnect():
    def __init__(self, path):
            self.path = path
            self.conn = None
            self.cursor = None
            self.connect_db()  # Criar conexão na inicialização

    def connect_db(self):
        if self.conn is None or self.cursor is None:
            try:
                self.conn = sqlite3.connect(self.path, timeout=10)  # Timeout de 10 segundos
                self.cursor = self.conn.cursor()
                print("Conexão com o banco estabelecida")
            except sqlite3.Error as e:
                print(f"Erro ao conectar ao banco: {e}")
                raise
        return self.cursor

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

    def select_cliente(self):
        cursor = self.connect_db()
        try:
            if cursor:
                cursor.execute(
                    """
                    SELECT T1.ID, T1.ATIVO, T1.STATUS_ENVIO, 
                        T1.NOME, T1.CNPJ, T1.EMAIL, 
                        T2.NOME, T1.SISTEMA, 
                        T1.LINK_SISTEMA, T1.USER_SISTEMA, 
                        T1.SENHA_SISTEMA , T1.DATE_UPDATE

                    FROM CLIENTS T1
                    LEFT JOIN CONTABILIDADE T2
                    ON T2.ID = T1.ID
                    ORDER BY T1.DATE_UPDATE ASC
                """
                )
                data = cursor.fetchall()
                return data
            
        except Exception as e:
            print(e)

    def select_contabilidade(self):
        cursor = self.connect_db()
        try:
            if cursor:
                cursor.execute(
                    """
                    SELECT ID, ATIVO, CNPJ, NOME, RAZAOSOCIAL, EMAIL, PHONE
                    FROM CONTABILIDADE
                """
                )
                data = cursor.fetchall()
                return data
        except Exception as e:
            print(e)

    def get_contabilidade(self, contador):
        cursor = self.connect_db()
        try:
            if cursor:
                # Usar parâmetro para evitar injeção de SQL
                cursor.execute("SELECT ID FROM CONTABILIDADE WHERE NOME = ?", (contador,))
                result = cursor.fetchone()  # fetchone retorna uma tupla ou None
                return result
        except Exception as e:
            print(e)

    def post_cliente(self, data):
        cursor = self.connect_db()
        try:
            if cursor:
                cursor.execute(
                    "INSERT INTO CLIENTS (nome, razaoSocial, cnpj, email, id_contador, sistema, link_sistema, user_sistema, senha_sistema, user_create)" \
                    "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (*data,)
                )
                self.commit()
                print("Cliente criado com sucesso")
            else:
                print("Cursor não está definido.\nErro ao criar Cliente")
        except sqlite3.OperationalError as e:
                    self.conn.rollback()
                    raise e

    def post_contabilidade(self, data):
        cursor = self.connect_db()
        try:
            if cursor:
                cursor.execute(
                    "INSERT INTO CONTABILIDADE (cnpj, nome, razaoSocial, email, phone, user_create)" \
                    "VALUES (?, ?, ?, ?, ?, ?)", (*data,)
                )
                self.commit()
                print("Contabilidade criado com sucesso")
            else:
                print("Cursor não está definido.\nErro ao criar contabilidade")
        except sqlite3.OperationalError as e:
                    self.conn.rollback()
                    print(f"Erro post_contabilidade: {e}")
                    raise e

    def put_cliente(self):
        pass

    def put_contabilidade(self):
        pass