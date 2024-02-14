import pandas as pd

df = pd.read_csv('Employees.csv')

df.drop_duplicates(inplace=True)

df['Age'] = df['Age'].apply(lambda x: int(x))

df['Salary(USD)'] = df['Salary(USD)'] * 30.80

avg_age = df['Age'].mean()
median_salaries = df['Salary(USD)'].median()
ratio_males_females = df['Gender'].value_counts(normalize=True)

print(f'Average age: {avg_age}')
print(f'Median salaries: {median_salaries}')
print(f'Ratio between males and female employees: {ratio_males_females}')

df.to_csv('output_data.csv', index=False)