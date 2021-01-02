# String Method
name = "Jibon Ahmed"
print(name)

# len () method
print("len : ", len(name))

# lower () method
a = name.lower()
print("lower :", a)

# upper() method
b = name.upper()
print("Upper : ", b)


# title method
c = name.title()
print("title :", c)


# count () method
d = name.count('o')
print("count :", d)


# Take two comma separated inputs from user
# 1. User's name example - "JIbon"
# 2. a single character, "h"

# output - 2 print lines

# 1). User's name length
# 2). count the character that user inputed

# lstrip () method
name = "    Jibon   "
dost = "..........."
x = name.lstrip()  # remove white space for leftside
print(x)

y = dost.rstrip()  # remove white space for rightside
print(y)


# Example remove extra space
x = "Hello      World    programmer"
y = x.replace(" ", "")
print("Remove extra space :", y)


# Example

string = "she is beautiful and she is a good dancer"
print(string)

# replace () method
# x = string.replace(" ", "_")
# print(x)
print(string)
y = string.replace("is", "was")
print("Replace :", y)

# find () method
z = string.find("is")
print("Find : ", z)

# More example
learn = "how to find position and how to use string find method"
print(learn)
c = learn.find("how")
d = learn.find('how', 1)    # Here 1 for start 1 position
print(c)

