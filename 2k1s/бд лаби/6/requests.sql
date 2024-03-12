select * from employee where name LIKE "%o%" limit 9

select * from repair group by object_id order by date

select name from objectOwner inner join repair where objectOwner.object_id = repair.object_id and 
repair.type = "unplanned" group by objectOwner.name

