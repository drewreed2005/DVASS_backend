""" database dependencies to support sqliteDB examples """
from random import randrange
from datetime import date
import os, base64
import json

from __init__ import app, db
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash, check_password_hash


''' Tutorial: https://www.sqlalchemy.org/library.html#tutorials, try to get into Python shell and follow along '''


# Define the User class to manpassword actions in the 'users' table
# -- Object Relational Mapping (ORM) is the key concept of SQLAlchemy
# -- a.) db.Model is like an inner layer of the onion in ORM
# -- b.) User represents data we want to store, something that is built on db.Model
# -- c.) SQLAlchemy ORM is layer on top of SQLAlchemy Core, then SQLAlchemy engine, SQL
class SimulationData(db.Model):
    __tablename__ = 'simulations'  # table name is plural, class name is singular

    # Define the User schema with "vars" from object
    _username = db.Column(db.String(255), unique=True, nullable=False)
    _streak = db.Column(db.String(255), unique=True, nullable=False)
    
    
    # constructor of a User object, initializes the instance variables within object (self)
    def __init__(self, username="Sreeja", streak=10):
       # variables with self prefix become part of the object, 
        self._username = username
        self._streak= streak
       
    
    
    # output content using str(object) in human readable form, uses getter
    # output content using json dumps, this is ready for API response
    def __str__(self):
        return json.dumps(self.read())

   
"""Database Creation and Testing """

# Builds working data for testing
def initSimulationData():
    with app.app_context():
        """Create database and tables"""
        db.create_all()

        """Tester data for table"""

        s1 = SimulationData(username='sreeja', streak=1 )
        
        simulations = [s1]

        """Builds sample user/note(s) data"""
        for s in simulations:
            try:
                s.create()
                
            except IntegrityError:
                '''fails with bad or duplicate data'''

                db.session.remove()
                print(f"Records exist, duplicate email, or error: s.username")