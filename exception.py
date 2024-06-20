# Types of except types
# 1)default except block
# a=[1,3,45]
# try:
#     print(a[7])
# except:
#     print('exception handle')

# 2)specific except block
# a=10
# try:
#   print(a/b)
# except NameError:
#     print('name error')

# 3) multiple except block
# l=[1,2,3,4]
# try:
#  print(l(10))
# except NameError:
#     print('name error')
# except KeyError:
#     print('key error')
# except TypeError:
#     print('Type error')
# except IndexError:
# #     print('index error')
#
# l=[1,2,3,4]
# try:
#  print(l(10))
# except (NameError,KeyError,TypeError,IndexError):
#     print(' error')


# 4)Generic error
# l=[4,5,6]
# try:
#     print(l.values())
# except Exception as abc:
#      print('error')
#      print(abc)

# s=1283
# try:
#     print(len(s))
# except Exception as abc:
#     print(abc)

# s={1,2,3,4,5}
# try:
#     print(s.remove(50))
# except KeyError:
#     print('Keyerror')

# Nested try-except block
a=10
b=2
try:
    print(a/b)
    try:
        print(a/c)
    except NameError:
        print('name error')
except 

