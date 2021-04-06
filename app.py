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
    # results = db.session.query(Beach.beach_name, Beach.id).first()
    results = db.session.query(Beach.id, Beach.beach_name).first()
    print(results)
    return render_template("index.html", text1 = "jinja test1", text2 = results)




@app.route("/api/beaches")
def beaches():
    results = db.session.query(
    Beach.id,
    Beach.region,
    Beach.county,
    Beach.area,
    Beach.beach_name,
    Beach.beach_url,
    Beach.address,
    Beach.city,
    Beach.state,
    Beach.zip,
    Beach.latitude,
    Beach.longitude,
    Beach.park_name,
    Beach.owner,
    Beach.owner_url,
    Beach.activities,
    Beach.amenities,
    Beach.pet_policy,
    Beach.pets_allowed,
    Beach.fees,
    Beach.free_parking,
    Beach.phone,
    Beach.other_names
    ).all()
    # hover_text = [result[0] for result in results]
    # lat = [result[1] for result in results]
    # lon = [result[2] for result in results]
    beach_data = []
    for beach_info in results:
        beach_data.append({
            "id": beach_info[0],
            "region": beach_info[1],
            "county": beach_info[2],
            "area": beach_info[3],
            "beach_name": beach_info[4],
            "beach_url": beach_info[5],
            "address": beach_info[6],
            "city": beach_info[7],
            "state": beach_info[8],
            "zip": beach_info[9],
            "latitude": beach_info[10],
            "longitude": beach_info[11],
            "park_name": beach_info[12],
            "owner": beach_info[13],
            "owner_url": beach_info[14],
            "activities": beach_info[15],
            "amenities": beach_info[16],
            "pet_policy": beach_info[17],
            "pets_allowed": beach_info[18],
            "fees": beach_info[19],
            "free parking": beach_info[20],
            "phone": beach_info[21],
            "other_names": beach_info[22]
    #     "type": "scattergeo",
    #     "locationmode": "USA-states",
    #     "lat": lat,
    #     "lon": lon,
    #     "text": hover_text,
    #     "hoverinfo": "text",
    #     "marker": {
    #         "size": 50,
    #         "line": {
    #             "color": "rgb(8,8,8)",
    #             "width": 1
    #         },
    #     }
    })

    return jsonify(beach_data)

    # return jsonify(pet_data)


@app.route("/api/grades")
def grades():
    grades_data = query_builder_func(session, Beaches, Grade_data, Grade_data_dummy)
    return jsonify(grades_data)

# Run app
if __name__ == "__main__":
    app.run()