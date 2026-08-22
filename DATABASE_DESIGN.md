# Database Design

## Database

The application uses a local SQLite database named `movies.db` in the project directory.

## Table: `movies`

```sql
CREATE TABLE IF NOT EXISTS movies (
    movie_id INTEGER PRIMARY KEY AUTOINCREMENT,
    movie_name TEXT NOT NULL,
    genre TEXT NOT NULL,
    rating REAL NOT NULL CHECK (rating >= 0 AND rating <= 10),
    release_year INTEGER NOT NULL CHECK (release_year >= 1888),
    status TEXT NOT NULL DEFAULT 'Active' CHECK (status IN ('Active', 'Inactive'))
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

## Feature Queries

```sql
-- View movies
SELECT movie_id, movie_name, genre, rating, release_year
FROM movies
ORDER BY release_year DESC, movie_name ASC;

-- Average rating
SELECT AVG(rating) AS average_rating FROM movies;

-- Highest-rated movie or movies
SELECT movie_name, genre, rating, release_year
FROM movies
WHERE rating = (SELECT MAX(rating) FROM movies);

-- Genre-wise summary
SELECT genre, COUNT(*) AS movie_count, AVG(rating) AS average_rating
FROM movies
GROUP BY genre
ORDER BY movie_count DESC, genre ASC;
```

The application will create the database and table automatically at startup, so a separate database installation is not required.