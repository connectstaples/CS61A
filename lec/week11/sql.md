#### CS61A Sp25 Prof Denero
# SQL 
#### Sean Villegas


## Notes
- you can use `sqlite3` terminal command (built in for mac and linux) or use [sql interpreter](sql.cs61a.org)
- select statements display to user but arent stored; instructional language
- `UNION` of two `SELECT` statements are a table of the result of their own data
- other commands: 
    - `AND`
    - `INSERT`
    - `DELETE`
## Creating tables

Code: 
```sql
CREATE TABLE [table_name] AS 
    SELECT [value1] AS [col1], [val2] AS [col2] UNION
    SELECT [value3], [value4], UNION 
    SELECT [value5], [value6] ... 
```
Structure: 

| Column Name | Column Name| 
| ---- | --- |
| value1 | value2 |


## SQL Queries 

- you can perform arithmetic on columns
    - if you want float just change one of the numbers into a float to produce a float 
- `LIMIT` -- how many values to select 
- `GROUP BY [columns]`
- `HAVING [conditions] -- condition on aggregation / filters groups`
- `count(*)`
- basic arithmetic and equality/comparison statements apply 


```sql 

SELECT [columns] FROM [tables] WHERE [condition] ORDER BY [columns] LIMIT [limit]; 


SELECT [col1], [col2 / (51 * 40) AS [new_col_name]] FROM records; 


```

## Joining 
- select data from multiple tables 
- make sure to use `ON` clause after a `JOIN`  
```sql
SELECT * from [table_name], [table_name1]

-- combining rows when they have the same name implies dot notation 
 
/*
SELECT * from [table_name], [table_name1] where [table_name].[col_name] = [table_name1].[col_name1]
*/

SELECT * from meetings, records where meeting.division = record.divison 
```

## Aliasing 
- you can filter based on condition, "value" or col_name will return a table based on different filtering
```sql
SELECT [column] AS [new_name]

SELECT [original column name] AS [new_name], [original column name1], [new_name1] FROM [og table] AS ...
```
- rename output column in the result of that query
- doesnt alter original table
- useful when joining a table with itself or having shorter names
- `AS` gives a new name

## String Expressions
```sql
sql> SELECT "hello, " || "world"; 
-- outputs ; hello, world 
```

## `GROUP BY` -- aggregation 
- perform operations on groups of data

How it works: 
1. splits rows into separate "tables" based on columns provided 
2. runs aggregator for each table
3. combines data back together again
