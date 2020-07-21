# print("Enter your number here:\n")
# var1 = 10
# var2 = 20
# var3 = int(input())

# if var3 > var2:
#     print("Greater")

# elif var2 == var3:
#     print("Equal")

# else:
#     print("Lesser")

# all if elif and else are termed as if else ladder

# list1 = [1,2,3,4,5]
# print(2 in list1)
# print(77 not in list1)

# if 2 in list1:
#     print("Yes....its in list1")


# quiz - voting system
# age = int(input("What is your age:\n"))

# if (age > 100):
#     print("Age entered is ilogical")

# elif (age == 18):
#     print("You are applicable for voting")

# elif (age > 18):
#     print("You can vote")

# else:
#       print("You are kid now")



# Quiz - driving test 
# age = int(input("Enter your age:\n")) 

# if (age > 100):
#     print("Plz enter logical age") 
# elif(age > 18) :
#     print("you can drive now") 
# elif (age==18):
#     print("we will decide plz visit office") 
# else:
#     print("you cant drive car now baccha")


# Quiz- Grading system in class
Number = int(input("Enter your marks:\n"))

if (Number > 90 and Number < 100):
    grade = "A"
elif (Number > 80 and Number < 100):
    grade = "B"
elif (Number >100):
    grade = " not valid"

else:
    grade = "C"
print("The grade is", grade)