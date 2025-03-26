import chardet

def read_txt(txt_file: str) -> str: 
    """Reads a .txt file and returns its content as a string"""
    with open(txt_file, "rb") as file:
        raw_data = file.read()
        result = chardet.detect(raw_data)
        encoding_detected = result['encoding']

    with open(txt_file, "r", encoding=encoding_detected) as file:
        txt_content = file.read()
        return txt_content