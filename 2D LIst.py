letter_grid = [
    ["A", "B", "C"],
    ["D", "F", "G"],
    ["H", "I", "J"],
]

print(letter_grid[0][1])           #透過數字排列來選擇想要的

for row in letter_grid:
    print(row) #直接顯示出全部

for row in letter_grid:
    for col in row:
        print(col) #把框框所有的印成直向
