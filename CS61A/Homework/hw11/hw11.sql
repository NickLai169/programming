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
  SELECT a.name, b.size FROM sizes AS b, dogs AS a WHERE a.height <= b.max AND a.height > b.min ORDER BY a.name;

-- All dogs with parents ordered by decreasing height of their parent
CREATE TABLE by_parent_height AS
  SELECT a.child FROM parents AS a, dogs AS b WHERE a.parent = b.name ORDER BY -b.height;

-- Filling out this helper table is optional
CREATE TABLE siblings AS
  SELECT a.child AS "sib_A", b.child AS "sib_B", c.height AS "height_of_A", d.height AS "height_of_B"
  FROM parents AS a, parents AS b, dogs AS c, dogs AS d
  WHERE a.parent = b.parent AND a.child != b.child AND a.child < b.child
  AND c.name = a.child AND d.name = b.child;


-- Sentences about siblings that are the same size
CREATE TABLE sentences AS
  SELECT a.sib_A||" and "||a.sib_B||" are "||b.size||" siblings"
  FROM siblings AS a, sizes AS b
  WHERE a.height_of_A <= b.max AND a.height_of_A > b.min AND a.height_of_B <= b.max AND a.height_of_B > b.min ORDER BY -a.sib_A;

-- Ways to stack 4 dogs to a height of at least 170, ordered by total height
CREATE TABLE stacks_helper(dogs, stack_height, last_height);
INSERT INTO stacks_helper SELECT name, height, height FROM dogs;
INSERT INTO stacks_helper(dogs, stack_height, last_height)
SELECT dogs || ", " || name, stack_height + height, height FROM dogs, stacks_helper WHERE height > last_height;

INSERT INTO stacks_helper(dogs, stack_height, last_height)
SELECT dogs || ", " || name, stack_height + height, height FROM dogs, stacks_helper WHERE height > last_height;

INSERT INTO stacks_helper(dogs, stack_height, last_height)
SELECT dogs || ", " || name, stack_height + height, height FROM dogs, stacks_helper WHERE height > last_height;
-- Add your INSERT INTOs here


CREATE TABLE stacks AS
  SELECT dogs, stack_height FROM stacks_helper WHERE stack_height > 170 ORDER BY stack_height;
