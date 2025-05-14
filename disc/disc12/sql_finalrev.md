#### CS61A Apollo Loh 
# SQL and Final Review
#### Sean Villegas


## `FROM`
- We might need to select multiple tables. Use aliases if they duplicate 


## `GROUP BY`
What does the `GROUP BY` function look like in memory? 
- `HAVING`:
    - create groups with a filter, having applies to the groups 
    - 


## Data 
```sql
CREATE TABLE pizzas AS
  SELECT "Artichoke" AS name, 12 AS open, 15 AS close UNION
  SELECT "La Val's"         , 11        , 22          UNION
  SELECT "Sliver"           , 11        , 20          UNION
  SELECT "Cheeseboard"      , 16        , 23          UNION
  SELECT "Emilia's"         , 13        , 18;

CREATE TABLE meals AS
  SELECT "breakfast" AS meal, 11 AS time UNION
  SELECT "lunch"            , 13         UNION
  SELECT "dinner"           , 19         UNION
  SELECT "snack"            , 22;
```

## Q1 
You'd like to have pizza before 13 o'clock (1pm). Create a opening table with the names of all pizza places that open before 13 o'clock, listed in reverse alphabetical order.

- To order by name in reverse alphabitical order, write ORDER BY name DESC.

| name | 
| ---- |
| Sliver | 
| La Val's |
| Artichoke | 

```sql
CREATE TABLE opening AS
    SELECT name
    FROM pizzas
    WHERE open < 13
    ORDER BY name < name DESC; # check this one
```

## Q2
You're planning to study at a pizza place from the moment it opens until 14 o'clock (2pm). 

Create a table study with two columns, the name of each pizza place and the duration of the study session you would have if you studied there (the difference between when it opens and 14 o'clock). For pizza places that are not open before 2pm, the duration should be zero. Order the rows by decreasing duration.
- Hint: Use an expression of the form MAX(_, 0) to make sure a result is not below 0.
    - any negative numbers become 0 

```sql
/* 
IDEA: 
    1. name, duration (do math )  -- difference between opening and 14
    2. pizza places not open before 2pm == 0 -- MAX(14, 0) 
    3. order rows by decreasing duration 
*/ 

CREATE TABLE study AS
    SELECT name, MAX(14 - open, 0) as duration
    FROM pizzas
    WHERE 
    ORDER BY 
```

## Q3 
What's still open for a late night snack? Create a late table with one column named status that has a sentence describing the closing time of each pizza place that closes at or after snack time. Important: Don't use any numbers in your SQL query! Instead, use a join to compare each restaurant's closing time to the time of a snack. The rows may appear in any order.

| status | 
| --- | 
| Cheeseboard closes at 23 | 
| La Val's closes at 22| 

```sql
CREATE TABLE late AS
  SELECT a.name || " closes at " || a.close AS status 
  FROM pizzas as a, meals as b 
  WHERE b.time <= a.close;

-- answer 
CREATE TABLE late AS
  SELECT name || " closes at " || close AS status 
  FROM pizzas, meals
  WHERE meal="snack" AND time <= close;
```

## Q4
If two meals are more than 6 hours apart, then there's nothing wrong with going to the same pizza place for both, right? Create a `double` table with three columns. 

1. The first column is the earlier meal
2. The second column is the later meal, 
3. Name column is the name of a pizza place. 

Only include rows that describe two meals that are more than 6 hours apart and a pizza place that is open for both of the meals. The rows may appear in any order.

```sql

/* 
IDEA: 
    1. Which pizza place is open for both of the meals
    2. rows with two meals that are .time > 6 AND .open >= a.time AND .open <= b.time
    3. 

*/ 

-- skeleton 
CREATE TABLE double AS  
  SELECT AS first,  AS second, name
  FROM , , pizzas 
  WHERE
    multiline answer here

     ;


CREATE TABLE double AS  
  SELECT a.meal AS first,  b.meal AS second, name
  FROM meals as a, meals as b, pizzas 
  WHERE 
    multiline answer here

     ;


```



## Final
- don't focus on `except` not in scope 
- difference between lambda and mu? 
- pair class in project
- do class OOP/Inheritance, generators review 
    - recorded on zoom? 
- 2 practice exam 3 hour straights 
- rubber-ducking concepts 
