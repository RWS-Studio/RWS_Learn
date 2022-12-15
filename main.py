from flask import Flask, render_template, url_for, request, redirect

from models import Grade

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/grade/new')
def new_grade():

    # get if the form is submitted or not
    try:
        form = request.args["form"]
    except Exception:
        form = False

    # if form == submitted, create grade with args in url and then redirect on the home
    if form:
        value = request.args["value"]
        factor = request.args["factor"]
        subject = request.args["subject"]
        description = request.args["description"]

        new_grade = Grade(value=value, factor=factor, subject=subject, description=description)
        return render_template('add_grade.html', grade=new_grade)
        # return redirect('/')
    else:  # if form != submitted show template
        return render_template('add_grade.html', grade="")


if __name__ == "__main__":
    app.run(debug=True)
