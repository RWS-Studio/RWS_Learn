
from flask import Flask, render_template, url_for, request, redirect

from models import Grade

app = Flask(__name__)


@app.route('/')
def index():
    # shows list of all grades + links to view them
    # in next version : graphs
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
        value_max = request.args["value-max"]
        factor = request.args["factor"]
        subject = request.args["subject"]
        description = request.args["description"]

        new_grade = Grade(value=value, value_max=value_max, factor=factor, subject=subject, description=description)


        # here code for add the grade in the db


        return render_template('add_grade.html', grade=new_grade)
    else:  # if form != submitted show template
        return render_template('add_grade.html', grade="")


@app.route('/grade/update')
def update_grade():
    # required : id of the grade in the url -> /grade/update?id=[id]
    pass


@app.route('/grade/delete')
def delete_grade():
    # required : id of the grade in the url -> /grade/delete?id=[id]
    # template : asks user before deleting the grade
    pass


@app.route('/grade/view')
def view_grade():
    # required : id of the grade in the url -> /grade/view?id=[id]
    pass


if __name__ == "__main__":
    app.run(debug=True)
