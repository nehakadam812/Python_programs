# def uoter (fun):
#     def inner(a,b):
#         print('Addition Operator')
#         fun(a,b)
#     return  inner()
# import time



# import time
# def outer (Greet):
#     def inner():
#         print("Good Morning")
#     Greet()
#     return inner
#
# @outer
# def Greet():
#
#     print('Cool')
#     time.sleep(3)
#     print('Good morning')
#Greet()
#
# def outer(func):
#     def inner(*args,**kwargs):
#         print("Hello EveryOne")
#         func(*args,**kwargs)
#     return inner
# @outer
# def main_fun():
#     print('Good morning')
#
# main_fun()

# 2.write a decorator function to print main function name before executing any decorator function

# def outer(func):
#
#     def inner(*args,**kwargs):
#         print("Hello EveryOne")
#         print(func.__name__)
#         func(*args,**kwargs)
#     return inner
# @outer
# def main_fun():
#     print('Good morning')
#
# main_fun()
#
#3.write a decorator which inputs 5 seconds of delay before executing any decorator function
# import time
# def deco(func):
#
#     def inner(*args,**kwargs):
#         time.sleep(5)
#         print('Hiiiiii')
#         func(*args,**kwargs)
#     return inner
#
# @deco
# def add(a,b):
#     print(a+b)
# add(10,20)

# 4.write a decorator function calculate the execution time of any function

# import time
#
#
# def deco(func):
#     time.sleep(3)
#     def inner(*args,**kwargs)
#         start = time.time()
#         print('by')
#         func(*args,**kwargs)
#         end=time.time()
#         print(end-start)

#     return inner
# @deco
# def sub(a,b):
#     print(a-b)
#     y=time.time()
#
#     print(y-x)
#
# sub(10,2)


# 5.wadf to check if the 1st arguments is lesser than 2nd argument if then swap them and perform division
# but the condition is you should not modify the original function
#
# def fun_1(func):
#     def inner(a,b):
#         if a<b:
#             a,b=b,a
#         return func(a,b)
#     return inner
# @fun_1
#
# def rel(a,b):
#     print(a/b)
# rel(2,4)

# 6.wadf to add 2 numbers and display the message before "i am doing addition operation" after
# performing print the message "addition operation is done"
#
# o/p--->i am doing addition operation"
#        value
#      "addition operation is done


# def dec(func):
#     def inner(*args,**kwargs):
#         print('i am doing addition operation')
#         func(*args,**kwargs)
#         print('addition operation is done')
#     return inner
# @dec
# def add(a,b):
#     print(a+b)
# add(10,20)

# 7.create a decorator to return only positive out from any subtraction
# def dec(func):
#     def inner(a,b):
#         if a<b:
#             a,b=b,a
#         return func(a,b)
#     return inner
# @dec
# def sub(a,b):
#     print(a-b)
# sub(1,5)

# 8.create a decorator which counts the number of function calls
# def printting():
#     print("Neha")
# printting()

#9.wap to sum of the positional arguments and get the length of the keywords arguments

# def deco(func):
#     def inner(*args,**kwargs):
#         return func(*args,**kwargs)
#     return inner
# @deco
# def main(*args,**kwargs):
#     print(sum(args))
#     print(len(kwargs))
# main(2,4,a=10,b=20)

# 10.write a decorator function to print the type of datatype before performing the action
# def deco_fun(func):
#     def in_fun(b):
#         print(type(b))
#         return func(b)
#     return in_fun
# @deco_fun
# def main_fun(a):
#     print(a)
# main_fun('hii')

#11.write a decorator operation on the given number and the condition is A>B
# then perform multiplication in decorator function else
#  cube it in decorator

# def deco_fun(func):
#     def in_fun(a,b):
#         if a>b:
#             print(a*b)
#         else:
#             print(a**3)
#             print(b**3)
#         func(a,b)
#     return in_fun
# @deco_fun
# def main_f(a,b):
#     return a,b
# main_f(10,5)

# 12.create a decorators to which prints name of called main function and counts the function calls
# from itertools import count
# def deco(great):
#     def inner(*args,**kwargs):
#
#         great()
#     return inner
# @deco
# def abc():
#     print("hi")
# abc()
# abc()
# abc()
# print(count())

# 13.create a decorators to which prints names of called functions and checks the number is even or odd

# def deco_fun(func):
#
#     def inner(*args,**kwargs):
#         print(func.__name__)
#         func(*args,**kwargs)
#     return inner
# @deco_fun
# def even_odd(a):
#     if a%2==0:
#         print('Even')
#     else:
#         print('Odd')
# even_odd(10)

# 14.create a decorator which delays its execution as per user input

import time
# def dec_fun(func):
#     def inner(b):
#         time.sleep(b)
#         return func(b)
#     return inner
# @dec_fun
# def main_fun(a):
#     print('hii')
# a=int(input('Enter the delay time :='))
# main_fun(a)
#

# 15.write a multilevel decorator to log some message

# def deco_fun1(func):
#     def inner_fun1(*args,**kwargs):
#         print("From deco1")
#         func(*args,**kwargs)
#     return inner_fun1
#
# def deco_fun2(func):
#     def inner_fun2(*args,**kwargs):
#         print("From deco2")
#         func(*args,**kwargs)
#     return inner_fun2
# def deco_fun3(func):
#     def inner_fun3(*args,**kwargs):
#         print("From deco3")
#         func(*args,**kwargs)
#     return inner_fun3
# @deco_fun2
# @deco_fun1
# @deco_fun3
# def main_fun():
#     print("from main")
# main_fun()

# 16.write a multilevel decorators to accept username and register number of employee
# def deco_fun1(func):
#     def inner_fun1(username,register):
#         print(username,register)
#         return  func(username,register)
#     return inner_fun1
#
# def deco_fun2(func):
#     def inner_fun2(username,register):
#         print(username,register)
#         func(username,register)
#     return inner_fun2
# def deco_fun3(func):
#     def inner_fun3(username,register):
#         print(username,register)
#         return func(username,register)
#     return inner_fun3
# @deco_fun2
# @deco_fun1
# @deco_fun3
# def main_fun(username,register):
#      return username,register
# username=input('ENter the username :=')
# register_number=int(input('ENter the register number :='))
# main_fun(username,register_number)

# 17.WADF TO DELAY FOR 3 SECONDS AND DISPLAY THE NAME, DELAY FOR 3 SECONDS AND DISPLAY EMAIL ADDRESS ,
#  DELAY FOR 3 SECONDS AND DISPLAY PHONE NUMBER
# import time
# def demo(func):
#     def inner(n,a,e):
#         time.sleep(3)
#         print(n)
#         time.sleep(3)
#         print(e)
#         time.sleep(3)
#         print(a)
#         return func(n,a,e)
#     return inner
# @demo
# def main_fun(n,a,e):
#     return n,a,e
# name=input("Enter the name :=")
# add=input("Enter the address :=")
# e_mail=input('Enter the email address :=')
# main_fun(name,add,e_mail)

