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
    csvwriter.writerow(dict) # zapis słownika

products = [
    {"sku": 1, "exp_date": 'today', "price": 100},
    {"sku": 2, "exp_date": 'today', "price": 200},
    {"sku": 3, "exp_date": 'tomorrow', "price": 500},
    {"sku": 4, "exp_date": 'today', "price": 50.00},
    {"sku": 5, "exp_date": 'today', "price": 999},
]

filename = "records_products.csv"
fields_product = [key for key in products[0]]
print(fields_product)  # ['sku', 'exp_date', 'price']

with open(filename, "w", newline="") as f:
    csvwriter = csv.DictWriter(f, fieldnames=fields_product, delimiter=";")
    csvwriter.writeheader()
    csvwriter.writerows(products) # zapis listy

