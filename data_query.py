def query_builder_func (session, Beaches, Grade_data, Grade_data_dummy) :
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
            "beach_name": beaches_info[1],
            "latitude": beaches_info[2],
            "longitude": beaches_info[3],
            "date": beaches_info[4],
            "dry_grade": grades_info[5],
            "wet_grade": grades_info[6],
            "annual_summer_dry": grades_info[7],
            "annual_year_wet": grades_info[8],
            "annual_winter_dry": grades_info[9],
            "annual_year": grades_info[10]
    })


# Querying for all grade beach data
    grades_results = session.query(
        Grade_data.id,
        Grade_data.json_id,
        Grade_data.title,
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
        Grade_data.grade_created,
        Grade_data.alerts
        ).all()


    grades_data = []
    for grades_info in grades_results:
        grades_data.append({
            "id": grades_info[0],
            "beach_name": grades_info[1],
            "latitude": grades_info[2],
            "longitude": grades_info[3],
            "date": grades_info[4],
            "dry_grade": grades_info[5],
            "wet_grade": grades_info[6],
            "annual_summer_dry": grades_info[7],
            "annual_year_wet": grades_info[8],
            "annual_winter_dry": grades_info[9],
            "annual_year": grades_info[10]
    })

    grades_dummy_results_results = session.query(
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

    grades_data = []
    for grades_info in results:
        grades_data.append({
            "id": grades_info[0],
            "beach_name": grades_info[1],
            "latitude": grades_info[2],
            "longitude": grades_info[3],
            "date": grades_info[4],
            "dry_grade": grades_info[5],
            "wet_grade": grades_info[6],
            "annual_summer_dry": grades_info[7],
            "annual_year_wet": grades_info[8],
            "annual_winter_dry": grades_info[9],
            "annual_year": grades_info[10]
    })

    return grades_data
