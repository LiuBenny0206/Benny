
test1 = open("test1.text", "a")

print(test1.write("\nI'm doing it! "))
# 檔案.write 是可以加資料進去（a） 整個重新修改是(w)
# \n是讓輸入的東西到下一行

test1.close()