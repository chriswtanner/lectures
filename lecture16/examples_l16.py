"""
LECTURE 17 -  NUMPY AND PANDAS
Introduction: We have analyzed data using the fundamentals of python.
While this is okay, it is not optimized for analysis on large sets of
data. Numpy and Pandas provide new tools for numerical data analysis.
"""


"""
NUMPY -- supports computing on large arrays of data.
Python lists don't have notions of math operations like addition,
subtraction, multiplication, and division and require long loops, which
can become ugly and slow. Numpy helps us solve this problem.

More info: numpy.org
With anaconda, we have all the necessary tools to use numpy.
"""

import numpy as np

# basic data structure is an array of fixed length
# (can't append items to the same list, if you try, it's actually
# making a new copy of the list and returning the new copy)
li = [0,1,2,3,4,5,6,7,8,9]
li2 = [4,5,6,7,8]


matrix = np.zeros((3,4))
matrix1 = np.ones((3,4))

print(matrix1 + matrix)
'''
# The arrays don't support different types. If so, it will guess the
# type. For below, it'll make everyhting a string
array = np.array([0,1,2.5])

#Kind of like python's range function, we can use arange
array = np.arange(10)
array = np.arange(1,10,.1)

#indexing and slicing an array work like a list.
print(array[0])
print(array[len(array)-1])
print(array[-1]) #getting last element another way
print(array[[0,1,19]]) #passing in multiple indices to get multiple elements

#Operators (+,-,/,*) work element-wise.
array = array + array - array * array

#Comparison Operators:
#This will return another array, where each index represents
#the truth value of the comparison at each index.
array == array
array != array
#how to get whether each value is positive
array > 0
array < 0

#Summarizing Operators -- max and min of elements in the array
np.min(array)
np.max(array)

#minimum and maximum -- takes in 2 arrays and finds the
#minimum at each index
np.minimum(array, array[::-1]) #the array and reversed array

#Math Operators
np.sum(array)
np.mean(array)
np.median(array)
np.var(array)
np.std(array)

#trigonometry
np.sin(array)
np.cos(array)
np.sqrt(array)

#Filtering an array
#Let's say we want to get indices of all elements greater than 0
are_positive = array>0.0 #are_positive is an array of booleans
array[are_positive] #returns array of elements in original array that are >0.0

array[array>0.0] #another way of writing the above

#indexing into a matrix
print(m[0,1])
print(m[0:10,0]) #getting all rows, first col of data
print(m[:,0]) #getting all elements in a single column
print(m[0,:]) #getting all elements in a single row

#assigning a value/list to a slice of values
m[0,:] = 1 #first row of matrix to be 1s
print(m)

#Comparison Operators -- not that this causes matrix to lose its shape!
m[m>5] #notice that this returns a single list of numbers

#math operators - must match dimensions
print(m+m)
print(m-m)

#Maximum/minimum -- also must be same shape
np.maximum(m,m[::-1,::-1]) #m[::-1,::-1] reverses all values in cols and rows

#Other summarizing math operators
np.max(m)
np.max(m,axis=0) #max value for each column
np.max(m,axis=1) #max along all the rows
np.mean(m,axis=1)
np.sum(m,axis=0)
#if you don't specify axis, will compute over whole matrix
np.sum(m)

"""
PANDAS -- data analysis library built on top of numpy.

More info: pandas.pydata.org
With anaconda, we have all the necessary tools to use numpy.
"""

import pandas as pd
import numpy as np

#create a series, similar to numpy 1d array
series = pd.Series(np.arange(10))

#supports giving a customized index value to each values
series = pd.Series(np.arange(5), index=['zero','one','two','three','four'])
print(series[0])
print(series['zero'])
print(series['one':'three']) #can even do slicing

#We can even create a series from a dict
series= pd.Series({"one":1, "two":2, "three":3})

#basic math operations
series + series - series
np.mean(series)


#power of pandas -- dataframe datastruture
#Convinient to read a dataframe from csv file!
data_frame = pd.read_csv("data.csv")
data_frame.head() #shows the first few rows of data
data_frame.tail() #last few rows of data
data_frame.describe() #summary of data (headers, summary operations for each col).
data_frame["header name"] #to refer to specific columns by header name
data_frame[0:3] #to refer to specific rows (first 3 rows of each column)
data_frame.iloc[0] #specific row
data_frame.at[0,'header name'] #getting a single data point

#adding another column
data_frame["another column"]  = 10.0 - data_frame["header name"]
print(data_frame["another column"])

# filtering
data_frame[data_frame["header"]>7] #return rows that are greater than 7
data_frame[data_frame["header"]>7]["another header"] #another col that corresponds to the rows greater than 7

#summarizing ops  -- only occur on single axis (must specify)
data_frame.mean() #mean of col data
data_frame.max(axis=1) #by row

#writing to csv file
data_frame.to_csv("output_file_name.csv")

#reading and writing to excel files
data_frame.to_excel("excel_file_name.xlsx", sheet_name="Sheet1")
pd.read_excel("file_name.xlsx")
'''
