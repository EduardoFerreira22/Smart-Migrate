import pandas as pd
import re

# Função para ler o arquivo CSV e identificar possíveis erros
def ler_csv_com_erro_ajustado(filepath, sep=';', encoding='latin1'):
    try:
        df = pd.read_csv(filepath, sep=sep, encoding=encoding, on_bad_lines='skip')  # 'skip' ignora as linhas problemáticas
        return df
    except pd.errors.ParserError as e:
        print(f"Erro ao processar o CSV: {e}")
        return None

# Função para corrigir CPF e CNPJ
def corrigir_cnpjcpf(cnpjcpf):
    cnpjcpf = re.sub(r'\D', '', str(cnpjcpf))  # Remove caracteres não numéricos
    
    if len(cnpjcpf) == 10:  # CPF com 10 dígitos (precisa de um zero à esquerda)
        return cnpjcpf.zfill(11)
    elif len(cnpjcpf) == 12:  # CNPJ com 12 dígitos (precisa de dois zeros à esquerda)
        return cnpjcpf.zfill(14)
    else:
        return cnpjcpf  # Retorna o valor original se não for CPF nem CNPJ ou se já tiver o tamanho correto

# Tenta carregar o arquivo CSV
df = ler_csv_com_erro_ajustado('CLIENTES.CSV')

# Se o DataFrame foi carregado corretamente, aplica a correção
if df is not None:
    df['CNPJCPF'] = df['CNPJCPF'].apply(corrigir_cnpjcpf)
    
    # Salva o DataFrame corrigido de volta no CSV
    df.to_csv('CLIENTES_CORRIGIDO.CSV', index=False, sep=';', encoding='utf-8')
    print("Correção concluída! Os dados corrigidos foram salvos em 'CLIENTES_CORRIGIDO.CSV'.")
else:
    print("O DataFrame não pôde ser carregado devido a erros no arquivo.")
