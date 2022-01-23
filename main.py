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

app.run()