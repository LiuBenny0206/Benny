'''
def GatArea(width, height):
    area = width * height
    return area
gate1 = GatArea(6,9)
print(gate1)
print (GatArea(width=5, height=7))
'''
import time

'''
def ct(c):
    f = c * 1.8 + 32
    return f
f = float(input("請輸入攝氏溫度: "))
print("華氏溫度為: %8.2f " %(ct(f)))
'''
'''
def k(u):
    k = i * 2.2
    return k
i = float(input("請輸入體重公斤數: "))
print("你的體衝為: %6.1f 磅" % (k(i)))
'''
'''
def Getsquare(width, height):
    return width * height * 2
ret1 = Getsquare(6, 10)
print(ret1)
'''
'''
def scope():
    global var2 #全域會覆蓋掉區域
    var1 = 5
    var2 = 2
    print(var1, var2)

var1 = 10
var2 = 20
scope()
print(var1, var2)
'''
'''
x = abs(-5) #絕對值
print(x)

z = pow(3, 2, 9) #次方 最後一個數值為除9的餘數
print(z)

y = divmod(40, 8) #互除取的商數和餘數
print(y[0], y[1])

a = round(3.6) #四捨五入
print(a)
'''
'''
apple = int(input("請輸入蘋果總數: "))
person = int(input("請輸入總人數: "))
ret = divmod(apple, person)
print("每個學生可得到" + str(ret[0])+ "個" )
print("蘋果剩餘" +  str(ret[1]) + "個")
'''
'''
lifefee = 10000
dailycost = 350
spend = int(input("請輸入第幾天: "))
day = dailycost * spend
lifecost = lifefee - day
ret = divmod(lifecost, dailycost)
print("可維持的生活" + str(ret[0]) + "天")
print("生活費剩餘" + str(lifecost) + "元")
'''
"""
efee = 0
list1 = []
while ( efee != -1):
    efee = int(input("請輸入電費(-1結束): "))
    list1.append(efee)
list1.pop()
print("共輸入" + str(len(list1)) + "個數")
print("最多電費:" + str(max(list1)))
print("最少電費:" + str(min(list1)))
print("電費總和:" + str(sum(list1)))
print("電費由大到小: " + str(sorted(list1, reverse=True)))
"""
'''
month = 1
list1 = []
while month != 5:
    money = int(input("請輸入第 %d 個月的支出金額: " % month))
    month += 1
    list1.append(money)
print("支出最多的金額為: " + str(max(list1)))
print("支出最少的金額為: " + str(min(list1)))
print("支出的總金額為: " + str(sum(list1)))
print("支出金額從小排到大: " + str(sorted(list1)))
'''
'''
web = input("請輸入網址: ")
if web.startswith("http://") or web.startswith("https://"):
    print("網址輸入格式正確")
else:
    print("網址輸入不正確")
'''
'''
pic = input("請輸入圖片名稱: ")
if pic.endswith("jpg"):
    print("檔案格式是JPG")
else:
    print("檔案格式不是JPG")
'''
'''
names = ["Lin", "Chen", "Zheng"]
number = [1, 2, 3]
Chinese = [100, 74, 82]
Math = [87, 88, 65]
English = [79, 100, 8]
print("Name      Number Chinese Math English")
for i in range(0,3):
    print(names[i].ljust(12), str(i+1), str(Chinese[i]).rjust(6), str(Math[i]).rjust(6), str(English[i]).rjust(8))
'''
'''
names = ["鐘", "鄭", "何"]
FirstSeason = [34210, 23600, 145000]
SecondSeason = [9000, 23900, 83400]
ThirdSeason = [186500, 127800, 100000]
ForthSeason = [78900, 125000, 90000]
print("姓名", "第一季".rjust(8), "第二季".rjust(5), "第三季".rjust(5), "第四季".rjust(5))
for i in range(0,3):
    print(names[i], str(FirstSeason[i]).rjust(11), str(SecondSeason[i]).rjust(7), str(ThirdSeason[i]).rjust(7), str(ForthSeason[i]).rjust(7))
'''
'''
date1 = "2022-9-14"
date1 = ("西元" + str(date1).replace("-","年", 1))
date1 = str(date1.replace("-", "月"))
date1 += "日"
print(date1)
'''
'''
time = "16:26:50"
time = str(time).replace(":", "點", 1)
time = str(time).replace(":", "分", 1)
time += "秒"
print(time)
'''
'''
import random

print(random.random())
for num in range(10):
    print(random.randrange(0,10), end=",")
'''
'''
import random

RandomNumber = input("輸入任意鍵丟骰子，案Enter離開: ")
while RandomNumber != "":
    print("你骰的骰子點數為: %d" %(random.randint(1,6)))
    RandomNumber = input("輸入任意鍵丟骰子，案Enter離開: ")
else:
    print("遊戲結束!")
'''
'''
import random as r
sum = 0
print("丟骰子三次的點數為:", end=" ")
for i in range(3):
    num = r.randint(1,6)
    sum += num
    print(num, end=" ")
print("，總點數: %d " %(sum))
'''
'''
import random
for i in range(5):
    print(random.choice("ABCDEFG"), end=" ") #隨機取得一個字元或串列
    print(random.choice("1234567"), end=" ")

print(random.sample("ABCDEFGH", 5), end=" ") #跟Choice差在可以選數量但不能大於字元長度或字串,列印出來也有括號。
'''
'''
import random as r
list1 = r.sample(range(1, 50), 7)
special = list1.pop()
list1.sort()
print("本期中獎號碼為: ", end="")
for i in range(6):
    if i == 5: print(str(list1[i]), end="")
    else: print(str(list1[i]), end=", ")

print("\n本期特別號為:" + str(special))
'''
'''
import random as r
listNumber = r.sample(range(0,9),4)
listNumber.sort()
print("本期四星彩中獎號碼: ", end="")
for i in range(4):
    if i == 3:
        print(listNumber[i], end=" ")
    else:
        print(listNumber[i], end=" , ")
'''
'''
import time as t
print(time.localtime())
time1 = (time.localtime(time.time()))
print(t.ctime())

time2 = t.localtime()
print("今天是今年的第"+str(time2.tm_yday)+"天,", end="")
if time2.tm_yday >=182:
    print("屬於下半年.", end="")
else:
    print("屬於上半年.", end="")
'''
import time as t
'''
week = ["1", "2", "3", "4", "5", "6", "7"]
dst = ["無日光節約間", "有日光節約時間"]
time1 = t.localtime()
show = "現在時刻:中華民國" + str(int(time1.tm_year-1911)) + "年"
show += str(time1.tm_mon) + "月" + str(time1.tm_mday) + "日"
show += str(time1.tm_hour) + "點" + str(time1.tm_min)+ "分"
show += str(time1.tm_sec) + "秒 星期" + week[time1.tm_wday] + "\n"
show += "今天是今年的第" + str(time1.tm_yday) + "天,此地" + dst[time1.tm_isdst]
print(show)
'''
'''
print("三秒後下一行")
t.sleep(3)
print("三秒到了")
'''
'''
print(str(t.perf_counter()))
t.sleep(2)
print(str(t.perf_counter()))
'''
'''
timestart = t.perf_counter()
for j in range(0, 1000):
    for i in range(0, 1000):
        n= j * i
    time = t.perf_counter()
print("執行一百萬次要" + str(time-timestart) + "秒" )
'''
'''
ftime = t.perf_counter()
for i in range(1, 1000):
    for x in range(1, 1000):
        z = float(x) * float(i)
    stime=  t.perf_counter()
print(stime-ftime)
'''
'''
grade = 0
gradeList = []
for i in range(1,5):
    grade = int(input(("Enter " +str(i)+ " classmate's grade: ")))
    gradeList.append(grade)
print("Highest grade: " + str(max(gradeList)))
print("Lowest grade: " + str(min(gradeList)))
print("Total grade: %d " % (sum(gradeList)))
print("Average: %d" % (sum(gradeList)/4))
'''
'''
def transformHeight(height):
    height = x * 30.48

    return height


x = float(input("輸入你的身高(呎): "))
Cmheight = transformHeight(x)
print("你的身高為:%3.1f 公分" %(Cmheight))
'''
'''
timeHours = t.localtime()
timeMinutes = t.localtime()
timeSecond = t.localtime()

print("現在時刻:上午 %d 點 %d 分 %d 秒"%(timeHours.tm_hour,timeMinutes.tm_min,timeSecond.tm_sec))
'''

def autoChange(m, coin):
    c = m // coin
    return c
money = [50,10,5,1]
m = int(input("請輸入換幣金額: "))
while m > 0 :
    for i in range(len(money)):
        coin = money[i]
        if (m >= coin):
            c = autoChange(m, coin)
            print("{}元 * {}個" .format(coin,c))
            m = m % coin




































































