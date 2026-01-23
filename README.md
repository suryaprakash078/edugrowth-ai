-- Create Database
CREATE DATABASE college;
USE college;

-- Department table
CREATE TABLE dept (
  deptid NUMBER(2) PRIMARY KEY,
  deptname VARCHAR(20),
  loc VARCHAR(10)
);

INSERT INTO dept VALUES
(1,'cs','cbe'),
(2,'cs','cbe'),
(3,'it','che'),
(4,'ct','erd');

-- Employee table
CREATE TABLE empl (
  empid NUMBER(4) PRIMARY KEY,
  empname VARCHAR(10),
  deptid NUMBER(2),
  FOREIGN KEY (deptid) REFERENCES dept(deptid)
);

INSERT INTO empl VALUES
(101,'aa',1),
(102,'bb',2),
(103,'cc',1),
(104,'dd',3);

-- INNER JOIN
SELECT d.deptname, e.empname
FROM dept d JOIN empl e
ON d.deptid = e.deptid
WHERE d.deptid > 2
ORDER BY d.deptname;

-- LEFT OUTER JOIN
SELECT d.deptname, e.empname
FROM dept d LEFT JOIN empl e
ON d.deptid = e.deptid
WHERE d.deptid > 2
ORDER BY d.deptname;

-- RIGHT OUTER JOIN
SELECT d.deptname, e.empname
FROM dept d RIGHT JOIN empl e
ON d.deptid = e.deptid
WHERE d.deptid > 2
ORDER BY d.deptname;

-- FULL OUTER JOIN
SELECT d.deptname, e.empname
FROM dept d FULL JOIN empl e
ON d.deptid = e.deptid
WHERE d.deptid > 2
ORDER BY d.deptname;

-- CROSS JOIN
SELECT d.deptname, e.empname
FROM dept d CROSS JOIN empl e
WHERE d.deptid > 2
ORDER BY d.deptname;


-- Table creation
CREATE TABLE exe6 (
  id NUMBER(10),
  fname VARCHAR2(15),
  lname VARCHAR2(15),
  email VARCHAR2(30),
  hiredate VARCHAR2(20),
  jodid VARCHAR2(10),
  salary NUMBER(10),
  mid NUMBER(5),
  deptid NUMBER(5)
);

-- Insert records
INSERT INTO exe6 VALUES (761,'deepika','balu','deepabalu2005@gmail.com','05-11-2005','ap',70000,123,12);
INSERT INTO exe6 VALUES (763,'madhu','hasini','medhunhasini2014@gmail.com','12-03-2014','ap',70000,124,12);
INSERT INTO exe6 VALUES (765,'jeen','mersaline','jeenmarsaline2002@gmail.com','10-01-2002','HOD',100000,NULL,12);
INSERT INTO exe6 VALUES (767,'sambath','kumar','sambathkumar2004@gmail.com','04-12-2004','HOD',100000,NULL,15);
INSERT INTO exe6 VALUES (769,'nandhini','mam','nandhini2011@gmail.com','09-10-2011','ap',60000,125,15);
INSERT INTO exe6 VALUES (721,'siva','kumar','sivakumar2016@gmail.com','08-05-2016','ap',65000,126,15);

-- Display all
SELECT * FROM exe6;

-- Salary greater than Madhu
SELECT fname||' '||lname AS name
FROM exe6
WHERE salary > (SELECT salary FROM exe6 WHERE id = 763);

-- Same job as Nandhini
SELECT fname||' '||lname AS name, salary, deptid, jodid
FROM exe6
WHERE jodid = (SELECT jodid FROM exe6 WHERE id = 769);

-- Salary above average
SELECT id, fname||' '||lname AS name
FROM exe6
WHERE salary > (SELECT AVG(salary) FROM exe6);

-- Same salary as Deepika
SELECT *
FROM exe6
WHERE salary = (SELECT salary FROM exe6 WHERE fname = 'deepika');