# MULTIPLE INHERITANCE
# class A:
#     def m(self):
#         print("Parent1 Class")
#
#
# class B(A):
#     def m(self):
#         print("In Parent2 class")
#
# class E(A):
#     def m(self):
#         print("In Parent3 class")
#
#
# class C(B, E):
#     pass
#
#
# obj = C()
# # obj.m()
# A.m(obj)
# E.m(obj)


# CONSTRUCTOR EXAMPLE
# import math
# class Circle:
#     def __init__(self, r):
#         self.r = r
#
#     def area(self):
#         return print("The are of the circle is: {:2.0f}".format(2*math.pi*self.r))
#
#     def perimeter(self):
#         return print("The perimeter of the circle is: {:2.0f}".format(math.pi*self.r**2))
#
#
# c = Circle(5)
# c.area()
# c.perimeter()

# PRINT ING STRING BACKWARDS
# def str_rev(s: str):
#     String = s.split()[::-1]
#     req_str = []
#     for i in String:
#         req_str.append(i)
#     print(" ".join(req_str))
#
# String = "I am disco dancer, zindagi mera gana"
#
# str_rev(String)


# RETURNING THE LIST WITH NO DUPLICATES
# def remove_duplicates(X: list[int]):
#     new_lst = []
#
#     for i in X:
#         if i not in new_lst:
#             new_lst.append(i)
#     print(new_lst)
#
#
# lst = [1, 1, 2, 2, 32, 35, 56, 11, 11]
# remove_duplicates(lst)

#FIBONACCI
import integer as integer

#
# def fib(n: int):
#     if n<=1:
#         return n
#     else:
#         return fib(n-2) + fib(n-1)
#
#
# n = int(input("Enter range of fibonacci sequence and use positive value: "))
# if n <= 0:
#     print("Enter positive number.")
# else:
#     print("The Fibonacci sequence is: ")
#     for i in range(n):
#         print(fib(i))
#

# TO PRINT ALL THE UNIQUE VALUES IN DICTIONARY
# sample_data= [{'V': "S001"},
#               {'V': "S002"},
#               {'VI': "S001"},
#               {'VII': "S005"},
#               {'V': "S009"},
#               {'VII': "S007"}
#
# ]
# u_value = set(val for dict in sample_data for val in dict.values())
# print(u_value)

# TAKE LIST AS INPUT AND RETURN ONLY THE FIRST AND LAST ELEMENTS FROM THE GIVEN LIST
# def index_last_val(X: list):
#     req_lst = [X[0], X[-1]]
#     print(req_lst)
#
# lst = [1, 2, 2, 5]
# index_last_val(lst)

# HIGH-LOW GAME
# import random
# number = random.randint(1, 10)
# # print(number)
# guess = 0
# count = 0
#
# while guess != number and guess != "exit":
#     guess = input("Gues a number between 1 and 9: ")
#
#     if guess == "exit":
#         print("Game over.")
#         break
#
#     guess = int(guess)
#
#     count += 1
#
#     if guess not in range(1, 10):
#         print("Please guess a number between 1 and 9.")
#     elif guess > number:
#         print("Guesses high.")
#     elif guess < number:
#         print("Guessed low")
#     else:
#         if count == 1:
#             print("You guessed correctly")
#         elif count <= 3:
#             print("You guessed it in {} turns.".format(count))
#         elif count > 3:
#             print("You got it in {}".format(count))
# **********************************************************************************
# a = [1, 4, 9, 16, 25, 49, 64, 8, 100]
# l = []
# k = [l.append(x)for x in a if x % 2 == 0]
# print(l)

# *********************************************************************************
#
# """ ROCK PAPER SCISSORS GAME"""
# C = ['rock', 'paper', 'scissor']
# R = ['It\'s a draw! ', 'Player1 Wins! ', 'Player 2 Wins!']
#
# again = 'Y'
# while  again == 'Y':
#     P1 = input("Player 1 ~~ Rock ,paper or Scissors -- Choose: ")
#     P2 = input("Player 2 ~~ Rock ,paper or Scissors -- Choose: ")
#
#     winner = (C.index(P1.lower()) - C.index(P2.lower()))
#
#     print(R[winner])
#
#     again = input("Wanna play again[Y/N]: ")

#############################SUPER() KEYWORD ############################################


# class Parent():
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname
#
#     def name(self):
#         print(self.firstname, self.lastname)
#
#
# class Child(Parent):
#     def __init__(self, fname, lname):
#         super().__init__(fname, lname)
#
#
# x = Child("John", 'Doe')
# x.name()
######################################### PALINDROME #########################################
# str = "xyxz"
#
# # for i in str:
# if str == str[::-1]:
#     print(f"String {str} is palindrome.")
#
# else:
#     print(f"String {str} is not palindrome.")

################################### Specific Word count ##########################################
# str = "He is John. John is fine."
# special_characters = ['@', '#', '$', '.', '%', '^', '*']
# n_str = str
# for i in special_characters:
#     n_str = n_str.replace(i, "")
# # print(n_str)
# x = 0
# for i in n_str.split():
#     if i == "John":
#         x += 1
# print(f"The count of John is: {x}")
###################################### PRIME NUMBER ################################################

# def prime_num(n: int):
#     if n > 1:
#         for i in range(2, (n//2)+1):  # or  range(2, math.sqrt(n)+1)
#             if n % i == 0:
#                 print(f"The number {n} is not prime number.")
#                 break
#         else:
#             print(f"The number {n} is a prime number.")
#     else:
#        print(f"The number {n} is not a prime number.")
#
#
# prime_num(65)
#
# '''
#  In the above line of code we iterate till either `sqrt(n)+1` or `(n//2)+1` because:-
#  ***
#      e.g. to understand the following explaination
#      Let n=6 and a=2 and b=3
#
#      Suppose `n` is not a prime number (greater than 1). So there are numbers a and b such that:
#
#      ---> n = ab   (1 < a<=b <n)  (a and b are positive numbers.)
#
#      By multiplying the relation a<=b by a and b we get:
#
#      --->   a^2 <= ab
#             ab <= b^2
#
#       Therefore: (note that n=ab)
#
#       ---> a^2 <= n <= b^2
#       ---> a <=  sqrt(n)  <= b
# '''

################################### ENUMERATE ##################################
#
# l1 = ["eat", "sleep", "repeat"]
# s1 = "geek"
#
# # creating enumerate objects
# obj1 = enumerate(l1)
# obj2 = enumerate(s1)
#
# print ("Return type:", type(obj1))
# print (list(enumerate(l1)))
#
# # changing start index to 2 from 0
# print (list(enumerate(s1, 2)))

##################################### LETTERF OSILVER OAK UNIVERSITY WITHOUT E AND S #####################################
# str = "Silver Oak University"
# rm_char = ['e', 's']
# n_str=str
# for i in rm_char:
#     n_str = n_str.replace(i,"").casefold()
#
# print(" ".join(n_str))
#################################### RECURSION ADDITION OF FIRST 5 NUMBERS #############################################
# def recur_sum(n):
#     if n <= 1:
#         return n
#     else:
#         return n + recur_sum(n-1)
#
# num =5
# if num < 0:
#     print("Enter a positive number.")
# else:
#     print("The sumof {} is : {}".format(num, recur_sum(num)))

#################################### PALINDROME NUMBER ############################
# def palind(n: int):
#         if str(n) == str(n)[::-1]:
#             print(f"THe number {n} is a palindrome number. ")
#         else:
#             print(f"The number {n} is not a plaindrome number.")
#
#
# num = int(input("Enter integer number: "))
# palind(num)
#
#
#***************************************************************************
# n=int(input("Enter number:"))
# temp=n
# rev=0
# while(n>0):
#     dig=n%10
#     rev=rev*10+dig
#     n=n//10
# if(temp==rev):
#     print("The number is a palindrome!")
# else:
#     print("The number isn't a palindrome!")
#******************************************************************************


# def find_(n :str,x:str):
#     rm_chars = ['.', ',', '/']
#     n_str=n
#     ct=0
#     for i in rm_chars:
#         n_str = n_str.replace(i, " ")
#
#     for i in n_str.casefold().split():
#         if i == x.casefold():
#             ct+=1
#     return print(ct)
#
#
# str = "His name is John. John is fine."
# find_(str, 'John')




