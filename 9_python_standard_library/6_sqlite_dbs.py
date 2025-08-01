# SQLite is a a light-weight database
import sqlite3
import json
from pathlib import Path

movies = json.loads(Path("9_python_standard_library/ecommerce/movies.json").read_text())
print(movies)


# with sqlite3.connect("9_python_standard_library/ecommerce/db.sqlite3") as conn:
#     command = "INSERT INTO Movies VALUES(?,?,?)"
#     for movie in movies:
#         conn.execute(command,tuple(movie.values()))
#     conn.commit()

with sqlite3.connect("9_python_standard_library/ecommerce/db.sqlite3") as conn:
    command = "SELECT * FROM Movies"
    cursor = conn.execute(command)

    # all_movies = cursor.fetchall()

    for row in cursor:
        print(row)
    conn.commit()
