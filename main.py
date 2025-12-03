from flask import Flask, render_template, request
import db

app = Flask(__name__)
app.secret_key = "revmovies"


@app.route("/")
def Home():
    movieData = db.GetAllMovies()
    return render_template("movies.html", movies=movieData)


app.run(debug=True, port=5000)
