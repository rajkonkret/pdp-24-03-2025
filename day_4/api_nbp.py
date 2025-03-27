import requests

url = "https://api.nbp.pl/api/exchangerates/rates/A/EUR/"

response = requests.get(url)

data = response.json()
print(data)
# {'table': 'A', 'currency': 'euro', 'code': 'EUR',
#  'rates': [{'no': '060/A/NBP/2025', 'effectiveDate': '2025-03-27', 'mid': 4.1913}]}

print(data['rates'])  # [{'no': '060/A/NBP/2025', 'effectiveDate': '2025-03-27', 'mid': 4.1913}]
print(data['rates'][0])  # {'no': '060/A/NBP/2025', 'effectiveDate': '2025-03-27', 'mid': 4.1913}
print(data['rates'][0]['mid'])  # 4.1913
