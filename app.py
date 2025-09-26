from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# "База" в памяти
forms = []
counter = 1


@app.route("/")
def index():
    return render_template("index.html", forms=forms)


@app.route("/create", methods=["GET", "POST"])
def create():
    global counter
    if request.method == "POST":
        new_form = {
            "id": counter,
            "name": request.form.get("name"),
            "email": request.form.get("email"),
            "category": request.form.get("category")
        }
        forms.append(new_form)
        counter += 1
        return redirect(url_for("index"))
    return render_template("create.html")


if __name__ == "__main__":
    app.run(debug=True)
