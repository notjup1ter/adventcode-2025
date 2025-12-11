res = 0

with open("ids.txt", "r") as file:

    ranges = []
    ids = []

    for line in file:
        line.strip()
        if '-' in line:
            r = line.rstrip('\n').split("-")
            ranges.append(list(map(int, r)))
        
        elif line != '\n':
            ids.append(int(line.rstrip('\n')))
        

    for id in ids:
        fresh = False
        for r in ranges:
            if int(id) >= int(r[0]) and int(id) <= r[1]:
                fresh = True
                #print(f"{id} is between {r[0]} and {r[1]}")
        if fresh:
            res += 1

        fresh = False

print(res)


