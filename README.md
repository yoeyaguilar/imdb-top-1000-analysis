# 100 Years of Cinema: Analyzing IMDb's Top 1,000 Films

A small data analysis project exploring trends in critically acclaimed films across a century of cinema. Built as a portfolio piece using Python, SQL, and matplotlib against a public Kaggle dataset.

## What's in here

- **`clean_data.py`** — Cleans the raw IMDb CSV (Runtime, Released_Year, and Gross columns require type coercion) and loads the result into a SQLite database.
- **`queries.py`** — SQL queries against the cleaned data: top movies, top directors, ratings by decade, etc.
- **`make_charts.py`** — Generates three visualizations using matplotlib, themed in black and gold to match my personal site.
- **`explore_data.py`** — A short exploration script used during initial EDA.

## Findings

Three things stood out from the analysis:

1. **Movies have gotten dramatically longer** — average runtime climbed from 86 minutes in the 1920s to 128 minutes in the 2010s.
2. **"Best of" lists have a strong recency bias** — only 11 films from the 1920s made the top 1,000 vs. 242 from the 2010s, despite barely any difference in average rating.
3. **Christopher Nolan is modern cinema's most consistently acclaimed director** — 8.46 average rating across 8 films in the top 1,000.

Full writeup with charts and code samples on my [Projects page](https://www.yoeyaguilar.com/projects.html).

## How to run it

Requires Python 3.10+ with `pandas` and `matplotlib` installed:

```bash
pip install pandas matplotlib
```

Then:

```bash
python clean_data.py    # creates movies.db
python queries.py       # prints query results to terminal
python make_charts.py   # creates 3 PNG charts
```

## Data source

[IMDb Movies Dataset on Kaggle](https://www.kaggle.com/datasets/harshitshankhdhar/imdb-dataset-of-top-1000-movies-and-tv-shows) by Harshit Shankhdhar.

## About me

I'm Joe — a Data Science BS graduate (summa cum laude, University of Phoenix) starting a Master of Computer Science in Data Science at the University of Illinois Urbana-Champaign in Fall 2026. More projects (and personality) at [yoeyaguilar.com](https://www.yoeyaguilar.com).