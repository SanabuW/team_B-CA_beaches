from sqlalchemy import func

def beach_query (session, Beaches) :
# Querying for all general beach data
    beaches_results = session.query(
        Beaches.id,
        Beaches.region,
        Beaches.county,
        Beaches.area,
        Beaches.beach_name,
        Beaches.beach_url,
        Beaches.address,
        Beaches.city,
        Beaches.state,
        Beaches.zip,
        Beaches.latitude,
        Beaches.longitude,
        Beaches.park_name,
        Beaches.owner,
        Beaches.owner_url,
        Beaches.activities,
        Beaches.amenities,
        Beaches.pet_policy,
        Beaches.pets_allowed,
        Beaches.fees,
        Beaches.free_parking,
        Beaches.phone,
        Beaches.other_names
        ).all()

    beaches_data = []
    for beaches_info in beaches_results:
        beaches_data.append({
            "id": beaches_info[0],
            "region": beaches_info[1],
            "county": beaches_info[2],
            "area": beaches_info[3],
            "beach_name": beaches_info[4],
            "beach_url": beaches_info[5],
            "address": beaches_info[6],
            "city": beaches_info[7],
            "state": beaches_info[8],
            "zip": beaches_info[9],
            "latitude": beaches_info[10],
            "longitude": beaches_info[11],
            "park_name": beaches_info[12],
            "owner": beaches_info[13],
            "owner_url": beaches_info[14],
            "activities": beaches_info[15],
            "amenities": beaches_info[16],
            "pet_policy": beaches_info[17],
            "pets_allowed": beaches_info[18],
            "fees": beaches_info[19],
            "free_parking": beaches_info[20],
            "phone": beaches_info[21],
            "other_names": beaches_info[22]
    })
    return beaches_data


def grades_query (session, Grade_data) :
# Querying for all grade beach data
    grades_results = session.query(
        Grade_data.id,
        Grade_data.json_id,
        Grade_data.name1,
        Grade_data.latitude,
        Grade_data.longitude,
        Grade_data.address,
        Grade_data.city,
        Grade_data.county,
        Grade_data.state,
        Grade_data.zip,
        Grade_data.active,
        Grade_data.grade_updated,
        Grade_data.dry_grade,
        Grade_data.wet_grade,
        Grade_data.annual_summer_dry,
        Grade_data.annual_year_wet,
        Grade_data.annual_winter_dry,
        Grade_data.annual_year,
        Grade_data.grade_created
        ).all()

    grades_data = []
    for grades_info in grades_results:
        grades_data.append({
            "id": grades_info[0],
            "json_id": grades_info[1],
            "name1": grades_info[2],
            "latitude": grades_info[3],
            "longitude": grades_info[4],
            "address": grades_info[5],
            "city": grades_info[6],
            "county": grades_info[7],
            "state": grades_info[8],
            "zip": grades_info[9],
            "active": grades_info[10],
            "grade_updated": grades_info[11],
            "dry_grade": grades_info[12],
            "wet_grade": grades_info[13],
            "annual_summer_dry": grades_info[14],
            "annual_year_wet": grades_info[15],
            "annual_winter_dry": grades_info[16],
            "annual_year": grades_info[17],
            "grade_created": grades_info[18]
    })
    return grades_data

def grades_dummy_query (session, Grade_data_dummy) :
    grades_dummy_results = session.query(
        Grade_data_dummy.id,
        Grade_data_dummy.beach_name,
        Grade_data_dummy.latitude,
        Grade_data_dummy.longitude,
        Grade_data_dummy.date,
        Grade_data_dummy.dry_grade,
        Grade_data_dummy.wet_grade,
        Grade_data_dummy.annual_summer_dry,
        Grade_data_dummy.annual_year_wet,
        Grade_data_dummy.annual_winter_dry,
        Grade_data_dummy.annual_year
        ).all()

    grades_dummy_data = []
    for grades_dummy_info in grades_dummy_results:
        grades_dummy_data.append({
            "id": grades_dummy_info[0],
            "beach_name": grades_dummy_info[1],
            "latitude": grades_dummy_info[2],
            "longitude": grades_dummy_info[3],
            "date": grades_dummy_info[4],
            "dry_grade": grades_dummy_info[5],
            "wet_grade": grades_dummy_info[6],
            "annual_summer_dry": grades_dummy_info[7],
            "annual_year_wet": grades_dummy_info[8],
            "annual_winter_dry": grades_dummy_info[9],
            "annual_year": grades_dummy_info[10]
    })

    # return grades_dummy_data
    return grades_dummy_data


def latest_grades_query (session, Grade_data) :
# Querying for all grade beach data
    subq = session.query(func.max(Grade_data.id)).group_by(Grade_data.name1).all()

    id_list = []
    for x in subq:
        id_list.append(x[0])

    query = session.query(Grade_data).where(Grade_data.id.in_(id_list)).all()

    latest_grades_data = []
    for grades_info in query:
        latest_grades_data.append({
            "id": grades_info.id,
            "json_id": grades_info.json_id,
            "name1": grades_info.name1,
            "latitude": grades_info.latitude,
            "longitude": grades_info.longitude,
            "address": grades_info.address,
            "city": grades_info.city,
            "county": grades_info.county,
            "state": grades_info.state,
            "zip": grades_info.zip,
            "active": grades_info.active,
            "grade_updated": grades_info.grade_updated,
            "dry_grade": grades_info.dry_grade,
            "wet_grade": grades_info.wet_grade,
            "annual_summer_dry": grades_info.annual_summer_dry,
            "annual_year_wet": grades_info.annual_year_wet,
            "annual_winter_dry": grades_info.annual_winter_dry,
            "annual_year": grades_info.annual_year,
            "grade_created": grades_info.grade_created
    })

    return latest_grades_data

def unq_years_query (session, Grade_data) :
# Querying for unique years in grade data
    grades_results = session.query(
        distinct(func.date_part('YEAR', Grade_data.grade_updated)))

    years_data = []
    for grades_info in grades_results:
        years_data.append(int(grades_info[0]))

    years_data.sort()

    return years_data

def count_by_year (session, Grade_data, year) :
# Querying for unique years in grade data

    grade_values = ["A+", "A", "B", "C", "D", "F"]

    count_data = []
    for month in range(1,13):
        for grade in grade_values:
            grades_results = (session.query (
                func.count(Grade_data.id))
                .filter(func.date_part('YEAR', Grade_data.grade_updated) == int(year))
                .filter(func.date_part('MONTH', Grade_data.grade_updated) == month)
                .filter(Grade_data.dry_grade == grade)).scalar()

            # append grade, month number, and count of dry grades
            count_data.append([grade, month, grades_results])
            session.commit()
            

            grades_results = (session.query (
                func.count(Grade_data.id))
                .filter(func.date_part('YEAR', Grade_data.grade_updated) == int(year))
                .filter(func.date_part('MONTH', Grade_data.grade_updated) == month)
                .filter(Grade_data.wet_grade == grade)).scalar()
            
            # append count of wet grades to list
            count_data[-1].append(grades_results)
            session.commit()


    return count_data