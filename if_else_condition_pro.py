# 1.wap to check the number is even or  odd (take user input)
# num=int(input('enter the numebr  '))
# if num%2==0:
#     print(f'number is even')
# else:
#     print(f'number is odd')


# 2.wap to check whether the male and female are eligible for wedding (take user input)
# m=int(input(f'enter the age of male  '))
# f=int(input(f'enter the age of female  '))
# if m>=22 and f>=20:
#     print(f'eligible for wedding')
# else:
#     print(f'not eligible')

# 3.wap to return uppercase if the char is lower,else return same char (by taking user input)
# ch=input('enter the character  ')
# if 'a'<=ch<='z':
#     ch=chr(ord(ch)-32)
#     print(ch)
# else:
#     print(ch)

# 4.wap to return lower case if the upper ,else return same char (by taking user input)
# ch=input('enter the character  ')
# if 'A'<=ch<='Z':
#     ch=chr(ord(ch)+32)
#     print(ch)
# else:
#     print(ch)

# 5.wap to find greater value among the two number
# n1=34
# n2=54
# n1=34
# n2=54
# if n1>n2:
#     print(f'{n1} is greater ')
# else:
#     print(f'{n2} is greater')


# 6.wap to check if the given number is even or not,if it is not even add+1 and make it even (take user input)
# num=int(input('enter the numebr  '))
# if num%2==0:
#      print(f'number is even')
# else:
#     num=num+1
#     print(f'{num}')

# 7.wap to check whether the first character in the given string is starting
# with uppercase or Not if it is not Then capitalize it s="python"

# st=input('enter the string  ')
# if 'A'<=st[0]<='Z':
#     print(f'first character is uppercase')
# else:
#     st=chr(ord(st[0])-32)
#     print(f'{st}')

# 8.wap to check if the given number is even
# ,if it is even reduce it to its Half else make exponent (take user input)
# num=eval(input('enter the numebr  '))
# if num%2==0:
#     num=num/2
#     print(f'{num}')
# else:
#     num=num**num
#     print(f'{num}')


# 9.wap to check number should be divisible by 3 and 7 (take user input)
# num=eval(input('enter the numebr  '))
# if num%3==0 and num%7==0:
#     print(f'yes it is divisible')
# else:
#     print(f'not divisible')

# 10.wap if the length of string is even then reverse else convert into upper case (take user input)

# st=input('enter the string  ')
# if len(st)%2==0:
#     st=st[::-1]
#     print(f'{st}')
# else:
#     st=st.upper()
#     print(f'{st}')

# 11.wap to check a number is +ve/-ve number (take user input)
# num=eval(input('enter the numebr  '))
# if num>=0:
#    print(f'{num} is +ve number')
# else:
#       print(f'{num} is -ve number')


# 12.wap to check a data is individual or collection data type or not (take user input)
# d=eval(input('enter the data '))
# if isinstance(d,(int,str,float)):
#     print(f'{type(d)}')
# else:
#     print(f'not data type')





# 13.wap to check whether the specified character is present in the given string
# s="Python"
# ch=input('enter the char ')
# if s.find(ch)>0:
#     print(f'it is present')
# else:
#     print(f'not present')


# 14.wap to check the length of dictionary and length of dictionary is even or Not if even
# print as it is or else add a item and make it even
#
# D={"a":"apple","b":"ball","c":"cat"}
# D={"a":"apple","b":"ball","c":"cat"}
# if len(D)%2==0:
#     print(f'it is even length')
# else:
#     D.setdefault("D","dog")
#     print(f'{D}')


# 15.wap to check the given number is greater than 5,if it is greater convert that number into negative number
# else print the same number
# num=eval(input('Enter the number '))
# if num>5:
#     num=-num
#     print(f'{num}')
# else:
#     print(f'{num}')

# 16.wap to check the given number is smaller than 10 ,if it is smaller find the exponent of it
# else print the number as it is

# num=eval(input('enter the number '))
# if num<10:
#     num=num**num
#     print(f'{num}')
# else:
#     print(f'{num}')

# 17.wap to check the given number is odd, if it is odd divide it by 2
# and print reminder and quotient else print it is even (take user input)
# num=eval(input('enter the number  '))
# if num%2!=0:
#     print(f'{divmod(num,2)}')
# else:
#     print(f'it is even')



# 18.wap to check if the given character is alphabets or Not
# ,if it is alphabet create a replica of it for 2 times. (take user input)

# ch=input('enter the character  ')
# if ch.isalpha():
#     ch=ch+ch
#     print(f'{ch}')
# else:
#     print(f'not alphabet')


# 19.WAP to check whether the given number value is divisible by 6 or not,
# if it is divisible cube that number or else perform left shift operation by 3 (take user input)

# num=eval(input('enter the number '))
# if num%6==0:
#     num=num**3
#     print(f'{num}')
# else:
#     num=num<<3
#     print(f'{num}')
