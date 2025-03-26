import chardet

# pip install chardet
with open("text.log", "r", encoding="utf-8") as f:
    raw_data = f.read()

print(raw_data)

# rb odczyt binarnie
with open("text.log", "rb") as f:
    raw_data = f.read()

print(raw_data)  # b'Nowe\r\nDodane\r\nDodane\r\nDodane\r\nDo\xc5\x9bdane\r\n'
print(type(raw_data))  # <class 'bytes'>

result = chardet.detect(raw_data)
print(result)
# {'encoding': 'MacRoman', 'confidence': 0.584, 'language': ''}
# po zwiększeniu liczby próbek
# {'encoding': 'utf-8', 'confidence': 0.99, 'language': ''}
print(type(result))  # <class 'dict'>
encoding = result['encoding']

print("Znalezione kodowanie znaków:", encoding)  # Znalezione kodowanie znaków: utf-8

print(raw_data.decode(encoding=encoding))
# Nowe
# Dodane
# Dodane
# Dodane
# Dośdane
# Dośąźćdane
