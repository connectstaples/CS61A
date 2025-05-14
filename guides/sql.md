#### CS61A Guide Sp25
# SQL 
#### Sean Villegas

# 


## Writing a `SELECT` statement
1. Describe the input rows using `FROM` and `WHERE` clauses.
    - Step 1 can have joining tables (using commas) to form input rows that consist of two or more rows from existing tables 
2. Group those rows and determine which groups should appear as output rows using `GROUP BY` and `HAVING` clauses.
3. Format and order the output rows and columns using `SELECT` and `ORDER BY` clauses.

```sql
SELECT (Step 3) FROM (Step 1) WHERE (Step 1) GROUP BY (Step 2) HAVING (Step 2) ORDER BY (Step 3);
```



## `COUNT(DISTINCT x)`
- evaluates to the number of distinct values that appear in column x for a group.


## `Inner JOIN`
_as it relates to lexicographical order_ 

<details>
<summary>Logic</summary>

- Using `<` or `>` in a self-join prevents duplicate pairs by enforcing a consistent order — here's how:
    - Without < or >:
        - e.g. if you join the table to itself with just a.child != b.child, then for siblings bella and charlie, you'll get:
        ```
        (bella, charlie)
        (charlie, bella)
        ```
        - These are duplicates logically, even though the order is flipped.
        - With a.child < b.child:
            - Now you only get:
            ```
            (bella, charlie)
            ```
        - Because the join condition only keeps the pair when a.child comes alphabetically before b.child. The flipped version, (charlie, bella), fails the < condition and gets dropped.
            - i.e. it ensures no duplicates and alphabetical order
- we can assume that the < or > will handle no duplications, and that < will sort based on alphabetical order in
</details> 

**Main Takeaway:** 

- we can assume **ONLY** the `WHERE` clause with the `<` or `>` will handle no duplications, and that `<` will sort based on alphabetical order
- other clauses such as `JOIN ON`, `ORDER BY`, `SELECT`, `CASE` or `HAVING` will filter based on ordering but **does not** prevent duplicates 


## Creating helper SQL tables
There are two pairs of siblings that have the same size. Create a table that contains a row with a sentence describing the siblings by their size for each pair.

```sql
-- [Optional] Filling out this helper table is recommended
CREATE TABLE siblings AS
  SELECT "REPLACE THIS LINE WITH YOUR SOLUTION";

-- Sentences about siblings that are the same size
CREATE TABLE sentences AS
  SELECT "REPLACE THIS LINE WITH YOUR SOLUTION";
```

**Main Takeaway:**
- I learned that we can perform operations in the `SELECT` statement 
- `GROUP BY` runs aggregation on the table based on the columns you provide in the `SELECT` clause
- When performing inner joins it is important to rename them in the select statement so that the can be retrieved later 
