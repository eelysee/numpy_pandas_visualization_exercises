import numpy as np

# Use the following code for the questions below:

a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

# 1. How many negative numbers are there?

# print(a < 0)

l = a < 0

# the True statements evaluate to '1'. Sum of array minus the number of elements (length) yields 

print()
print('How many negative numbers are there?')
print(len(l) - l.sum())



# 2. How many positive numbers are there?

print()
print('How many positive numbers are there?')
print(l.sum())

# 3. How many even positive numbers are there?

e = (a % 2 == 0) & (a > 0)

print()
print('How many even positive numbers are there?')
print(e.sum())


# 4. If you were to add 3 to each data point, how many positive numbers would there be?

three = a + 3
pt = three > 0

print()
print('If you were to add 3 to each data point, how many positive numbers would there be?')
print(pt.sum())


# 5. If you squared each number, what would the new mean and standard deviation be?

sq = a ** 2

print()
print('If you squared each number, what would the new mean and standard deviation be?')
print('mean if squared')
print(np.mean(sq))
print('standard deviation')
print(np.std(sq))

# 6. A common statistical operation on a dataset is centering. 
# This means to adjust the data such that the mean of the data is 0. 
# This is done by subtracting the mean from each data point. 
# Center the data set. See this link for more on centering.

# ma = mean
ma = np.mean(a)
cen_a = a - ma


print()
print('Cnetered array')
print(cen_a)


# 7. Calculate the z-score for each data point. Recall that the z-score is given by:



"""
z = ( x - μ ) / σ

z = Z-score
x = the value being evaluated
μ = the mean
σ = the standard deviation
"""

# ma = mean
# std_a = stadard deviation of 'a'
std_a = np.std(a)

print()
print('Z Score')
print((a - ma) / (std_a))


"""

Z
=
x
−
μ
σ
Copy the setup and exercise directions from More Numpy Practice into your numpy_exercises.py and add your solutions.

"""

# Life w/o numpy to life with numpy

## Setup 1
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use python's built in functionality/operators to determine the following:

# Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list

sum_of_a = sum(a)

print()
print('Sum of a')
print((sum_of_a))

# Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list

min_of_a = min(a)

print()
print('Min of a')
print((min_of_a))

# Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list

max_of_a = max(a)

print()
print('Max of a')
print((max_of_a))

# Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list

mean_of_a = sum_of_a / len(a)

print()
print('Mean of a')
print((mean_of_a))

# Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all the numbers in the above list together

product_of_a = 1

for n in a:
    product_of_a *= n

print()
print('Product of a')
print((product_of_a))

# Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared like [1, 4, 9, 16, 25...]

squares_of_a = []

for n in a:
    squares_of_a.append(n**2)

print()
print('Squares of a')
print((squares_of_a))

# Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers

odds_in_a = []

for n in a:
    if n % 2 != 0:
        odds_in_a.append(n)

print()
print('Odds in a')
print((odds_in_a))

# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.

evens_in_a = []

for n in a:
    if n % 2 == 0:
        evens_in_a.append(n)

print()
print('Evens in a')
print((evens_in_a))

## What about life in two dimensions? A list of lists is matrix, a table, a spreadsheet, a chessboard...
## Setup 2: Consider what it would take to find the sum, min, max, average, sum, 
# product, and list of squares for this list of two lists.

b = [
    [3, 4, 5],
    [6, 7, 8]
]

# Exercise 1 - refactor the following to use numpy. 
# Use sum_of_b as the variable. **Hint, you'll first need to make sure that the "b" variable is a numpy array**

# Refactor the list of lists to matrix
b = np.array(b)

sum_of_b = 0

for row in b:
    sum_of_b += sum(row)

sum_of_b_n = b.sum()

print()
print('Sum of b')
print((sum_of_b))

print()
print('Sum of b numpy')
print((sum_of_b_n))

# Exercise 2 - refactor the following to use numpy. 
min_of_b = min(b[0]) if min(b[0]) <= min(b[1]) else min(b[1])  

min_of_b_r = b.min()

print()
print('Min of  b')
print(min_of_b)

print()
print('Min of refactored b')
print(min_of_b_r)

# Exercise 3 - refactor the following maximum calculation to find the answer with numpy.
max_of_b = max(b[0]) if max(b[0]) >= max(b[1]) else max(b[1])

max_of_b_r = b.max()

print()
print('Max of  b')
print(max_of_b)

print()
print('Max of refactored b')
print(max_of_b_r)

# Exercise 4 - refactor the following using numpy to find the mean of b
mean_of_b = (sum(b[0]) + sum(b[1])) / (len(b[0]) + len(b[1]))

print()
print('Max of  b')
print(max_of_b)

print()
print('Max of refactored b')
print(max_of_b_r)

# Exercise 5 - refactor the following to use numpy for calculating the product of all numbers multiplied together.

product_of_b = 1
for row in b:
    for number in row:
        product_of_b *= number

product_of_b_r = np.prod(b)

print()
print('Product of b')
print(product_of_b)

print()
print('Product of refactored b')
print(product_of_b_r)

# Exercise 6 - refactor the following to use numpy to find the list of squares 
squares_of_b = []
for row in b:
    for number in row:
        squares_of_b.append(number**2)

squares_of_b_r = b * b

print()
print('Square of b')
print(squares_of_b)

print()
print('Square of refactored b')
print(squares_of_b_r)


# Exercise 7 - refactor using numpy to determine the odds_in_b
odds_in_b = []
for row in b:
    for number in row:
        if(number % 2 != 0):
            odds_in_b.append(number)


print()
print('Square of b')
print(squares_of_b)

print()
print('Square of refactored b')
print(squares_of_b_r)


# Exercise 8 - refactor the following to use numpy to filter only the even numbers
evens_in_b = []
for row in b:
    for number in row:
        if(number % 2 == 0):
            evens_in_b.append(number)

#evens_in_b = b[b % 2==0]

# Exercise 9 - print out the shape of the array b.

# Exercise 10 - transpose the array b.

# Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)

# Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1)

## Setup 3
c = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# HINT, you'll first need to make sure that the "c" variable is a numpy array prior to using numpy array methods.
# Exercise 1 - Find the min, max, sum, and product of c.

# Exercise 2 - Determine the standard deviation of c.

# Exercise 3 - Determine the variance of c.

# Exercise 4 - Print out the shape of the array c

# Exercise 5 - Transpose c and print out transposed result.

# Exercise 6 - Get the dot product of the array c with c. 

# Exercise 7 - Write the code necessary to sum up the result of c times c transposed. Answer should be 261

# Exercise 8 - Write the code necessary to determine the product of c times c transposed. Answer should be 131681894400.


## Setup 4
d = [
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
]

# Exercise 1 - Find the sine of all the numbers in d

# Exercise 2 - Find the cosine of all the numbers in d

# Exercise 3 - Find the tangent of all the numbers in d

# Exercise 4 - Find all the negative numbers in d

# Exercise 5 - Find all the positive numbers in d

# Exercise 6 - Return an array of only the unique numbers in d.

# Exercise 7 - Determine how many unique numbers there are in d.

# Exercise 8 - Print out the shape of d.

# Exercise 9 - Transpose and then print out the shape of d.

# Exercise 10 - Reshape d into an array of 9 x 2

