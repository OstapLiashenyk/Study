select * from repair where object_id = 1;

INSERT INTO repair
VALUES (8,"unplanned","2025-02-10");



START TRANSACTION;
delete from repair where object_id = 9;
update repair set type = "planned" where oid = 10;
commit;

select * from repair where object_id > 7;

delete from repair where object_id = 1;

select * from repair;



