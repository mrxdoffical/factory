from django.db import models
import uuid
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, validates

engine = create_engine("sqlite:///bero.db")

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    username = Column(String, primary_key=True)
    email = Column(String)
    permission = Column(String)

    @validates('email')
    def validate_email(self, key, address):
        if not address:
            return f"{self.firstname}{self.lastname}@gmail.com"
        return address
    
    
    def __init__(self, firsname, lastname,  permission, email=None):
        self.firstname = firsname
        self.lastname = lastname
        self.email = email or f"{firsname}{lastname}@gmail.com"
        self.permission = permission


class Employee(Base):
    __tablename__ = 'employees'

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    firstname = Column(String)
    lastname = Column(String)
    age = Column(Integer)
    pay = Column(Integer)
    email = Column(String)

    @validates('email')
    def validate_email(self, key, address):
        if not address:
            return f"{self.firstname}{self.lastname}@gmail.com"
        return address

    def __init__(self, firstname, lastname, age, pay, email=None):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.pay = pay
        self.email = email or f"{firstname}{lastname}@gmail.com"

    def fullname(self) -> str:
        return f"{self.firstname} {self.lastname}"

    def __repr__(self) -> str:
        return f"Employee: firstname={self.firstname}, lastname={self.lastname}, age={self.age}, pay={self.pay}, email={self.email}"

# uncomment the next line to Drop the existing table if it exists
# Base.metadata.drop_all(engine, tables=[Employee.__table__])

# Create the table with the updated schema
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()