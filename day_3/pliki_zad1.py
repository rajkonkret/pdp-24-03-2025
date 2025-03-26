# działania z plikami
# filehandler - rura do pliku
# context manager - pomaga w pracy z zasobami np.: plikami
# with - context managery w pythonie
# ========= ===============================================================
#     Character Meaning
#     --------- ---------------------------------------------------------------
#     'r'       open for reading (default)
#     'w'       open for writing, truncating the file first
#     'x'       create a new file and open it for writing
#     'a'       open for writing, appending to the end of the file if it exists
#     'b'       binary mode
#     't'       text mode (default)
#     '+'       open a disk file for updating (reading and writing)
#     ========= ===============================================================
with open("text.log", "w", encoding="utf-8") as fh:
    fh.write("Powitanie\n")
    fh.write("Kolejne\n")
    fh.write("Jescze jedno\n")

# FileExistsError: [Errno 17] File exists: 'text.log'
# with open("text.log", "x",  encoding="utf-8") as file:
#     file.write("Dodane\n")

# "w" plik zostanie nadpisany jeśli istnieje
with open("text.log", "w", encoding="utf-8") as f:
    f.write("Nowe\n")

with open("text.log", "a", encoding="utf-8") as fh:
    fh.write("Dodane\n")
    fh.write("Dodane\n")
    fh.write("Dodane\n")
    fh.write("Dośdane\n")

with open("text.log", "r", encoding="utf-8") as f:
    lines = f.read()

print(lines)
