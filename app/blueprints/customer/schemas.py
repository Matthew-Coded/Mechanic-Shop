from app.extensions import ma
from app.models import Customer


class CustomerSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Customer
        load_instance = True
        ordered = True

    id = ma.auto_field()
    first_name = ma.auto_field()
    last_name = ma.auto_field()
    email = ma.auto_field()
    password = ma.auto_field()
    phone = ma.auto_field()
    address = ma.auto_field()
    dob = ma.auto_field()

customer_schema = CustomerSchema()
customers_schema = CustomerSchema(many=True)