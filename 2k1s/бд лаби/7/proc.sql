DELIMITER //
CREATE PROCEDURE countByName (IN fname CHAR(48))
BEGIN
CREATE TABLE IF NOT EXISTS mydb.stats (object_id INT unsigned, category CHAR(48), 
amount INT UNSIGNED);
TRUNCATE mydb.stats;
INSERT INTO mydb.stats SELECT object.id AS object_id ,name AS category,
COUNT(repair.date) AS amount
FROM object INNER JOIN repair
ON object.id = repair.object_id
where object.name = fname
GROUP BY object_id;
END// 
DELIMITER ;

CALL countByName('-');
select*from stats;



Select object.name as name, count(repair.date) as amount from object inner JOIN repair on object.id = repair.object_id group by object.id;
select * from repair WHERE date BETWEEN '2020-01-01' AND '2922-09-09' order by date;
select * from repair order by date;
 
 SELECT object.name AS category,
COUNT(repair.date) AS amount
FROM object INNER JOIN repair
ON object.id = repair.object_id
where object.name = '-'
GROUP BY object_id;
 