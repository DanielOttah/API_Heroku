from db import db
from app import app


db.init_app(app)


# Nb SQLAlchemy can create the table instaed of using the create_table.py to create the tables


@app.before_first_request
def create_table():
    db.create_all()
