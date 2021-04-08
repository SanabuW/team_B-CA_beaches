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

# Query functions to be applied to the separate api routes
from data_query import beach_query, grades_query, grades_dummy_query, latest_grades_query



# For secure/live ops version deployment
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
## WILL NEED TO CHECK IF THESE CLASSES ARE CORRECT
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
    results = session.query(Grade_data_dummy.id, Grade_data_dummy.beach_name).first()
    print(results)
    return render_template("index.html", text1 = "jinja test1", text2 = results)

# Routes for data queries to be used by JS apps
@app.route("/api/beaches")
def beaches():
    Beaches_output = beach_query(session, Beaches)
    return jsonify(Beaches_output)

@app.route("/api/grades")
def grades():
    Grades_output = grades_query(session, Grade_data)
    return jsonify(Grades_output)

@app.route("/api/latest_grades")
def latest_grades():
    Latest_grades_output = latest_grades_query(session, Grade_data)
    return jsonify(Latest_grades_output)

@app.route("/api/grades_dummy")
def grades_dummy():
    Grades_dummy_output = grades_dummy_query(session, Grade_data_dummy)
    return jsonify(Grades_dummy_output)

# Run app
if __name__ == "__main__":
    app.run()