friends = ["Loky", "Stu", "Abn"]

for number in friends:
    print(number)


for index in range(len(friends)):
    print(friends[index])


for index in range(3, 5): #range (3, 5) 會跑3 4 不會跑5
    print(index)

for index in range(4):
    if index == 0:
        print("test")
    elif index == 1:
        print("test1")
    elif index == 2:
        print("test2")
    else:
        print("test3")


