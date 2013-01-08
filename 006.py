"""
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025  385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

# From memory, there factorial of some sort for this,
# ie, expanding the square for 
#     (a+b)^2 = a^2 + b^2 + 2ab
# it can be elaborated to include more than 2 nomials.  Cannot remember now..

# The below is good enough :)

sum_of_sqs = sum([n*n for n in range(1, 101)])
sq_of_sum = sum([n for n in range(1, 101)])**2

print sq_of_sum - sum_of_sqs

# PS. Found this.
# http://www.trans4mind.com/personal_development/mathematics/series/multiNomialExpansion.htm
