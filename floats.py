# Convert a float to an integer with an inbuilt function in Python
# temp = 56.8926 to 57
temp = 56.8926
print(round(56.8926,0))

# Convert the float below to give the results as follows
# temp = 56.8926 to 56.89 
temp = 56.8926
print(round(56.8926,2))

# Convert the float below to give the results as follows
# temp = 56.8926 to 56.893 
temp = 56.8926
print(round(56.8926,3))

# Convert the float below to give the results as follows
# temp=56.8926 to 8.926 
# NB: Use string  slice & concatenation, but have result as float 
temp=56.8926
x=str(temp)
temp=x[3]+'.'+x[4: ]
# temp=float
print(temp)
# Attempt questions below. Whether you get the right answer or not, still read the solution explanation.
# https://realpython.com/quizzes/python-data-types/

w = (10 % 3)
print(w)

x =(10 // 3)
print(x)

# Python follows this rule:The remainder always has the same sign as the divisor (the second number).
y = (-10 % 3)
print(y)

z =(-10 // 3)
print(z)