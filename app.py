####################################
# Import libraries
####################################
from flask import (
    Flask,
    render_template,
    jsonify
)
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from config import username, password

# Query functions to be applied to the separate api routes
from data_query import beach_query, grades_query, unq_years_query, latest_grades_query, count_by_year, grades_query_geojson
# from data_query import grades_dummy_query

# For secure/live ops version deployment
from flask_sqlalchemy import SQLAlchemy
from models import create_classes
from models import create_grade_classes


####################################
# Begin Flask app setup
####################################
# Set up Flask app
app = Flask(__name__)

####################################
# Setup database connection
####################################
# DEV/EDUCATIONAL VERSION
# Use SQLAlchemy to connect to postgreSQL server
engine = create_engine("postgresql://" + username + ":" + password + "@ec2-54-87-34-201.compute-1.amazonaws.com:5432/ddh5sm9o0kv98b")
conn = engine.connect()
Base = automap_base()
Base.prepare(engine, reflect=True)
session = Session(bind=engine)
Beaches = Base.classes.beaches
Grade_data = Base.classes.grade_data
# Test class
# Grade_data_dummy = Base.classes.grade_data_dummy


# # SECURE/LIVE OPS VERSION
# # To be used if the online live app's login needs to be secure
# # Set up database connection
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '').replace("://", "ql://", 1)
# # Remove tracking modifications
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)
# # Will need to switch to using models.py to create classes instead of sqlAlchemy reflectiosn
# Beaches = create_classes(db)
# Beach_grades = create_grade_classes(db)


####################################
# Create/Define Flask app routes
####################################
# Front-end page routes
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/currwq.html")
def currwq():
    return render_template("currwq.html")

@app.route("/histwq.html")
def histwq():
    return render_template("histwq.html")


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

@app.route("/api/grades_geojson")
def grades_geojson():
    grades_geojson_output = grades_query_geojson(session, Grade_data)
    return jsonify(grades_geojson_output)

@app.route("/api/years")
def years():
    Years_output = unq_years_query(session, Grade_data)
    return jsonify(Years_output)

@app.route("/api/count/<year>")
def getCountsByYear(year):
    Count_output = count_by_year(session, Grade_data, year)
    return jsonify(Count_output)

# Test route
# @app.route("/api/grades_dummy")
# def grades_dummy():
#     Grades_dummy_output = grades_dummy_query(session, Grade_data_dummy)
#     return jsonify(Grades_dummy_output)

# Run app
if __name__ == "__main__":
    app.run()

