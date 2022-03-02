from distutils.log import info
import os
from unicodedata import name
import flask
from flask import Flask, redirect, render_template, request, url_for, session, flash
import json
import requests
import random
from enum import unique
from flask_sqlalchemy import SQLAlchemy
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())


app = flask.Flask(__name__)
app.secret_key = "Secret key"

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


BASE_URL = "https://api.themoviedb.org/3"

query_params = {"api_key": os.getenv("API_KEY")}


top_films = requests.get(f"{BASE_URL}/movie/popular", params=query_params)
search_url = requests.get(f"{BASE_URL}/search/movie", params=query_params)

data = top_films.json()

for pop_movie in data["results"]:
    Movie_title = pop_movie["title"]
    brief_summary = pop_movie["overview"]
    Release_date = pop_movie["release_date"]
    rating = pop_movie["vote_average"]
    genres = pop_movie["genre_ids"]
    movie_image = pop_movie["poster_path"]
    movie_id = pop_movie["id"]


@app.route("/")
@app.route("/home", methods=["GET", "POST"])
def home():
    #  if flask.request.method == "POST":
    #     udata = flask.request.form
    #     new_user = Users(
    #        name=udata["name"],
    #       movieID=udata["movieID"],
    #      movideRating=udata["movieRating"],
    #     comments=udata["comments"],
    # )
    # db.session.add(new_user)
    # db.session.commit()

    #   user = Users.query.all()
    # num_users = len(user)
    flash("You are not logged in. Please log in if you have an account.")
    return render_template("home.html", data=data)


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        session["email"] = email
        session["password"] = password
        flash("Login successful.")
        return redirect(url_for("register"))
    if "user" in session:
        flash("User logged in!")
        return redirect(url_for("home"))
    else:
        if "email" in session:
            email = session["email"]
        if "password" in session:
            password = session["password"]
        return render_template("login.html", email=email, password=password)


@app.route("/register", methods=["POST", "GET"])
def register():

    email = None
    password = None

    if "user" in session:
        user = session["user"]
        flash("You are not logged in. Please make an account.")
        return render_template("register.html")

    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        session["email"] = email
        session["password"] = password
        flash("User Info Saved! Please log into your account")
        return redirect(url_for("login"))

    else:
        flash("You are not logged in. Please make an account.")
        return render_template("register.html")


@app.route("/search")
def search():
    return render_template("search.html", data=data)


@app.route("/trivia")
def trivia():
    return render_template("trivia.html", data=data)


@app.route("/trailers")
def trailers():
    return render_template("trailers.html", data=data)


@app.route("/logout")
def logout():

    if "user" in session:
        user = session["user"]
    flash("You have been successfully logged out!", "info")
    session.pop("user", None)
    session.pop("fname", None)
    session.pop("lname", None)
    session.pop("uname", None)
    session.pop("psw", None)

    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(
        host=os.getenv("IP", "0.0.0.0"), port=int(os.getenv("PORT", 8080)), debug=True
    )
