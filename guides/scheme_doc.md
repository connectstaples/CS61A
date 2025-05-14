#### CS61A Scheme 
#### [Official Scheme Guide](https://cs61a.org/articles/scheme-spec)
# Docs for using CS61A Program `Scheme`
#### Sean Villegas

_I created this doc so its a quick reference compared to their webpage guide TLDR_

#

# When in doubt ASK: 
- Am I using prefix notation? 
- Am I checking parenthesis? 
- For most problems in CS61A Scheme, apply recursion
    - "In python, this can be solved with a for loop. This implies I use recursion"

# Quick Table Reference 

# Section 1: `Special Forms` 

## `cond`

Rules: 
- `cond` is already if, elif, else logic. 
    - You do not need to specify(write) if, or elif. Just else
- 

## `even?`
- self explanatory, will check if your parameter passed in is even
    - **note**: this only allows for one parameter to be checked. Increase functionality with if else logic, `and`, `mapand`, or `map`
- `even?` returns boolean logic that can be further used in programs to execute certain branches

```scheme
(even? x) ; > (even? 2) ; returns #t
```

## `zero?`