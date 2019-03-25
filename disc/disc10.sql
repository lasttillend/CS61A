-- SQL
CREATE TABLE records AS
    SELECT "Ben Bitdiddle" AS name, "Computer" AS division, "wizard" AS title, 60000 AS salary, "Oliver Warbucks" AS supervisor UNION
    SELECT "Alyssa P Hacker", "Computer", "Programmer", 40000, "Ben Bitdiddle" UNION
    SELECT "Cy D Fect", "Computer", "Programmer", 35000, "Ben Bitdiddle" UNION
    SELECT "Lem E Tweakit", "Computer", "Technician", 25000, "Ben Bitdiddle" UNION
    SELECT "Louis Reasoner", "Computer", "Programmer Trainee", 30000, "Alyssa P Hacker" UNION
    SELECT "Oliver Warbucks", "Administration", "Big Wheel", 150000, "Oliver Warbucks" UNION
    SELECT "Eben Scrooge", "Accounting", "Chief Accounting", 75000, "Oliver Warbucks" UNION
    SELECT "Robert Cratchet", "Accounting", "Scrivener", 18000, "Eben Scrooge";

CREATE TABLE meetings AS
    SELECT "Accounting" AS division, "Monday" AS day, "9am" AS time UNION
    SELECT "Computer", "Wednesday", "4pm" UNION
    SELECT "Administration", "Monday", "11am" UNION
    SELECT "Administration", "Thursday", "1pm";

-- 2.1
SELECT name
FROM records
WHERE supervisor = "Oliver Warbucks";

-- 2.2
SELECT *
FROM records
WHERE name = supervisor;

-- 2.3
SELECT name
FROM records
WHERE salary > 50000
ORDER BY name;

-- 3.1
SELECT b.name AS employee, b.salary, b.supervisor, a.salary
FROM records AS a, records AS b
WHERE a.name = b.supervisor AND a.salary > 2 * b.salary;

-- 3.2
SELECT b.name
FROM records AS a, records AS b
WHERE a.name = b.supervisor AND a.division <> b.division;

-- 3.3
SELECT b.day, b.time
FROM records AS a, meetings AS b
WHERE a.division = b.division AND a.supervisor = "Oliver Warbucks";

-- 3.4
SELECT DISTINCT a.name
FROM records AS a, records AS b
WHERE a.name = b.supervisor AND a.name <> a.supervisor;

-- 3.6
SELECT r2.name
FROM records AS r1, records AS r2, meetings AS m1, meetings AS m2
WHERE r1.division = m1.division AND r2.division = m2.division AND r1.name = r2.supervisor AND m1.day = m2.day AND r1.name <> r1.supervisor;

-- Modifying Tables
CREATE TABLE dogs (name, age, phrase DEFAULT "woof");

INSERT INTO dogs (name, age) VALUES ("Fido", 1), ("Sparky", 2);
INSERT INTO dogs VALUES ("Lassie", 2, "I'll save you!"), ("Floory", 3, "Much doge");

UPDATE dogs SET age = age + 1; -- If condition isn't specified, every row is updated
UPDATE dogs SET phrase = "bark" WHERE age = 2;
DELETE FROM dogs WHERE age = 3;

DROP TABLE dogs;

-- 4.1
INSERT INTO dogs (age, name) VALUES ("Rover", 3);

UPDATE dogs SET name = age, age = name WHERE name;

DELETE FROM dogs WHERE age < 3;
