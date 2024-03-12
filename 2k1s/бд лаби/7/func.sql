select * from object;
select * from objectowner;
select * from employee;
select * from repair;
select * from team;

CREATE FUNCTION name_ureverse (name CHAR(48))
RETURNS CHAR(48)
RETURN REVERSE(UCASE(name)) ;



Select name_reverse(name) from employee
