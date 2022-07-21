'''
dict1 = {"王": 50, "黃": 60, "劉": 70}
dict2 = ([["A", 50], ["B", 60], ["C", 70]])
dict3 = dict(z=50, x=60, y=70)

print(dict3['x'])
print(dict1.get("劉"))
'''
'''
dict1 = {"A": "內向穩重", "B":"外相樂觀", "O":"堅強自信", "AB":"聰明自然"}
name = input("輸入要查詢的血型: ")
Blood = dict1.get(name) #沒有鍵存在時會產生None而不是Error
if (Blood==None):
    print("沒有" + str(name) + "血型!")
else:
    print(str(name)+ "血型的個性為:" + str(Blood))
'''
'''
weather = {"夏天": "乾熱", "秋天": "涼爽", "冬天": "寒冷", "春天": "涼爽"}
a = input("輸入季節名稱: ")
answer = weather.get(a)

if (answer==None):
    print("沒有「"+str(a)+"」季節!")
else:
    print(str(a)+"的天氣為"+str(answer))
'''
'''
fruits = {"Apple": 50}
fruits["Apple"] = 60 # 新的元素會取代舊的元素
print(fruits["Apple"])
fruits["Orange"] = 100 # 輸入不存在的就是新增元素
print(fruits)

del fruits["Orange"] # 刪掉Orange這個元素
print(fruits)
fruits.clear() #刪掉字典裡所有元素
print(fruits)
'''
'''
grades = ([["Ae", 20], ["B", 30]])
dict1 = {"王": 50, "黃": 60, "劉": 70}
dict2 = {"A": 50, "B": 60, "C": 70}

print(len(grades)) # 取得字典裡個元素個數

grade1= grades.copy() # 複製字典
print(grade1)

v = "A" in dict2
print(v)
'''
'''
dict1 = {"劉秉彥": 60, "楊中岳": 70, "王馨": 80}
name = input("輸入學生名字: ")

if name in dict1:
    print(name + "的成績為" + str(dict1[name])) # dict1[name]前面+str 是因為印出不能有字跟值同時
else:
    scores = input("輸入學生成績: ")
    dict1[name] = scores
    print("字典內容" + str(dict1))
'''
'''
dict1 = {"電視": 15000, "冰箱": 23000, "冷氣": 28000}
name = input("輸入電器名稱: ")

if name in dict1:
    print(name + "的價格為" + str(dict1[name]))
else:
    money = input("輸入電器價格: ")
    dict1[name] = money
    print("字典內容: " + str(dict1))
'''
'''
dict1 = {"金牌": 55, "銀牌": 44, "銅牌": 87}
listkey = list(dict1.keys())
lisvalue = list(dict1.values())
for i in range (len(listkey)):
    print("得到的 %s 數目為 %d 面" % (listkey[i], lisvalue[i] ))
'''
'''
dict1 = {"水瓶座": "怪", "金牛座": "摳", "射手座": "沒"}
listkey = list(dict1.keys())
listvaule = list(dict1.values())
for x in range(len(listkey)):
    print(" %s 的性格為 %s" % (listkey[x], listvaule[x]))
'''
'''
dict1 = {"JAN": 1, "FEB": 2, "MAR": 3, "APR": 4, "MAY": 5, "JUN": 6, "JUL": 7, "AUG": 8, "SEP": 9, "OCT": 10, "NOV": 11, "DEC": 12}
month = input("請輸入要查詢的月份數字: ")

if month in dict1:
    print(str(dict1[month])+"月份的英文簡寫為:" + str(month))
else:
    print("None")
'''
'''
dict1 = { 0: "零", 1 : "壹", 2 : "貳", 3 : "叁", 4 : "肆", 5 : "伍", 6 : "陸", 7: "柒", 8 : "捌", 9 : "玖"}
number = (input("請輸入小於五位的數字: "))
for n in number:
    print(dict1[int(n)], end= "")
'''
'''
city = {"台北市": 6, "新北市": 2, "桃園市": 5, "台中市": 8, "台南市": 3, "高雄市": 9}
search = input("輸入要查詢六都的名稱: ")
getsearch = city.get(search)

if search in city:
    print("%s 今天的 PM2.5 值為: %s" % (search, city[search]))
else:
    print("六都會中沒有「 %s 」" % (search))
'''
'''
animals = {"鼠": "親切", "牛": "保守", "虎": "熱情", "兔": "溫柔"}
ianimal = animals.items()

for ani, charc in ianimal:
    print("生肖屬" + str(ani) + "的個性為: " + str(charc))
'''

exchange = {"美金": 28.02, "日幣": 0.2513, "人民幣": 4.24}
Twd = float(input("請輸入台幣: "))
TUSA = float(Twd/exchange["美金"])
TJPAN = float(Twd/exchange["日幣"])
TCHA = float(Twd/exchange["人民幣"])
print("台幣 %8.3f元 等於美金 %8.3f 元 等於日幣 %8.3f 元 等於人民幣 %8.3f 元"%(Twd, TUSA, TJPAN, TCHA))















































































