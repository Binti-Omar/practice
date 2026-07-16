# Clean up the following variable to give the clean version in lower case. Using inbuilt methods in the str class 
# name = “  JOHn  .“ to “john”
# Slice the below string to get you the resulting sentence:
# sentence_one = “The Dog Breed is German Shepherd” only display “Breed is German”
# sentence_two = “Defeats for the Clinton forces, this was her moment of triumph” only display “Clinton forces”
# Split the below sentence using a semicolon i.e ; And display length of the result. 
# “The lazy dog; ran so fast; it hit the wall.” 
# first_name="  Joh.n"  last_name="   Do,e" Clean up and display Full name i.e John Doe
# Having the string r = '["E","W","C"]' #Manipulate it to display EWC
# Attempt questions in the link below. Whether you get the right answer or not, still read the solution explanation.
# https://realpython.com/quizzes/python-strings/


name = "  JOHn  ."
# print(name.lower())
# print(name.replace("."," "))
# print(name.strip())
# print(name.lower().replace("."," ").strip())
# if you don't want to replace the dot with a space you can remove it instead
# print(name.removesuffix("."))
print(name.lower().strip().removesuffix("."))

sentence_one = "The Dog Breed is German Shepherd"
print(sentence_one[8:23])

sentence_two = "Defeats for the Clinton forces, this was her moment of triumph"
print(sentence_two[16:30])

sentence_three= "The lazy dog; ran so fast; it hit the wall."
# print(sentence_three.split(';'))
print(len(sentence_three.split(";")))

first_name="  Joh.n"
first_name=first_name.replace(".","")
first_name=first_name.strip()
print(first_name)

last_name="   Do,e"
last_name=last_name.replace(',','')
last_name=last_name.strip()
print(last_name)
print(first_name + " " + last_name)

r = '["E","W","C"]'
clean_string=r[2:11:4]
print(clean_string)

# strings are immutable --- if you want to change a string store it in a variable first or at the print
x = "binti"
# y = x.capitalize()  
# print(y)
print(x.capitalize())