start = 50
pw = 0


with open("rotations.txt", "r") as file:
    for line in file:
        if line == "\n":
            continue
        dir = line[0]
        deg = line[1:]
        new_start = start
        

        if dir == "L":
            new_start -= int(line[1:])
        elif dir == "R":
            new_start += int(line[1:])


        if(start > 0 and new_start <= 0):
            pw += 1

        pw += abs(new_start) // 100
        start = new_start % 100
        
        
print(pw)

