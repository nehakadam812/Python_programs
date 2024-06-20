# local variable
# def spam():
#     a=10   #local variable
#     print(a)
# spam()
# print(a)

# def spam():
#     a=10
#     return a
# print(spam())


# global variable(another name=name space)
# a=10
# def spam():
#     ...
# spam()
# a+=100
# print(a)


# a=10
# def spam():
#     print(a)
# spam()
# print(a)

# a=10
# def spam():
#     global a
#     a+=100
#     print(a)
# spam()



# a=100 #global variable
# def span():
#     b=100 #local variable
#     print(a)
#     def demo():
#         c=300 #non-local variable
#         print(a)
#     demo()
# span()
# print(a)

# a=100
# def span():
#     b=100
#     print(b)
#     def demo():
#         c=300
#         print(b)
#     demo()
# span()
# print(b)
#
# a=100
# def span():
#     b=100
#
#     def demo():
#         c=300
#         print(c)
#
#     print(c)
#     demo()
# span()
# print(c)

# def span():
#     b=100
#     def demo():
#         nonlocal b
#         b=b+10
#         print(b)
#         c=50
#     demo()
# span()
