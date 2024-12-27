from flask import render_template, request, flash
from app import app

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/greet", methods=["POST", "GET"])
def greet():
    flash("Hi " + str(request.form['name_input']) + ", great to see you!")
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0')