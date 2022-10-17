# # Password Size
def passwordsize_evaluator(password):
    if (len(password) <5):
           return "Sorry, Your password is too short."
    elif(len(password) > 20):
        return "Sorry, Your password is too long"
    else:
        return "Great, Your password is acceptable"

password=input("Enter the password:")

print(passwordsize_evaluator(password))

# Shopping items
def food_bill():
    shoppin_items={"eggs":1.85,"bread":1.50,"peppers":0.90}

    print(shoppin_items.values())

    print("The total bill is :"+str(sum(shoppin_items.values())))
    for item in shoppin_items:
        print(item)
food_bill()

def total_value(shopping):
    sub_total=0
    for value in shopping:
         sub_total +=value
    return sub_total

shopping={"eggs":1.60,"lamb":6.40}
print(total_value(shopping.values()))

def find_smallest_interval(numbers) :
 numbers.sort()
 return numbers[0]

numbers=[12,3,4,89,23,7]

print(find_smallest_interval(numbers))

def findlargestnumbers(list):
    list1=list.sort
    return list[-1]

list = [1,4,6,12,67,91]
print(findlargestnumbers(list))

# list syntax
listings = [1, 2, 3, 4, 5]

# tuple syntax
tuples = (1, 2, 3, 4, 5)

# indexing always starts at 0 for any data structure in python

# print 3rd and 5th item from list
for i in range(5):
    if i == 2:
        print(i)
    elif i == 4:
        print(i)

# print 3rd and 5th item from tuple
for i in range(5):
    if i == 2:
        print(i)
    elif i == 4:
        print(i)

