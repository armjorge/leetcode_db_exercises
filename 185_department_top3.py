import pandas as pd
data = [[1, 'Joe', 85000, 1], [2, 'Henry', 80000, 2], [3, 'Sam', 60000, 2], [4, 'Max', 90000, 1], [5, 'Janet', 69000, 1], [6, 'Randy', 85000, 1], [7, 'Will', 70000, 1]]
employee = pd.DataFrame(data, columns=['id', 'name', 'salary', 'departmentId']).astype({'id':'Int64', 'name':'object', 'salary':'Int64', 'departmentId':'Int64'})
data = [[1, 'IT'], [2, 'Sales']]
department = pd.DataFrame(data, columns=['id', 'name']).astype({'id':'Int64', 'name':'object'})

def top_three_salaries(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    df_merged = pd.merge(left = employee, right=department, left_on = 'departmentId', right_on = 'id' )
    df_merged['salary_dense_rank'] = df_merged.groupby('name_y')['salary'].rank(method='dense', ascending=False).astype(int)
    df_merged.rename(columns={'name_y': 'Department', 'name_x': 'Employee', 'salary': 'Salary'}, inplace=True)
    df_merged =df_merged[df_merged['salary_dense_rank']<= 3][['Department', 'Employee', 'Salary']]
    return df_merged
    
df_m = top_three_salaries(employee,department )
print(df_m.head(20))

import pandas as pd

# Versión óptima
def top_three_salariesOPTIMO(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:

    top_salary = employee[employee.groupby('departmentId').salary.rank(method='dense', ascending=False) <= 3]

    employee_department = top_salary.merge(department, left_on='departmentId', right_on='id')[['name_y', 'name_x', 'salary']]

    return employee_department.rename(columns = {'name_y': 'Department', 'name_x': 'Employee', 'salary': 'Salary'})