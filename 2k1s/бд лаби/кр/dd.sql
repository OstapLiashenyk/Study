select objectowner.name, count(employee.id) from
team inner join objectowner on team.object_id = objectowner.object_id 
inner join employee on employee.team_id = team.id group by team.id;

select employee.name, count(repair.date) from
team inner join repair on team.object_id = repair.object_id 
inner join employee on employee.team_id = team.id 
group by employee.name 
;

select objectowner.name, objectOwner.phone as id,count(repair.date) from
repair inner join objectowner on repair.object_id = objectowner.object_id 
where repair.date > '2000-01-01'
group by objectOwner.object_id
;

select * from objectOwner;
select*from repair;
select * from
team inner join repair on team.object_id = repair.object_id ;

select*from repair;
select*from team;


INSERT INTO employee(team_id,name,phone,position)
VALUES (1,"Ostap","+38023548","builder");
delete from employee where id>24