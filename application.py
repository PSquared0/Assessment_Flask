from flask import Flask, render_template, request, redirect
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)


# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

@app.route("/application")
def index():

    return render_template("application-form.html")


    # Alte  rnately, we could make this a Jinja template in `templates/`
    # and return that result of rendering this, like:
    #
    # return render_template("index.html")

@app.route("/application-response.html", methods = ['POST'])
def response():
    firstname = request.form.get("firstname")
    lastname = request.form.get("lastname")
    position = request.form.get("position")
    desiredsalary = request.form.get("desiredsalary")

    print request.form
    return render_template("application-response.html",
                            firstname=firstname,
                            lastname=lastname,
                            position=position,
                            desiredsalary=desiredsalary,
                            )

if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")

