#!/usr/bin/env python
# coding: utf-8

# ## Numpy Exercises

# In[102]:


import numpy as np


# Use the following code for the questions below:

# In[103]:


a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])
print(a[a<0].shape)


# ### How many negative numbers are there?

# In[104]:


print(f"There are {a[a < 0].shape[0]} negative numbers.")
# We can first create a boolean mask that generates True values for each element of the array that is negative and False for all others
# [a < 0]
# Then we can use that boolean mask as an index into the array and negate the False values
# a[a < 0]
# Then we can get the shape of that array
# a[a < 0].shape --> (4,)
# In the case of a one-dimensional array, it is a tuple with one element instead of an integer value. Note that a tuple with one element has a trailing comma.
# To isolate the value from the tuple, we can call the tuple using indexing
# a[a < 0].shape[0] --> 4
# We can pass in this code to a formatted string to get the output we want


# ### How many positive numbers are there?

# In[105]:


print (f"There are {a[a > 0].shape[0]} positive numbers.")
# We use the same process as above, but we change the direction of the operand from < to >


# ### How many even positive numbers are there?

# In[5]:


print(f"There are {a[(a > 0) & (a % 2 == 0)].shape[0]} positive even numbers.")
# If we want to run multiple operands, we need to use:
# & for and
# | for or
# ~ for not
# In this case we want both positive numbers and even numbers to be True
# So our boolean mask includes both [(a > 0) & (a % 2 == 0)]
# As we did above, we can take the shape and then call index 0 to extract the value


# ### If you were to add 3 to each data point, how many positive numbers would there be?

# In[107]:


print(f"There are {(a + 3)[(a + 3) > 0].shape[0]} positive numbers if you add 3 to each data point.")
# We can call our array and apply vectorized arithmetic operators as we do so
# In this case a is replaced by a + 3, representing adding 3 to every value in array a


# In[6]:


a_plus_3 = a + 3
print(f"There are {a_plus_3[a_plus_3 > 0].shape[0]} positive numbers if you add 3 to each data point.")
# We can also assign the results of vectorized operation to a variable and use that variable name instead


# ### If you squared each number, what would the new mean and standard deviation be?

# In[17]:


a_sqr = a ** 2
print(f"The new mean is {np.mean(a_sqr)} and the new standard deviation is {np.std(a_sqr)}.")
# This is similar to above, we are simply applying the vectorized operation of squaring the values
# And then applying the np.mean() function to determine the mean and the #np.std() function to determine the standard deviation


# ### A common statistical operation on a dataset is centering. This means to adjust the data such that the center of the data is at 0. This is done by subtracting the mean from each data point. Center the data set.

# In[22]:


a_centered = a - np.mean(a)
print(a_centered)
# We create a new variable by applying vectorized operations to the original array using the result of an array function (np.mean())
# Again, we don't have to declare a variable to reach our solution, but this does make the code slightly easier to read and interpret


# ### Calculate the z-score for each data point. Recall that the z-score is given by:
# 
# Z = (value - mean) / stddev

# In[27]:


z_score_a = (a - np.mean(a)) / np.std(a)
print(z_score_a)

# We can apply multiple numpy functions simultaneously as part of the same arithmetic expression


# ## More Numpy Practice

# In[28]:


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# Use python's built in functionality/operators to determine the following:
# 
# #### Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list

# In[33]:


sum_of_a = sum(a)
# Sums all of the elements of the list


# #### Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list

# In[32]:


min_of_a = min(a)
# Finds the smallest value in a list


# #### Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list

# In[34]:


max_of_a = max(a)
# Finds the largest value in a list


# #### Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list

# In[36]:


mean_of_a = sum(a) / len(a)
# Uses length as a counting method to calculate the average


# #### Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all the numbers in the above list together

# In[38]:


product_of_a = 1
for num in a:
    product_of_a *= num

# We declare a variable and then apply looped operations to that variable 


# #### Make a variable named squares_of_a. It should hold each number in a squared like [1, 4, 9, 16, 25...]

# In[40]:


squares_of_a = [num ** 2 for num in a]
# We use list comprehension to create a new list from the elements of a
# We take every element from a, but square it as we add it to our new list


# #### Make a variable named odds_in_a. It should hold only the odd numbers

# In[41]:


odds_in_a = [num for num in a if num % 2 == 1]
# Using list comprehension again
# We take every element from a if that element is odd


# #### Make a variable named evens_in_a. It should hold only the evens.

# In[42]:


evens_in_a = [num for num in a if num % 2 == 0]
# Using list comprehension again
# We take every element from a if that element is even


# #### What about life in two dimensions? A list of lists is matrix, a table, a spreadsheet, a chessboard...
# 
# ## Setup 2
# 
# #### Consider what it would take to find the sum, min, max, average, sum, product, and list of squares for this list of two lists.

# In[43]:


b = [
[3, 4, 5],
[6, 7, 8]
]


# Exercise 1 - refactor the following to use numpy. Use sum_of_b as the variable. **Hint, you'll first need to make sure that the "b" variable is a numpy array**
# ```python
# sum_of_b = 0
# for row in b:
#     sum_of_b += sum(row)
# ```

# In[49]:


b = np.array(b) # We turn b into a 2x3 array for all future functions calling on b
sum_of_b = np.sum(b) # We use np.sum() to determine the largest value in the array
print(sum_of_b)


# Exercise 2 - refactor the following to use numpy. 
# ```python
# min_of_b = min(b[0]) if min(b[0]) <= min(b[1]) else min(b[1])
# ```

# In[53]:


min_of_b = np.min(b) # np.min() will determine the smallest value in the array
print(min_of_b)


# Exercise 3 - refactor the following maximum calculation to find the answer with numpy.
# ```python
# max_of_b = max(b[0]) if max(b[0]) >= max(b[1]) else max(b[1])
# ```

# In[54]:


max_of_b = np.max(b) # np.max() will determine the largest value in the array
print(max_of_b)


# Exercise 4 - refactor the following using numpy to find the mean of b
# 
# ```python
# mean_of_b = (sum(b[0]) + sum(b[1])) / (len(b[0]) + len(b[1]))
# ```

# In[55]:


mean_of_b = np.mean(b) # np.mean() will determine the arithmetic mean of the values in the array
print(mean_of_b)


# Exercise 5 - refactor the following to use numpy for calculating the product of all numbers multiplied together.
# ```python
# product_of_b = 1
# for row in b:
#     for number in row:
#         product_of_b *= number
# ```

# In[56]:


product_of_b = np.prod(b) # np.prod() will multiple all of the numbers together
print(product_of_b)


# Exercise 6 - refactor the following to use numpy to find the list of squares 
# ```python
# squares_of_b = []
# for row in b:
#     for number in row:
#         squares_of_b.append(number**2)
# ```

# In[57]:


squares_of_b = b ** 2 # Instead of iterating through a double loop, we can simply use vectorized multiplication
print(squares_of_b)


# Exercise 7 - refactor using numpy to determine the odds_in_b
# ```python
# odds_in_b = []
# for row in b:
#     for number in row:
#         if(number % 2 != 0):
#             odds_in_b.append(number)
# ```

# In[58]:


odds_in_b = b[b % 2 == 1] # We can pass a boolean mask that has set odd numbers to True, and then use that to index the array
print(odds_in_b)


# Exercise 8 - refactor the following to use numpy to filter only the even numbers
# ```python
# evens_in_b = []
# for row in b:
#     for number in row:
#         if(number % 2 == 0):
#             evens_in_b.append(number)
#             ```

# In[59]:


evens_in_b = b[b % 2 == 0] # Same as above, but even numbers are now True
print(evens_in_b)


# Exercise 9 - print out the shape of the array b.

# In[60]:


print(b.shape) # The shape gives us the (number of rows, number of columns) as a tuple 


# Exercise 10 - transpose the array b.

# In[61]:


np.transpose(b) # np.transpose() turns our A x B array into a B x A array


# Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)

# In[62]:


np.reshape(b, 6) # np.reshape(array, shape) converts our array into a 1x6


# Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1)

# In[64]:


np.reshape(b, (6, 1)) #np.reshape(array, shape) converts our array into a shape represented by a tuple


# ## Setup 3

# In[67]:


c = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


# In[68]:


# HINT, you'll first need to make sure that the "c" variable is a numpy array prior to using numpy array methods.
c = np.array(c)


# Exercise 1 - Find the min, max, sum, and product of c.

# In[69]:


print(np.min(c))
print(np.max(c))
print(np.sum(c))
print(np.product(c))
# The shape of the array doesn't matter much with these simple functions


# Exercise 2 - Determine the standard deviation of c.

# In[70]:


print(np.std(c)) # Numpy has a function for standard deviations (np.std())


# Exercise 3 - Determine the variance of c.

# In[71]:


print(np.var(c))
# We can use the np.var()
# Also can be determined by taking square root of standard deviation


# Exercise 4 - Print out the shape of the array c

# In[73]:


print(c.shape)
# array.shape will provide us a tuple showing the rows x columns as (rows, columns)


# Exercise 5 - Transpose c and print out transposed result.

# In[74]:


print(np.transpose(c))
# Transpose takes the first element of each row and puts them together, then the second element of each row and so on


# Exercise 6 - Get the dot product of the array c with c. 

# In[78]:


np.dot(c, c)
# The dot product array can be calculated with np.dot(), with each array passed in as arguments


# Exercise 7 - Write the code necessary to sum up the result of c times c transposed. Answer should be 261

# In[80]:


np.sum(c * np.transpose(c))
# We can use both the np.transpose() function and the np.sum() function to perform this in a single line of code


# Exercise 8 - Write the code necessary to determine the product of c times c transposed. Answer should be 131681894400.

# In[81]:


np.product(c * np.transpose(c)) # Same as above, but we are using np.product() instead of np.sum()


# ### Setup 4

# In[88]:


d = [
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
]
d = np.array(d)


# Exercise 1 - Find the sine of all the numbers in d

# In[89]:


np.sin(d) #Without having to import math, we can use numpys np.sin() function


# Exercise 2 - Find the cosine of all the numbers in d

# In[90]:


np.cos(d) #Same with np.cos()


# Exercise 3 - Find the tangent of all the numbers in d

# In[91]:


np.tan(d) #And np.tan()


# Exercise 4 - Find all the negative numbers in d

# In[92]:


d[d < 0] 
# We can use a boolean mask as an index 


# Exercise 5 - Find all the positive numbers in d

# In[93]:


d[d > 0]
# Same as above


# Exercise 6 - Return an array of only the unique numbers in d.
# 

# In[94]:


np.unique(d)
# np.unique() gives us all of the unique elements of the selected array


# Exercise 7 - Determine how many unique numbers there are in d.

# In[95]:


np.unique(d).shape[0]
# Once we have an array made up of only unique values, we can use the .shape function 
# To output a one-dimensional tuple (11,) essentially counting the elements in the array
# To pass that output without the parens and the comma, we can use an index argument


# Exercise 8 - Print out the shape of d.

# In[97]:


print(d.shape) # Simply using the array.shape function will produce our tuple of (rows, columns)


# Exercise 9 - Transpose and then print out the shape of d.

# In[98]:


print(np.transpose(d).shape)
# Because transposition takes the first element of each row and collects them, 
# Then takes the second element and collects them and so on,
# We expect the tuple to be the inverse of the original array, and it is. 


# Exercise 10 - Reshape d into an array of 9 x 2

# In[99]:


np.reshape(d, (9, 2))
# As long as the product of rows x columns remains the same, we can use the reshape() 
# function to change the number of rows x columns of the array
# Notice that the original array was "read" from left to right across each row as the
# Values were ordered into the desired lists

