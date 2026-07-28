from flask import Flask
from flask import request
from flask import Response

import requests

app = Flask(__name__)


COURSE_SERVICE = "http://localhost:5001"

STUDENT_SERVICE = "http://localhost:5002"


# --------------------------------------
# HOME
# --------------------------------------

@app.route("/")

def home():

    return {

        "service":"API Gateway"

    }


# --------------------------------------
# COURSE SERVICE ROUTES
# --------------------------------------

@app.route(

    "/api/courses",

    methods=["GET","POST"]

)

def courses():

    url = COURSE_SERVICE + "/api/courses"

    response = requests.request(

        method=request.method,

        url=url,

        headers=request.headers,

        json=request.get_json(silent=True)

    )

    return Response(

        response.content,

        status=response.status_code,

        content_type=response.headers.get(

            "Content-Type",

            "application/json"

        )

    )


@app.route(

    "/api/courses/<path:path>",

    methods=["GET","PUT","DELETE"]

)

def course_detail(path):

    url = f"{COURSE_SERVICE}/api/courses/{path}"

    response = requests.request(

        method=request.method,

        url=url,

        headers=request.headers,

        json=request.get_json(silent=True)

    )

    return Response(

        response.content,

        status=response.status_code,

        content_type=response.headers.get(

            "Content-Type",

            "application/json"

        )

    )


# --------------------------------------
# STUDENT SERVICE ROUTES
# --------------------------------------

@app.route(

    "/api/students",

    methods=["GET","POST"]

)

def students():

    url = STUDENT_SERVICE + "/api/students"

    response = requests.request(

        method=request.method,

        url=url,

        headers=request.headers,

        json=request.get_json(silent=True)

    )

    return Response(

        response.content,

        status=response.status_code,

        content_type=response.headers.get(

            "Content-Type",

            "application/json"

        )

    )


@app.route(

    "/api/students/<path:path>",

    methods=["GET","POST","PUT","DELETE"]

)

def student_detail(path):

    url = f"{STUDENT_SERVICE}/api/students/{path}"

    response = requests.request(

        method=request.method,

        url=url,

        headers=request.headers,

        json=request.get_json(silent=True)

    )

    return Response(

        response.content,

        status=response.status_code,

        content_type=response.headers.get(

            "Content-Type",

            "application/json"

        )

    )


if __name__ == "__main__":

    app.run(

        port=5000,

        debug=True

    )
