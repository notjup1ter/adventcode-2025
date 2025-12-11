total = 0

with open("ids.txt", "r") as file:
    ranges = []
    valid_ids = {0}
    valid_ids.remove(0)

    for line in file:
        line.strip()
        if '-' in line:
            r = line.rstrip('\n').split("-")
            ranges.append(list(map(int, r)))

    sorted_ranges = sorted(ranges, key = lambda x: x[0])
    
    exclusive_ranges = []
    for r in sorted_ranges:
        if not exclusive_ranges: #handling first range
            exclusive_ranges.append(r)
            continue

        last = exclusive_ranges[-1]
        '''
        if current lower bound is going to cause an adjacent merge (r[0] = last[1] + 1 or r[0] = last[1]) 
        or partial merge (r[0] < last[1)
        we merge, replacing the high with the max between the current highest exclusive range or r
        ''''
        if r[0] <= last[1] + 1:
            last[1] = max(r[1], last[1])
        else:
            exclusive_ranges.append(r)

    for r in exclusive_ranges:
        total += r[1] - r[0] + 1
    print(exclusive_ranges)
    print(total)
    print()



