import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to the database
conn = sqlite3.connect('movies.db')

# LAFC color palette - matching your website
LAFC_BLACK = '#000000'
LAFC_GOLD = '#C8A15C'
LAFC_DARK_GRAY = '#111111'
LAFC_RED = '#E31837'

# Set up some default chart styling so all 3 charts have a consistent look
plt.rcParams['figure.facecolor'] = LAFC_BLACK
plt.rcParams['axes.facecolor'] = LAFC_DARK_GRAY
plt.rcParams['axes.edgecolor'] = LAFC_GOLD
plt.rcParams['axes.labelcolor'] = LAFC_GOLD
plt.rcParams['xtick.color'] = LAFC_GOLD
plt.rcParams['ytick.color'] = LAFC_GOLD
plt.rcParams['text.color'] = LAFC_GOLD
plt.rcParams['axes.titlecolor'] = '#FFFFFF'
plt.rcParams['font.family'] = 'Arial'

# ===== CHART 1: Average runtime by decade =====
runtime_data = pd.read_sql("""
    SELECT (CAST(Released_Year AS INTEGER) / 10) * 10 AS decade,
            ROUND(AVG(Runtime), 0) AS avg_runtime
    FROM movies
    WHERE Released_Year IS NOT NULL
    GROUP BY decade
    ORDER BY decade
""", conn)

fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(runtime_data['decade'].astype(str),
       runtime_data['avg_runtime'],
       color=LAFC_GOLD,
       edgecolor=LAFC_BLACK)
ax.set_title('Movies Got Longer: Average Runtime by Decade', fontsize=16, pad=15)
ax.set_xlabel('Decade')
ax.set_ylabel('Average Runtime (minutes)')
ax.grid(axis='y', color=LAFC_GOLD, alpha=0.2, linestyle='--')
ax.set_axisbelow(True)

plt.tight_layout()
plt.savefig('chart_runtime_by_decade.png', dpi=150, facecolor=LAFC_BLACK)
plt.close()
print("Saved; chart_runtime_by_decade.png")

# ===== CHART 2: Movie count by decade (recency bias) =====
count_data = pd.read_sql("""
    SELECT (CAST(Released_Year AS INTEGER) / 10) * 10 AS decade,
           COUNT(*) AS movie_count
    FROM movies
    WHERE Released_Year IS NOT NULL
    GROUP BY decade
    ORDER BY decade
""", conn)

fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(count_data['decade'].astype(str),
       count_data['movie_count'],
       color=LAFC_RED,
       edgecolor=LAFC_BLACK)
ax.set_title('Recency Bias: How Many "Top 1000" Films Came From Each Decade',
             fontsize=16, pad=15)
ax.set_xlabel('Decade')
ax.set_ylabel('Number of Films in Top 1000')
ax.grid(axis='y', color=LAFC_GOLD, alpha=0.2, linestyle='--')
ax.set_axisbelow(True)

plt.tight_layout()
plt.savefig('chart_count_by_decade.png', dpi=150, facecolor=LAFC_BLACK)
plt.close()
print("Saved: chart_count_by_decade.png")

# ===== CHART 3: Top directors by average rating =====
directors_data = pd.read_sql("""
    SELECT Director,
           COUNT(*) AS movie_count,
           ROUND(AVG(IMDB_Rating), 2) AS avg_rating
    FROM movies
    GROUP BY Director
    HAVING COUNT(*) >= 3
    ORDER BY avg_rating DESC
    LIMIT 10
""", conn)

# Reverse the order so the highest-rated appears at the top of the chart
directors_data = directors_data[::-1]

fig, ax = plt.subplots(figsize=(10, 7))
bars = ax.barh(directors_data['Director'],
               directors_data['avg_rating'],
               color=LAFC_GOLD,
               edgecolor=LAFC_BLACK)

# Add the rating value at the end of each bar for clarity
for bar, rating in zip(bars, directors_data['avg_rating']):
    ax.text(bar.get_width() - 0.05,
            bar.get_y() + bar.get_height() / 2,
            f'{rating}',
            va='center', ha='right',
            color=LAFC_BLACK, fontweight='bold')

ax.set_title('Top 10 Directors by Average IMDb Rating (3+ films)',
             fontsize=16, pad=15)
ax.set_xlabel('Average IMDb Rating')
ax.set_xlim(7.5, 8.6)  # Tight x-axis range so differences are visible
ax.grid(axis='x', color=LAFC_GOLD, alpha=0.2, linestyle='--')
ax.set_axisbelow(True)

plt.tight_layout()
plt.savefig('chart_top_directors.png', dpi=150, facecolor=LAFC_BLACK)
plt.close()
print("Saved: chart_top_directors.png")


conn.close()
print()
print("All charts saved.")