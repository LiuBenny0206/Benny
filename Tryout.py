'''
print("{} is a good guy! {} is a bad guy".format("Benny", "Hank"))

print("姓名 座號 國文 數學 英文")
print("{:2}  {:2}  {:3}  {:3}  {:3}".format("劉秉彥", 12, 100, 100, 100))
'''
'''
number1 = input("A number")
number2 = input("Another number")
print(float(number1)**float(number2))

height = input("Enter a height: ")
long = input("Enter a long: ")
area = int(height)*int(long)

print("長方形面積為:" + str(area))
'''
'''
name1 = input(" Name: ")
grade1 = int(input(" First Grade :"))
name2 = input(" Second name: ")
grade2 = int(input("Second Grade: "))
Tgrade = grade1 + grade2
print("Name", "Grade")
print("{:2}, {:2}".format(name1, grade1))
print("{:2}, {:2}".format(name2, grade2))

print("Total Grade:" + str(Tgrade))
'''
'''
k = int(input("Enter your kilometer: "))
fee = 70 + (k - 1) * 30
money = print("Total payment: " + str(fee))
'''
'''
long = int(input("輸入長: "))
wide = int(input("輸入寬: "))
area = long * wide
length = (long + wide) * 2

print("長為:" + str(long), "寬為: " + str(wide), "面積:" + str(area), "邊長" + str(length))
'''
'''
mh = int(input("Your height?: "))
ih = mh / 2.54
i1 = ih // 12
i2 = ih % 12
print("身高 %d 公分等於 %d 呎%.f 吋" %(mh, i1, i2))
'''
'''
CM = float(input("你的身高: "))
KG = float(input("你的體重: "))
bmi = KG / (CM/100)**2 #公分換公尺要除100
print("身高 %d 公分，體重 %d 公斤，BMI為 %.2f" % (CM, KG, bmi))
'''
'''
Grade = input("Give me your Grade: ")

if int(Grade) >= 60:
    print("Ok Ok")
else:
    print("Nahhhh fuck off")
'''
'''
Age = input("Tell me your age: ")

if int(Age) >= 18:
    print("限制級")
elif int(Age) >= 12:
    print("除了限制級")
elif int(Age) >= 6:
    print("保護級")
else:
    print("普遍級")
'''
'''
a = int(input("Enter a number for A: "))
b = int(input("Enter a number for B: "))
c = int(input("Enter a number for C: "))
'''
'''
if a > b and a > c:
    print("最大為a")
elif b > a and b > c:
    print("最大為b")
else:
    print("最大為c")
'''
'''
if ( a > b ):
    if ( a > c ):
        print("A")
    else:
        print("C")
else:
    if ( b > c ):
        print("B")
    else:
        print("C")
'''
'''
answer = input("Will it rain today?: ")

if answer == "Yes":
    print("帶傘")
else:
    print("不用帶")
'''
'''
num = int(input("Enter a number: "))

if ((num % 2)==1):
    print("奇數")
else:
    print("偶數")
'''
'''

season = int(input("Enter a month: "))

if (season >= 1 and season <= 3):
    print("春天")
elif (season >= 4 and season <=6):
    print("夏天")
elif (season >= 7 and season <= 9):
    print("秋天")
elif (season >= 10 and season <= 12):
    print("冬天")
else:
    print("沒有這月份")
'''
'''
tax = int(input("Enter your tax: "))

if (tax >= 2000000):
    print( tax * 0.3 )
elif (tax >= 1000000):
    print( tax * 0.21 )
elif (tax >= 600000):
    print( tax * 0.13 )
else:
    print( tax * 0.6 )
'''
'''
syear = int(input("Enter a year:"))

if (syear % 100 == 0) or (syear % 4 == 0):
    print("{}是閏年".format(syear))
else:
    print("{}不是閏年".format(syear))
'''
'''

sum = 0
n = int(input("A number: "))
for i in range(1, n+1):
    sum += i
print("1到 %d 的整數和為 %d" % (n, sum))

i = 1
n = int(input("A number: "))
while (i <= n):
    print(i, end=" ")
    i += 2
'''
'''
for x in range(1, 10):
    for y in range(1, 10):
        answer = x * y
        print("%d*%d=%2d" % (y, x, answer))
print()
'''
'''
for k in range(1,7):
    print("out",k,"ran","inside",k,"ran:",end="")
    for l in range(1, k+1):
        print("O", end="")
    print()
'''
'''
nu = int(input("Enter a number: "))

for s in range(1, nu+1):
    for j in range(1, s+1):
        print(j, end="")
    print()
'''
'''
x = int(input("pretty number: "))

for s in range(1, x+1):
    if s ==4 :
        continue
    print(s, end="   ")
'''
'''
total = n = 0
while n <= 10:
    total += n
    n += 1

print(total)
'''
'''

t = s = 1
m = int(input("Number: "))
while s <= m:
    t *= s
    s += 1
print(t)
'''
'''
x = int(input("Number: "))
y = 2
while (y<=x):
    print(y, end=" ")
    y += 2
'''

'''
answer = 0
for s in range(1, 100, 2):
    answer += s
print(answer, end=" ")
'''
'''
for a in range(2, 10):
    for b in range(2, 10):
        t = a * b
        print("%dx%d=%2d" % (a, b,t), end=" ")
print()
'''
'''
n = int(input("Number: "))
for s in range(1, n+1):
    for w in range(s, n+1):
        print("*", end="")
    print()
'''
'''
a = 0
b = 0
for i in range(1, 101):
    if (i%3==0 or i%7==0):
        a += i
        print(a, end="")
'''
'''
y = 1
x = int(input("Enter a number: "))
print(x, "的因數有", end=" ")
while (y <= x):
    if (x%y==0):
        print(y, end=" ")
    y += 1
print()
if (y%1==0 and x%2==0):
    print("%d是質數" % (x))
else:
    print("%d不是質數" % (x))
'''
'''
list = ["姓名: LIN", "姓名: WUN", "姓名: SHAO"]
num = ["編號: 1號", "編號: 2號", "編號: 3號"]
print(num [0] + list[0],)
print(num [1] + list[1])
print(num [2] + list[2])
'''
'''
list = ["LIN", "WUN", "SHAO"]
i = 1
for s in list:
    print( "NUMBER: %d NAME: %s " % (i, s))
    i += 1
'''
'''
scores = [85 , 79, 93]
subjects = ["Chinese", "Math", "English"]
s = 1
for i in range(len(scores)):
    print(subjects[i], "成績:", scores[i],"分") #也可以 print(" %s成績%d分: " % (subjects[i], socres[i]))
    s += 1
'''
'''
names = ["LIN", "WUN", "SHAO"]
i = 2
s = 2
for s in range(len(names)):
    print(names[i])
    i -= 1
'''
'''
list1 = ["Apple", "Banana", "Code"]

n = list1.index("Banana")
print(n)
'''
'''
scores = []
total = inscores = 0
while inscores != -1:
    inscores = int(input(("Enter your grade: ")))
    if (inscores != -1):
        scores.append(inscores)
print("共有 %d 位學生" % (len(scores)))
for score in scores:
    total += score
average = (total / (len(scores)))
print("本班總成績: %d 分, 平均成績: %f.2" % (total, average))
'''
'''
day = 1
sa = 0
sa1 = 0
money = []
while (day != 8):
    sa = int(input("請輸入第%d天: " % (day)))
    money.append(sa)
    day += 1
for mm in money:
    sa1 += mm
print("Total saving: %d" % (sa1))
'''
'''
players = ["10", "9", "11", "8", "5", "6", "22", "18", "14", "3", "1"]

while True:
    print("上場名單: %s " % (players) )
    player = str(input("Enter a player number u want to delete:  "))
    if (player ==""):
        break
    n = players.count(player)
    if (n > 0):
        players.remove(player)
    else:
        print("Not on the list")
'''
'''
colors = ["紅", "橙", "黃", "綠", "藍"]

while True:
    print("有的顏色: %s " % (colors))
    color = input("刪掉不喜歡的顏色: ")
    if (color == ""):
        break
    n = colors.count(color)
    if (n>=1):
        colors.remove(color)
    else:
        print("沒有這顏色==")
'''
'''
scores = []
while True:
    inscore = (input("Enter your score: "))
    if (inscore==""):
        break
    scores.append(int(inscore))

scores2 = sorted(scores, reverse=True)
print(scores2)
'''
'''
scores = []

while True:
    s = input("Enter your grade: ")
    if (s==""):
        break
    scores.append(int(s))

scores2 = sorted(scores, reverse=False)
print("成績由小排到大: ", (scores2))
'''
'''
tuple = ("A", "B", "C")
list1 = list(tuple)
list1[1] = "Benny"
print(list1[1])
print(tuple[1])
'''
'''
numbers = [21, 4, 35, 1, 8, 7, 3, 6, 9]
odd = []

for s in numbers:
    if ( s % 2 == 1 ):
        odd.append(s)

print(odd)
'''
'''
fruits = ["香蕉", "蘋果", "橘子", "鳳梨", "西瓜"]

while True:
    x = input("請輸入喜歡的水果(Enter 結束): ")
    if x == "":
        break
    n = fruits.count(x)
    if ( n > 0):
        p = fruits.index(x)
        print("%s 在串列中的第%d項" % (x, p+1))
    else:
        print("%s 不在串列中" % (x))
'''
'''
t = 0
scores = []

for i in range(1,6):
    inscore = input("請輸入成績第 %d 位同學的成績: " % (i))
    scores.append(inscore)

for score in scores:
    t += int(score)
a = (t /len(scores))
print("本班成績: %d 分 , 平均成績: %5.3f 分" %(t, a))
'''
'''
numbers = [1, 2, 3, 4, 2, 7, 3, 2, 2]
numbers2 = []

for number in numbers:
    n = numbers2.count(number)
    if (n == 0):
        numbers2.append(number)
print(numbers2)

x = numbers.count(number)

print(x)
'''
'''
names = []
grades = []

for i in range(1,4):
    name = input("請輸入第" + str(i) + "同學的姓名: ")
    grade = input("請輸入第" + str(i) + "同學的成績: ")
    names.append(name)
    grades.append(grade)
grade2 = sorted(grades, reverse=True)
n = grades.index(grade2[0])
print("姓名: %s  成績:  %s" %(names[n], grades[n]))
'''
'''
animal= ["鼠", "牛", "虎", "兔", "龍", "蛇", "馬", "羊", "猴", "雞", "狗", "豬"]

year = int(input("請輸入你的出生西元年: "))

print("西元{}年出生屬{}".format(year, animal[(year-2020) % 12]))
'''
'''
dict = {"香蕉": 20, "蘋果": 50}
print(dict["香蕉"])
'''
fruits = dict([["Banana", 20], ["Apple", 50]])

print(fruits["Banana"])




























































































