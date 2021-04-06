-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- Link to schema: https://app.quickdatabasediagrams.com/#/d/synSnR
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.

-- Modify this code to update the DB schema diagram.
-- To reset the sample schema, replace everything with
-- two dots ('..' - without quotes).

CREATE TABLE "beaches" (
    "id" int   NOT NULL,
    "region" VARCHAR   NOT NULL,
    "county" VARCHAR   NOT NULL,
    "area" VARCHAR   NOT NULL,
    "beach_name" VARCHAR   NOT NULL,
    "beach_url" VARCHAR   NOT NULL,
    "address" VARCHAR   NOT NULL,
    "city" VARCHAR   NOT NULL,
    "state" VARCHAR NOT NULL,
    "zip"   VARCHAR NOT NULL,
    "park_name" VARCHAR   NOT NULL,
    "owner_url" VARCHAR   NOT NULL,
    "activities" VARCHAR   NOT NULL,
    "amenities" VARCHAR   NOT NULL,
    "pet_policy" VARCHAR   NOT NULL,
    "pets_allowed" VARCHAR  NOT NULL,
    "fees" VARCHAR   NOT NULL,
    "free_parking" VARCHAR  NOT NULL,
    "phone" VARCHAR   NOT NULL,
    "other_names" VARCHAR   NOT NULL,
    "latitude" FLOAT    NOT NULL,
    "longitude" FLOAT   NOT NULL,
    CONSTRAINT "pk_beaches" PRIMARY KEY (
        "id"
     )
);

CREATE TABLE "grade_data" (
    "id" VARCHAR   NOT NULL,
    "title" VARCHAR   NOT NULL,
    "name1" VARCHAR   NOT NULL,
    "latitude" VARCHAR   NOT NULL,
    "longitude" VARCHAR   NOT NULL,
    "address" VARCHAR   NOT NULL,
    "city" VARCHAR   NOT NULL,
    "county" VARCHAR   NOT NULL,
    "state" VARCHAR   NOT NULL,
    "zip" VARCHAR   NOT NULL,
    "active" VARCHAR   NOT NULL,
    "grade_updated" VARCHAR   NOT NULL,
    "dry_grade" VARCHAR   NOT NULL,
    "wet_grade" VARCHAR   NOT NULL,
    "annual_summer_dry" VARCHAR   NOT NULL,
    "annual_year_wet" VARCHAR   NOT NULL,
    "annual_winter_dry" VARCHAR   NOT NULL,
    "annual_year" VARCHAR   NOT NULL,
    "grade_created" VARCHAR   NOT NULL,
    "alerts" VARCHAR    NOT NULL
);

CREATE TABLE "beaches_location" (
    "id" int   NOT NULL,
    "region" VARCHAR   NOT NULL,
    "county" VARCHAR   NOT NULL,
    "area" VARCHAR   NOT NULL,
    "beach_name" VARCHAR   NOT NULL,
    "beach_url" VARCHAR   NOT NULL,
    "address" VARCHAR   NOT NULL,
    "city" VARCHAR   NOT NULL,
    "state" VARCHAR NOT NULL,
    "zip" VARCHAR NOT NULL,
    "park_name" VARCHAR   NOT NULL,
    "owner_url" VARCHAR   NOT NULL,
    "activities" VARCHAR   NOT NULL,
    "amenities" VARCHAR   NOT NULL,
    "pet_policy" VARCHAR   NOT NULL,
    "pets_allowed" VARCHAR  NOT NULL,
    "fees" VARCHAR   NOT NULL,
    "free_parking" VARCHAR  NOT NULL,
    "phone" VARCHAR   NOT NULL,
    "other_names" VARCHAR   NOT NULL,
    "latitude" VARCHAR   NOT NULL,
    "longitude" VARCHAR   NOT NULL,
    CONSTRAINT "pk_beaches_location" PRIMARY KEY (
        "id"
     )
);

CREATE TABLE "beaches_grade" (
    "id" int   NOT NULL,
    "beach_name" VARCHAR   NOT NULL,
    "latitude" VARCHAR   NOT NULL,
    "longitude" VARCHAR   NOT NULL,
    "grade_updated" VARCHAR   NOT NULL,
    "dry_grade" VARCHAR   NOT NULL,
    "wet_grade" VARCHAR   NOT NULL,
    "annual_summer_dry" VARCHAR   NOT NULL,
    "annual_year_wet" VARCHAR   NOT NULL,
    "annual_winter_dry" VARCHAR   NOT NULL,
    "annual_year" VARCHAR   NOT NULL,
    CONSTRAINT "pk_beaches_grade" PRIMARY KEY (
        "id"
     )
);

ALTER TABLE "beaches" ADD CONSTRAINT "fk_beaches_region_county_area_beach_name_beach_url_address1_address2_park_name_owner_url_activities_amenities_pet_policy_fees_phone_other_names" FOREIGN KEY("region", "county", "area", "beach_name", "beach_url", "address1", "address2", "park_name", "owner_url", "activities", "amenities", "pet_policy", "fees", "phone", "other_names")
REFERENCES "beaches_location" ("region", "county", "area", "beach_name", "beach_url", "address1", "address2", "park_name", "owner_url", "activities", "amenities", "pet_policy", "fees", "phone", "other_names");

ALTER TABLE "grade_data" ADD CONSTRAINT "fk_grade_data_name1_latitude_longitude" FOREIGN KEY("name1", "latitude", "longitude")
REFERENCES "beaches_location" ("beach_name", "latitude", "longitude");

ALTER TABLE "grade_data" ADD CONSTRAINT "fk_grade_data_grade_updated_dry_grade_wet_grade_annual_summer_dry_annual_year_wet_annual_winter_dry_annual_year" FOREIGN KEY("grade_updated", "dry_grade", "wet_grade", "annual_summer_dry", "annual_year_wet", "annual_winter_dry", "annual_year")
REFERENCES "beaches_grade" ("grade_updated", "dry_grade", "wet_grade", "annual_summer_dry", "annual_year_wet", "annual_winter_dry", "annual_year");

ALTER TABLE "beaches_location" ADD CONSTRAINT "fk_beaches_location_beach_name_latitude_longitude" FOREIGN KEY("beach_name", "latitude", "longitude")
REFERENCES "beaches_grade" ("beach_name", "latitude", "longitude");

