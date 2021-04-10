-- SELECT * FROM grade_data
-- WHERE name1 = 'Dockweiler State Beach'
-- ORDER BY grade_updated DESC
-- -- AND grade_updated = '2008-04-29'
-- -- 2021-04-02

-- Select * from grade_data
-- where id in (
-- Select a.id from (
-- Select * from grade_data
-- where min(id in (
-- SELECT min(id)
-- FROM grade_data
-- GROUP BY name1, grade_updated)) a
-- GROUP BY a.name1
-- having max(a.grade_updated)=a.grade_updated)


-- SELECT * FROM grade_data
-- WHERE id in (
-- 	SELECT min(id)
-- 	FROM grade_data
-- 	GROUP BY name1, grade_updated
-- 	HAVING max(grade_updated) = grade_updated
-- )
-- AND name1 = 'Dockweiler State Beach'

	
	
	
	
	
	
	
-- THIS↓
-- USE SUB QUERIES

--THEN select the grade data
Select * from grade_data
where id in (
-- group by names, and get the record with the "latest"/the latest max id
-- Making an assumption that max(id) is the latest grade
	Select max(id) from grade_data
	group by name1
)

