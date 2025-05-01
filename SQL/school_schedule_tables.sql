USE schoolschedules;

CREATE TABLE students (
    studentid int NOT NULL,
    lastname varchar(25) NOT NULL,
    firstname varchar(25) NOT NULL,
    grade int NOT NULL,
    DOB datetime NOT NULL,
    scheduleid int,
    honorsstatus bool NOT NULL,
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
