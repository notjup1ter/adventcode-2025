#idea, make a movement array indicating directions in which forklifts can move
moves = [(1,0), (-1, 0), (0, 1), (0,-1), (-1, 1), (-1, -1), (1, 1), (1 , -1)]
res = 0
with open("paperrolls.txt", "r+") as file:
    arr = list(file.read().splitlines())
    print(arr)

con = True
while con:
    temp_res = 0 #reset only when con (non-zero pass) is met
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            char = arr[i][j]
            adj_count = 0
            if char == '.':
                continue
            
            for dx, dy in moves:
                nx, ny = j + dx, i + dy
                if nx >= 0 and nx <= len(arr[0]) - 1 and ny >= 0 and ny <= len(arr) - 1:
                    if arr[ny][nx] == "@" or arr[ny][nx] == "x":
                        adj_count += 1
            if adj_count < 4:
                row = list(arr[i])
                row[j] = "x"
                arr[i] = "".join(row)
                temp_res += 1
    print(temp_res)
    if temp_res == 0: #when no new paper rolls can be collected
        con = False
    res += temp_res
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == "x":
                row = list(arr[i])
                row[j] = "."
                arr[i] = "".join(row)

                

print(res)

                

            
