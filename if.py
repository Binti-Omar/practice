# Take three inputs from a user, separately. Print the largest of the numbers.
#     Hint: Determine what type of data is taken in as input.

# we will use "and" to compare not "or" since all of these conditions must be true
no1=int(input("Enter the first number:"))
no2=int(input("Enter the second number:"))
no3=int(input("Enter the third number:"))
if no1 > no2 and no1 > no3:
    print("The largest number is",no1)
if no2 > no1 and no2 > no3:
    print("The largest number is",no2)
if no3 > no1 and no3 > no2:
    print("The largest number is",no3)
# 2.Take as input from a user the temperature if the temperature is above 30°C display “The temperature is too high”,if the temperature is above 15 display “Normal temperature” otherwise display “Cold temperature”
temp=float(input("What is your temperature?"))
if temp > 30:
    print("The temperature is too high")
elif temp > 15 :
    print("Normal temperature")
else:
    print("Cold temperature")
# 3.	Write a Python program that checks if a variable x is between 10 and 20 (inclusive)
# and if another variable y is greater than 100. If both conditions are true, print "Conditions met", otherwise print "Conditions not met"
x = 20
y = 100
if x >= 10 and x<= 20 and y > 100:
    # if y > 100:
    print("Conditions met")
else:
    print("Conditions not met")
# 4. Write a Python program that checks if a variable password is equal to the string "secret123". If it is, print "Access   granted", otherwise print "Access denied"
password = "secret123"
if password == "secret123":
    print("Access   granted")
else:
    print("Access   denied")


#          Attempt the questions in the link below
# https://realpython.com/quizzes/python-conditional-statements/
