CREATE TABLE finals AS
  SELECT 'RSF' AS hall, '61A' AS course UNION
  SELECT 'Wheeler'    , '61A'           UNION
  SELECT 'Pimentel'   , '61A'           UNION
  SELECT 'Li Ka Shing', '61A'           UNION
  SELECT 'Stanley'    , '61A'           UNION
  SELECT 'RSF'        , '61B'           UNION
  SELECT 'Wheeler'    , '61B'           UNION
  SELECT 'Morgan'     , '61B'           UNION
  SELECT 'Wheeler'    , '61C'           UNION
  SELECT 'Pimentel'   , '61C'           UNION
  SELECT 'Soda 310'   , '61C'           UNION
  SELECT 'Soda 306'   , '10'            UNION
  SELECT 'RSF'        , '70';

CREATE TABLE sizes AS
  SELECT 'RSF' AS room, 900 AS seats    UNION
  SELECT 'Wheeler'    , 700             UNION
  SELECT 'Pimentel'   , 500             UNION
  SELECT 'Li Ka Shing', 300             UNION
  SELECT 'Stanley'    , 300             UNION
  SELECT 'Morgan'     , 100             UNION
  SELECT 'Soda 306'   , 80              UNION
  SELECT 'Soda 310'   , 40              UNION
  SELECT 'Soda 320'   , 30;

CREATE TABLE sharing AS
  SELECT a.course, COUNT(DISTINCT a.hall) AS shared FROM finals AS a, finals AS b WHERE a.hall = b.hall AND a.course != b.course GROUP BY a.course;

-- IDEA: 
  -- Name of course from finals, 
  -- number of rooms the course uses that are also shared with other courses as shared 
  -- inner join => aliasing 


CREATE TABLE pairs AS
  SELECT a.room || ' and ' || b.room || ' together have ' || (a.seats + b.seats) || ' seats' AS rooms
    FROM sizes AS a, sizes AS b WHERE (a.seats + b.seats) >= 1000 AND a.room != b.room AND a.room < b.room
    ORDER BY (a.seats + b.seats) DESC;

-- IDEA: 
  -- string representation of one column with the rooms with pairs of rooms that have 1,000 seats together
  -- Two room names in alphabetical order
  -- State combined number of seats in two rooms 
  -- Only include the pairs where seats total are at least 1000
    -- rows are in decreasing order of total seats (DESC)

CREATE TABLE big AS
  SELECT course FROM finals, sizes AS a WHERE hall == a.room GROUP BY course HAVING sum(seats) >= 1000;

-- IDEA: 
  -- create big table with one column that has the course string name FROM finals 
  -- include courses WHERE total number of seats across all final exam rooms FROM sizes is >= 1000
  -- each course should appear in its own row

CREATE TABLE remaining AS
  SELECT course, sum(b.seats) - max(b.seats) AS remaining
  FROM finals as a, sizes as b WHERE a.hall = b.room GROUP BY a.course;

-- IDEA: 
  -- remaining table with two cols (course from finals) and (remaining (seats from sizes))
  -- remaining should be total number of seats in all rooms used for that course,
    -- exclude room with largest number of seats i.e. the max(seats)
  -- include one row for each course that is the sum of seats from all BUT largest room