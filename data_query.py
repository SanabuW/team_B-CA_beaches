def query_builder_func (session, Grade_data_dummy) :

    results = session.query(
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
