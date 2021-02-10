import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_titles")
def get_titles():
    titles = list(mongo.db.titles.find())
    return render_template("titles.html", titles=titles)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    titles = list(mongo.db.titles.find({"$text": {"$search": query}}))
    return render_template("titles.html", titles=titles)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # puts the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Thanks for Joining!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in mongo
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensures that hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                        session["user"] = request.form.get("username").lower()
                        flash("Nice to have you, {}!".format(
                            request.form.get("username")))
                        return redirect(url_for(
                            "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Something went wrong please check your Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("See you soon!")
    session.pop("user")
    return redirect(url_for("login"))


# I have recoded and added mu own lines of code here
@app.route("/add_title", methods=["GET", "POST"])
def add_title():
    if request.method == "POST":
        is_urgent = "on" if request.form.get("is_urgent") else "off"
        title = {
            "genre_name": request.form.get("genre_name"),
            "title_name": request.form.get("title_name"),
            "authors_description": request.form.get("authors_description"),
            "published_by": request.form.get("published_by"),
            "child_friendly": request.form.get("child_friendly"),
            "year_dated": request.form.get("year_dated"),
            "page_numbers": request.form.get("page_numbers"),
            "is_urgent": is_urgent,
            "due_date": request.form.get("due_date"),
            "created_by": session["user"]
        }
        mongo.db.titles.insert_one(title)
        flash("Title Successfully Added")
        return redirect(url_for("get_titles"))

    genres = mongo.db.genres.find().sort("genre_name", 1)
    return render_template("add_title.html", genres=genres)


# I have recoded and added mu own lines of code here
@app.route("/edit_title/<title_id>", methods=["GET", "POST"])
def edit_title(title_id):
    if request.method == "POST":
        is_urgent = "on" if request.form.get("is_urgent") else "off"
        submit = {
            "genre_name": request.form.get("genre_name"),
            "title_name": request.form.get("title_name"),
            "authors_description": request.form.get("authors_description"),
            "published_by": request.form.get("published_by"),
            "child_friendly": request.form.get("child_friendly"),
            "year_dated": request.form.get("year_dated"),
            "page_numbers": request.form.get("page_numbers"),
            "is_urgent": is_urgent,
            "due_date": request.form.get("due_date"),
            "created_by": session["user"]
        }
        mongo.db.title.update({"_id": ObjectId(title_id)}, submit)
        flash("You've Include a New Title!")

    title = mongo.db.titles.find_one({"_id": ObjectId(title_id)})
    genres = mongo.db.genres.find().sort("genre_name", 1)
    return render_template("edit_title.html", title=title, genres=genres)


@app.route("/delete_title/<title_id>")
def delete_title(title_id):
    mongo.db.titles.remove({"_id": ObjectId(title_id)})
    flash("Title Successfully Removed!")
    return redirect(url_for("get_titles"))


@app.route("/get_genres")
def get_genres():
    genres = list(mongo.db.genres.find().sort("genre_name", 1))
    return render_template("genres.html", genres=genres)


@app.route("/add_genre", methods=["GET", "POST"])
def add_genre():
    if request.method == "POST":
        genre = {
            "genre_name": request.form.get("genre_name")
        }
        mongo.db.genres.insert_one(genre)
        flash("New Genre Added")
        return redirect(url_for("get_genres"))

    return render_template("add_genre.html")


@app.route("/edit_genre/<genre_id>", methods=["GET", "POST"])
def edit_genre(genre_id):
    if request.method == "POST":
        submit = {
            "genre_name": request.form.get("genre_name")
        }
        mongo.db.genres.update({"_id": ObjectId(genre_id)}, submit)
        flash("Genre Successfully Updated")
        return redirect(url_for("get_genres"))

    genre = mongo.db.genres.find_one({"_id": ObjectId(genre_id)})
    return render_template("edit_genre.html", genre=genre)


@app.route("/delete_genre/<genre_id>")
def delete_genre(genre_id):
    mongo.db.genres.remove({"_id": ObjectId(genre_id)})
    flash("Genre Successfully Removed")
    return redirect(url_for("get_genres"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)