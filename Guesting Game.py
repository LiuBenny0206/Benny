
guess_num = "10"
guess = ""
guess_count = 0
guess_limit = 3
Loser = False

while guess != guess_num and not Loser:
    if  guess_count < guess_limit:
        guess=input("Guess a number: ")
        guess_count += 1
    else:
        Loser = True

if Loser:
    print("You Lose! ")
else:
     print("Are you god? ")


feeling = "lazy"
guess1 = ""
count = 0
limit = 5
LLoseerr = False

while guess1 != feeling and not LLoseerr:
    if count < limit:
     guess1 = input("How are you?: ")
     count += 1
    else:
         LLoseerr = True

if LLoseerr:
    print("Oh U suck!")
else:
    print("same")