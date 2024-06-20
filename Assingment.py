# 1.WAP to extract & store the extensions of files in a list
# l = ['forloop.txt', 'python.py', 'while.pdf', 'functions.pptx','lambda.png', 'map.py', 'python.pdf', 'oops.py']
# list=[]
# for i in l:
#       i=i.split('.')
#       list.append(i[1])
# print(list)

# 2.wp to print first and last char of each name in the list
# l = ["Sunil", "anil", "Suresh", "Mahesh", "Dinesh"]
# for i in l:
#     print(f'{i[0]}{i[len(i)-1]}',end=' ')

#3.wp to create new list as squares of each number of below list
# l = [2, 4, 5, 1, 9, 7, 3]
# sl=[]
# for i in l:
#     sl.append(i*i)
# print(sl)

# 4.wp if number is even the print its square else print its cube
# l = [2, 4, 5, 1, 9, 7, 3]
# for i in l:
#     if i%2==0:
#         print(i*i,end=' ')
#     else:
#         print(i**3,end=' ')

# 5.wp to create a new list of separate even number and odd number
# l = [2, 4, 5, 1, 9, 7, 3]
# even=[]
# odd=[]
# for i in l:
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)
# print(f'Even list {even}')
# print(f'odd list {odd}')

# 6.wp to create a new list reversing each name from the list.
# names = ["Sunil", "denga", "panga", "Harsha", "manga"]
# reverselist=[]
# for i in names:
#     reverselist.append(i[-1::-1])
# print(reverselist)

# 7. WAP  to find the number of digits present in a number
# n = 123456
# i=0
# c=0
# while n>0:
#     c = c + 1
#     n = n // 10
# print(c)

# 8.WAP to print largest number in the list without using
# #inbuilt function
# numbers = [10, 30, 50, 80, 15, 20, 70,25]
# l=0
# for i in numbers:
#     if i>l:
#         l=i
# print(l)

# 9.WAP to print all numeric values in a list
# l = ['apple', 123, 'google', '45.6', 'yahoo', [1,2,3], True, (1,3,7), 6+3j]
# for i in l:
#     if isinstance(i,(int,float,complex)):
#         print(i,end=' ')
#     elif i.isdigit():
#         print(i,end=' ')
#     elif isinstance(i,list):
#

# 10.WAP to perform copy method in a list without using copy()(take user input)
# list=eval(input('Enter the element of list '))
# copy_list=[]
# for i in list:
#     copy_list.append(i)
# print(copy_list)

#11.WAP to check the given number is Armstrong or not
# num=370
# num1=num
# #Armstrong : Sum of cube of the digits
# a=0
# b=0
# while num1>0:
#     a=num1%10
#     b=a**3+b
#     a=0
#     num1=num1 // 10
# if num==b:
#     print(f'{num} is armstrong number')
# else:
#     print('not armstrong number')

# 12.WAP to check given number is perfect number or not(take user input)
# #sum of its proper divisor should be equal to original value
# num=int(input('enter the number :'))
# sum=0
# for i in range(1,num):
#     if num%i==0:
#         sum=sum+i
# if num==sum:
#     print('it is perfect number')
# else:
#     print('not perfect number')

# 13.WAP to print Fibonacci numbers up to 10
# a=0
# b=1
# for i in range(10):
#     print(a ,end=' ')
#     b=b+a
#     a=b+a
#     print(b,end=' ')

# 14.WAP to check given number is Automorphic or not
#automorphic means:-->square end with the given integer
# 1,5,6,25,76,376,625,9376
# num=int(input('enter the number :'))
# s=num**2
# a=s%10
# if num==a:
#     print('it is automorphic')
# else:
#     print('not')

# 15. WAP to reverse each element in a list, then reverse entire list
# names = ['apple', 'google', 'yahoo', 'Walmart']
# for i in reversed(names):
#     print(i[::-1],end=" ")







