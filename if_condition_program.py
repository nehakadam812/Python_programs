# 1.wap to check the number is odd (take user input)
# num=int(input('enter the number'))
# if num%2==1:
#     print(f'the given number is odd')


# 2.wap to check the number is even (take user input)
# num=eval(input('enter the number'))
# if num%2==0:
#     print(f'the number is even')


# 3.wap to check if the student has scored 70% print "good luck "(take user input)
# marks=eval(input('enter the scored marks'))
# if marks==70:
#     print(f'good luck')

# 4.wap to check which number is greater using if condition
# a=98
# b=67

# a=98
# b=67
# if a>b:
#     print(f'{a} is greater than {b}')



# 5.wap to check if the given string has even length of character
# s="hey guys you all are Osam"

# s="hey guys you all are Osam"
# if len(s)%2==0:
#     print(f'given string has even length')

# 6.wap to check if the given number is divisible by 5 (take user input)
# num=int(input('enter the number'))
# if num%5==0:
#   print(f'the given number is dividible by 5')

# 7.wap to check if the given programming language is present in the list
# p=["java","python","c","c++","RUBy","golang"]
# a=input("enter the programming language ")
# p=["java","python","c","c++","RUBy","golang"]
# if a in p:
#     print(f'{a} language is present in list')


# 8.wap to check eligible to vote take user input as a age
# age=eval(input("Enter the person age"))
# if age>=18:
#   print(f'the person is eligible for voting')

# 9.wap to check if the given number is positive take user input
# num=eval(input('enter the number'))
# if num>=0:
#  print(f'the given number is positive')

# 10.wap to check if the given string is palindrome (take user input)
# a=input("enter the word ")
# if a==a[::-1]:
#  print(f'given string {a} is palindrome')

# 11.wap to check if the first letter in the given string is consonant

# s="Lahari is a good student"
# if s[0] not in('a','e','i','o','u'):
#     print(f"the string is starting with consonant")

# 12.wap to check the given string is uppercase or not (take user input)
# a=input("enter the word ")
# if a.isupper():
#  print(f'given string {a} is in uppercase')
# else:
#     print(f'the given string is not uppercase')

# 13.wap to check the given value is string (take user input)
# a=eval(input('enter the value '))
# if type(a)==str:
#     print(f'given value is string')

# 14.wap to display "Python Coding" if the number is greater than 1 and less than 5 (take user input)
# num=eval(input("enter the number "))
# if num>1 and num<5 :
#     print(f'Python Coding')


# 15.wap to check whether given number is negative and print "its negative guys"
# num=eval(input("enter the number "))
# if num<0:
#   print(f'its negative guys')

# 16.wap to check whether given input is divisible by 2 and 6 if condition is True ,convert the given number to complex number.(take user input)
# num=eval(input("enter the number "))
# if num%2==0 and num%6==0:
#     print(complex(num))

# 17.wap to check whether the given number is even or not,if even store the value inside the list (take user input)
# num=eval(input("enter the number "))
# a=[]
# if num%2==0:
#     a.append(num)  #without using inbuilt function : a=a+[num]
#     print(f'{a}')





# 19.wap to check whether a given value is divisible by 5 and 7,if the value is divisible then display the square of the values (take user input)
# num=eval(input("enter the number "))
# if num%5==0 and num%7==0:
#     n=num*num
#     print(f'{n}')

# 20.wap to check whether a given value is present in between 45 and 200 and
# the number should be divisible by 4 and 5 ,if satisfied,display the ascii characters (take user input)
# v=eval(input("Enter the value "))
#
# if 45<=a<=200  and v%4==0 and v%5==0:
#
#      print(f'the ascii characters is {chr(v)}')


# 21.wap to checking if a string contains a substring
#
# string="hello world"
# sub_string="world"

# s="hello world"
# sub_str="world"
# if sub_str in s:
#     print(f'string contains substring')


# # 22.wap to check whether a character is in the alphabet or not,if it is
# #     alphabet,store the value inside  a dict(key as a character and value as a ascii value)
# v=input("Enter the character ")
# di={}
# if v.isalpha():
#     di.setdefault(v,ord(v))
#     print(f'{di}')

# 23.wap to check whether a character is in uppercase or not,ifuppercase,convert to lowercase
# and store the value inside the dictionary (character as key and ascii as value) take user input
# v=input("Enter the character ")
# d={}
# if "A"<=v<="Z":
#     v=v.lower()
#     d[v]=ord(v)
#     print(d)
# v1=input("Enter the character ")
# d={}
# if "A"<=v1<="Z":
#     v1=chr(ord(v1)+32)
#     d[v1]=ord(v1)
#     print(d)

#with using inbuilt function
# v=input("Enter the character ")
# d={}
# if v.isupper():
#     v=v.lower()
#     d[v]=ord(v)
#     print(d)

# Q-24

x=input(("enter the character  "))
a={}
if 'a'<=x<='z':
    x=chr((ord(x)-32))
    a[x]=ord(x)
    print(a)