import pandas as pd


name_list = []
salary_list = []
department_list = []
employee_list = {}

#----------------------------COLLECT USER DATA-------------------------------#

for n in range(5):
    name = input("What is your name?")
    salary = int(input("What is your monthly salary?"))
    departmentid = int(input("What is your department ID?"))

    name_list.append(name)
    salary_list.append(salary)
    department_list.append(departmentid)

#----------------------------------------------------------------------------#
#------------------------------CREATE TABLE----------------------------------#

employee_list['name'] = name_list
employee_list['salary'] = salary_list
employee_list['departmentid'] = department_list

employee_table = pd.DataFrame(employee_list)

print(employee_table)

#----------------------------------------------------------------------------#
#-------------------------FINDING HIGHEST SCORE------------------------------#

list1 = []
list2 = []

for index, row in employee_table.iterrows():
    if row['departmentid'] == 1:
        list1.append(row['salary'])
    else:
        list2.append(row['salary'])

for index, row in employee_table.iterrows():
    if row['departmentid'] == 1:
        if row['salary'] < max(list1):
            employee_table.drop(index, inplace=True)
    else:
        if row['salary'] < max(list2):
            employee_table.drop(index, inplace = True)

employee_table.replace(1, 'IT', inplace= True)
employee_table.replace(2, 'Sales', inplace= True)
employee_table.rename(columns = {'departmentid': 'department'}, inplace = True)
print(employee_table)

#----------------------------------------------------------------------------#

