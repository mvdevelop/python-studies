
from flask import request, jsonify, current_app
from ..services.upload_service import save_image

students = []

def create_student():

    name = request.form.get("name")
    age = request.form.get("age")

    image_file = request.files.get("image")

    image_name = None

    if image_file:
        image_name = save_image(image_file, current_app.config["UPLOAD_FOLDER"])

    student = {
        "id": len(students) + 1,
        "name": name,
        "age": age,
        "image": image_name
    }

    students.append(student)

    return jsonify(student), 201


def list_students():
    return jsonify(students)
