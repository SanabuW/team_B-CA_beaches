# Import libraries
from models import create_classes
import os
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)
from flask_sqlalchemy import SQLAlchemy


# Set up Flask app
app = Flask(__name__)

# Set up database connection
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '').replace("://", "ql://", 1)
# app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://ydpymkcqnwzgyh:4ff9574af72fa725ed0d902a2dcafc72636ecdfdc2745af2f871229ced540f5c@ec2-54-87-34-201.compute-1.amazonaws.com:5432/ddh5sm9o0kv98b"

# Remove tracking modifications
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

Beach = create_classes(db)


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
    Beach.address1,
    Beach.address2,
    Beach.park_name,
    Beach.owner_url,
    Beach.activities,
    Beach.amenities,
    Beach.pet_policy,
    Beach.fees,
    Beach.phone,
    Beach.other_names
    ).first()
    # hover_text = [result[0] for result in results]
    # lat = [result[1] for result in results]
    # lon = [result[2] for result in results]

    beach_data = [{
        "id": results[0],
        "region": results[1],
        "county": results[2],
        "area": results[3],
        "beach_name": results[4],
        "beach_url": results[5],
        "address1": results[6],
        "address2": results[7],
        "park_name": results[8],
        "owner_url": results[9],
        "activities": results[10],
        "amenities": results[11],
        "pet_policy": results[12],
        "fees": results[13],
        "phone": results[14],
        "other_names": results[15]
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
    }]

    return jsonify(beach_data)

    # return jsonify(pet_data)



# Run app
if __name__ == "__main__":
    app.run()