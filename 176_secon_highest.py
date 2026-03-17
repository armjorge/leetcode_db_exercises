import pandas as pd
import numpy as np
data = [[1, 100], [2, 200], [3, 300]]
employee = pd.DataFrame(data, columns=['id', 'salary']).astype({'id':'int64', 'salary':'int64'})

slist = employee['salary'].unique().tolist()
slist = sorted(slist, reverse = True)
print(slist)
secondh = [np.nan]
if len(slist)>=2:
    secondh = [slist[1]]

final_df = pd.DataFrame(secondh, columns=['SecondHighestSalary']).astype({'SecondHighestSalary':'int64'})
print(final_df)

print('\nOtra versión usando iloc[1]')
f_serie = employee['salary'].sort_values(ascending = False).unique()
print(f_serie)