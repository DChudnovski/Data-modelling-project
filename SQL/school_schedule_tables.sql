USE schoolschedules;

INSERT INTO students 
VALUES (1,'Rogers','Joy',6,4.0,0,True,06-22-2012);

CREATE TABLE students (
    studentid int NOT NULL,
    lastname varchar(25) NOT NULL,
    firstname varchar(25) NOT NULL,
    grade int NOT NULL,
    GPA float,
    scheduleid int,
    honors boolean NOT NULL,
    DOB date NOT NULL,
    PRIMARY KEY (studentid)
);

CREATE TABLE teachers (
    teacherid int NOT NULL,
    lastname varchar(25) NOT NULL,
    firstname varchar(25) NOT NULL,
    yearstaught int NOT NULL,
    scheduleid int,
    PRIMARY KEY (teacherid)
);

CREATE TABLE sections (
    sectionid int NOT NULL,
    teacherid int,
    name varchar(40) NOT NULL,
    period int NOT NULL,
    grade int NOT NULL,
    capacity int,
    subject varchar(15) NOT NULL,
    PRIMARY KEY (sectionid)
)
