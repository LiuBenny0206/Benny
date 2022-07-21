

try:
    number = int(input("Enter a number: "))
    print(number)
except ValueError as erro:
    print(erro) # except 是來修正發生error 並讓它變成一個value
except ZeroDivisionError:
    print("Dumb ass fuck go back to element school! ") #可以用各種except + specific error 來細分變成value

