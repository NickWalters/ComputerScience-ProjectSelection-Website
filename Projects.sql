drop database information;
CREATE DATABASE information;
USE information;

DROP TABLE IF EXISTS Projects;
CREATE TABLE IF NOT EXISTS Projects (
	ProjectID INT(11) UNIQUE NOT NULL AUTO_INCREMENT,
    Title MEDIUMTEXT NOT NULL,
    Descrip LONGTEXT NOT NULL,
    Category TEXT, -- Example, category can be Mining, Engineering, Chemical, Software
    Unit MEDIUMTEXT,
    IPID MEDIUMTEXT,
    CreationDate TIMESTAMP,
    studentCapacity INT(11),
    
    
    sponsorUserID INT(11) NOT NULL, -- This is used to link to the Client Table, and get client information if needed
    
    PRIMARY KEY(ProjectID)
);

CREATE TABLE IF NOT EXISTS auth_user (
	UserID INT(11) UNIQUE NOT NULL AUTO_INCREMENT,
    First_Name MEDIUMTEXT NOT NULL,
    Last_Name MEDIUMTEXT NOT NULL,
    Email varchar(255) NOT NULL,
    Password varchar(25) NOT NULL,
    Phone integer NOT NULL,
    Company_Name text,
    Company_Business text,
    
    PRIMARY KEY(UserID)
);