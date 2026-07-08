# TASK 1: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that prompts the user to enter the base and height of a triangle and returns its area.
# Once you learn functions,revisit this and write this code inside a function.

# base = int(input("Enter the base here:"))
# height = int(input("Enter the height here:"))
# c = 1/2
# area =c * base * height
# print(area)

base = int(input("Enter the base here:"))
height = int(input("Enter the height here:"))
# half = 1/2

def area_triangle(base,height):
    area = 1/2 * base * height
    # sends the result back to where the function was called.
    return area

print(area_triangle(base,height))

# TASK 2: Using Python or PHP or Java or Ruby or JavaScript
# Prompt the user for a number either on a form input or the terminal. Depending on whether the number is even or odd, display  either “odd” or “even” to the user.
#  Hint: how does an even / odd number react differently when divided by 2?
# Once you learn functions,revisit this and write this code inside a function.
# Extras:
# If the number is a multiple of 4, print out “divisible by 4”.
# Once you learn functions,revisit this and write this code inside a function.

# numb = int(input("Write a number here:"))

# if numb%2==0:
#     print("The number is an even number")
#     if numb%4==0:
#         print("The number is divisible by 4")
# else:
#     print("The number is an odd number")

# # method 2 is logically correct
# numb = int(input("Write a number here: "))

# if numb % 4 == 0:
#     print("The number is even.")
#     print("The number is divisible by 4.")
# elif numb % 2 == 0:
#     print("The number is even.")
# else:
#     print("The number is odd.")   

number = int(input("Enter your number: ")) 

def check_number(number):
    if number % 4  == 0:
        message = "The number is even and divisible by 4"
    elif number % 2 == 0:
        message = "The number is even"
    else:
        message = "The number is odd"    

    return message

print(check_number(number))

# TASK 3: Using Python or PHP or Java or Ruby or JavaScript
# Write a program which gets a phone number from a form input or terminal. Validates the phone number by checking if it starts with +254.. or 07.. or 7… or 254.. or 01... or  1.. Convert the number to start with +254… 
# e.g if a user enters “0712345678”, the program should display “+254712345678”
# e.g if a user enters “0112345678”, the program should display “+254112345678”
# e.g if a user enters “712345678”, the program should display “+254712345678”
# Once you learn functions,revisit this and write this code inside a function.

# phone_number = input("Enter phone number: ").strip()

# if phone_number.startswith("+254") and len(phone_number) == 13:
#     print("The number is correct")

# elif phone_number.startswith("07") and len(phone_number) == 10:
#     phone_number = "+254" + phone_number[1:]
#     print(phone_number)

# elif phone_number.startswith("7") and len(phone_number) == 9:
#     phone_number = "+254" + phone_number
#     print(phone_number)

# elif phone_number.startswith("254") and len(phone_number) == 12:
#     phone_number = "+" + phone_number
#     print(phone_number)

# elif phone_number.startswith("01") and len(phone_number) == 10:
#     phone_number = "+254" + phone_number[1:]
#     print(phone_number)

# elif phone_number.startswith("1") and len(phone_number) == 9:
#     phone_number = "+254" + phone_number
#     print(phone_number)

# else:
#     print("Invalid phone number.")

phone_number = input("Enter phone number: ").strip()

def validate_phone_number(phone_number):
    if phone_number.startswith("+254") and len(phone_number) == 13:
        return "the number is correct"

    elif phone_number.startswith("07") and len(phone_number) == 10:
        return "+254" + phone_number[1:]

    elif phone_number.startswith("7") and len(phone_number) == 9:
        return "+254" + phone_number

    elif phone_number.startswith("254") and len(phone_number) == 12:
        return "+" + phone_number

    elif phone_number.startswith("01") and len(phone_number) == 10:
        return "+254" + phone_number[1:]

    elif phone_number.startswith("1") and len(phone_number) == 9:
        return "+254" + phone_number

    else:
        return "Invalid phone number."
print(number(phone_number))

# TASK 4: Using Python or PHP or Java or Ruby or JavaScript
# Write a program which accepts email as form input or from terminal. Validate the email by checking if it's a valid email. 
# Hint: Check if it contains an “@” symbol and “.” symbol.
# Once you learn functions,revisit this and write this code inside a function.

# email=input("enter the email: ")

# if email.find('@')==-1 or email.count('.')==0:
#     print('invalid email')
# else:
#     print('valid email')

# email=input("enter email:")

# if '@' in email and '.' in email:
#     print('Valid email')
# else:
#     print("invalid email")

email=input("enter the email: ")

def check_email(email):
    if '@' in email and '.' in email:
        return "Valid email"
    else:
        return "invalid email"
print(check_email(email))

# TASK 5: Using Python or PHP or Java or Ruby or JavaScript
# Implement a program that takes 3 users  inputs from the terminal or the Browser, and stores them in three variables. Return the largest of the three. Do this without using the the inbuilt max () function!
# The goal of this exercise is to think about some internals that programs normally take care of for us. 

a = int(input("enter the first number: "))
b = int(input("enter the second number: "))
c = int(input("enter the third number: "))

if a>=b and a>=c:
    print(f"the largest number is {a}")
elif b>=a and b>=c:
    print(f"the largest number is {b}")
else:
    print(f"the largest number is {c}")

# TASK 6:Using Python or PHP or Java or Ruby or JavaScript
# Write a program that lets the user input a password. Give them only 4 attempts to check the passwords entered against “admin@123”. If the password is correct access is granted. After you show them a message , the account is blocked.
# Once you learn functions,revisit this and write this code inside a function.

# attempts = 4
# correct_password="admin@123"
# for i in range(1, attempts + 1):
#     password = input("enter password here: ")
#     if password == correct_password:
#         print("Access granted")
#         break
#     else:
#         remaining_attempts  =attempts - i
#         if remaining_attempts > 0:
#             print(f"Access denied.You have {remaining_attempts} attempts remaining")
#         else:
#             print("The account is blocked.")

attempts = 4
correct_password = "admin@123"

for i in range(4):
    password = input("Enter password: ")

    if password == correct_password:
        print("Access granted")
        break
    else:
        remaining_attempts = attempts - i - 1

        if remaining_attempts > 0:
            print(f"Access denied. You have {remaining_attempts} attempt(s) remaining.")
        else:
            print("The account is blocked.")

# TASK 7: Using Python or PHP or Java or Ruby or JavaScript
# Write that prompts the user to input student marks. The input should be between 0 and 100.Then output the correct grade: 
# A > 79 , B - 60 to 79, C  > 49 to 59, D - 40 to 49, E - less 40
# Once you learn functions,revisit this and write this code inside a function.
students_marks = int(input("Enter marks : "))

if students_marks < 0 or students_marks > 100:
    print("Invalid marks")

elif students_marks >= 79:
    print("A")

elif students_marks >= 60:
    print("B")

elif students_marks >= 49:
    print("C") 

elif students_marks >= 40:
    print("D") 
    
else:
    print("E") 

# TASK 8: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that takes as input the speed of a car e.g 80. If the speed is less than 70, it should print “Ok”. Otherwise, for every 5 km/s above the speed limit (70), it should give the driver one demerit point and print the total number of demerit points.
# For example, if the speed is 80, it should print: “Points: 2”. If the driver gets more than 12 points, the function should print: “License suspended”.
# Once you learn functions,revisit this and write this code inside a function.
# speed = int(input("Enter the car speed: "))

# if speed <= 70:
#     print("OK")
# else:
#     total_points = (speed - 70) // 5
#     print(f"demerit points:{total_points}")
#     if total_points > 12:
#         print("License suspended")
#     else:
#         print("Do not exceed the speed limit.")

speed = int(input("Enter the car speed: "))

if speed <= 70:
    print("OK")
else:
    total_points = (speed - 70) // 5
    print(f"Points: {total_points}")

    if total_points > 12:
        print("License suspended")  


# TASK 9: Using Python or PHP or Java or Ruby or JavaScript
# Write a program called stars. It should prompt the user for a number, and it should print the number of stars till the number entered.
# Example If rows is 5, it should print the following:
# *
# **
# ***
# ****
# *****.....
# Once you learn functions,revisit this and write this code inside a function.
stars = int(input("Enter a number: "))

for i in range(1,stars + 1):
   print("*" * i)

# TASK 10: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that calculates the total stock in a company from the array/list below if we know that the stock is the last digit in every array/list.

# prods = [[‘omo’,’30kshs’,’300’], [‘milk’,’50kshs’,’200’],[‘bread’,’45kshs’,’359’], [‘coffee’,’5kshs’,’79’]]

# NB: ONCE YOU COPY AND PASTE THE LIST ABOVE,REWRITE THE SINGLE QUOTES AS THE ABOVE LIST WILL GIVE YOU AN ERROR.
# Once you learn functions,revisit this and write this code inside a function.
# prods = [['omo','30kshs','300'], ['milk','50kshs','200'], ['bread','45kshs','359'], ['coffee','5kshs','79']]

# for product in prods:
#     product[2] = int(product[2])

# x=prods[0][2]+prods[1][2]+prods[2][2]+prods[3][2]

# print(x)

prods = [['omo','30kshs','300'], ['milk','50kshs','200'],['bread','45kshs','359'], ['coffee','5kshs','79']]

total_stock=0

for i in prods:
    print(int((i[2])))
    total_stock=total_stock +int((i[2]))

print(total_stock)


# TASK 11: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that takes the date of birth of a person and the program outputs the age in terms of years,months,days TODAY.datetime
# Once you learn functions,revisit this and write this code inside a function.

# TASK 12: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that prints the largest of 4 inputs taken as input from a user.
# Once you learn functions,revisit this and write this code inside a function.

# TASK 13: Using Python or PHP or Java or Ruby or JavaScript or C# or Go
# Write a program that takes the email and password as input from a user and checks if they are equal to “admin@mail.com” and password is “Admin@123” , if so then print  “Login is Successful” and if not print “Invalid username or password”. ONLY accept 3 tries after which it notifies you that you have been blocked.
# Once you learn functions,revisit this and write this code inside a function.

# TASK 14: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that takes input of 2 values and adds them. The program should only accept numbers and floats only or otherwise display an error “invalid character entered” and take the user to re-enter the inputs .
# Once you learn functions,revisit this and write this code inside a function.





# TASK 15: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that takes input of someone's basic salary and benefits, adds them to find the gross salary then uses  the gross salary to find the NHIF. 
# To find the Kenya NHIF Rate using THIS LINK:  
# Write a normal program but use functions if you feel comfortable.

# TASK 16: Using Python or PHP or Java or Ruby or JavaScript
# Continue with the program above, then use  the gross salary to find the NSSF. 
# To find the Kenya NSSF Rate  using 6% of the Gross Salary. BUT ONLY A MINIMUM OF 18,000 Gross Salary CAN BE USED IN NSSF. 
# Write a normal program but use functions if you feel comfortable.

# Task 17: Using Python or PHP or Java or Ruby or JavaScript
# Continue with the same program and calculate an individual’s NHDF using:
#  i.e NHDF = gross_salary *  0.015
# Write a normal program but use functions if you feel comfortable.

# Task 18: Using Python or PHP or Java or Ruby or JavaScript
# Calculate the taxable income.
# i.e taxable_income = gross salary - (NSSF + NHDF + NHIF) 
# Write a normal program but use functions if you feel comfortable.

# TASK 19: Using Python or PHP or Java or Ruby or JavaScript
# Continue with the same program and find the person's PAYEE using the taxable income above.
# Find the Kenya PAYEE Tax Rate using THIS LINK
# Write a normal program but use functions if you feel comfortable.

# Task 20: Using Python or PHP or Java or Ruby or JavaScript
# Continue with the same program and calculate an individual’s Net Salary using:
#  net_salary = gross_salary - (nhif + nhdf +  nssf + payee)

# Write a normal program but use functions if you feel comfortable.


# MILESTONE TASK Using Python or PHP or Java or Ruby or JavaScript
# Create a class called Payroll whose major task is to calculate an individual’s Net Salary by getting the inputs basic salary and benefits. Create 5 different class methods which will calculate the payee, nhif_deductions, nhdf_deductions, nssf_deductions, gross_salary and net_salary. 

# NB: Use KRA, NpHIF and NSSF values provided in the links above.


# Attempt questions below for Python. Whether you get the right answer or not, still read the solution explanation.


# https://realpython.com/quizzes/python-data-types/
# https://realpython.com/quizzes/python-strings/ 
# https://realpython.com/quizzes/python-lists-tuples/
# https://realpython.com/quizzes/python-dicts/
# https://realpython.com/quizzes/pybasics-conditional-logic/
# https://realpython.com/quizzes/pybasics-functions-loops/