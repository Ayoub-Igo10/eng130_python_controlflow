# # Sudo Coding
#
# weather = "time"
# # if it's cold:
#
# if weather == "sunny":# True or False
#     print("lets go to the beach")
#     #take jacket
#
# elif weather == "sunny":
#     print("lets go to the beach")
#
# # if its raining:
# else:
#      print("no match found better luck next time")
#      # rain mack
#
#
#
# #if its sunny: booleon value true - next line
#     #lets go to the beach
# # else or elif
#
# # age restriction for movie ticket
# # create a condition for 18 & above
# # 16 & above
# # PG
# # 12a
# # 15 & above
# # if nothing matched inform the user to enter their age again = ELSE
# # user ust not be allowed to enter age over 117 years
#
# weather = "time"
# # if it's cold:

# age restriction for movie ticket
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
