

ALTER TABLE mydb.objectOwner
ADD COLUMN created DATE DEFAULT NULL;

select * from objectOwner;

CREATE TRIGGER objectOwner_created 
after INSERT ON objectOwner
FOR EACH ROW 
UPDATE objectOwner SET NEW.created=now()
WHERE objectOwner.object_id = NEW.object_id;



INSERT INTO objectOwner
VALUES (8,"Oleg","+38901234",NULL);





