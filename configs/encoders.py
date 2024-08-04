import chardet

def detectar_encoding(path_csv):
    with open(path_csv, 'rb') as f:
        result = chardet.detect(f.read())
    return result['encoding']