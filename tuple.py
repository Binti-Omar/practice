days = ("monday","tuesday","wednesday","thursday", "friday","saturday","sunday")
#1. Find wednesday using an index
print(days[2])
#2. Using a function a find the length of the tuple.
print(len(days))
#3. Replace Thursday with Thur
days=list(days)
days[3]="thur"
print(days)
days=tuple(days)
print(days)

# 1. numbers = (10, 20, 30, 40, 50)Add 60 to the end,Replace 30 with 35.
numbers = (10, 20, 30, 40, 50)
number=list(numbers)
print(number)
number.append(60)
number[2]=35
print(tuple(number))
# 2. values = (15, 5, 30, 25, 10) arrange the elements in ascending order.
values = (15, 5, 30, 25, 10)
x=list(values)
x.sort()
print(tuple(x))
# 3. fruits = ("apple", "banana", "cherry", "banana", "mango", "banana")
# Count occurrences of "banana",Remove all occurrences of "banana".
fruits = ("apple", "banana", "cherry", "banana", "mango", "banana")
fruits=list(fruits)
print(fruits.count("banana"))
fruits.remove("banana")
fruits.remove("banana")
fruits.remove("banana")
print(tuple(fruits))
# 4. names = ("Alice", "Bob", "Charlie", "David") Reverse the order of elements using sort method.
names = ("Alice", "Bob", "Charlie", "David")
names=list(names)
names.sort()
print(tuple(names))
# 5. colors = ("red", "blue", "green")add "yellow" at index 1,Extend with ["purple", "orange"]
colors = ("red", "blue", "green")
colors=list(colors)
colors.insert(1,"yellow")
colors.extend(["purple", "orange"])
print(tuple(colors))
# Attempt questions in the link below. Whether you get the right answer or not, still read the solution explanation.
# https://realpython.com/quizzes/python-lists-tuples/viewer/
