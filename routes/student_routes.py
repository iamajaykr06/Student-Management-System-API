from flask import Blueprint
from flask import jsonify, request
student_bp = Blueprint("student_bp", __name__)

@student_bp.route("/students", methods=["POST"])
def create_student():
    data = request.get_json()

    # Step 1: JSON check
    if data is None:
        return jsonify({"message": "Request must be JSON"}), 400

    # Step 2: required fields
    required_fields = ["name", "department", "course", "academic_session"]

    for field in required_fields:
        if field not in data:
            return jsonify({"message": f"attribute {field} missing"}), 400

        if not str(data[field]).strip():
            return jsonify({"message": f"attribute {field} cannot be empty"}), 400

    # Step 3: success
    return jsonify({
        "message": "Student received successfully",
        "data": data
    }), 200

