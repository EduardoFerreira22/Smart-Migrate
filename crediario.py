import pandas as pd

# Carregar as planilhas de clientes e crediário
clientes_df = pd.read_csv('ClientesNoronha.csv', delimiter=';', encoding='latin1')
crediario_df = pd.read_csv('crediario.csv', delimiter=';', encoding='latin1')

# Garantir que os nomes usados para a comparação estejam em uma forma padronizada
clientes_df['Nome Padronizado'] = clientes_df['Nome fantasia'].str.lower().str.strip()
crediario_df['Nome Padronizado'] = crediario_df['cli_razao'].str.lower().str.strip()

# Criar um dicionário para mapear os nomes padronizados aos IDs corretos
nome_para_id = dict(zip(clientes_df['Nome Padronizado'], clientes_df['Codigo do cliente']))

# Substituir os IDs incorretos na planilha de crediário pelos corretos
crediario_df['id_cliente_corrigido'] = crediario_df['Nome Padronizado'].map(nome_para_id)

# Verificar se há clientes na planilha de crediário que não foram encontrados na de clientes
nao_encontrados = crediario_df[crediario_df['id_cliente_corrigido'].isna()]

if not nao_encontrados.empty:
    print("Alguns clientes não foram encontrados na tabela de clientes:")
    print(nao_encontrados[['cli_razao', 'id_cliente']])

# Preencher os IDs corretos na coluna original
crediario_df['id_cliente'] = crediario_df['id_cliente_corrigido']

# Remover a coluna temporária usada para padronização de nomes
crediario_df.drop(columns=['Nome Padronizado', 'id_cliente_corrigido'], inplace=True)

# Salvar o novo DataFrame em uma nova planilha CSV
crediario_df.to_csv('crediario_corrigido.csv', sep=';', index=False, encoding='latin1')

print("A planilha de crediário corrigida foi gerada com sucesso.")
