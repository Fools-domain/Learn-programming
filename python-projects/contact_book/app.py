from flask import Flask, redirect, render_template, request, url_for

from database import init_db
from models.contact import Contact

app = Flask(__name__)
init_db()


@app.route("/")
def home():
    contacts = Contact.get_all()
    return render_template("index.html", contacts=contacts)


@app.route("/add", methods=["GET", "POST"])
def add_contact():
    if request.method == "POST":
        name = request.form["name"]
        phone = request.form["phone"]
        email = request.form["email"]
        Contact(name=name, phone=phone, email=email).save()
        return redirect(url_for("home"))
    return render_template("add.html")


@app.route("/delete", methods=["GET", "POST"])
def delete_contact():
    if request.method == "POST":
        contact_id = request.form["id"]
        Contact.delete_contact(id=contact_id)
        return redirect(url_for("home"))
    return render_template("delete.html")


@app.route("/search", methods=["GET", "POST"])
def search():
    results = []
    if request.method == "POST":
        query = request.form["name"]
        results = Contact.search(query=query)
    return render_template("search.html", results=results)


if __name__ == "__main__":
    app.run(debug=True)
