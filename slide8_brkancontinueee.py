# break-stop the loop

# while true aisa loop hai jo hamesha chalta rahta hai

# i = 0
# while (True):
#     print(i+1, end = ' ')
#     if (i == 40):
#         break
#     i+=1  #conditional statement

# continue -
# i = 0
# while (True):    WHILE TRUE OR WHILE 1 EK HE KAM KRTE HAI
#     if i+1<5:
#         i+=1
#         continue
#     print(i+1, end = ' ') #it will print no above 5 

#     if (i == 44):
#         break       # it will stop the loop 
#     i+=1  #conditional statement

# quiz -
while(True):
    inp = int(input("Enter a number:\n"))
    if inp > 100:
        print("congrats you have entered number greater than 100")
        break
    else:
        print("try again")
        continue
