**Students Table (MSSQL)**

-   studentid int (Primary Key)
-   lastname varchar(25)
-   firstname varchar(25)
-   grade int
-   DOB datetime
-   scheduleid int
-   honorsstatus bool
-   GPA float

**Schedules Table (Mongo)**

-   scheduleid int
-   schedule Document
    -   1st sectionid int
    -   2nd sectionid int
    -   3rd sectionid int
    -   4th sectionid int
    -   5th sectionid int
    -   6th sectionid int

**Teachers Table (MSSQL)**

-   teacherid int
-   lastname varchar(25)
-   firstname varchar(25)
-   yearstaught int
-   scheduleid int

**Sections Table (MSSQL)**

-   sectionid int
-   teacherid int
-   name varchar(40)
-   period int
-   grade int
-   capacity int
-   subject varchar(15)
