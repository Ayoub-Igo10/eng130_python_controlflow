

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

# student_data = {
#     "name" : "Ayoub",
#     "surname" : "Igozouln",
#     "age" : "22"

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

