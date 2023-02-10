# 1.function are object the decorators
# def sum_five(num):
#     print(num + 5)
# sum_five(3)

#2.functions within a functions

# def add_five(num):
#     def add_two(num):
#         return num+2
#     add_plus_two= add_two(num)
#     print(add_plus_two + 3)
# add_five(10)

   
#3 Returning function with function

# def get_math_function (operation):
#     def add(n1, n2):
#         return n1 + n2
#     def sub(n1, n2):
#         return n1 - n2   
#     if operation == '+':
#         return add
#     elif  operation == '-':
#         return sub
# add_function = get_math_function('+')
# print( add_function(4,6))




#4 Decorating a function

def print_name():
    print('Avinash sharma')
print(print_name)

#5 Decorators
#6 Decorators v/s Parameter