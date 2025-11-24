from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Date, ForeignKey
from .extentions import db
from datetime import date, datetime



class Mechanic(db.Model):
    __tablename__ = "mechanics"

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(250), nullable=False)
    last_name: Mapped[str] = mapped_column(String(250), nullable=False)
    email: Mapped[str] = mapped_column(String(350), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String(150), nullable=False)
    phone: Mapped[str] = mapped_column(String(20), nullable=False)
    address: Mapped[str] = mapped_column(String(500), nullable=False)
    dob: Mapped[date] = mapped_column(Date, nullable=True)


class Customer(db.Model):
    __tablename__ = "customers"

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(250), nullable=False)
    last_name: Mapped[str] = mapped_column(String(250), nullable=False)
    email: Mapped[str] = mapped_column(String(350), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String(150), nullable=False)
    phone: Mapped[str] = mapped_column(String(20), nullable=False)
    address: Mapped[str] = mapped_column(String(500), nullable=False)
    dob: Mapped[Date] = mapped_column(Date, nullable=True)

    # Relationship
    vehicles: Mapped[list["Vehicle"]] = relationship(
        back_populates="customer"
    )
    service_tickets: Mapped[list["ServiceTicket"]] = relationship(
        back_populates="customer"
    )


class Vehicle(db.Model):
    __tablename__ = "vehicles"

    id: Mapped[int] = mapped_column(primary_key=True)
    customer_id: Mapped[int] = mapped_column(ForeignKey('customers.id'))
    make: Mapped[str] = mapped_column(String(150), nullable=False)
    model: Mapped[str] = mapped_column(String(150), nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    vin: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)

    # Relationship
    customer: Mapped["Customer"] = relationship(
        back_populates="vehicles"
    )
    service_tickets: Mapped[list["ServiceTicket"]] = relationship(
        back_populates="vehicle"
    )


class ServiceTicket(db.Model):
    __tablename__ = "service_tickets"

    id: Mapped[int] = mapped_column(primary_key=True)
    customer_id: Mapped[int] = mapped_column(ForeignKey('customers.id'))
    vehicle_id: Mapped[int] = mapped_column(ForeignKey('vehicles.id'))
    service_reason: Mapped[str] = mapped_column(String(1000), nullable=False)

    # Relationships
    customer: Mapped["Customer"] = relationship(
        back_populates="service_tickets"
    )
    vehicle: Mapped["Vehicle"] = relationship(
        back_populates="service_tickets"
    )


class MechanicServiceTicket(db.Model):
    __tablename__ = "mechanic_service_tickets"

    mechanic_id: Mapped[int] = mapped_column(
        ForeignKey('mechanics.id'),
        primary_key=True
    )

    service_ticket_id: Mapped[int] = mapped_column(
        ForeignKey('service_tickets.id'),
        primary_key=True
    )


