# The sum of the squares of the first ten natural numbers is,
#
# 1^2 + 2^2 + ... + 10^2 = 385
#
# The square of the sum of the first ten natural numbers is,
#
# (1 + 2 + ... + 10)^2 = 55^2 = 3025
#
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
#  3025 − 385 = 2640.
#
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
import math

# x = (pow(11,2))+ (12 ^ 2) + (13 ^ 2) + (14^2) + (15^2) + (16^2) + (17^2) + (18^2) + (19^2) + (20^2)
x = pow(21, 2) + pow(22, 2) + pow(23, 2) + pow(24, 2) + pow(25, 2) + pow(26, 2) + pow(27, 2) + pow(28, 2) + pow(29, 2)\
    + pow(30, 2)
y = pow((21 + 22 + 23 + 24 + 25 + 26 + 27 + 28 + 29 + 30), 2)
print(y,x)