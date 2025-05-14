#### Sean Villegas
# A guide on Shallow Copies v.s. Pointers (Deep copies)
#### Python

## Lists
- `pointers` are references to original `values`
- `shallow` copies create pointers to inner lists (sub lists)
    - therefore, elements in a list will be shallow copies **EXCEPT** the sublists within
    - in other words: **it shallow copies top level elements only**
    - You are able to mutate sub-objects such as `lists`, `dicts`, `custom objects`
- You cannot perform arithmetic on each elements of the lists unless with brackets and an iterative process
- You can concatenate lists with `+`; which will add the elements of the list together to create the list but NOT add every element to each element
- `list` will create a shallow copy, and it doesn't create a list on a list (i.e. no sublist will form if its already a list)
- `copy` is a shallow copy
- 

## Syntax
_Creating a `pointer` to original list elements in python via **referencing**_

```python
lst = [12, 13]
lst1 = [19, 20]
reference = [lst, lst1] # OR [lst] + [lst1] OR []
```
### Shallow Copies 
_creating shallow copies of a list_

```python
lst = [12, 13]
lst1 = [19, 20]
shallow = [lst[:], lst[:]] # OR lst() OR copy() OR any sort of indexing of elements with slicing
```
