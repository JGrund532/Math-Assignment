import pandas as pd

# Load the data into a pandas dataframe
df = pd.read_csv('data.csv')

# Prompt the user for input
column_names = input("Enter column names separated by commas: ").split(',')
row_indices = input("Enter row indices separated by commas: ").split(',')
filter_criteria = input("Enter filter criteria (optional): ")
groupby_criteria = input("Enter groupby criteria (optional): ")

# Extract the data based on user input
if filter_criteria:
    df = df[df.eval(filter_criteria)]
if groupby_criteria:
    df = df.groupby(groupby_criteria).agg('mean')

if row_indices:
    if df.index.dtype == int:
        row_indices = [int(i) for i in row_indices]
    df = df.iloc[row_indices]
if column_names:
    df = df[column_names]

# Print the resulting dataframe
print(df)