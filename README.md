# Python Control Flow
## if elif else
### Loops - for loop - while loop
#### Python keywords break - continue etc
 
# Control flow:
```python
# Sudo Coding

weather = "time"
# if it's cold:

if weather == "sunny":# True or False
    print("lets go to the beach")
    #take jacket

elif weather == "sunny":
    print("lets go to the beach")

# if its raining:
else:
     print("no match found better luck next time")
     # rain mack



#if its sunny: booleon value true - next line
    #lets go to the beach
# else or elif

# age restriction for movie ticket
# create a condition for 18 & above
# 16 & above
# PG
# 12a
# 15 & above
# if nothing matched inform the user to enter their age again = ELSE
# user ust not be allowed to enter age over 117 years

```
Loops Task
```python


list_data = [1, 2, 3, 4, 5]
for number in list_data:
    if number  == 3:
       print("found 3")
    elif number > 3:
       print("You have passed 3")
    else:
        print("too soon")


# create a dictionary student_1
# iterate through the dictionary
# using control flow - if elif - else and for loop print all the keys
# print all the values
# print key with matching value



student_data = {
    "name" : "Ayoub",
    "surname" : "Igozouln",
    "age" : "22"
}


for key in student_data:
    print(key)
values = student_data.values()
print(values)
for key in student_data:
    if key in student_data:
        print(key, student_data[key])


```
# Control Flow Refactor
```python
print("Hello Welcome to Ayoub's Cinema")
age = int(input('What is your age?:'))
def movie_rating(age):
    if age > 117:
        print("Your age must be under 117")
    elif age >= 18:
        print("You are eligible for the 18 plus movie!")
    elif age >= 16:
        print("You are eligible for the 16 plus movie!")
    elif age >= 15:
        print("You are eligible for the 15 plus movie!")
    elif age >= 12:
        print("You are eligible for the 12 plus movie!")
    else:
        print("Sorry, You are too young ! ")
    return f"Your age is {age}"
print(movie_rating(age))
```

# Loops Refactor
```python
def print_key_and_values(dictionary):

    for key in dictionary:         # loops through all the items in dictionary and stores it in name
        print(key)                 # print first key
        print(dictionary[key])    # print corresponding value


student_data = {
    "name" : "Ayoub",
    "surname" : "Igozouln",
    "age" : "22"
}
print_key_and_values(student_data)
```
# While Loop Refactor
```python
def cal_Age(birth_year , current_year ):
    age = current_year - birth_year
    return age
current_year = int(input(" what is the current year?"))
birth_year = int(input(" what year was you born in?"))
print(cal_Age(birth_year , current_year))
```