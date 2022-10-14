# #
#
# data = 0
#
# while data < 10:
#     print(f"its working - >{data}")
#     if data == 5:
#         break
# #     data += 1
# age = 18
# user_prompt = True

# while user_prompt:
#     age = input("please enter your age")
#     if age.isdigit():
#         user_prompt = False
#     else:
#         print("Please enter your age in digits only")
# print(f"your age is {age}")
# calculate their age - year of birth etc.


#  while user_prompt:
# age = input("please enter your age")
#      if age.isdigit():
#          user_prompt = False
#      else:
#          print("Please enter your age in digits only")
#  print(f"your age is {age}")
#  # calculate their age - year of birth etc.




def cal_Age(birth_year , current_year ):
    age = current_year - birth_year
    return age
current_year = int(input(" what is the current year?"))
birth_year = int(input(" what year was you born in?"))
print(cal_Age(birth_year , current_year))