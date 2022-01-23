from flask import Flask, request, render_template

from functions import *

app = Flask(__name__)

@app.route("/movie/<title>")
def get_movie_by_title(title):
    return get_info_by_title(title)


app.run()