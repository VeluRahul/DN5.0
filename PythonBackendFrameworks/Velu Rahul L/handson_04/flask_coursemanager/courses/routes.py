from flask import Blueprint
from flask import jsonify
from flask import request


courses_bp = Blueprint(

    "courses",

    __name__,

    url_prefix="/api/courses"

)


courses=[]


@courses_bp.route("/",methods=["GET"])

def get_courses():

    return jsonify(courses)


@courses_bp.route("/",methods=["POST"])

def add_course():

    data=request.get_json()

    courses.append(data)

    return jsonify(data),201
