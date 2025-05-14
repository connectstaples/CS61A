""" Juniper Interview

Asked how to start venv and pip program 

OOP: encapsulation, inheritance, polymorphism, and abstraction

microservices: Independent efficient program
monolithic application: Dependent; all components are interconnected and share memory/state; all run as same process
Multithreading: Multiple threads within the same process interact

"""
# import numpy as np
import pandas as pd

file = "/file path"
file1 = "/file path"


read_write = pd.read_csv(file) 
read_write1 = pd.read_csv(file1) 


# mask func that will print out the different values in the same two files; automatically T/F and print remaining 
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.mask.html

comparison = read_write != read_write1
difference = pd.DataFrame(comparison, other=read_write1, inplace=False)

print(f'Difference in two csv files {difference}')

