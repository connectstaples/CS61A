#### Sean Villegas
# A guide on Built in List Operations 
#### Python

#

## `append`
In Python, the append() method is used to add a single element to the end of a list. If you pass in a list (or any other iterable) inside brackets, that entire iterable will be added as a single element, not its individual elements.

```python
my_list = [1, 2, 3]
my_list.append([4, 5])
print(my_list) # [1, 2, 3, [4, 5]]
```


## `extend`
The extend() method, unlike append(), adds each element of an iterable to the list, not the iterable itself.

```python
my_list = [1, 2, 3]
my_list.extend([4, 5])
print(my_list) # [1, 2, 3, 4, 5]
```