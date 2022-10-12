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