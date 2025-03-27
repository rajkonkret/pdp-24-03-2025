import csv

filename = "records.csv"
# filename = "records_products.csv"

fields = []
rows = []

with open(filename, "r") as f:
    dialect = csv.Sniffer().sniff(f.read(1024))
    print(dialect.delimiter)  # ;

    f.seek(0)  # ustawienie odcczytu na początek pliku
    # csvreader = csv.reader(f, delimiter=";")
    csvreader = csv.reader(f, delimiter=dialect.delimiter)

    print(csvreader)  # <_csv.reader object at 0x000001F2693CE7A0>

    fields = next(csvreader)  # pobiera pierwszy element, ustawia odczyt na drugi

    for row in csvreader:  # zacznie od drugiego elementu
        # print(row)
        rows.append(row)

print("Fields:", fields)
print("Rows:", rows)
# Fields: ['name', 'branch', 'year', 'cgpa']
# Rows: [['Radek', 'coe', '3', '0']]
