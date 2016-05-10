# The largest prime factors of 13195 are 5,7,13 and 29.
# What is the largest prime factor of the number 600851475143?

# first answer that worked fine, but only for smaller numbers
# x = 13195
# i = 3
# n = 2
# results = []
#
# while i < x:  # while we could still divide
#     if x % i == 0:  # if x is divisible by i check to see if i is prime
#         while n < i:  # start to check if i is prime
#             if i % n == 0:  # dang it, it is not
#                 n = 2  # reset n to 2 for next i
#                 break  # leave while loop, we're done here
#             else:
#                 n = n + 1  # i might still be prime check next number n
#         if n != 2:  # if n did not get reset to 2 during our while loop, then we never found a number n to divide i by
#             n = 2  # reset n to 2 for next i
#             results.append(i)  # add i to results
#     i = i + 1  # go to next i
# print(results)

# Second answer that will implement the sieve up until sqrt(number x)
# The sieve says:
# Input: an integer n > 1
#
# Let A be an array of Boolean values, indexed by integers 2 to n,
# initially all set to true.
#
# for i = 2, 3, 4, ..., not exceeding √n:
#   if A[i] is true:
#     for j = i2, i2+i, i2+2i, i2+3i, ..., not exceeding n :
#       A[j] := false
#
# Output: all i such that A[i] is true.
import math
x = 600851475143
#  x = 13195
n = math.floor(math.sqrt(x))  # because we only have to check up to sqrt(x) to find prime factors
nn = math.floor(math.sqrt(n))  # because we only have to check up to sqrt(n) to find prime numbers less than n
L = [False] * 2 + [True] * (n - 1)

for i in range(2, nn + 1):
    if L[i]:
        for j in range(i*i, n + 1, i):
            L[j] = False
for y, item in enumerate(L):
    if item:
        if x % y == 0:
            print(y)
















