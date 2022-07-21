
num1 = (float(input("Enter a number: "))) #float是可以有小數點
op = (input("Enter a operator: "))
num2 = (float(input("Enter second number")))

if op == "+":
    print(num1+num2)
elif op == "-":
    print(num1-num2)
elif op == "*":
    print(num1*num2)
elif op == "/":
    print(num1/num2)
else:
    print("invaild operator")





answer1 = (input("Are you tall or short: "))
answer2 = (input("Are you big or small: "))

if answer1 == "tall" and answer2 == "big":
    print("You are wonderful ")
elif answer1 == "tall" and answer2 == "small":
    print("Useless features...")
elif answer1 == "short" and answer2 == "big":
    print("Not bad bro!")
else:
    print("You just normal")