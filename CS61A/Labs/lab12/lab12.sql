.read sp19data.sql

-- Q2
CREATE TABLE obedience AS
  SELECT seven, animal from students;

-- Q3
CREATE TABLE smallest_int AS
  SELECT time, smallest from students where smallest> 2 order by smallest LIMIT 20;

-- Q4
CREATE TABLE matchmaker AS
  SELECT a.pet, a.song, a.color, b.color FROM students AS a, students AS b WHERE a.pet = b.pet and a.song = b.song and a.time < b.time;
