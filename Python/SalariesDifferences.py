import pandas as pd
import numpy as np

#Given the employee and department data frames, find the difference between the highest salaries found in the marketing
#and engineering departments. Output the absolute difference in salaries.

employee_info = {'id': [10301, 10302, 10303, 10304, 10305, 10306, 10307], 'first_name': ['Keith', 'Tyler', 'Clifford', 'Mary', 'Melissa', 'Ashley', 'Joseph'], 'last_name': ['Morgan', 'Booth', 'Nguyen', 'Jones', 'Lucero', 'Li', 'Solomon'], 'salary': [27056, 32199, 32165, 49488, 27024, 28516, 19945], 'department_id': [2, 3, 2, 2, 3, 4, 1]}
dept_info = {'id': [1, 2, 3, 4, 5, 6], 'department': ['engineering', 'human resources', 'operation', 'marketing', 'sales', 'customer care']}

db_employee = pd.DataFrame(data=employee_info)
db_dept = pd.DataFrame(data=dept_info)


merged_dfs = pd.merge(db_employee, db_dept, how = 'left', left_on = ['department_id'], right_on = ['id'])
mkt_df = merged_dfs[merged_dfs["department"] == "marketing"]
top_mkt_salary = mkt_df.groupby('department')['salary'].max().reset_index(name = 'mkt_salary')
eng_df = merged_dfs[merged_dfs["department"] == "engineering"]
top_eng_salary = eng_df.groupby('department')['salary'].max().reset_index(name = 'eng_salary')

salary_diff = abs(pd.DataFrame(top_mkt_salary['mkt_salary'] - top_eng_salary['eng_salary']))

salary_diff.columns = ['salary_difference']
print(salary_diff['salary_difference'][0])
