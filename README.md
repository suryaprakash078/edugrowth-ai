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