print("Welcome to the faulty calculator -ANKS ")

num1 = int(input("Please enter number one:\n"))
num2 = int(input("Please enter number two:\n"))
print("So what you want : +,-, *, /, ** ,%")

num3 =input()

if num1 == 56 and num2 == 9 and num3 == "+" :
        print("77")

elif num1 == 56 and num2 == 9 and num3 == "-" :
        print("77")

elif num1 == 45 and num2 == 3 and num3 == "*" :
        print("555")
elif num1 == 56 and num2 == 6 and num3 == "/" :
        print("4")

elif num3 == "+":
    percent =num2 + num1
    print(Plus)

elif num3 == "-":
    Minus =num2 - num1
    print(Minus)

elif num3 == "*":
    Multiplication =num2 * num1
    print(Multiplication)

elif num3 == "%":
    percent =num2 % num1
    print(percent)

else:
    print("Unexpected error! Please check your input")
