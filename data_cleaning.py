"""
Task 1: Data Cleaning and Preprocessing
Dataset: netflix_titles.csv

File: data_cleaning.py
Usage:
    python data_cleaning.py

Outputs:
    - cleaned_netflix_titles.csv (cleaned dataset)
    - cleaning_summary.md (markdown summary of changes)
"""

import pandas as pd
import numpy as np

# ----------------------------
# 0. File Paths
# ----------------------------
INPUT_PATH = "netflix_titles.csv"   # raw dataset path (same folder as script)
OUTPUT_PATH = "cleaned_netflix_titles.csv"
SUMMARY_PATH = "cleaning_summary.md"

# ----------------------------
# 1. Load Dataset
# ----------------------------
df = pd.read_csv(INPUT_PATH)
print("Raw dataset shape:", df.shape)
print(df.head())
print(df.info())
print("Missing values before:\n", df.isnull().sum())
print("Duplicates before:", df.duplicated().sum())

# ----------------------------
# 2. Rename Columns (snake_case)
# ----------------------------
df.columns = (
    df.columns
      .str.strip()
      .str.lower()
      .str.replace(" ", "_")
      .str.replace("(", "", regex=False)
      .str.replace(")", "", regex=False)
)

# ----------------------------
# 3. Convert date_added to datetime
# ----------------------------
df['date_added'] = pd.to_datetime(df['date_added'], format='%B %d, %Y', errors='coerce')
df['added_year'] = df['date_added'].dt.year
df['added_month'] = df['date_added'].dt.month
df['date_added_ddmmyyyy'] = df['date_added'].dt.strftime('%d-%m-%Y')

# ----------------------------
# 4. Parse duration into numeric + type
# ----------------------------
def parse_duration(x):
    if pd.isna(x):
        return pd.Series([np.nan, np.nan])
    s = str(x).strip()
    if 'min' in s:
        num = ''.join([c for c in s.split()[0] if c.isdigit()])
        return pd.Series([int(num) if num else np.nan, 'minutes'])
    elif 'Season' in s or 'Seasons' in s:
        num = ''.join([c for c in s.split()[0] if c.isdigit()])
        return pd.Series([int(num) if num else np.nan, 'seasons'])
    else:
        return pd.Series([np.nan, np.nan])

df[['duration_int', 'duration_type']] = df['duration'].apply(parse_duration)

# ----------------------------
# 5. Clean text columns (strip whitespace)
# ----------------------------
text_cols = ['type', 'title', 'director', 'cast', 'country', 'rating', 'listed_in', 'description']
for c in text_cols:
    if c in df.columns:
        df[c] = df[c].where(df[c].isna(), df[c].str.strip())

# ----------------------------
# 6. Standardize categorical values
# ----------------------------
df['type'] = df['type'].str.title()   # Movie / Tv Show

def take_first_country(x):
    if pd.isna(x): return np.nan
    return str(x).split(',')[0].strip()
if 'country' in df.columns:
    df['country'] = df['country'].apply(take_first_country)

# ----------------------------
# 7. Handle Missing Values
# ----------------------------
# Fill rating with mode
if 'rating' in df.columns:
    mode_rating = df['rating'].mode()
    if not mode_rating.empty:
        df['rating'] = df['rating'].fillna(mode_rating[0])
    else:
        df['rating'] = df['rating'].fillna('Not Rated')

# Fill director and cast with "Unknown"
df['director'] = df['director'].fillna('Unknown')
df['cast'] = df['cast'].fillna('Unknown')

# Leave date_added missing as NaT
# (Option: fill with release_year Jan 1 if you want — see previous script)

# ----------------------------
# 8. Fix Data Types
# ----------------------------
df['release_year'] = df['release_year'].astype('Int64')
df['duration_int'] = df['duration_int'].astype('Int64')

# ----------------------------
# 9. Optional Features
# ----------------------------
df['title_lower'] = df['title'].str.lower()

def count_cast(x):
    if pd.isna(x) or x == 'Unknown': return 0
    return len([p for p in str(x).split(',') if p.strip()])
df['num_cast'] = df['cast'].apply(count_cast)

# ----------------------------
# 10. Save Cleaned Dataset
# ----------------------------
df.to_csv(OUTPUT_PATH, index=False)
print("Saved cleaned dataset to:", OUTPUT_PATH)

# ----------------------------
# 11. Create Cleaning Summary
# ----------------------------
rows_before = pd.read_csv(INPUT_PATH).shape[0]
rows_after = df.shape[0]
missing_before = pd.read_csv(INPUT_PATH).isnull().sum().to_dict()
missing_after = df.isnull().sum().to_dict()
duplicates_before = pd.read_csv(INPUT_PATH).duplicated().sum()
duplicates_after = df.duplicated().sum()

summary_text = f"""
# Cleaning summary for netflix_titles.csv

- Rows before: {rows_before}
- Rows after: {rows_after}
- Duplicates before: {duplicates_before}
- Duplicates after: {duplicates_after}

## Missing values (before)
{missing_before}

## Missing values (after)
{missing_after}

## Transformations applied
- Renamed columns to snake_case.
- Converted date_added to datetime and created added_year/added_month.
- Parsed duration into duration_int (numeric) and duration_type (minutes/seasons).
- Standardized country (kept first country only).
- Filled rating with mode; filled director/cast with 'Unknown'.
- Added title_lower and num_cast features.
"""

with open(SUMMARY_PATH, 'w') as f:
    f.write(summary_text)

print("Saved cleaning summary to:", SUMMARY_PATH)
