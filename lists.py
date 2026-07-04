# Create a List of days of the Week. Print the day today using an index
days1=["monday","tuesday","wednesday","thursday"]
days2=["friday","saturday","sunday"]
# accessing a day
print(days1[2])
# length of the list
print(len(days1))
# Concatenate two list
print(days1+days2)
# Repetition
print(days2*4)
# Membership (in) returns a boolean
print("friday" in days2)
# Delete element in a list
del days1[0]
print(days1)
# Update values in a list 
list=days1[0]="friday"
print(list)
print(days1)
# Adding a value at end of list 
days2.append("tuesday")
print(days2)

# trainees = ["John", [2, ["James","Mary"]]]
# 1. Display 2 from the list.
# 2. Output James  from the list.
# 3. Using a method add 56 at the end of the list.
# 4. Using a method add the name Mike between James and Mary
# 5. Change the value of 2 to 8
# 6. Remove John and Mary from the list.
# 7. Using a function, determine the length of the list
# Attempt questions in the link below. Whether you get the right answer or not, still read the solution explanation.
# https://realpython.com/quizzes/python-lists-tuples/viewer/

trainees = ["John", [2, ["James","Mary"]]]
print(trainees[1][0])
print(trainees[1][1][0])
trainees.append(56)
print(trainees)
trainees[1][1].insert(1,"Mike")
print(trainees)
trainees[1][0]=8
print(trainees)
trainees.remove("John")
# we are starting with index 0 since we removed john from the list
trainees[0][1].remove("Mary")
# trainees[0][1].pop()
print(len(trainees))


