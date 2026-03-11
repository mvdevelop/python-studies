
from flask import Blueprint
from ..controllers.student_controller import create_student, list_students

student_bp = Blueprint("students", __name__, url_prefix="/students")


@student_bp.route("/", methods=["POST"])
def create():
    return create_student()


@student_bp.route("/", methods=["GET"])
def list_all():
    return list_students()
