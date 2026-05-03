import pandas as pd

# Load the CSV file into a pandas DataFrame
df = pd.read_csv('imdb_top_1000.csv')

# Quick summary of what we loaded
print("shape(rows, columns):",df.shape)
print()
print("column names:")
print(df.columns.tolist())
print()
print("First 3 rows:")
print(df.head(3))
print()
print("Data types:")
print(df.dtypes)
