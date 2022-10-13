'''
Freezing_point = int(input("Enter a Freezing Point of Water(Celsius): "))
Boiling_point = int(input("Enter a boiling Point of Water(Celsius): "))
Mid_Point = int(Freezing_point + Boiling_point //2)
Celsius_to_Fahrenheit = int((Freezing_point + Boiling_point)//2 * (9/5)+32)
print("Water freezes at " + str(Freezing_point) + " degree Celsius ")
print("Water boils at " + str(Boiling_point) + " degree Celsius ")
print("The mid point is " + str(Mid_Point) + " degree Celsius or " + str(Celsius_to_Fahrenheit) + " degrees Fahrenheit")
'''
'''
import math
print("This program will ask you to enter 3 numbers"
"(a, b and c) that will be used in the quadratic formula to"
"calculate the roots of an equation.")
a = float(input("Enter a value for a: "))
b = float(input("Enter a value for b: "))
c = float(input("Enter a value for c: "))
d = True
e = True
while (d == True) and (e == True):
    if ( a == 0 ):
        print("0 is not a good number")
        a = float(input("Enter another value for a: "))
    elif b**b < 4*a*c:
        print("Is a imaginary number")
        b = float(input("Enter another value for b: "))
        c = float(input("Enter another value for c: "))
    else:
        d = False
        e = False
Root1 = ((-b)+math.sqrt(b*b-4*a*c)/2*a)
Root2 = ((-b)-math.sqrt(b*b-4*a*c)/2*a)
print("***************************************************")
print("*       Root1 is          %7.1f                 *"%(Root1))
print("*       Root2 is          %7.1f                 *"%(Root2))
print("***************************************************")
'''
'''
### Lucky7 part1
import random as r
pot = float(input("How much you want to put into the pot(Max 20$): "))
if pot > 0:
    dice1 = r.randint(1, 6)
    dice2 = r.randint(1, 6)
    total = dice1 + dice2
    print("The number is %d" % (total))
    if total == 7:
        print("You won! you earned 4$")
        pot += 4
        print("You have %d$ left!" % (pot))
    else:
        print("You lost! you lost 1$")
        pot -= 1
        if pot == 0:
            print("You have no money left!")
            exec
        else:
            print("You have %d$ left!" % (pot))
else:
    print("You have no money left!")

'''
'''
###Lucky part2
import random as r
pot = 0
pot = float(input("How much you want to put into the pot(Max 20$): "))
while pot > 0:
    dice1 = r.randint(1, 6)
    dice2 = r.randint(1, 6)
    total = dice1 + dice2
    print("Dice point is %d" % (total))
    if total == 7:
        print("You won! you earned 4$")
        pot += 4
        print("You have %d$ left!" % (pot))
        again = input("Do you want to play again(Yes/No)? ")
        if str(again) == "Yes":
            continue
        elif str(again) == "No":
            print("You have %d$ left!" % (pot))
            print("Thank you for playing")
    else:
        print("You lost! you lost 1$")
        pot -= 1
        if pot == 0:
            print("You have no money left!")
            PutMoneyQuestion = (input("Do you want to put more money(Yes/No)? "))
            if str(PutMoneyQuestion) == "Yes":
                PutMoney = int(input("How much you want to put(Max20$)? "))
                pot += PutMoney
                continue
            else:
                print("Thank you for playing")
                break
        else:
            print("You have %d$ left!" % (pot))
            again = input("Do you want to play again(Yes/No)? ")
            if str(again) == "Yes":
                continue
            elif str(again) == "No":
                print("You have %d$ left!" % (pot))
                print("Thank you for playing")
                break
else:
    print("You have no money left!")
    print("Thank you for playing")
'''
'''
fileNameIn = input("Enter a input file name: ")
infile = open(fileNameIn, 'r')
for line in infile:
    for line in infile:
        wordlist = line.split()
        fName = str(wordlist[0])
        lName = str(wordlist[1])
        name = fName+lName
        units = float(wordlist[2])
        unitPrice = float(wordlist[3])
        totalSales = units * unitPrice
        if totalSales <= 10000:
            commission = totalSales * (0.1)
        else:
            commission = totalSales * 0.3/2
'''
'''
####################################
# Name: Pin-Yen,Liu                #
# Assignment 6                     #
####################################
def getDate():
            ###############################################################
            # Precondition: To type in the file name that you want to open#
            # Postcondition: To open a file and list successfully         #
            ###############################################################
        fileNameIn = input("Enter a input file name: ")
        infile = open(fileNameIn, 'r')
        infile = infile.read()
        return infile
def calculateTotalSale(units, unitPrice):
        #######################################################################################
        # Precondition: This function requires two integer as parameter"units" and "unitPrice"#
        # Postcondition: Ensure TotalSale is calculated correctly                             #
        #######################################################################################
    totalSale = units * unitPrice
    return totalSale
def calculateCommission(totalSale):
        ###########################################################################
        # Precondition: This function requires an integer as parameter"totalSale" #
        # Postcondition: To judge the totalSale and calculate the right commission#
        #           if totalSale > 10000$ get 20% commission                      #
        #           if totalSale < 10000$ get 10% commission                      #
        ###########################################################################
    if totalSale>10000:
        commission = 1000+(totalSale-10000)*(0.2)
    else:
        commission = totalSale*(0.1)
    return commission
def printResults(name, units, unitPrice, totalSale, commission):
    ########################################################################################################################
    # Precondition: This function requires a string as "name"and four float as "units" "unitPrice" "totalSale" "commission"#
    # Postcondition: It will print all of calculated data                                                                  #
    ########################################################################################################################
    print(name," ",units," ","$",unitPrice,"$",totalSale, "$",commission)
def main():
    inputList = getDate().split()
    i = 0
    for line in range(len(inputList)//3):
        name = inputList[i]
        units = float(inputList[i+1])
        unitPrice = float(inputList[i+2])
        totalSale = calculateTotalSale(units,unitPrice)
        commission = calculateCommission(totalSale)
        printResults(name, units, unitPrice,totalSale,commission)
        i=i+3
main()
'''
def calculatPower(x, n):
    #####################################################################################
    # Precondition: This function requires one integer and one float as parameter "x""n"#
    # Postcondition: It will calculate x to the power of n                              #
    #####################################################################################
    result = 1
    for i in range(1, n+1):

        result = result * x
    return result

def calculatFactorial(n):
    ###################################################################
    #Precondition: This function requires one integer as parameter "n"#
    #Postcondition: It will return "n" factorial                      #
    ###################################################################
    factorial = 1
    for i in range(1, n+1):
        factorial = factorial * i
    return factorial
def calculatExp (x, n):
    #####################################################################################
    # Precondition: This function requires one float and one integer as parameter "x""n"#
    # Postcondition: It will calculate exp(x)                                           #
    #####################################################################################
    exp = 0
    for i in range(n):
        exp = exp + (calculatPower(x, i)/calculatFactorial(i))
    return  exp






userResponse = 0
while userResponse != 4:
    print("Chose one of the following options: ")
    print("1. Calculate x to the power of n")
    print("2. Calculate factorial of n")
    print("3. Calculate exp(x)")
    print("4. Exit")
    userResponse = int(input("Please enter your choice here: "))
    if userResponse == 1:
        x = float(input("Enter value of x as float: "))
        n = int(input("Enter value of n as integer: "))
        p = calculatPower(x, n)
        print("%1.1f to the power of %d is %1.1f" % (x,n,p))
    if userResponse == 2:
        n = int(input("Enter value of n as integer: "))
        if n <= 0:
            print("There is no factorial")
        else:
            f = calculatFactorial(n)
            print("Factorial of %d is %d" % (n,f))
    if userResponse == 3:
        x = float(input("Enter value of x as float: "))
        n = int(input("Enter number of terms as integer: "))
        e = calculatExp(x, n)
        print(e)
else:
    print("Goodbye!")







