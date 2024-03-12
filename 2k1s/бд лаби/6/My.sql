INSERT INTO object (name,adress,type)
VALUES ("Olvia","first str.","Ecohouse" );
INSERT INTO object (name,adress,type)
VALUES ("Mandarun","sec str.","Shop" );
INSERT INTO object(name,adress,type) 
VALUES ("-","third str.","House" );
INSERT INTO object (name,adress,type)
VALUES ("Sunshine","forth str.","Ecohouse" );
INSERT INTO object (name,adress,type)
VALUES ("Express","fifth str.","Shop" );
INSERT INTO object (name,adress,type)
VALUES ("-","sixth str.","House" );
INSERT INTO object (name,adress,type)
VALUES ("Ecoclub","seventh str.","Ecohouse" );
INSERT INTO object (name,adress,type)
VALUES ("-","eight str.","House" );


INSERT INTO team (type,object_id)
VALUES ("Fast",1);
INSERT INTO team (type,object_id)
VALUES ("Fast",2);
INSERT INTO team (type,object_id)
VALUES ("Medium",3);
INSERT INTO team (type,object_id)
VALUES ("Medium",4);
INSERT INTO team (type,object_id)
VALUES ("Medium",5);
INSERT INTO team (type,object_id)
VALUES ("Slow",6);
INSERT INTO team (type,object_id)
VALUES ("Slow",7);
INSERT INTO team (type,object_id)
VALUES ("Extra",8);

INSERT INTO objectOwner
VALUES (1,"Petro","+38909382");
INSERT INTO objectOwner
VALUES (2,"Olga","+38932382");
INSERT INTO objectOwner
VALUES (3,"Maksym","+38907456");
INSERT INTO objectOwner
VALUES (4,"Nadija","+38909234");
INSERT INTO objectOwner
VALUES (5,"Annastasia","+38902382");
INSERT INTO objectOwner
VALUES (6,"Lubow","+380934982");
INSERT INTO objectOwner
VALUES (7,"Andrij","+38906582");
INSERT INTO objectOwner
VALUES (8,"Oleg","+38901234");

INSERT INTO repair
VALUES (1,"unplanned","2022-01-08");
INSERT INTO repair
VALUES (2,"planned","2021-02-02");
INSERT INTO repair
VALUES (3,"unplanned","2020-01-10");
INSERT INTO repair
VALUES (4,"planned","2019-01-09");
INSERT INTO repair
VALUES (5,"unplanned","2022-08-08");
INSERT INTO repair
VALUES (6,"planned","2018-11-08");
INSERT INTO repair
VALUES (7,"unplanned","2172-01-11");
INSERT INTO repair
VALUES (8,"unplanned","2025-02-10");

INSERT INTO repair
VALUES (4,"planned","2016-02-05");
INSERT INTO repair
VALUES (8,"uplanned","2020-12-12");
INSERT INTO repair
VALUES (3,"planned","2020-12-5");
INSERT INTO repair
VALUES (2,"uplanned","2018-02-06");
INSERT INTO repair
VALUES (5,"planned","2023-06-03");
INSERT INTO repair
VALUES (3,"uplanned","2018-11-08");
INSERT INTO repair
VALUES (5,"planned","2020-01-11");
INSERT INTO repair
VALUES (3,"planned","2023-01-7");


INSERT INTO employee(team_id,name,phone,position)
VALUES (1,"Ostap","+38023548","builder");
INSERT INTO employee(team_id,name,phone,position)
VALUES (1,"Andriy","+38045423","builder");
INSERT INTO employee(team_id,name,phone,position)
VALUES (1,"Oleg","+38023423","Leader");

INSERT INTO employee(team_id,name,phone,position)
VALUES (2,"John","+38058901","builder");
INSERT INTO employee(team_id,name,phone,position)
VALUES (2,"Andy","+38045798","builder");
INSERT INTO employee(team_id,name,phone,position)
VALUES (2,"Molf","+380325563","Leader");

INSERT INTO employee(team_id,name,phone,position)
VALUES (3,"Maksym","+38023548","builder");
INSERT INTO employee(team_id,name,phone,position)
VALUES (3,"Oliver","+38045423","builder");
INSERT INTO employee(team_id,name,phone,position)
VALUES (3,"Noah","+38023423","Leader");

INSERT INTO employee(team_id,name,phone,position)
VALUES (4,"Elijah","+38023548","builder");
INSERT INTO employee(team_id,name,phone,position)
VALUES (4,"Liam","+38045423","builder");
INSERT INTO employee(team_id,name,phone,position)
VALUES (4,"Daniel","+38023423","Leader");

INSERT INTO employee(team_id,name,phone,position)
VALUES (5,"Michael","+38023548","builder");
INSERT INTO employee(team_id,name,phone,position)
VALUES (5,"Mason","+38045423","builder");
INSERT INTO employee(team_id,name,phone,position)
VALUES (5,"Jacob  ","+38023423","Leader");

INSERT INTO employee(team_id,name,phone,position)
VALUES (6,"Luke","+38023548","builder");
INSERT INTO employee(team_id,name,phone,position)
VALUES (6,"Andriy","+38045423","builder");
INSERT INTO employee(team_id,name,phone,position)
VALUES (6,"Ezra","+38023423","Leader");

INSERT INTO employee(team_id,name,phone,position)
VALUES (7,"Gabriel","+38023548","builder");
INSERT INTO employee(team_id,name,phone,position)
VALUES (7,"Jayden","+38045423","builder");
INSERT INTO employee(team_id,name,phone,position)
VALUES (7,"Luca","+38023423","Leader");

INSERT INTO employee(team_id,name,phone,position)
VALUES (8,"Landon","+38023548","builder");
INSERT INTO employee(team_id,name,phone,position)
VALUES (8,"Colton","+38045423","builder");
INSERT INTO employee(team_id,name,phone,position)
VALUES (8,"Roman","+38023423","Leader");
