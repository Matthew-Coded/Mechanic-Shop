from flask import jsonify, request
from app.models import Customer
from app.extensions import db
from . import customer_bp
from .schemas import customer_schema, customers_schema


# Create Customer
@customer_bp.route("", methods=["POST"])
def create_customer():
    data = request.get_json()
    customer: Customer = customer_schema.load(data)

    db.session.add(customer)
    db.session.commit()

    return customer_schema.jsonify(customer), 201


# Read Customers
@customer_bp.route("/test", methods=["GET"])
def test_customer():
    return jsonify(
        {
            "message": "Customer blueprint is working!"
        }
    )

# All Customers
@customer_bp.route("", methods=["GET"])
def get_customers():
    customers = Customer.query.all()
    return customers_schema.jsonify(customers)

# One Customer
@customer_bp.route("/<int:customer_id>", methods=["GET"])
def get_customer(customer_id):
    customer = Customer.query.get_or_404(customer_id)
    return customer_schema.jsonify(customer)


# Update Customer
@customer_bp.route("/<int:customer_id>", methods=["PUT"])
def update_customer(customer_id):
    customer = Customer.query.get_or_404(customer_id)
    data = request.get_json()

    updated_customer: Customer = customer_schema.load(
        data,
        instance=customer,
        partial=False
    )

    db.session.commit()

    return customer_schema.jsonify(updated_customer), 200


# Delete Customer
@customer_bp.route("/<int:customer_id>", methods=["DELETE"])
def delete_customer(customer_id):
    customer = Customer.query.get_or_404(customer_id)
    
    db.session.delete(customer)
    db.session.commit()

    return "", 204 # No content (204)


