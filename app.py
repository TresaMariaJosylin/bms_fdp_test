import sqlite3
from contextlib import contextmanager
from pathlib import Path

import pandas as pd
import streamlit as st


DATABASE_PATH = Path(__file__).with_name("movies.db")
GENRES = ["Action", "Comedy", "Drama", "Thriller", "Science Fiction"]


def apply_styles():
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap');
        :root { --ink: #18232d; --muted: #61717d; --teal: #087f8c; --coral: #ef8354; --paper: #f7f5ef; }
        .stApp { background: var(--paper); color: var(--ink); }
        .stApp, .stApp p, .stApp label { font-family: 'DM Sans', sans-serif; }
        h1, h2, h3 { font-family: 'Space Grotesk', sans-serif !important; letter-spacing: 0 !important; color: var(--ink); }
        h1 { font-size: 2.8rem !important; margin-bottom: 0.15rem !important; }
        [data-testid='stSidebar'] { background: #173b44; }
        [data-testid='stSidebar'] * { color: #f4f5ef !important; }
        [data-testid='stSidebar'] .stRadio label { padding: 0.35rem 0; }
        [data-testid='stMetric'] { background: white; border: 1px solid #e5e2d9; border-radius: 8px; padding: 1rem; box-shadow: 0 5px 18px rgba(24,35,45,.05); }
        [data-testid='stMetricLabel'] { color: var(--muted); }
        [data-testid='stMetricValue'] { color: var(--teal); font-family: 'Space Grotesk', sans-serif; }
        .hero { background: #173b44; border-radius: 8px; padding: 1.7rem 2rem; margin: 0.5rem 0 1.4rem; color: #f4f5ef; }
        .hero h2 { color: #f4f5ef; margin: 0; font-size: 1.8rem; }
        .hero p { color: #c6d8d5; margin: 0.35rem 0 0; }
        .eyebrow { color: #f2b880; font-size: .75rem; font-weight: 700; letter-spacing: .12em; text-transform: uppercase; }
        div.stButton > button, div[data-testid='stFormSubmitButton'] button { border-radius: 6px; font-weight: 700; }
        </style>
        """,
        unsafe_allow_html=True,
    )


@contextmanager
def get_connection():
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    try:
        yield connection
        connection.commit()
    except Exception:
        connection.rollback()
        raise
    finally:
        connection.close()


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
apply_styles()

st.title("Movie Collection Manager")
st.caption("A considered home for the films worth remembering.")

with st.sidebar:
    st.markdown("## 🎬 Cinevault")
    st.caption("Your personal screening room")
    st.divider()
    page = st.radio("Choose a view", ["Dashboard", "Add Movie", "View Movies"], label_visibility="collapsed")
    sidebar_movies = fetch_movies()
    st.divider()
    st.caption("COLLECTION PULSE")
    st.metric("Titles", len(sidebar_movies))
    st.metric("Genres", len({movie['genre'] for movie in sidebar_movies}))

if page == "Add Movie":
    st.markdown('<div class="eyebrow">Expand the collection</div>', unsafe_allow_html=True)
    st.header("Add a movie")
    st.write("Capture the details now. The memories can do the rest.")
    with st.form("add_movie_form", clear_on_submit=True):
        movie_name = st.text_input("Movie Name", placeholder="e.g. Spirited Away")
        genre_choice = st.selectbox("Genre", GENRES + ["Other"])
        custom_genre = st.text_input("Custom Genre", placeholder="Optional") if genre_choice == "Other" else ""
        rating = st.number_input("Rating", min_value=0.0, max_value=10.0, value=5.0, step=0.1, help="Choose a rating from 0 to 10.")
        release_year = st.number_input("Release Year", min_value=1888, max_value=2100, value=2024, step=1)
        submitted = st.form_submit_button("Add Movie to Collection", type="primary", width="stretch")

    if submitted:
        genre = custom_genre.strip() if genre_choice == "Other" else genre_choice
        if not movie_name.strip() or not genre:
            st.error("Movie name and genre are required.")
        else:
            add_movie(movie_name, genre, rating, release_year)
            st.success(f'"{movie_name.strip()}" was added successfully.')

elif page == "View Movies":
    st.markdown('<div class="eyebrow">The archive</div>', unsafe_allow_html=True)
    st.header("Movie collection")
    movies = fetch_movies()
    if movies:
        search = st.text_input("Search your collection", placeholder="Search by title or genre", label_visibility="collapsed")
        filter_col, sort_col = st.columns(2)
        genre_filter = filter_col.selectbox("Filter by genre", ["All genres"] + sorted({movie["genre"] for movie in movies}))
        sort_order = sort_col.selectbox("Sort collection", ["Newest first", "Highest rated", "Title A-Z"])
        movie_frame = pd.DataFrame([dict(movie) for movie in movies])
        if search:
            searchable = movie_frame["movie_name"].str.contains(search, case=False, na=False) | movie_frame["genre"].str.contains(search, case=False, na=False)
            movie_frame = movie_frame[searchable]
        if genre_filter != "All genres":
            movie_frame = movie_frame[movie_frame["genre"] == genre_filter]
        if sort_order == "Highest rated":
            movie_frame = movie_frame.sort_values(["rating", "movie_name"], ascending=[False, True])
        elif sort_order == "Title A-Z":
            movie_frame = movie_frame.sort_values("movie_name")
        st.caption(f"Showing {len(movie_frame)} of {len(movies)} titles")
        st.dataframe(movie_frame, width="stretch", hide_index=True, column_config={"rating": st.column_config.NumberColumn("Rating", format="%.1f / 10")})
    else:
        st.info("No movies have been added yet.")

else:
    st.markdown('<div class="hero"><div class="eyebrow">Collection dashboard</div><h2>Tonight, what deserves a rewatch?</h2><p>See the shape of your collection at a glance.</p></div>', unsafe_allow_html=True)
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
        st.dataframe([dict(movie) for movie in highest_rated], width="stretch", hide_index=True)
    else:
        st.info("Add a movie to see the highest-rated title.")

    st.subheader("Genre-wise Summary")
    if summary:
        summary_frame = pd.DataFrame([dict(row) for row in summary])
        chart_col, table_col = st.columns([1.15, 1])
        with chart_col:
            st.bar_chart(summary_frame.set_index("genre")["movie_count"], color="#087f8c")
        with table_col:
            st.dataframe(summary_frame, width="stretch", hide_index=True)
    else:
        st.info("Add movies to see genre statistics.")