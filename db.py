import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash


def GetDB():

    # Connect to the database and return the connection object
    db = sqlite3.connect(".database/revmovies.db")
    db.row_factory = sqlite3.Row

    return db


def GetAllMovies():

    # Connect, query all guesses and then return the data
    db = GetDB()
    movies = db.execute("SELECT * FROM Movies").fetchall()
    db.close()
    return movies
