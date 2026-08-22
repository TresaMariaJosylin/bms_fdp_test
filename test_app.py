import sqlite3
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import app


class MovieDatabaseTests(unittest.TestCase):
    def setUp(self):
        self.database_file = tempfile.NamedTemporaryFile(suffix=".db", delete=False)
        self.database_file.close()
        self.database_path = Path(self.database_file.name)
        self.path_patcher = patch.object(app, "DATABASE_PATH", self.database_path)
        self.path_patcher.start()
        app.initialize_database()

    def tearDown(self):
        self.path_patcher.stop()
        self.database_path.unlink(missing_ok=True)

    def test_add_and_fetch_movie(self):
        app.add_movie("Inception", "Science Fiction", 8.8, 2010)

        movies = app.fetch_movies()

        self.assertEqual(len(movies), 1)
        self.assertEqual(movies[0]["movie_name"], "Inception")

    def test_statistics(self):
        app.add_movie("Inception", "Science Fiction", 8.8, 2010)
        app.add_movie("The Dark Knight", "Action", 9.0, 2008)

        self.assertAlmostEqual(app.fetch_average_rating(), 8.9)
        self.assertEqual(app.fetch_highest_rated()[0]["movie_name"], "The Dark Knight")
        self.assertEqual(app.fetch_genre_summary()[0]["movie_count"], 1)

    def test_invalid_rating_is_rejected(self):
        with self.assertRaises(sqlite3.IntegrityError):
            app.add_movie("Invalid", "Drama", 11, 2020)


if __name__ == "__main__":
    unittest.main()