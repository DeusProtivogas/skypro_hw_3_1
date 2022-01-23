from flask import Flask, request, render_template, jsonify

from functions import *

app = Flask(__name__)

@app.route("/movie/<title>")
def get_movie_by_title(title):
    return get_info_by_title(title)

@app.route("/movie/<year1>/to/<year2>")
def films_in_interval(year1, year2):
    films = get_films_in_interval(year1, year2)
    return jsonify(films)


@app.route("/rating/children")
def rating_children():
    return jsonify(get_films_by_rating(['G']))

@app.route("/rating/family")
def rating_family():
    return jsonify(get_films_by_rating(['G', 'PG', 'PG-13']))

@app.route("/rating/adult")
def rating_adult():
    return jsonify(get_films_by_rating(['R', 'NC-17']))

@app.route("/genre/<genre>")
def ten_freshest_films_in_genre(genre):
    return jsonify(get_films_by_genre(genre))


app.run()