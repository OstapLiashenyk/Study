SHOW INDEX FROM team;

CREATE INDEX teamINDX ON team (id, type); 
explain Select team.id as id,team.type, count(repair.date) as amount from team inner JOIN repair on team.object_id = repair.object_id group by team.object_id;
select * from repair WHERE date BETWEEN '2020-01-01' AND '2922-09-09' order by date;