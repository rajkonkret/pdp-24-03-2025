# csv - dane odzielone znakiem podziału
# Kowalski,Jan,Kłodzko
# Nowak,Zenon,Szczecin
# Brzęczyszczykiewicz,Grzegorz,Chrząszczyżewoszyce

import csv

fields = ['name', 'branch', 'year', 'cgpa']
row = ["Radek", "coe", "3", "0"]

dict = dict(zip(fields, row))
print(dict)  # {'name': 'Radek', 'branch': 'coe', 'year': '3', 'cgpa': '0'}

filename = 'records.csv'
with open(filename, "w", newline="") as fh:
    csvwriter = csv.writer(fh)
    csvwriter.writerow(fields)
    csvwriter.writerow(row)
# newline="" - ominięcie problemu pustej linii

filename = "records_dict.csv"
with open(filename, "w", newline="") as csv_fh:
    csvwriter = csv.DictWriter(csv_fh, fieldnames=fields)
    csvwriter.writeheader()
    csvwriter.writerow(dict)
