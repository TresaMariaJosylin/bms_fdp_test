# Prompts Used During Development

The following prompts were used while developing this project.

## Prompt 1 - Requirements Analysis

Analyze the Movie Collection Manager business scenario. Identify the objective, technology constraints, functional requirements, database fields, expected workflow, documentation requirements, screenshot evidence, and Git assessment requirements.

## Prompt 2 - Database Design

Design a SQLite database named `movies.db` with a `movies` table containing `movie_id`, `movie_name`, `genre`, `rating`, and `release_year`. Include suitable data types, constraints, and SQL queries for viewing movies, average rating, highest-rated movies, and genre-wise summary.

## Prompt 3 - Application Development

Build a Python Streamlit Movie Collection Manager connected to SQLite. Implement movie entry, collection browsing, average rating, highest-rated movie, genre-wise statistics, validation, and a usable interface.

## Prompt 4 - Interface Enhancement

Improve the Streamlit application visually and add useful collection tools such as custom styling, dashboard metrics, charts, search, genre filtering, sorting, and custom genre entry while preserving the SQLite requirements.

## Prompt 5 - Movie Management

Add edit and update functionality to the Movie Collection Manager. Add a Manage Movies page where users can select a movie, change its title, genre, rating, and release year, and save the changes.

## Prompt 6 - Inactive Record Handling

When a user deletes a movie, do not permanently remove the database record. Add an `Active` or `Inactive` status, show inactive records in the collection, exclude inactive records from active statistics, and provide a restore option. Migrate existing databases safely.

## Prompt 7 - Authentication and Export

Add a login page with session-based authentication, logout, configurable credentials, and CSV export for the visible movie collection. Keep the existing Streamlit and SQLite functionality working.

## Prompt 8 - Personal Collection Features

Add favorite movies, a favorites-only filter, a favorite count, a random active-movie recommendation, and a release-year trend chart. Update the database migration, tests, and documentation.

## Prompt 9 - Testing and Submission

Create testing documentation, automated database tests, setup instructions, and Git evidence for the Movie Collection Manager submission.

## Prompt 10 - Final Documentation and Publishing

Create a project report covering the problem statement, features, database design, screenshots, prompts used, testing, and learning outcomes. Run all tests, verify the app, commit the changes, and push both `main` and `feature/category-summary` branches.