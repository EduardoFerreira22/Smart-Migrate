import chardet

def detectar_encoding(path_csv):
    try:
        with open(path_csv, 'rb') as f:
            result = chardet.detect(f.read())
        return result['encoding']
    except Exception as e:
        print(f"Não foi possível carregar o arquivo:\n{e}")