#idea, make a movement array indicating directions in which forklifts can move
moves = [(1,0), (-1, 0), (0, 1), (0,-1), (-1, 1), (-1, -1), (1, 1), (1 , -1)]
res = 0
with open("paperrolls.txt", "r") as file:
    arr = file.read().splitlines()

    for i in range(len(arr)):
        for j in range(len(arr[0])):
            char = arr[i][j]
            print(char)
            adj_count = 0
            if char == '.':
                continue
        
            for dx, dy in moves:
                nx, ny = j + dx, i + dy
                if nx >= 0 and nx <= len(arr[0]) - 1 and ny >= 0 and ny <= len(arr) - 1:
                    if arr[ny][nx] == "@":
                        adj_count += 1
            if adj_count < 4:
                res += 1

print(res)

                

            
