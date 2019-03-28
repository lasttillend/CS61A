-- 2 SQL

-- 4 Highly Exclusive
CREATE TABLE X AS SELECT 20 AS X;

WITH ints(n) AS
    (SELECT 1 UNION
     SELECT n + 1 FROM ints, X WHERE n < X)
    SELECT a.n, COUNT(*)
    FROM ints AS a, ints AS b
    WHERE b.n % a.n = 0 AND b.n > a.n
    GROUP BY a.n
    HAVING COUNT(*) >= 3;

-- 6 Anagrams
CREATE TABLE anagrams AS
    WITH word(letter, position) AS (
        SELECT 'c',     1 UNION
        SELECT 'a',    10 UNION
        SELECT 't',   100 UNION
        SELECT 's',  1000
    )
    SELECT w1.letter || w2.letter || w3.letter || w4.letter
    FROM word as w1, word as w2, word as w3, word as w4
    WHERE w1.position + w2.position + w3.position + w4.position = 1111;
