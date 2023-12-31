import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt

# Establishing Connection to MYsql
host = "localhost"
user = 'root'
password = 'Keshika2001'
database = 'emp'
connection_string = "mysql+pymysql://" + \
                    f"{user}:{password}@{host}/{database}"
engine = create_engine(connection_string)
# Connection Successful

#retrive the details of employee who is assigned to projects in a department
q6=("SELECT e.employee_id, pa.proj_assign_id, p.project_id, d.department_id FROM employee e JOIN works_on w ON e.employee_id = w.employee_id JOIN project_assignment pa ON w.proj_assign_id = pa.proj_assign_id JOIN project p ON pa.project_id = p.project_id JOIN department d ON pa.department_id = d.department_id")
df6=pd.read_sql_query(q6, engine)
print(df6.head(5))
df6_subset=df6.head(10)
project_counts = df6_subset.groupby('employee_id')['project_id'].nunique()
# Create a bar plot

project_counts.plot(kind='bar', color='blue')
# Add labels and title
plt.xlabel('Employee ID')
plt.ylabel('Number of Projects Assigned')
plt.title('Number of Projects Assigned to Each Employee')
# Show the plot
plt.show()

#retrive the names and details of employee whose performance is greater than 4
q5= ("SELECT e.employee_id, e.employee_name, r.reward_type, p.score FROM EMPLOYEE e JOIN PERFORMANCE p ON e.performance_id = p.performance_id JOIN REWARD r ON e.employee_id = r.employee_id WHERE EXISTS (SELECT 1 FROM PERFORMANCE p WHERE p.performance_id = e.performance_id AND p.score >= 4) ORDER BY p.score DESC;")
df5 = pd.read_sql_query(q5, engine)
print(df5.head(5))
#v1 pie chart on moneratry and non monetary rewards
df5_subset = df5.head(10)
type_counts = df5_subset['reward_type'].value_counts()
type_counts.plot(kind='pie', autopct='%1.1f%%', colors=['blue', 'orange'])
plt.title('Distribution of Reward Types')
plt.show()

#retrive the projects which belong to department 110
q1=("select project_id from project where department_id='110';")
df1=pd.read_sql_query(q1, engine)
print(df1.head(5))

#retrive employee details and reason for leave for employee who has taken leave between the given dates
q4=("SELECT e.employee_id, e.employee_name, l.leave_id, l.start_date, l.end_date, l.reason FROM EMPLOYEE e JOIN LEAVE_TAKEN l ON e.employee_id = l.employee_id WHERE l.start_date BETWEEN '11/14/2022' AND '11/18/2022'")
df4 = pd.read_sql_query(q4, engine)
print(df4.head(5))

# Visualize the data with a bar chart
plt.bar(df4['employee_name'], df4['leave_id'])
plt.xlabel('Employee Name')
plt.ylabel('Number of Leaves')
plt.title('Leaves Taken by Employees (Nov 14, 2022 - Nov 18, 2022)')
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
plt.show()











