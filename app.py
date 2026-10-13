
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/students")
def students():
    student_list = [
        "Ade",
        "Tunde",
        "Blessing",
        "Mary"
    ]

    return render_template(
        "students.html",
        students=student_list
    )


if __name__ == "__main__":
    app.run(debug=True)
