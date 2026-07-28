from flask import Blueprint
from flask import jsonify
from flask import request

courses_bp = Blueprint(
    "courses",
    __name__,
    url_prefix="/api/courses"
)

courses = [
    {
        "id": 1,
        "name": "Data Structures",
        "code": "CS101",
        "credits": 4
    },
    {
        "id": 2,
        "name": "Database Management",
        "code": "CS102",
        "credits": 3
    }
]


def make_response_json(data, status_code):

    return jsonify({
        "status": "success",
        "data": data
    }), status_code


@courses_bp.route("/", methods=["GET"])
def get_courses():

    return make_response_json(courses, 200)


@courses_bp.route("/", methods=["POST"])
def add_course():

    data = request.get_json()

    if data is None:

        return jsonify({
            "status": "error",
            "message": "Request body must be JSON"
        }), 400

    required_fields = [
        "name",
        "code",
        "credits"
    ]

    for field in required_fields:

        if field not in data:

            return jsonify({
                "status": "error",
                "message": f"{field} is required"
            }), 400

    new_course = {
        "id": len(courses) + 1,
        "name": data["name"],
        "code": data["code"],
        "credits": data["credits"]
    }

    courses.append(new_course)

    return make_response_json(new_course, 201)


@courses_bp.route("/<int:course_id>", methods=["GET"])
def get_course(course_id):

    for course in courses:

        if course["id"] == course_id:

            return make_response_json(course, 200)

    return jsonify({
        "status": "error",
        "message": "Course not found"
    }), 404


@courses_bp.route("/<int:course_id>", methods=["PUT"])
def update_course(course_id):

    data = request.get_json()

    for course in courses:

        if course["id"] == course_id:

            course["name"] = data.get(
                "name",
                course["name"]
            )

            course["code"] = data.get(
                "code",
                course["code"]
            )

            course["credits"] = data.get(
                "credits",
                course["credits"]
            )

            return make_response_json(course, 200)

    return jsonify({
        "status": "error",
        "message": "Course not found"
    }), 404


@courses_bp.route("/<int:course_id>", methods=["DELETE"])
def delete_course(course_id):

    for course in courses:

        if course["id"] == course_id:

            courses.remove(course)

            return jsonify({
                "status": "success",
                "message": "Course deleted successfully"
            }), 200

    return jsonify({
        "status": "error",
        "message": "Course not found"
    }), 404
