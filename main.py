from database.grades_manager import GradesManager
from database.subjects_manager import SubjectsManager
from models import Grade, Subject, SoftwareVersion

from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)


@app.route('/')
def index():
    # shows list of all grades + links to view them
    # in next version : graphs

    # version control
    try:
        is_update_available = request.args["update-available"]
    except Exception:
        is_update_available = ""

    all_subjects = SubjectsManager().view_subject()
    subjects_and_grades = {}
    for i in all_subjects:
        if list(i)[0] != "sqlite_sequence":
            subjects_and_grades[list(i)[0]] = []
    for subject in subjects_and_grades:
        counter = 1
        loop = True
        while loop:
            try:
                _grade = GradesManager().view_grade(subject, counter)
                _grade["id"] = counter
                subjects_and_grades[subject].append(_grade)
            except IndexError:
                loop = False
            counter += 1
    return render_template('index.html', subjects=subjects_and_grades, is_update_available=is_update_available)


@app.route('/version')
def version():
    version = SoftwareVersion()
    is_new_version_available = version.get_if_new_version()
    return render_template('version.html', is_update_available=is_new_version_available)


@app.route('/subject/new')
def new_subject():

    # get if the form is submitted or not
    try:
        form = request.args["form"]
    except Exception:
        form = False

    if form:
        subject_name = request.args["subject"]
        new_subject = Subject(subject_name)
        SubjectsManager().add_subject(subject_name)
        print("Send")
        return redirect('/')

    return render_template("subjects/add_subject.html")


@app.route('/subject/update')
def update_subject():
    # required : name of the subject in the url -> /subject/view?subject=[subject]
    try:
        form = request.args["form"]
    except Exception:
        form = False

    subject = request.args['subject']

    if form:
        new_name = request.args['new-name']

        SubjectsManager().update_subject(old_name=subject, new_name=new_name)
        return redirect('/')

    all_subjects = SubjectsManager().view_subject()
    subject_from_db = ""
    for i in all_subjects:
        if list(i)[0] == subject:
            subject_from_db = list(i)[0]
    return render_template('subjects/update_subject.html', subject=subject_from_db)


@app.route('/subject/delete')
def delete_subject():
    # required : name of the subject in the url -> /subject/view?subject=[subject]
    # template : asks user before deleting the subject
    try:
        form = request.args["form"]
    except Exception:
        form = False

    subject = request.args['subject']

    if form:
        confirmation = request.args['confirm']
        if confirmation == "on":
            SubjectsManager().del_subject(subject=subject)
            return redirect('/')

    return render_template('subjects/delete_subject.html')


@app.route('/subject/view')
def view_subject():
    # required : name of the subject in the url -> /subject/view?subject=[subject]
    subject_param = request.args['subject']
    all_subjects = SubjectsManager().view_subject()
    subject = ""
    for i in all_subjects:
        if list(i)[0] == subject_param:
            subject = list(i)[0]

    return render_template('subjects/view_subject.html', subject=subject)


@app.route('/grade/new')
def new_grade():

    # get if the form is submitted or not
    try:
        form = request.args["form"]
    except Exception:
        form = False

    # for <select> in the template
    all_subjects = SubjectsManager().view_subject()
    subjects = []
    for i in all_subjects:
        if list(i)[0] != "sqlite_sequence":
            subjects.append(list(i)[0])

    # if form == submitted, create grade with args in url and then redirect on the home
    if form:
        value = request.args["value"]
        value_max = request.args["value-max"]
        factor = request.args["factor"]
        subject = request.args["subject"]
        description = request.args["description"]

        new_grade = Grade(value=value, value_max=value_max, factor=factor, subject=subject, description=description)

        # value max is not required
        GradesManager().add_grade(subject, float(value), float(factor), description, int(value_max))

        return redirect('/')
    else:  # if form != submitted show template
        return render_template('grades/add_grade.html', subjects=subjects)


@app.route('/grade/update')
def update_grade():
    # required : id of the grade in the url -> /grade/update?id=[id] + subject
    try:
        form = request.args["form"]
    except Exception:
        form = False

    grade_id = request.args['id']
    subject = request.args['subject']

    if form:
        new_grade = request.args['new-value']
        new_value_max = request.args['new-value-max']
        new_factor = request.args['new-factor']
        new_subject = request.args['new-subject']
        new_description = request.args['new-description']

        GradesManager().update_grade(new_subject, float(new_grade), float(new_factor), new_description, grade_id,
                                        int(new_value_max))
        return redirect('/')

    grade = GradesManager().view_grade(subject=subject, grade_id=grade_id)

    return render_template('grades/update_grade.html', grade=grade, subject=subject)


@app.route('/grade/delete')
def delete_grade():
    # required : id of the grade in the url -> /grade/delete?id=[id]
    # template : asks user before deleting the grade
    try:
        form = request.args["form"]
    except Exception:
        form = False

    grade_id = request.args['id']
    subject = request.args['subject']

    if form:
        confirmation = request.args['confirm']
        if confirmation == "on":
            GradesManager().del_grade(subject=subject, grade_id=grade_id)
            return redirect('/')

    return render_template('grades/delete_grade.html')


@app.route('/grade/view')
def view_grade():
    # required : id of the grade in the url -> /grade/view?id=[id] + subject
    grade_id = request.args['id']
    subject = request.args['subject']
    grade = GradesManager().view_grade(subject=subject, grade_id=grade_id)
    return render_template('grades/view_grade.html', grade=grade, subject=subject)


if __name__ == "__main__":
    app.run()
