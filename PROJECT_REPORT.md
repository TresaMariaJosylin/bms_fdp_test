# Movie Collection Manager Project Report

## Problem Statement

Manual management of a personal movie collection makes it difficult to track movie details, browse titles, identify favorites, and understand genre patterns.

## Features Implemented

- Add movies with title, genre, rating, and release year
- Validate required fields and rating range
- View the complete collection
- Search by movie title or genre
- Filter by genre and sort the collection
- Edit existing movie details
- Delete movies with confirmation
- Protect the collection with session-based login and logout
- Export the visible collection as CSV
- Mark favorites and filter the collection to favorite movies
- Pick a random active movie for tonight
- View the collection by release-year trend
- Display total movies, average rating, and represented genres
- Identify the highest-rated movie or movies
- Display genre counts, average ratings, and a bar chart
- Store all data in SQLite

## Database Design

The application creates `movies.db` automatically. Its `movies` table contains `movie_id`, `movie_name`, `genre`, `rating`, and `release_year`. Full schema and query details are documented in [DATABASE_DESIGN.md](DATABASE_DESIGN.md).

## Screenshots

Capture and insert screenshots from the running application for:

1. SQLite database and `movies` table
2. Successful record addition
3. View Movies page
4. Dashboard average rating and highest-rated movie
5. Genre-wise chart and summary table
6. `feature/category-summary` branch
7. Successful Git push

The exact actions and expected results are listed in [TESTING.md](TESTING.md).

## Prompts Used

The development prompts are recorded in [PROMPTS_USED.md](PROMPTS_USED.md).

## Testing Performed

Three automated database tests pass. Manual test cases cover database creation, adding records, validation, browsing, search, filtering, statistics, and Git evidence. See [TESTING.md](TESTING.md).

## Learning Outcomes

- Designed a relational table and enforced data integrity with SQLite constraints
- Connected a Python application to a persistent SQLite database
- Built a multi-view Streamlit interface
- Used SQL aggregation for average ratings and genre summaries
- Added automated tests using Python `unittest`
- Practiced virtual-environment management and Git branching workflows