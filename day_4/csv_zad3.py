import pandas

# pip install pandas

# data = pandas.read_csv('records.csv')
data = pandas.read_csv('records_products.csv', delimiter=";")
print(data)
#    sku  exp_date  price
# 0    1     today  100.0
# 1    2     today  200.0
# 2    3  tomorrow  500.0
# 3    4     today   50.0
# 4    5     today  999.0

print(data.values)
# [[1 'today' 100.0]
#  [2 'today' 200.0]
#  [3 'tomorrow' 500.0]
#  [4 'today' 50.0]
#  [5 'today' 999.0]]

print(data.columns)  # Index(['sku', 'exp_date', 'price'], dtype='object')

print(data.items)
# <bound method DataFrame.items of    sku  exp_date  price
# 0    1     today  100.0
# 1    2     today  200.0
# 2    3  tomorrow  500.0
# 3    4     today   50.0
# 4    5     today  999.0>
