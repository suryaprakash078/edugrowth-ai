CREATE TABLE e16 (
    empno NUMBER(20) PRIMARY KEY,
    basic NUMBER(20),
    hra   NUMBER(20),
    da    NUMBER(20),
    ded   NUMBER(20),
    net   NUMBER(20),
    gross NUMBER(20)
);

INSERT INTO e16 VALUES (&empno, &basic, &hra, &da, &ded, &net, &gross);
INSERT INTO e16 VALUES (&empno, &basic, &hra, &da, &ded, &net, &gross);

SELECT * FROM e16;

CREATE TABLE backup1 (
    empno NUMBER(20),
    gross NUMBER(20),
    net   NUMBER(20)
);

CREATE OR REPLACE TRIGGER sal_change
AFTER UPDATE ON e16
FOR EACH ROW
BEGIN
    INSERT INTO backup1 (empno, gross, net)
    VALUES (:OLD.empno, :OLD.gross, :OLD.net);
END;
/

UPDATE e16 SET basic = 30000 WHERE empno = 101;

SELECT * FROM e16;
SELECT * FROM backup1;