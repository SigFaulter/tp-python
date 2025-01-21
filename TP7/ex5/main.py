import pandas as pd

df = pd.read_csv('employees.csv', nrows=5)
print(f"Moyenne d'age est: {df["Age"].mean()}")

