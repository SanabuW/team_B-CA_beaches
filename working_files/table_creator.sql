CREATE TABLE beaches (	
	id SERIAL PRIMARY KEY,
	Region VARCHAR,
	County VARCHAR,
	Area VARCHAR,
	Beach_Name VARCHAR,
	Beach_URL VARCHAR,
	Address1 VARCHAR,
	Address2 VARCHAR,
	Park_Name VARCHAR,
	Owner_URL VARCHAR,
	Activities VARCHAR,
	Amenities VARCHAR,
	Pet_Policy VARCHAR,
	Fees VARCHAR,
	Phone VARCHAR,
	Other_Names VARCHAR
);



CREATE TABLE grade_data (	
	id SERIAL PRIMARY KEY,
	json_id INT,
	name1 VARCHAR,
	latitude VARCHAR,
	longitude VARCHAR,
	address VARCHAR,
	city VARCHAR,
	county VARCHAR,
	state VARCHAR,
	zip VARCHAR,
	active VARCHAR,
	grade_updated VARCHAR,
	dry_grade VARCHAR,
	wet_grade VARCHAR,
	annual_summer_dry VARCHAR,
	annual_year_wet VARCHAR,
	annual_winter_dry VARCHAR,
	annual_yaer VARCHAR,
	grade_created VARCHAR,
	alerts VARCHAR
);