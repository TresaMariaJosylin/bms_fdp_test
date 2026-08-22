# Testing and Evidence

## Automated Testing

Run the database tests from the activated virtual environment:

```powershell
python -m unittest test_app.py -v
```

The tests verify database creation, valid record insertion, average rating, highest-rated movie, genre summary, invalid rating rejection, favorites, update/delete behavior, restore behavior, and login credentials. Tests use a temporary database and do not modify the project collection.

## Login

The default local credentials are `admin` / `movie123`. For a different account, set `MOVIE_APP_USERNAME` and `MOVIE_APP_PASSWORD` before starting Streamlit.

## Manual Testing Checklist

| Test | Action | Expected result | Evidence |
| --- | --- | --- | --- |
| Database creation | Start the Streamlit app | `movies.db` and `movies` table are created | Screenshot of SQLite database/table |
| Login | Enter valid credentials | Dashboard opens | Screenshot of dashboard after sign in |
| Login validation | Enter an incorrect password | Error message appears and access is denied | Screenshot of login error |
| Add record | Submit a valid movie | Success message appears and record is stored | Screenshot of success message |
| Required validation | Submit without a movie name or genre | Validation error appears | Screenshot of error |
| View records | Open `View Movies` | Stored records appear in a table | Screenshot of movie collection |
| Search and filter | Search a title and select a genre | Matching records are shown | Screenshot of filtered table |
| Edit record | Open `Manage Movies`, change details, and save | Updated values appear in the collection | Screenshot of updated record |
| Delete record | Select a movie, confirm deletion, and delete | Movie is removed from the collection | Screenshot of delete confirmation/result |
| Export records | Filter the collection and select `Download CSV` | A CSV file downloads with the visible records | Screenshot of export control |
| Favorite movie | Mark a movie as a favorite | Favorite flag and favorites filter update | Screenshot of favorite collection |
| Movie picker | Select `Pick a movie for tonight` | An active movie recommendation appears | Screenshot of recommendation |
| Summary calculation | Open `Dashboard` | Total and average rating are correct | Screenshot of dashboard metrics |
| Highest rated | Add a high-rated movie | Highest-rated title appears | Screenshot of highest-rated section |
| Genre summary | Add movies across genres | Counts and chart update correctly | Screenshot of chart and table |
| Git branch | Run `git branch --all` | `feature/category-summary` is present | Screenshot of branch |
| Git push | Run `git push` | Push completes successfully | Screenshot of terminal output |

## Manual Test Data

| Movie | Genre | Rating | Year |
| --- | --- | ---: | ---: |
| Inception | Science Fiction | 8.8 | 2010 |
| The Dark Knight | Action | 9.0 | 2008 |
| Toy Story | Comedy | 8.3 | 1995 |