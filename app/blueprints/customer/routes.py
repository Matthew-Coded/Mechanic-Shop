from flask import jsonify
from . import customer_bp
from app.models import Customer


@customer_bp.route("/test", methods=["GET"])
def test_customer():
    return jsonify(
        {
            "message": "Customer blueprint is working!"
        }
    )

@customer_bp.route("", methods=["GET"])
def get_customers():
    customers = Customer.query.all()

    result = []
    for c in customers:
        result.append({
            "id": c.id,
            "first_name": c.first_name,
            "last_name": c.last_name,
            "email": c.email,
            "phone": c.phone,
            "address": c.address,
            "dob": c.dob.isoformat() if c.dob else None
        })

    return jsonify(result)

