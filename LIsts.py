lucky_number = [3, 1, 5, 9, 7, 10]
friends = ["Shane", "Hank", "Alex", "Jerry", "Betty", "Jack"]
print("Benny's friends list " + friends[0])

friends.extend(lucky_number)
print(friends)

friends.append("Bell")
print(friends)

friends.insert(3, "Fay")
print(friends)

friends.pop()
print(friends)

friends.remove("Fay")
print(friends)


print(friends.index("Shane"))

print(friends.count("Shane"))

lucky_number.sort()
print(lucky_number)

lucky_number.reverse()
print(lucky_number)

friends2= friends.copy()
print(friends2)
