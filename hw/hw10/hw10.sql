CREATE TABLE parents AS
  SELECT "ace" AS parent, "bella" AS child UNION
  SELECT "ace"          , "charlie"        UNION
  SELECT "daisy"        , "hank"           UNION
  SELECT "finn"         , "ace"            UNION
  SELECT "finn"         , "daisy"          UNION
  SELECT "finn"         , "ginger"         UNION
  SELECT "ellie"        , "finn";

CREATE TABLE dogs AS
  SELECT "ace" AS name, "long" AS fur, 26 AS height UNION
  SELECT "bella"      , "short"      , 52           UNION
  SELECT "charlie"    , "long"       , 47           UNION
  SELECT "daisy"      , "long"       , 46           UNION
  SELECT "ellie"      , "short"      , 35           UNION
  SELECT "finn"       , "curly"      , 32           UNION
  SELECT "ginger"     , "short"      , 28           UNION
  SELECT "hank"       , "curly"      , 31;

CREATE TABLE sizes AS
  SELECT "toy" AS size, 24 AS min, 28 AS max UNION
  SELECT "mini"       , 28       , 35        UNION
  SELECT "medium"     , 35       , 45        UNION
  SELECT "standard"   , 45       , 60;


-- ### P1 All dogs with parents ordered by decreasing height of their parent ###
CREATE TABLE by_parent_height AS
  -- SELECT name AS a FROM dogs, parents AS b WHERE a.name = b.name ORDER BY a.height DESC;
  -- SELECT parent as a FROM parents, dogs AS b WHERE a.parent = b.name ORDER BY b.height DESC; 
  SELECT a.child 
    FROM parents AS a, dogs AS b 
    WHERE a.parent = b.name 
    ORDER BY b.height DESC; 
-- IDEA: 
  -- column of names of ALL dogs that have a parent, ordered by height of parent dog from tallest to shortest 
  -- name as a FROM dogs, parent as b WHERE a.name = b.name AND 
  -- ORDER BY name.height DESC 

-- ### P2 The size of each dog ###
CREATE TABLE size_of_dogs AS
  SELECT a.name, b.size
    FROM dogs as a, sizes as b
    WHERE b.min < a.height AND b.max >= a.height;

-- IDEA: 
  -- use the sizes table to assign a size to a dog name based on their height
  -- outputting the dog name, and size in a 2 col tbl 
  -- min < dog.height AND max <= dog.height to qualify for column size in sizes # correction for second AND is >= 



-- [Optional] Filling out this helper table is recommended
CREATE TABLE siblings AS
  SELECT a.child AS c1, b.child AS c2 -- specify col names so you can refer to them later
  FROM parents AS a, parents AS b
  WHERE a.parent = b.parent AND a.child < b.child; -- use < when comparing strings for alphabetical order -- make sure to use the same names as they do not exist yet from SELECT clause
-- IDEA:
  -- table containing names of each pair of siblings
  -- inner JOIN implies using aliasing 
  -- listed in alphabetical order "bella and charlie..." instead of "charlie and bella..."

-- Sentences about siblings that are the same size
CREATE TABLE sentences AS
  SELECT "The two siblings, " || a.c1 || " and " || a.c2 || ", have the same size: " || b.size -- sql want " instead of '
  FROM siblings AS a, size_of_dogs AS b, size_of_dogs AS c
  WHERE a.c1 = b.name AND a.c2 = c.name AND b.size = c.size;

  -- IDEA:
    -- two pairs of siblings with same size
    -- create table that has a row with a sentence describing siblings by their size for each pair 
    -- use size_of_dogs for size
  


-- Height range for each fur type where all of the heights differ by no more than 30% from the average height

CREATE TABLE low_variance AS
  SELECT a.fur, max(a.height) - min(a.height) as h_range
  FROM dogs as a
  GROUP BY a.fur HAVING 
    max(a.height) <= 1.3 * avg(a.height) AND min(a.height) >= 0.7 * avg(a.height);

-- IDEA: 
  -- table with height range (difference between max and min height) for all dogs that have same fur type
  -- this is only for fur types where each dog is 30% within average height of all dogs with fur type
  -- e.g. avg h for short haired dogs is 10, to be included in output all dogs with short hair need a height at most 13 and at least 7 
