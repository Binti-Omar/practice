# # 1.write a program that takes users age as input
# # if the age is 18 and above ,check if they have  drivers license if they do we print you are eligible to drive
# # if they dont have a drivers license print you are not eligible to drive
# # otherwise you are too young to drive
# age=int(input("Enter your age here: "))
# if age >= 18:
#     license=input("Do you have a drivers license? (Yes/No):" ).strip().lower()
#     if license == "Yes":
#         print("You are eligible to drive")
#     else:
#         print("You are not eligible to drive")
# else:
#     print("You are too young to drive")

# # This approach will ask about license even if the age is below 18
# # age=int(input("Enter your age here: "))
# #   license=input("Do you have a drivers license? (Yes/No):" ).strip().lower()
# # if age >= 18:
# #     if license == "Yes":
# #         print("You are eligible to drive")
# #     else:
# #         print("You are not eligible to drive")
# # else:
# #     print("You are too young to drive")


# # 2.# Write a program that:
# # # = > Takes the user's credit score and annual income as input.
# # # =>If the credit score is above 700, check if the income is above 50,000:
# # # =>If both conditions are met, print "Loan approved."
# # # =>If only the credit score is high, print "Income requirement not met."
# # # =>If the credit score is below 700, print "Credit score too low."
# credit_score=int(input("Enter your credit score:"))
# if credit_score > 700:
#     income=float(input("Enter your annual income:"))
#     if income > 50000:
#         print("Loan approved")
#     else:
#         print("Income requirement not met.")
# else:
#     print ("Credit score too low.")

# # This method will ask about income even if the score is below 700
# # credit_score=int(input("Enter your credit score:"))
# # income=float(input("Enter your annual income:"))
# # if credit_score > 700:
# #     if income > 50000:
# #         print("Loan approved")
# #     else:
# #         print("Income requirement not met.")
# # else:
# #     print ("Credit score too low.")


# # 5. Write a Python program that checks if a variable student_score is greater than 90. If true, check if the attendance is greater than 80. If both conditions are true, print "Excellent student", otherwise print "Good score, but attendance needs improvement"
# student_score=10
# attendance=89
# if student_score > 90:
#     if attendance > 80:
#         print("Excellent student")
#     else:
#         print("Good score, but attendance needs improvement")
# else:
#     print("Improve the score")

# Write a program that:
# Takes a transaction amount and account type ("Standard" or "Premium") as input.
# If the account type is "Standard":
# Check if the amount is above 500:
# If it is, print "Transaction exceeds the limit for Standard accounts."
# If not, print "Transaction approved."
# If the account type is "Premium":
# Check if the amount is above 1,000:
# If it is, print "Transaction exceeds the limit for Premium accounts."
# If not, print "Transaction approved."
# Otherwise “Wrong account type”
# account = input("Is your account type standard or premium?").strip().lower()
# if account == "standard":
#     amount = int(input("enter your amount :"))
#     if amount > 500:
#         print("Transaction exceeds the limit for Standard accounts.")
#     else:
#         print("Transaction approved.")
# elif account=="premium":
#     amount = int(input("enter your amount :"))
#     if amount > 1000:
#         print("Transaction exceeds the limit for Premium accounts.")
#     else:
#         print("Transaction approved.")
# else:
#     print("Wrong account type")
# 1.Assume start_date = '2024-01-01' and end_date = '2024-12-31'. Write a conditional statement that checks:
# If start_date comes before end_date, print "Valid period",
# If start_date is after end_date, print "Invalid period".
# If both dates are the same, print "One-day period".
start_date=2024_01_01
end_date=2024-12-31
if start_date < end_date:
      print("valid period")
elif start_date > end_date:
      print("invalid period")
else:
      print("one-day period") 
# 2.Given two strings str1 and str2, write a conditional statement that checks:
# If str1 is longer than str2, print "str1 is longer".
# If str2 is longer than str1, print "str2 is longer".
# If both have equal length, print "Both are of equal length".
str1=20
str2=21
if str1 >str2:
      print("str1 is longer")
elif str1<str2:
      print("str2 is longer")
else:
      print("both are of equal length")
# 3.Given a list valid_ids = [101, 102, 103] and a variable user_id = 105, write a conditional statement that:
# Prints "Access Granted" if user_id is in valid_ids.
# Prints "Access Denied" if user_id is not in valid_ids.
valid_ids = [101, 102, 103]
user_id = 105
if user_id in valid_ids:
    print("Access Granted")
else:
    print("Access Denied")   
# 4.Given a variable value that could be of any type, write a conditional statement that:
# Prints "String Detected" if value is a string.
# Prints "Integer Detected" if value is an integer.
# Prints "Unknown Type" for any other type.
value=190.09
if type(value) ==str:
      print("string detected")
elif type( value) ==int:
     print("integer detected")
else:
      print("unknown type")
# 5.Given x = 7 and y = 14, write nested conditional statements that print:
# "x and y are both even" if both x and y are even numbers.
# "Only y is even" if only y is even.
# "Neither x nor y are even" if both are odd.
x = 7
y = 14
if x%2==0 and y%2==0:
    print("both x and y are even numbers.")
    if y%2==0:
       print("Only y is even")  
    else:
        print("y is not even") 
else:
    print("Neither x nor y are even")   

