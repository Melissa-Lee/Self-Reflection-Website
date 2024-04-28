# Implement a self-reflection form to store the date in SQLite datatabase

from cs50 import SQL
from flask import Flask, redirect, render_template, request

app = Flask(__name__)

db = SQL("sqlite:///reflections.db")

def create_reflections_table():
    db.execute("""
        CREATE TABLE IF NOT EXISTS reflections (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            category TEXT NOT NULL,
            content TEXT NOT NULL
        );
    """)

create_reflections_table()  # Call this at the beginning of your application.


@app.route("/")
def main():
    reflections = db.execute("SELECT * FROM reflections")
    return render_template("index.html", reflections=reflections)

@app.route("/remove", methods=["POST"])
def remove():
    # Forget record
    id = request.form.get("id")
    if id:
        db.execute("DELETE FROM reflections WHERE id = ?", id)
    return redirect("/records")


@app.route("/add_reflection", methods=["POST"])
def add_reflections():
    date = request.form["date"]
    category = request.form["category"]
    content = request.form["content"]
    # Remember reflections
    db.execute("INSERT INTO reflections (date, category, content) VALUES(?, ?, ?)", date, category, content)
    # Confirm reflections
    return redirect("/records")

@app.route("/records")
def records():
    reflections = db.execute("SELECT * FROM reflections")
    return render_template("records.html", reflections=reflections)

if __name__ == "__main__":
    app.run(debug=True)
