def create_classes(db):
    class Beach(db.Model):
        __tablename__ = 'beaches'

        id = db.Column(db.Integer, primary_key=True)
        region = db.Column(db.String(64))
        county = db.Column(db.String(64))
        area = db.Column(db.String(64))
        beach_name = db.Column(db.String(64))
        beach_url = db.Column(db.String(64))
        address = db.Column(db.String(64))
        city = db.Column(db.String(64))
        state = db.Column(db.String(64))
        zip = db.Column(db.String(64))
        latitude = db.Column(db.String(64))
        longitude = db.Column(db.String(64))
        park_name = db.Column(db.String(64))
        owner_url = db.Column(db.String(64))
        activities = db.Column(db.String(64))
        amenities = db.Column(db.String(64))
        pet_policy = db.Column(db.String(64))
        pets_allowed = db.Column(db.String(1))
        fees = db.Column(db.String(64))
        free_parking = db.Column(db.String(1))
        phone = db.Column(db.String(64))
        other_names = db.Column(db.String(64))

        def __repr__(self):
            return '<Beach %r>' % (self.beach_name)
    return Beach



def create_grade_classes(db):
    class Beach(db.Model):
        __tablename__ = 'grade_data'

        id = db.Column(db.Integer, primary_key=True)
        region = db.Column(db.String(64))
        county = db.Column(db.String(64))
        area = db.Column(db.String(64))
        beach_name = db.Column(db.String(64))
        beach_url = db.Column(db.String(64))
        address = db.Column(db.String(64))
        city = db.Column(db.String(64))
        state = db.Column(db.String(64))
        zip = db.Column(db.String(64))
        latitude = db.Column(db.String(64))
        longitude = db.Column(db.String(64))
        park_name = db.Column(db.String(64))
        owner_url = db.Column(db.String(64))
        activities = db.Column(db.String(64))
        amenities = db.Column(db.String(64))
        pet_policy = db.Column(db.String(64))
        pets_allowed = db.Column(db.String(1))
        fees = db.Column(db.String(64))
        free_parking = db.Column(db.String(1))
        phone = db.Column(db.String(64))
        other_names = db.Column(db.String(64))

        def __repr__(self):
            return '<Beach %r>' % (self.beach_name)
    return Beach