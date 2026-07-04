# strings are iterable objects, they contain a sequence of characters:
for x in "banana":
  print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
  
# Exit the loop when x is "banana", but this time the break comes before the print:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

# With the continue statement we can stop the current iteration of the loop, and continue with the next:
# Do not print banana:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

# To loop through a set of code a specified number of times, we can use the range() function,The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.

# Write a program that displays a numbers 1 to 50 inside a list.
# for i in range(1,51):
#     print(list(range(1,51)))
# From 1 above display the ones divisible by 7 or 5 inside a list.
x=[]
for i in range(1,51):
    if i%7==0 or i%5==0:
        x.append(i)
print(x)
# Find sum and average of values in the range between 10 to 40.
sum=0
no=list(range(10,41))
for i in no:
    sum=sum+i
print(sum)
average=sum/len(no)
print(average)
# Put in a list the first 10 odd numbers between 10 to 50.
odd_numbers=[]
for i in range(10,30):
    if i%2!=0:
        odd_numbers.append(i)
print(odd_numbers) 
# write a program that takes a number as input and prints its multiplication table up to 10 using a for loop.
num=int(input("enter the number"))
u=range(0,11)
for i in u:
    multi=i*num
    print(f"{i}*{num}={multi}")
# write a program that counts and prints the number of even numbers between 1 and 50 using a for loop
count=0
no=list(range(1,51))
for i in no:
       if i%2==0:
              count=count+1
print(count)
# ls1 = [ (“Jay”, ‘20’), (“Mo”, ‘30’), (“Mya”, ‘32’) ]
# Display the total quantity of the 3 above.
