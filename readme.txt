Crate database table
CREATE TABLE students (
	id serial PRIMARY KEY,
	fname VARCHAR ( 40 ) NOT NULL,
	lname VARCHAR ( 40 ) NOT NULL,
	email VARCHAR ( 40 ) NOT NULL
);

SELECT * FROM students 

INSERT INTO students (fname, lname, email)
VALUES('cairocoders','ednalan', 'cairocoders@gmail.com');

Multiple insert
INSERT INTO
    students(id,fname,lname,email)
VALUES
    ('Quinn','Flynn'', 'Flynn'@gmail.com'),
    ('Tiger','nizon', 'nizon@gmail.com'),
    ('Airi','sato', 'sato@gmail.com');