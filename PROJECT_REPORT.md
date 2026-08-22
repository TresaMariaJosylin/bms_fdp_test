# Movie Collection Manager Project Report

## 1. Problem Statement

A movie enthusiast has a large personal collection across genres such as Action, Comedy, Drama, Thriller, and Science Fiction. Manual management makes it difficult to store movie details, browse titles, find highly rated movies, track favorites, and understand genre-wise statistics.

## 2. Objective

Build a simple, attractive, and reliable Movie Collection Manager using Python, Streamlit, SQLite, a virtual environment, and Git. The application provides session-based login and a complete interface for maintaining and analyzing movie records.

## 3. Technology Stack

- **Python 3.12** for application logic and automated tests
- **Streamlit** for the interactive web interface
- **SQLite** for persistent local storage in `movies.db`
- **Python virtual environment** in `.venv`
- **Git and GitHub** for version control and branch publishing
- **Pandas** for tables and collection charts

## 4. Features Implemented

### Authentication

- Login page with username and password
- Session-based authentication using Streamlit session state
- Logout button in the sidebar
- Failed-login error message
- Configurable credentials through `MOVIE_APP_USERNAME` and `MOVIE_APP_PASSWORD`
- Default local credentials documented in [README.md](README.md)

### Dashboard

- Total movie count
- Average rating for active movies
- Favorite movie count
- Highest-rated active movie or movies
- Genre-wise movie count and average rating
- Genre-count bar chart
- Release-year trend chart
- Random active-movie recommendation using **Pick a movie for tonight**

### Add Movie

- Movie name, genre, rating, and release year inputs
- Built-in genres: Action, Comedy, Drama, Thriller, and Science Fiction
- Custom genre support
- Rating validation from 0 to 10
- Release year validation from 1888 to 2100
- Favorite checkbox
- Required-field validation and success confirmation

### View Movies

- Full collection table with movie ID, name, genre, rating, year, status, and favorite fields
- Search by title or genre
- Filter by genre
- Favorites-only filter
- Sort by newest, highest rated, or title A-Z
- Visible-record count
- CSV download of the filtered collection

### Manage Movies

- Select any stored movie by title, year, and rating
- Edit movie name, genre, rating, release year, and favorite state
- Save changes to SQLite
- Deactivate a movie with confirmation
- Preserve deactivated records with `Inactive` status
- Restore inactive movies to `Active`
- Keep inactive records visible while excluding them from active statistics

### Visual Design

- Custom teal, coral, cream, and dark-green theme
- DM Sans and Space Grotesk typography
- Styled dashboard hero section
- Sidebar branding and collection pulse metrics
- Responsive Streamlit columns and full-width tables

## 5. Application Workflow

1. The user opens the Streamlit application.
2. The application creates or migrates `movies.db` and the `movies` table.
3. The user signs in.
4. The user selects Dashboard, Add Movie, View Movies, or Manage Movies.
5. Movie actions are validated and stored using parameterized SQLite queries.
6. Dashboard values and charts are calculated from active SQLite records.
7. The user can export the visible collection as CSV or sign out.

## 6. Database Design

The application uses a local SQLite database named `movies.db`. The `movies` table contains:

| Column | Type | Purpose and constraints |
| --- | --- | --- |
| `movie_id` | `INTEGER` | Auto-incrementing primary key |
| `movie_name` | `TEXT` | Required movie title |
| `genre` | `TEXT` | Required genre |
| `rating` | `REAL` | Required value from 0 to 10 |
| `release_year` | `INTEGER` | Required value from 1888 onward |
| `status` | `TEXT` | `Active` or `Inactive`, default `Active` |
| `is_favorite` | `INTEGER` | `0` or `1`, default `0` |

The application automatically migrates older databases by adding missing `status` and `is_favorite` columns with safe defaults. Full schema and queries are documented in [DATABASE_DESIGN.md](DATABASE_DESIGN.md).

## 7. Project Files

| File | Description |
| --- | --- |
| [app.py](app.py) | Streamlit interface, authentication, SQLite operations, charts, and workflows |
| [test_app.py](test_app.py) | Automated database and authentication tests |
| [requirements.txt](requirements.txt) | Streamlit dependency specification |
| [REQUIREMENTS.md](REQUIREMENTS.md) | Requirements analysis and acceptance criteria |
| [DATABASE_DESIGN.md](DATABASE_DESIGN.md) | SQLite schema and feature queries |
| [TESTING.md](TESTING.md) | Automated and manual testing checklist |
| [PROMPTS_USED.md](PROMPTS_USED.md) | Prompts used during development |
| [PROJECT_REPORT.md](PROJECT_REPORT.md) | Complete project report |
| [README.md](README.md) | Setup, login, and execution instructions |

## 8. Testing Performed

Automated testing is implemented with Python `unittest`. The suite contains **6 passing tests** covering:

- Adding and fetching a movie
- Average rating and highest-rated movie
- Genre summary
- Invalid rating rejection
- Editing, inactive status, and restoring a movie
- Login success and failed login
- Favorite record storage

Run the tests with:

```powershell
python -m unittest test_app.py -v
```

Additional validation performed:

- `app.py` and `test_app.py` compile successfully
- SQLite constraints were validated
- Streamlit server returned HTTP `200`
- `git diff --check` completed without formatting errors

## 9. Screenshot Evidence

Capture screenshots while the app is running at `http://localhost:8501` and insert them in this section before submission.

| Evidence | What to capture | Suggested filename |
| --- | --- | --- |
| Database created | SQLite browser or terminal showing `movies.db` and `movies` table | `01-database-created.png` |
| Login page | Login screen and successful dashboard access | `02-login.png` |
| Record added | Add Movie page showing success message | `03-record-added.png` |
| View records | View Movies table with stored records and status | `04-view-records.png` |
| Search/filter | Filtered or favorites-only collection | `05-search-filter.png` |
| Edit record | Manage Movies page after saving changes | `06-edit-record.png` |
| Inactive record | Record shown with `Inactive` status after deactivation | `07-inactive-record.png` |
| Dashboard summary | Total movies, average rating, favorites, and highest-rated movie | `08-dashboard-summary.png` |
| Genre summary | Genre chart and summary table | `09-genre-summary.png` |
| Movie picker | Random active-movie recommendation message | `10-movie-picker.png` |
| CSV export | View Movies page with Download CSV control | `11-csv-export.png` |
| Git branch | Terminal showing `feature/category-summary` | `12-git-branch.png` |
| Git push | Successful `git push` output | `13-git-push.png` |

The full expected-result checklist is available in [TESTING.md](TESTING.md).

## 10. Prompts Used

All development prompts are recorded in [PROMPTS_USED.md](PROMPTS_USED.md), including requirements analysis, database design, application development, UI enhancement, management actions, inactive status, authentication, export, favorites, testing, documentation, and Git publishing.

## 11. Git Operations

- Repository initialized and cloned from GitHub
- Source code and documentation committed on `main`
- Branch created: `feature/category-summary`
- Feature changes committed and pushed to the feature branch
- Feature branch fast-forwarded into `main`
- Both branches pushed to the GitHub repository

Repository: [TresaMariaJosylin/bms_fdp_test](https://github.com/TresaMariaJosylin/bms_fdp_test)

## 12. Learning Outcomes

- Designed a relational SQLite database with integrity constraints
- Added safe schema migration for existing local data
- Connected Python and Streamlit to persistent SQLite storage
- Built authentication and session-based access control
- Implemented create, read, update, soft-delete, restore, and export workflows
- Used SQL aggregation for ratings and genre statistics
- Built charts and filtering with Pandas and Streamlit
- Created repeatable automated tests with `unittest`
- Practiced virtual-environment setup and Git branching and publishing

## 13. Conclusion

The completed Movie Collection Manager meets the original business requirements and extends them with authentication, favorites, filtering, export, soft deletion, restoration, charts, recommendations, automated tests, and complete project documentation.
