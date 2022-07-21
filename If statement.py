

tall= True
big= True


if tall and big :
    print("you are wonderful")
elif tall and not(big):
    print("Useless feature...")
elif not(tall) and big:
    print("Not bad!")
else:
    print("you just normal")



def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max(20, 22.2, 22.1))


