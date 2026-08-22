# Database Design

## Database

The application uses a local SQLite database named `movies.db` in the project directory.
The database is created automatically when `app.py` starts. SQLite connections use parameterized queries and are committed on success, rolled back on errors, and closed after use.

## Table: `movies`

```sql
CREATE TABLE IF NOT EXISTS movies (
    movie_id INTEGER PRIMARY KEY AUTOINCREMENT,
    movie_name TEXT NOT NULL,
    genre TEXT NOT NULL,
    rating REAL NOT NULL CHECK (rating >= 0 AND rating <= 10),
    release_year INTEGER NOT NULL CHECK (release_year >= 1888),
    status TEXT NOT NULL DEFAULT 'Active' CHECK (status IN ('Active', 'Inactive')),
    is_favorite INTEGER NOT NULL DEFAULT 0 CHECK (is_favorite IN (0, 1))
);
```

| Column | SQLite type | Constraints |
| --- | --- | --- |
| `movie_id` | `INTEGER` | Primary key, automatically incremented |
| `movie_name` | `TEXT` | Required |
| `genre` | `TEXT` | Required |
| `rating` | `REAL` | Required, from 0 to 10 |
| `release_year` | `INTEGER` | Required, 1888 or later |
| `status` | `TEXT` | Required, `Active` or `Inactive`; defaults to `Active` |
| `is_favorite` | `INTEGER` | Required, `0` or `1`; defaults to `0` |

## Feature Queries

```sql
-- View movies
SELECT movie_id, movie_name, genre, rating, release_year, status, is_favorite
FROM movies
ORDER BY release_year DESC, movie_name ASC;

-- Average rating for active movies
SELECT AVG(rating) AS average_rating
FROM movies
WHERE status = 'Active';

-- Highest-rated active movie or movies
SELECT movie_name, genre, rating, release_year
FROM movies
WHERE status = 'Active'
    AND rating = (SELECT MAX(rating) FROM movies WHERE status = 'Active');

-- Genre-wise summary for active movies
SELECT genre, COUNT(*) AS movie_count, AVG(rating) AS average_rating
FROM movies
WHERE status = 'Active'
GROUP BY genre
ORDER BY movie_count DESC, genre ASC;

-- Deactivate a movie without deleting its record
UPDATE movies SET status = 'Inactive' WHERE movie_id = ?;

-- Restore a movie
UPDATE movies SET status = 'Active' WHERE movie_id = ?;
```

## Migration

When an older database is opened, the application checks the existing columns using `PRAGMA table_info(movies)`. If needed, it adds `status` with a default of `Active` and `is_favorite` with a default of `0`. Existing records are therefore preserved and remain active by default.

Inactive movies remain available in the View Movies and Manage Movies pages. They are excluded from average rating, highest-rated movie, genre summary, and movie-picker results until restored.