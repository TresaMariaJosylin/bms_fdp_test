# Movie Collection Manager

## 1. Problem Statement

A movie enthusiast needs a simple way to maintain a personal collection containing films from multiple genres. Manual tracking makes it difficult to add movies, browse the collection, identify highly rated titles, and understand genre-wise patterns.

## 2. Objective

Build a Movie Collection Manager using Python, Streamlit, and SQLite. The application must store movie details permanently in `movies.db` and provide useful collection statistics.

## 3. Technology Constraints

- Python
- Streamlit
- SQLite
- Python virtual environment
- Git

## 4. Functional Requirements

### Add Movie

The user can add a movie with:

- Movie name
- Genre
- Rating
- Release year

The application validates required fields and stores the record in the `movies` table.

### View Movies

The user can browse all stored movies in a readable table, ordered consistently by release year or movie name.

### Average Rating

The application displays the average rating for all movies. An empty collection displays a clear empty-state message instead of an invalid value.

### Highest Rated Movie

The application identifies and displays the movie or movies with the highest rating.

### Genre-wise Summary

The application displays one summary row per genre, including the number of movies and the average rating for that genre.

## 5. Database Requirements

Create `movies.db` automatically when the application starts. Create a `movies` table with:

| Column | Purpose |
| --- | --- |
| `movie_id` | Unique identifier for each movie |
| `movie_name` | Movie title |
| `genre` | Movie genre |
| `rating` | User rating |
| `release_year` | Year the movie was released |

## 6. Acceptance Criteria

- A new user can create the database by starting the application.
- A valid movie can be added and appears in the collection.
- Invalid or incomplete input is rejected with a useful message.
- The collection can be viewed after restarting the application.
- Average rating and highest-rated movie values are calculated from SQLite data.
- Genre-wise counts and average ratings are calculated from SQLite data.
- The project includes setup instructions, testing evidence, prompts used, and Git evidence.