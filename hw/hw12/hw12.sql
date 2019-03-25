CREATE TABLE parents AS
  SELECT "abraham" AS parent, "barack" AS child UNION
  SELECT "abraham"          , "clinton"         UNION
  SELECT "delano"           , "herbert"         UNION
  SELECT "fillmore"         , "abraham"         UNION
  SELECT "fillmore"         , "delano"          UNION
  SELECT "fillmore"         , "grover"          UNION
  SELECT "eisenhower"       , "fillmore";

CREATE TABLE dogs AS
  SELECT "abraham" AS name, "long" AS fur, 26 AS height UNION
  SELECT "barack"         , "short"      , 52           UNION
  SELECT "clinton"        , "long"       , 47           UNION
  SELECT "delano"         , "long"       , 46           UNION
  SELECT "eisenhower"     , "short"      , 35           UNION
  SELECT "fillmore"       , "curly"      , 32           UNION
  SELECT "grover"         , "short"      , 28           UNION
  SELECT "herbert"        , "curly"      , 31;

CREATE TABLE sizes AS
  SELECT "toy" AS size, 24 AS min, 28 AS max UNION
  SELECT "mini"       , 28       , 35        UNION
  SELECT "medium"     , 35       , 45        UNION
  SELECT "standard"   , 45       , 60;

-------------------------------------------------------------
-- PLEASE DO NOT CHANGE ANY SQL STATEMENTS ABOVE THIS LINE --
-------------------------------------------------------------

-- The size of each dog
CREATE TABLE size_of_dogs AS
  SELECT a.name, b.size
  FROM dogs AS a, sizes AS b
  WHERE b.min < a.height AND a.height <= b.max;

-- All dogs with parents ordered by decreasing height of their parent
CREATE TABLE by_height AS
  SELECT a.child
  FROM parents AS a, dogs AS b
  WHERE a.parent = b.name
  ORDER BY b.height DESC;

-- Filling out this helper table is optional
CREATE TABLE siblings AS
  SELECT a.child AS s1, b.child AS s2
  FROM parents AS a, parents AS b
  WHERE a.parent = b.parent AND a.child < b.child;

-- Sentences about siblings that are the same size
CREATE TABLE sentences AS
  SELECT a.s1 || " and " || a.s2 || " are " || b1.size || " siblings"
  FROM siblings AS a, size_of_dogs AS b1, size_of_dogs AS b2
  WHERE a.s1 = b1.name AND a.s2 = b2.name AND b1.size = b2.size;

-- Ways to stack 4 dogs to a height of at least 170, ordered by total height
CREATE TABLE stacks_helper(dogs, stack_height, last_height);

-- Add your INSERT INTOs here
INSERT INTO stacks_helper(dogs, stack_height, last_height)
  SELECT name, height, height
  FROM dogs;

INSERT INTO stacks_helper(dogs, stack_height, last_height)
  SELECT a.dogs || ", " || b.name, a.stack_height + b.height, b.height
  FROM stacks_helper AS a, dogs AS b
  WHERE b.height > a.last_height;

INSERT INTO stacks_helper(dogs, stack_height, last_height)
  SELECT a.dogs || ", " || b.name, a.stack_height + b.height, b.height
  FROM stacks_helper AS a, dogs AS b
  WHERE b.height > a.last_height;

INSERT INTO stacks_helper(dogs, stack_height, last_height)
  SELECT a.dogs || ", " || b.name, a.stack_height + b.height, b.height
  FROM stacks_helper AS a, dogs AS b
  WHERE b.height > a.last_height;

CREATE TABLE stacks AS
  SELECT dogs, stack_height
  FROM stacks_helper
  WHERE stack_height >= 170
  ORDER BY stack_height;

-- Second Method
-- Ways to stack 4 dogs to a height of at least 170, ordered by total height
CREATE TABLE stacks AS
  WITH stacks(dogs, num, so_far_height, last_dog_height) AS (  -- last_dog_height is set to control the order of dog
    SELECT name, 1, height, height FROM dogs UNION
    SELECT dogs || ', ' || name, num+1, so_far_height + height, height FROM stacks, dogs
    WHERE num <= 3 AND height > last_dog_height
  )
  SELECT dogs, so_far_height FROM stacks WHERE so_far_height >= 170 ORDER BY so_far_height;
