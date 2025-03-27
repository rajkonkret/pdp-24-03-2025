import pandas as pd
import numpy as np

technologies = ["Spark", "Pandas", "Python", "PHP"]
fee = [25000, 20000, 15000, 18000, 22200]
duration = ['50 Days', '35 Days', np.nan, '30 Days']
discount = [2000, 1000, 800, 500, 500]

columns = ['Courses', 'Fee', 'Durations', "Discount"]

df = pd.DataFrame(list(zip(technologies, fee, duration, discount)),
                  columns=columns)

print(df)
#   Courses    Fee Durations  Discount
# 0   Spark  25000   50 Days      2000
# 1  Pandas  20000   35 Days      1000
# 2  Python  15000       NaN       800
# 3     PHP  18000   30 Days       500

df.to_excel('courses.xlsx')
df.to_excel('courses_no_index.xlsx', index=False)
