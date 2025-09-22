
# Cleaning summary for netflix_titles.csv

- Rows before: 8807
- Rows after: 8807
- Duplicates before: 0
- Duplicates after: 0

## Missing values (before)
{'show_id': 0, 'type': 0, 'title': 0, 'director': 2634, 'cast': 825, 'country': 831, 'date_added': 10, 'release_year': 0, 'rating': 4, 'duration': 3, 'listed_in': 0, 'description': 0}

## Missing values (after)
{'show_id': 0, 'type': 0, 'title': 0, 'director': 0, 'cast': 0, 'country': 831, 'date_added': 98, 'release_year': 0, 'rating': 0, 'duration': 3, 'listed_in': 0, 'description': 0, 'added_year': 98, 'added_month': 98, 'date_added_ddmmyyyy': 98, 'duration_int': 3, 'duration_type': 3, 'title_lower': 0, 'num_cast': 0}

## Transformations applied
- Renamed columns to snake_case.
- Converted date_added to datetime and created added_year/added_month.
- Parsed duration into duration_int (numeric) and duration_type (minutes/seasons).
- Standardized country (kept first country only).
- Filled rating with mode; filled director/cast with 'Unknown'.
- Added title_lower and num_cast features.
