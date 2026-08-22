# Movie Collection Manager

This project is a Python and Streamlit application for managing a personal movie collection with SQLite.

Project workflow:

1. Requirements analysis: [REQUIREMENTS.md](REQUIREMENTS.md)
2. Database design: [DATABASE_DESIGN.md](DATABASE_DESIGN.md)
3. Application development
4. Testing and evidence: [TESTING.md](TESTING.md)
5. Documentation: [PROJECT_REPORT.md](PROJECT_REPORT.md) and [PROMPTS_USED.md](PROMPTS_USED.md)
6. Git operations

## Run Locally

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

The application opens at `http://localhost:8501` and creates `movies.db` automatically.

Default local login: username `admin`, password `movie123`. Set `MOVIE_APP_USERNAME` and `MOVIE_APP_PASSWORD` to use custom credentials.

Run automated tests with:

```powershell
python -m unittest test_app.py -v
```