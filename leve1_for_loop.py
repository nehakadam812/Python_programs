# 1.wap to print the number form 1 -20 segregate even and odd number into list
# e=[]
# o=[]
# for i in range(21):
#     if i%2==0:
#         e.append(i)
#     else:
#         o.append(i)
# print(f'even list {e}')
# print(f'odd list {o}')


# 2.wap to extract vowels and digits in a string
# s="hello123"
# v=['a','e','i','o','u']
# for i in s:
#     if i in v or i.isdigit():
#         print(i,end="  ")

#3.wap to capitalize only the first letter of every word in the given list
# l=["vaidegi","rahul","shivam","kapil","patil"]
# for i in l:
#     print(i.title(),end=" ")

# 4.wap to extract only individual data types form the list
# l=["hello",1,23.4,5+6j,"guys",[2,3,4],True,False]
# for i in l:
#     if isinstance(i,(int,float,complex,bool)):
#         print(i, end=" ")

# 5.wap to extract only individual data types from the list and sum all the individual data types
# l=["hello",1,23.4,5+6j,"guys",[2,3,4],True,False]
# sum=0
# for i in l:
#      if isinstance(i,(int,float,complex,bool)):
#          sum=sum+i
# print(sum)

# 6.wap to print the count of alphabets and numbers and space in the given string

# s="india got the independence in the year 1947"
# alpha=0
# space=0
# num=0
# for i in s:
#     if i.isalpha():
#         alpha=alpha+1
#     elif i.isdigit():
#         num=num+1
#     else:
#         space=space+1
#
# print(f'number of alphabet {alpha}' )
# print(f'number of alphabet {num}')
# print(f'number of alphabet {space}')


# 7.wap to check how many words are present in the given sentence

# s="hello world sentence"
# w=1
# for i in s:
#     if i.isspace():
#         w=w+1
# print(f'word present in sentence is {w}')


# 8.wap to create a dictionary and print the characters and its Ascii value pair
# s="hello world"
# output:--> {"h":ascii value,"e":ascii value........}

# s="hello world"
# d={}
# for i in s:
#     d.setdefault(i,ord(i))
# print(d)



# 9.wap to create a dictionary and traverse into it and if the length is even print as it else reverse it
# names=["apple","google","yahoo","microsoft","gmail","walmart"]
# output:-->{'apple': 'elppa', 'google': 'google', 'yahoo': 'oohay', 'microsoft': 'tfosorcim', 'gmail': 'liamg', 'walmart': 'tramlaw'}

# names=["apple","google","yahoo","microsoft","gmail","walmart"]
# d={}
# for i in names:
#     if len(i)%2==0:
#         d.setdefault(i)
#         d.update({i:i})
#     else:
#         d.setdefault(i)
#         d.update({i:i[::-1]})
# print(d)


# 10.wap to print series of factorial(take user input)

# 11.wap to create a dictionary with element and its count pair
# l=["yellow","red","black","pink","orange","green","red","pink","yellow"]
# output:-->
# {'yellow': 2, 'red': 2, 'black': 1, 'pink': 2, 'orange': 1, 'green': 1}
# l=["yellow","red","black","pink","orange","green","red","pink","yellow"]
# d={}
# c=0
# for i in l:
#     for j in l:
#         if i==j:
#             c=c+1
#     d.setdefault(i)
#     d.update({i:c})
#     c=0
# print(d)


# 12.wap to find the length of the string without using inbuilt function
# s="Never Give Up"
# len=0
# for i in s:
#     len=len+1
# print(f'length of "{s}"---{len}')

#13.wap to reverse a string without using inbuilt function
# x="you did it guys"
# s=""
# for i in x:
#     s=i+s
# print(s)

# 14.wap to print alternative character from a given string
s="hello python"
"""
syntax for 
for i in range (si,en+1,sv)
"""
# for i in range(len(s),2):
#     print(s,end="")
#


# 15.wap to replace all the character with "-" if the characters occurs more than once in a string
# s="hellohai"
# o/p---->-e--o-ai


# s="hellohai"
# for i in s:
#     if s.count(i)>1:
#         s=s.replace(i,"-")
# print(s)


# 16.wap to get  output:--->1234 in below question
# t=("1","2","3","4")
# res=''
# for i in t:
#     res+=i
# print(res)


# 17.wap to Sum of numbers
# s = 'Sony12India567pvt21ltd'
# sum=0
# for i in s:
#     if i.isdigit():
#         sum+=int(i)
# print(sum)


# 18.WAP to print sum of internal and external list
# l = [[1,2,3], [4,5,6], [7,8,9]]
# output:-->
#    #internal = 6, 15, 24
#    #external --> 45

# l = [[1,2,3], [4,5,6], [7,8,9]]
# rev=[]
# for i in l:
#     sum_internal=0
#     for j in i:
#         sum_internal+=j
#     rev.append(sum_internal)
#     external=0
#     for s in rev:
#          external+=s
#
# print(rev)
# print(external)






# 19. WAP to remove duplicates from the list without using inbuilt function

# d = [1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4]
# dup=[]
# non_dup=[]
# for i in d:
#     if i not in  dup:
#         dup.append(i)
#     else:
#         non_dup.append(i)
# print(dup)
# print(non_dup)




# 20.Print all the missing numbers from 1-10 in the below list
# l = [1, 2, 3, 4, 6, 7, 10]
# for i in range(1,11):
#   if i not in l:
#     print(i)


# 21.Reverse a list without using any built-in functions and slicing.
# l=[1,2,3,4]
# res=[]
# for i in l:
#     res=[i]+res
# print(res)

# 22.wap to get below out put
# s="Hi How are you"
# o/p-->"uoy era woH iH'
# s1=''
# s="Hi How are you"
# for i in s:
#   s1=i+s1
# print(s1)


# 23.wap to print repeated char and count the same
# s="helloword"
# o/p{'l': 2, 'o': 2}
# s="helloword"
# d={}
# for i in s:
#     if s.count(i)>1:
#         d[i]=s.count(i)
# print(d)

# 24.wap to filter out even and odd numbers in the given string
# s="hello 123 world 456 welcome to python1234567"
# eve=" "
# odd=" "
# for i in s:
#     if i.isdigit():
#         if int(i)%2==0:
#             eve+=i
#         else:
#             odd+=i
# print(eve)
# print(odd)

# 25.,wap to create a dictionary word and reverse word pair
# s="tomorrow is weekend and non-veg special"
# o/p:-->{'tomorrow': 'worromot', 'is': 'si', 'weekend': 'dnekeew', 'and': 'dna', 'non-veg': 'gev-non', 'special': 'laiceps'}
# s="tomorrow is weekend and non-veg special"
# d={}
# for i in s.split():
#     d[i]=i[::-1]
# print(d)
