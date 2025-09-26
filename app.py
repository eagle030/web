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


@app.route("/view/<int:form_id>")
def view(form_id):
    form = next((f for f in forms if f["id"] == form_id), None)
    return render_template("view.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
