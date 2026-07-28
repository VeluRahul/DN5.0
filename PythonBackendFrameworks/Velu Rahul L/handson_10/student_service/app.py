from flask import Flask
from flask import jsonify
from flask import request

import requests

from requests.exceptions import ConnectionError

from database import db
from models import Student


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///student.db"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():

    db.create_all()


@app.route("/")
def home():

    return {

        "service":"Student Service"

    }


# ----------------------------
# GET ALL STUDENTS
# ----------------------------

@app.route(

    "/api/students",

    methods=["GET"]

)

def get_students():

    students = Student.query.all()

    return jsonify(

        [

            s.to_dict()

            for s in students

        ]

    )


# ----------------------------
# CREATE STUDENT
# ----------------------------

@app.route(

    "/api/students",

    methods=["POST"]

)

def create_student():

    data = request.get_json()

    student = Student(

        name=data["name"],

        email=data["email"]

    )

    db.session.add(student)

    db.session.commit()

    return jsonify(

        student.to_dict()

    ),201


# ----------------------------
# GET STUDENT
# ----------------------------

@app.route(

    "/api/students/<int:id>",

    methods=["GET"]

)

def get_student(id):

    student = Student.query.get(id)

    if not student:

        return jsonify(

            {

                "message":"Student Not Found"

            }

        ),404

    return jsonify(

        student.to_dict()

    )


# ----------------------------
# ENROLL STUDENT
# ----------------------------

@app.route(

    "/api/students/<int:id>/enroll",

    methods=["POST"]

)

def enroll_student(id):

    student = Student.query.get(id)

    if not student:

        return jsonify(

            {

                "message":"Student Not Found"

            }

        ),404

    data = request.get_json()

    course_id = data["course_id"]

    try:

        response = requests.get(

            f"http://localhost:5001/api/courses/{course_id}"

        )

    except ConnectionError:

        return jsonify(

            {

                "message":"Course Service Unavailable"

            }

        ),503

    if response.status_code != 200:

        return jsonify(

            {

                "message":"Course Not Found"

            }

        ),404

    return jsonify(

        {

            "message":"Enrollment Successful",

            "student":student.to_dict(),

            "course":response.json()

        }

    )


if __name__ == "__main__":

    app.run(

        port=5002,

        debug=True

    )
