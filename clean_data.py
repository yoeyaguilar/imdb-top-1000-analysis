import pandas as pd
import sqlite3


df=pd.read_csv('imdb_top_1000.csv')

# Load the raw CSV
print(f"Loaded {len(df)} rows")

# --- CLEAN RUNTIME ---
# Original format: "142 min" -> we want: 142
# .str.replace removes the " min" portion, then we convert to int
df['Runtime'] = df['Runtime'].str.replace(' min', '').astype(int)
print("Cleaned Runtime")

# --- CLEAN RELEASED_YEAR ---
# Mostly already looks like a year, but stored as text
# Some rows might have weird values, so we convert to numeric and let bad ones become NaN
df['Released_Year'] = pd.to_numeric(df['Released_Year'], errors='coerce')
print("Cleaned Released_Year")

# --- CLEAN GROSS ---
# Original format: "28,341,469" -> we want: 28341469
# Remove the commas, then convert to numeric
# Blank values become NaN automatically (which is what we want)
df['Gross'] = df['Gross'].str.replace(',', '')
df['Gross'] = pd.to_numeric(df['Gross'], errors='coerce')
print("Cleaned Gross")

# --- VERIFY THE CLEANUP ---
print()
print("Updated data types:")
print(df.dtypes)
print()
print("Year range:", int(df['Released_Year'].min()), "to", int(df['Released_Year'].max()))
print("Runtime range:", df['Runtime'].min(), "to", df['Runtime'].max(), "minutes")
print("Movies with Gross data:", df['Gross'].notna().sum(), "out of", len(df))

# --- SAVE TO SQLITE DATABASE ---
# Open a connection to a database file (creates it if it doesn't exist)
conn = sqlite3.connect('movies.db')

# Write the entire DataFrame to a table called 'movies'
# if_exists='replace' means: if the table already exists, drop it and recreate
df.to_sql('movies', conn, if_exists='replace', index=False)

# Close the connection
conn.close()

print()
print("Saved to movies.db")