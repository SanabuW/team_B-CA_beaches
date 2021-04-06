####################################
# Import libraries
####################################
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func


from data_query import query_builder_func

#For secure/live ops version deployment
from flask_sqlalchemy import SQLAlchemy
from models import create_classes
from models import create_grade_classes
import os


####################################
# Begin Flask app setup
####################################
# Set up Flask app
app = Flask(__name__)

####################################
# Setup database connection
####################################
# # SECURE/LIVE OPS VERSION
# # Set up database connection
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '').replace("://", "ql://", 1)
# # Remove tracking modifications
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)
# Beaches = create_classes(db)
# Beach_grades = create_grade_classes(db)

# DEV/EDUCATIONAL VERSION
engine = create_engine("postgresql://ydpymkcqnwzgyh:4ff9574af72fa725ed0d902a2dcafc72636ecdfdc2745af2f871229ced540f5c@ec2-54-87-34-201.compute-1.amazonaws.com:5432/ddh5sm9o0kv98b")
conn = engine.connect()
Base = automap_base()
Base.prepare(engine, reflect=True)
session = Session(bind=engine)
Beaches = Base.classes.beaches
Grade_data = Base.classes.grade_data
Grade_data_dummy = Base.classes.grade_data_dummy


####################################
# Create/Define Flask app routes
####################################
@app.route("/")
def home():
    beach_name1 = session.query(Beaches.beach_name).first()
    return render_template("index.html", text1 = beach_name1, text2 = Base.classes.keys())


@app.route("/api/grades")
def grades():
    grades_data = query_builder_func(session, Grade_data_dummy)
    return jsonify(grades_data)

# Run app
if __name__ == "__main__":
    app.run()