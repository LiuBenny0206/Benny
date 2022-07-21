
# 檔案名稱，各種mod"r"，"w", "a", "r+"
# r= read only w= modify existing information a= add information r+= read and write
player_file = open("test", "r")
print(player_file.readable()) #來檢查檔案是否可讀取
# print(player_file.read())

# print(player_file.readline()) #這個會顯示檔案第一行以此類推
print(player_file.readlines()[1]) #可以顯示全部+[] 可以選要第幾行


player_file.close() #把檔案關閉 close when you done