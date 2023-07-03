################################### PROJECT 1 ###########################################
"""
Aim:- Read a number n and compute n+nn+nnn
"""

# num = int(input("Enter a number: "))
# req_value = num + (num*num) + (num*num*num)
# print(req_value)

##################################### PROJECT 2 ###########################################
"""
Aim:- Accept three distinct digits and print all the possible combinations from the digits.
"""

# a = int(input("Enter number 1: "))
# b = int(input("Enter number 2: "))
# c = int(input("Enter number 3: "))
#
# d = [a, b, c]
#
# for i in range(0, 3):
#     for j in range(0, 3):
#         for k in range(0, 3):
#             if i != j and j != k and k != i:
#                 print(d[i], d[j], d[k])

#################################### PROJECT 3 ##############################################
"""
Aim:- Print all the integers that are not divisible by either 2 or 3 and lie between 1 and 100.
"""
# for i in range(0, 101):
#     if i % 2 != 0 and i % 3 != 0:
#         print(i)

##################################### PRIHECT 4 ##############################################
"""
Aim:- Accept a number n and print an identity matrix of nXn.
"""
# num = int(input("Enter a number: "))
# for i in range(1, num+1):
#     for j in range(1, num+1):
#         if i == j:
#             print(1, end=" ")
#         else:
#             print(0, end=" ")
#     print()
#
###################################### PROJECT 5 ##############################################
"""
Aim:- Compute the value of Euler's number `e`. Use the Formula: e = 1 + 1/1! + 1/2! +........+ 1/n!
"""
### DO NOT USE RECURSION METHOD TO EVALUATE FACTORIAL!!!!

# def fact(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fact(n - 1) and fact(n - 2)


# def fact(n):
#     result = 1
#     for x in range(2, n + 1):
#         result *= x
#     return result
#
#
# nt = int(input("Enter the nth value: "))
# e = 0.0                                     # To get the value in double
# for i in range(1, nt+1):
#     e += (1.0 / fact(i))
#
# euler_val = e + 1
# print(euler_val)


#################################### PROJECT 6 #######################################
"""
Aim:- Read print prime numbers in a range using `Sieve of Eratosthenes`.
"""

#################################### PROJECT 7 #######################################
"""
Aim:- Generate Random numbers from 1 to 20 and append them in a list.
"""
import random

random_num = []
for i in range(1, 21):
    num = random.randint(1, 20)
    random_num.append(num)
print(random_num)

#################################### PROJECT 8 ########################################