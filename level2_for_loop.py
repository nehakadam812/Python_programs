# 1.wap to create a dictionary index and word pair
# s="tomorrow is weekend and non-veg special"
# o/p:-->{0: 'tomorrow', 1: 'is', 2: 'weekend', 3: 'and', 4: 'non-veg', 5: 'special'}
# s="tomorrow is weekend and non-veg special"
# d={}
# for i in s.split():
#         d[i]=s.index(i)
# print(d)

# 2.wap to create a dictionary words and its length pair
# s="tomorrow is weekend and non-veg special"
#
# o/p:-->{'tomorrow': 8, 'is': 2, 'weekend': 7, 'and': 3, 'non-veg': 7, 'special': 7}
# s="tomorrow is weekend and non-veg special"
# d={}
# for i in s.split():
#     d[i]=len(i)
# print(d)

# 3.wap to create a dictionary characters and its corresponding upper case characters
# s="sunday"
#
# o/p:-->{'s': 'S', 'u': 'U', 'n': 'N', 'd': 'D', 'a': 'A', 'y': 'Y'}
# s="sunday"
# d={}
# for i in s:
#     d[i]=i.upper()
# print(d)

# 4.wap to create a dictionary Ascii and character pair
# l=[89,51,111,77,108,120]
#
# o/p:-->{89: 'Y', 51: '3', 111: 'o', 77: 'M', 108: 'l', 120: 'x'}
# l=[89,51,111,77,108,120]
# d={}
# for i in l:
#     d[i]=chr(i)
# print(d)

# 5.wap to  create a list of characters and its Ascii value pair
# s="sunday"
# o/p:-->[('s', 115), ('u', 117), ('n', 110), ('d', 100), ('a', 97), ('y', 121)]

# s="sunday"
# d={}
# for i in s:
#     d[i]=ord(i)
# print(d)


# 6.WAp to perform clear() in list without using inbuilt method
# lst= ['hai', 'hello', 'python', 'world', 'jingalala']
# l=[]
# lst=l
# print(lst)
# print(lst)


# 7.wap to create a dictionary with words and its length pair and ends with vowel
# s="Today is Tuesday and attending python session aa"
# v=['a','A','o','O','E','e','I','i','U','u']
# d={}
# for i in s.split():
#   if i[len(i)-1] in v:
#       d[i]=len(i)
#       print(len(i))
#
# print(d)

# 8.wap to create a dictionary with letter and its words starting with that letter pair
# s="hi hello good morning welcome to python session"
# d={}
# for i in s.split():
#     d[i[0]]=i
# print(d)

# 9.wap to create a dictionary of characters and its indices pair
# s="hello python"
# o/p:-->{"h":[0,9],"e":1..........}
# s="hello python"
# d={}
# for i in s:
#     d[i]=s.index(i)
# print(d)

# 10.wap to using this list get the below output
#
l = ['sun flower', 'lily flower', 'Marigold flower', 'lion animal','tiger animal', 'eagle bird', 'snake animal', 'lotus flower', 'pigeon bird']
#
# o/p:-->{'flower': ['sun', 'lilly', 'Marigold', 'lotus'], 'animal': ['lion', 'tiger', 'snake'], 'bird': ['eagle', 'pigeon']}
# fl=[]
# an=[]
# br=[]
# d1={'flower','animal','bird'}
# d={}
# for i in l:
#     if i.endswith('flower'):
#         fl.append(i.strip('flower'))
#     elif i.endswith('animal'):
#         an.append(i.strip('animal'))
#     else:
#         br.append(i.strip('bird'))
# d['flower']=fl
# d['animal']=an
# d['bird']=br
# print(d)

# 11.wap to sum of same index element from
# l1=[1,2,3,4,5]
# l2=[2,3,4,5,6]
# l3=[11,12,13,14,15]
# from itertools import  zip_longest
# for i in zip_longest(l1,l2,l3):
#     sum=0
#     for j in i:
#         sum+=int(j)
#     print(sum,end=" ")

# 12.wap to pair values of both dictionary
#
# d={"apple":45,"mango":67,"cherry":90,"berry":23}
# p={"kashmir":"ind","america":"us","uk":"toronto","africa":"uganda"}
#
# for i in zip(d.values(),p.values()):
#     print(i,end=" ")
#



# 13.wap to group fruit name and country pair only if a fruit is even length

d={"apple":45,"mango":67,"cherry":90,"berry":23}
p={"kashmir":"ind","america":"us","uk":"toronto","africa":"uganda"}
for i in zip(d,p):
    if len(i[0])%2==0:
        print(i)





# 14.WAP to check whether string is ANAGRAM or not (anagrams : characters should be same it can different meaning)
# take user input
# s1=input('enter the string 1 : ')
# s2=input('enter the string 2  : ')
# if list(s1).sort() ==list(s2).sort():
#     print('true')

# 15.WAp to print longest word in a sentence
# s = 'life is full of surprises and miracles'
 # #exp o/p : surprises
# s = 'life is full of surprises and miracles'
# lw=''
# l=0
# for i in s.split():
#    if len(lw)<len(i):
#        lw=i
# print(lw)

# 16.Replaces whitespaces with new line char in the below string
# s = 'hello world welcome to python'
# for i in s.split():
#     print(i)


# 17.wap to check  whether the elements inside the list is even or odd and i want the dictionary pair
# l=["apple","samsung","oracle","flipkart","facebook","instagram","amazon","ebay"]
# o/p:-->{'odd': ['apple', 'samsung', 'instagram'], 'even': ['oracle', 'flipkart', 'facebook', 'amazon', 'ebay']}
# l=["apple","samsung","oracle","flipkart","facebook","instagram","amazon","ebay"]
# d={}
# o=[]
# e=[]
# for i in l:
#     if len(i)%2==0:
#         e.append(i)
#     else:
#         o.append(i)
# d.setdefault('odd',o)
# d.setdefault('even',e)
# print(d)

# 18.wap to traverse through a string and stop the execution at specific characters by using break keyword
# s="hello guys tomorrow holiday"
# specified char="d"
# s="hello guys tomorrow holiday"
# for i in s:
#     if i=='d':
#         break
#     print(i,end='')

# 19.wap to print double digit numbers present in list by using continue keyword
l=[2,3,45,67,89,11,2,3,4,5,6,7,8,11]
# for i in l:
#    if i<10:
#        continue
#    print(i,end=' ')


# 20.wap to print only positive numbers by using continue keyword

# l=[1,5,-2,-45,55,88,-100,-63]
# for i in l:
#     if i<0:
#         continue
#     print(i,end=' ')


# 21.wap to skip all the vowels in the given string
# s="good morning guys welcome to python session"
# v=['a','e','i','o','u','A','E','I','O','U']
# for i in s:
#     if i not in v:
#         print(i,end='')






