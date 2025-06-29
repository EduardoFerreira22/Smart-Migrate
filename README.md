# 📦 Smartmigrate

**Smartmigrate** é uma poderosa aplicação interna desenvolvida para automatizar e agilizar processos de migração, padronização e validação de dados empresariais. Idealizada para empresas que atuam com sistemas de gestão (ERP), contabilidade e automação fiscal, a ferramenta concentra múltiplas funcionalidades essenciais em uma interface intuitiva e inteligente.

---

## 🧠 Propósito

O objetivo do Smartmigrate é simplificar a manipulação de arquivos e registros durante processos de migração de dados, saneamento e análise, garantindo mais segurança, padronização e economia de tempo para os profissionais envolvidos.

---

## 🔍 Visão Geral de Funcionalidades

### 📥 Importação de Arquivos CSV

- Leitura e carregamento automático de planilhas.
- Mapeamento inteligente de colunas.
- Remoção de registros duplicados.
- Substituição de dados com base em regras definidas.
- Formatação automatizada de CPFs, CNPJs, códigos de barras etc.

---

## 🧭 Módulo de **Busca de Dados**

Ativado após a importação de um CSV para a tabela principal, o módulo **Opções de Busca** oferece:

- 🔎 **Buscar por NCM**
- ❌ **Identificar NCMs Inválidos**
- 🧮 **Buscar por Conteúdo (“Tudo que contém”)**
- 🧩 **Encontrar Duplicados por Coluna**
  - Exportação de duplicados para uma tabela auxiliar.
  - Permite salvamento separado em CSV para tratamento específico.

---

## 🛠️ Módulo de **Processamento de Dados**

O módulo **Opções de Processamento** oferece ferramentas automatizadas para limpeza e padronização:

- 🔁 **Buscar e Substituir Caracteres Especiais**
- ➖ **Transformar Valores Negativos em Zero**
- 🔍 **Filtrar e Copiar Linhas com Conteúdo Específico**
- 📤 **Separar Linhas para Tabela Lateral**
- 🧾 **Formatar Códigos de Barras**
- 👤 **Formatar CPF e CNPJ**
- 🔁 **Substituir NCM**
- 🔄 **Se Coluna A contém X, Coluna B recebe Y**
- ✏️ **“Tudo que contém” mude para**
- 🔡 **Transformar para minúsculas (A → a)**
- 🔠 **Transformar para maiúsculas (a → A)**

---

## 🧮 Módulo **Contábil-Fiscal**

Ferramentas voltadas à automação e análise de documentos fiscais e dados contábeis:

- 📁 **Importação de Pastas com XMLs**
  - Leitura automática de notas fiscais eletrônicas (NFe).
  - Extração e somatório de impostos por tipo (ICMS, PIS, COFINS etc.).
  - Conversão de XML para DANFE.
- 🌐 **Integração com a SEFAZ**
  - Utilização do MDFe para busca e download de documentos fiscais diretamente da SEFAZ.
  - Conversão de XMLs baixados para DANFE com visualização direta.
- 👥 **Cadastro e Gerenciamento**
  - Clientes
  - Contabilidades
- 📤 **Importação e Exportação de Dados**
  - Clientes e contabilidades (CSV/Planilhas).
  - Histórico de documentos e registros de cada entidade.

---

## 🗄️ Módulo de Conexão com Bancos de Dados

Capacidades completas para integração e manipulação de bases de dados:

- 🔗 **Conexão com múltiplos SGBDs:**
  - SQL Server
  - MySQL
  - PostgreSQL
  - SQLite
  - Firebird
- 📂 **Repositório de Queries**
  - Armazene e reutilize consultas SQL frequentes.
- 🖥️ **Terminal SQL Embutido**
  - Execução direta de comandos e scripts em qualquer banco conectado.

---

## 🧰 Tecnologias Utilizadas

- **Python 3.11+**
- **PyQt5 / PySide6** – Interface gráfica
- **pandas** – Manipulação de dados tabulares
- **xml.etree.ElementTree / xmltodict** – Leitura e conversão de XMLs
- **Drivers de banco:** `pyodbc`, `mysql-connector-python`, `psycopg2`, `sqlite3`, `fdb` (Firebird)
- **Outras bibliotecas:** `openpyxl`, `csv`, `re`, `collections`, `os`, `requests` (para integração SEFAZ)

---

## 🗂️ Estrutura do Projeto (Exemplo)

