def query_builder_func (session, Beaches, Grade_data, Grade_data_dummy) :
# # Querying for all general beach data
#     beaches_results = session.query(
#         Beaches.id,
#         Beaches.region,
#         Beaches.county,
#         Beaches.area,
#         Beaches.beach_name,
#         Beaches.beach_url,
#         Beaches.address,
#         Beaches.city,
#         Beaches.state,
#         Beaches.zip,
#         Beaches.latitude,
#         Beaches.longitude,
#         Beaches.park_name,
#         Beaches.owner,
#         Beaches.owner_url,
#         Beaches.activities,
#         Beaches.amenities,
#         Beaches.pet_policy,
#         Beaches.pets_allowed,
#         Beaches.fees,
#         Beaches.free_parking,
#         Beaches.phone,
#         Beaches.other_names
#         ).all()

#     beaches_data = []
#     for beaches_info in beaches_results:
#         beaches_data.append({
#             "id": beaches_info[0],
#             "region": beaches_info[1],
#             "county": beaches_info[2],
#             "area": beaches_info[3],
#             "beach_name": beaches_info[4],
#             "beach_url": beaches_info[5],
#             "address": beaches_info[6],
#             "city": beaches_info[7],
#             "state": beaches_info[8],
#             "zip": beaches_info[9],
#             "latitude": beaches_info[10],
#             "longitude": beaches_info[11],
#             "park_name": beaches_info[12],
#             "owner": beaches_info[13],
#             "owner_url": beaches_info[14],
#             "activities": beaches_info[15],
#             "amenities": beaches_info[16],
#             "pet_policy": beaches_info[17],
#             "pets_allowed": beaches_info[18],
#             "fees": beaches_info[19],
#             "free_parking": beaches_info[20],
#             "phone": beaches_info[21],
#             "other_names": beaches_info[22]
#     })


# # Querying for all grade beach data
#     grades_results = session.query(
#         Grade_data.id,
#         Grade_data.json_id,
#         Grade_data.title,
#         Grade_data.name1,
#         Grade_data.latitude,
#         Grade_data.longitude,
#         Grade_data.address,
#         Grade_data.city,
#         Grade_data.county,
#         Grade_data.state,
#         Grade_data.zip,
#         Grade_data.active,
#         Grade_data.grade_updated,
#         Grade_data.dry_grade,
#         Grade_data.wet_grade,
#         Grade_data.annual_summer_dry,
#         Grade_data.annual_year_wet,
#         Grade_data.annual_winter_dry,
#         Grade_data.annual_year,
#         Grade_data.grade_created,
#         Grade_data.alerts
#         ).all()


#     grades_data = []
#     for grades_info in grades_results:
#         grades_data.append({
#             "id": grades_info[0],
#             "json_id": grades_info[1],
#             "title": grades_info[2],
#             "name1": grades_info[3],
#             "latitude": grades_info[4],
#             "longitude": grades_info[5],
#             "address": grades_info[6],
#             "city": grades_info[7],
#             "county": grades_info[8],
#             "state": grades_info[9],
#             "zip": grades_info[10],
#             "active": grades_info[11],
#             "grade_updated": grades_info[12],
#             "dry_grade": grades_info[13],
#             "wet_grade": grades_info[14],
#             "annual_summer_dry": grades_info[15],
#             "annual_year_wet": grades_info[16],
#             "annual_winter_dry": grades_info[17],
#             "annual_year": grades_info[18],
#             "grade_created": grades_info[19],
#             "alerts": grades_info[20]
#     })




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



    beaches_data = [{
        "beach1 key1":"value1",
        "beach1 key2":"value2"
    },
    {
        "beach2 key1":"value1",
        "beach2 key2":"value2"
    }]

    grades_data = [{
        "grade1 key1":"value1",
        "grade1 key2":"value2"
    },
    {
        "grade2 key1":"value1",
        "grade2 key2":"value2"
    }]

    # return grades_dummy_data
    return beaches_data, grades_data, grades_dummy_data
