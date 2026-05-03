import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect('movies.db')

# Helper function to run a query and print results with a header
def run_query(title, query):
    print()
    print("=" * 70)
    print(title)
    print("=" * 70)
    results = pd.read_sql(query,conn)
    print(results.to_string(index=False))

# Query 1: Top 10 highest-rated movies
run_query("Top 10 Highest-Rated Movies", """
    SELECT Series_Title, Released_Year, IMDB_Rating, Director
    FROM movies
    ORDER BY IMDB_Rating DESC
    LIMIT 10
""")

# Query 2: Top 10 directors by average rating (with at least 3 movies)
run_query("Top 10 Directors (minimum 3 movies)", """
    SELECT Director,
           COUNT(*) AS movie_count,
           ROUND(AVG(IMDB_Rating), 2) AS avg_rating
    FROM movies
    GROUP BY Director
    HAVING COUNT(*) >= 3
    ORDER BY avg_rating DESC
    LIMIT 10
""")

# Query 3: Average rating by decade
run_query("Average Rating by Decade", """
    SELECT (CAST(Released_Year AS INTEGER) / 10) * 10 AS decade,
           COUNT(*) AS movie_count,
           ROUND(AVG(IMDB_Rating), 2) AS avg_rating,
           ROUND(AVG(Runtime), 0) AS avg_runtime_min
    FROM movies
    WHERE Released_Year IS NOT NULL
    GROUP BY decade
    ORDER BY decade
""")

# Query 4: Top 10 highest-grossing movies
run_query("Top 10 Highest-Grossing Movies", """
    SELECT Series_Title, Released_Year, IMDB_Rating, Gross
    FROM movies
    WHERE Gross IS NOT NULL
          ORDER BY Gross DESC
          LIMIT 10
""")

# Query 5: Longest movies (the 321-minute mystery)
run_query("Top 5 Longest Movies", """
    SELECT Series_Title, Released_Year, Runtime, IMDB_Rating
    FROM movies
    ORDER BY Runtime DESC
    LIMIT 5
""")

# Close
conn.close()