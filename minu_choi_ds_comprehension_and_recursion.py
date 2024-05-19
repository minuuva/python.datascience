# -*- coding: utf-8 -*-
"""Minu Choi DS - Comprehension and Recursion

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1mXJ0WSMahzUCL4au4jAt921uJOAikV33

### List comprehension

Many of you resisted my recommendation to use list comprehensions in the previous assignment, and so my hand is forced.  You made me require it.


Problem 1.  For each function you write below, you may assume the list being sent to the function will contain the appropriate data type.

Use list comprehensions to create a function that will take a list `l` and return . . .

(a) . . . a list containing the absolute value of each element of `l`
"""

absolute_list = [-2, -1, 0, 1, 2]

def absolute(absolute_list):
  result = []
  for i in absolute_list:
    if i < 0:
# This line of code will mutiply the value by negative so that the function will return its absolute value.
      result.append(i * -1)
    else:
      result.append(i)
  return result

print(absolute(absolute_list))

"""(b) . . . a list containing `True` for each even number in `l` and `False` for each odd number in `l`"""

odd_even_list = [1, 2, 3, 4, 5]

def odd_even (odd_even_list):
  result = []
  for i in odd_even_list:
# This condition will allow the function to filter whether a number is even or odd.
# If the remainder is 1, it would mean an odd number.
    if i % 2 == 1:
      result.append(False)
    else:
      result.append(True)
  return result

print(odd_even(odd_even_list))

"""(c) . . . a list containing only the numbers in `l` that are divisible by 3"""

divisible_list = [3, 5, 6, 7, 9]

def divisible_by3 (divisible_list):
  result = []
  for i in divisible_list:
# This will check the value such that if the remainder is 0, it will be recognized as being divisble by 3.
    if i % 3 == 0:
      result.append(i)
  return result

print(divisible_by3(divisible_list))

"""(d) . . . a list containing only the words in `l` whose first and last letters are the same"""

word_list = ["data", "area", "analysis", "noon", "commerce", "trust"]

def same_letter (word_list):
  result = []
  for i in word_list:
# This will check, by indexing, whether or not the first and last letter is the same.
    if i[0] == i[-1]:
      result.append(i)
  return result

print(same_letter(word_list))

"""(e) . . . a list containing the first letter of each word in `l` that ends with a vowel"""

vowel_list = ["sunny", "apple", "baseball", "bingo", "letter", "menu"]

def vowel_word (vowel_list):
  result = []
  for i in vowel_list:
# Again, by indexing the last letter, it will only print if the last letter is a vowel.
    if i[-1] in ("a", "e", "i", "o", "u"):
      result.append(i)
  return result

print(vowel_word(vowel_list))

"""### Multiplication as a recursive process
Problem 2.  Write a recursive function that computes the product of two positive integers `a` and `b` by adding `a` to itself `b` times.

Hints:  
1. if `b=1` then the product is `a`.
2. if `b>1` then the product is what you get by adding `a` to `a * (b-1)`.

Note:  the purpose of this exercise is to practice writing recursive functions.  Of course you can trivially ask for `a*b` and get the correct answer but that is worth no points.  Your function should not use any multiplications.

"""

def recursive_multiply(a, b):
  if b == 0:
# This is based on the multiplication rule that anything multiplied by zero is zero.
    return 0
  elif b == 1:
# This is because any number multiplied by 1 is the number itself.
    return a
  else:
# This adds a to itself b times. Each call reduces the value of b by 1,
# eventually reaching either b == 0 or b == 1 which terminate the recursion.
    return a + recursive_multiply(a, b-1)

print(recursive_multiply(7, 2))
print(recursive_multiply(3, 9))

"""### Division as a recursive process

Problem 3:  Write a recursive function that takes two positive integers `a` and `b` and returns the quotient `q` and remainder `r` obtained when `a` is divided by `b`.

Hints:  
1. If `a<b` then what should `q` and `r` be?

2. If `a>b` then think about how `q` and `r` are related to the values you would get from dividing `a-b` by `b`.
"""

def recursive_division(a, b):
  if a < b:
# If a is smaller than b, the function returns 0 as the quotient.
    return 0, a
  else:
# Subtracting b from a performs one step of the division, removing one b from a.
# This recursive call continues until the reduced value of a (a-b, a-2b, a-3b, etc.) becomes less than b.
    quotient, remainder = recursive_division(a-b, b)
# The quotient is incremented by 1 to account for the current division step (a-b).
    return quotient + 1, remainder

print(recursive_division(2, 3))
print(recursive_division(30, 3))

"""### The dot product of two vectors

Problem 4.  Write a recursive function `dot()` that takes two lists of numbers, of equal length, and returns the sum of the products of the elements of the same index from each list. For example, if `V=[1,2,3]` and `W=[4,5,6]` then the function should return the value $(1 \cdot 4) + (2\cdot 5) + (3\cdot 6)$, which equals 32.  In physics and linear algebra, this is called the "dot product" of the vectors `V` and `W`.

Other examples:
```
dot([3],[4])
12

dot([1,1,0],[2,7,17])
9
```
Hints:
1. How is `dot(V,W)` related to `dot(V[1:],W[1:])`?
2. What should happen if the lists are empty?
"""

def dot(V, W):
# This checks if either V or W is empty. The not operator checks for emptiness of the lists.
# If either list is empty, the function returns 0.
  if not V or not W:
    return 0
  else:
# V[0] * W[0] multiplies the first elements of both vectors.
# dot(V[1:], W[1:]) reduces the size of the problem in each step.
# It then reaches the base case when one or both of the vectors are exhausted.
    return V[0] * W[0] + dot(V[1:], W[1:])

print(dot([1, 2, 3], [4, 5, 6]))
print(dot([3], [4]))
print(dot([1, 1, 0], [2, 7, 17]))