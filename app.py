import sqlite3
from pathlib import Path

import streamlit as st


DATABASE_PATH = Path(__file__).with_name("movies.db")
GENRES = ["Action", "Comedy", "Drama", "Thriller", "Science Fiction"]


def get_connection():
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def initialize_database():
    with get_connection() as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS movies (
                movie_id INTEGER PRIMARY KEY AUTOINCREMENT,
                movie_name TEXT NOT NULL,
                genre TEXT NOT NULL,
                rating REAL NOT NULL CHECK (rating >= 0 AND rating <= 10),
                release_year INTEGER NOT NULL CHECK (release_year >= 1888)
            )
            """
        )


def add_movie(movie_name, genre, rating, release_year):
    with get_connection() as connection:
        connection.execute(
            """
            INSERT INTO movies (movie_name, genre, rating, release_year)
            VALUES (?, ?, ?, ?)
            """,
            (movie_name.strip(), genre, rating, release_year),
        )


def fetch_movies():
    with get_connection() as connection:
        return connection.execute(
            """
            SELECT movie_id, movie_name, genre, rating, release_year
            FROM movies
            ORDER BY release_year DESC, movie_name ASC
            """
        ).fetchall()


def fetch_average_rating():
    with get_connection() as connection:
        result = connection.execute("SELECT AVG(rating) AS average_rating FROM movies").fetchone()
        return result["average_rating"]


def fetch_highest_rated():
    with get_connection() as connection:
        return connection.execute(
            """
            SELECT movie_name, genre, rating, release_year
            FROM movies
            WHERE rating = (SELECT MAX(rating) FROM movies)
            ORDER BY movie_name ASC
            """
        ).fetchall()


def fetch_genre_summary():
    with get_connection() as connection:
        return connection.execute(
            """
            SELECT genre, COUNT(*) AS movie_count, ROUND(AVG(rating), 2) AS average_rating
            FROM movies
            GROUP BY genre
            ORDER BY movie_count DESC, genre ASC
            """
        ).fetchall()


st.set_page_config(page_title="Movie Collection Manager", page_icon="🎬", layout="wide")
initialize_database()

st.title("Movie Collection Manager")
st.caption("Keep your collection organized and your favorites easy to find.")

with st.sidebar:
    st.header("Navigation")
    page = st.radio("Choose a view", ["Dashboard", "Add Movie", "View Movies"], label_visibility="collapsed")

if page == "Add Movie":
    st.header("Add Movie")
    with st.form("add_movie_form", clear_on_submit=True):
        movie_name = st.text_input("Movie Name")
        genre = st.selectbox("Genre", GENRES)
        rating = st.number_input("Rating", min_value=0.0, max_value=10.0, value=5.0, step=0.1)
        release_year = st.number_input("Release Year", min_value=1888, max_value=2100, value=2024, step=1)
        submitted = st.form_submit_button("Add Movie", type="primary")

    if submitted:
        if not movie_name.strip():
            st.error("Movie name is required.")
        else:
            add_movie(movie_name, genre, rating, release_year)
            st.success(f'"{movie_name.strip()}" was added successfully.')

elif page == "View Movies":
    st.header("Movie Collection")
    movies = fetch_movies()
    if movies:
        st.dataframe([dict(movie) for movie in movies], use_container_width=True, hide_index=True)
    else:
        st.info("No movies have been added yet.")

else:
    st.header("Collection Dashboard")
    movies = fetch_movies()
    average_rating = fetch_average_rating()
    highest_rated = fetch_highest_rated()
    summary = fetch_genre_summary()

    metric_one, metric_two, metric_three = st.columns(3)
    metric_one.metric("Total Movies", len(movies))
    metric_two.metric("Average Rating", f"{average_rating:.2f}" if average_rating is not None else "-")
    metric_three.metric("Genres Represented", len(summary))

    st.subheader("Highest Rated Movie")
    if highest_rated:
        st.dataframe([dict(movie) for movie in highest_rated], use_container_width=True, hide_index=True)
    else:
        st.info("Add a movie to see the highest-rated title.")

    st.subheader("Genre-wise Summary")
    if summary:
        st.dataframe([dict(row) for row in summary], use_container_width=True, hide_index=True)
    else:
        st.info("Add movies to see genre statistics.")