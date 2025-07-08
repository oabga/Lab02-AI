# class MyClass:
#     def __init__(self, **kwargs):
#         print(kwargs)
#         self.__dict__.update(**kwargs)

# # Example usage:
# my_dict = {
#     'name': 'Alice',
#     'age':30, 
#     'city': 'New york'
# }
# # obj = MyClass(name="Alice", age=30, city="New York")
# obj = MyClass(my_dict= my_dict)
# # print(obj.name)  # Output: Alice
# # print(obj.age)   # Output: 30
# # print(obj.city)  # Output: New York
# print(dir(obj))

a = [1, 2, 3]
a.pop()
print(a)