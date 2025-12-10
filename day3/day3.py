total = 0
with open("voltages.txt", "r") as file:
    for line in file:
        if line == "\n":
            continue
       

        k = 12
        drop = len(line) - k
        st = ["0"] #forces a drop decrement on first number access

        for num in line:
            if num.isdigit():
                while st and drop and st[-1] < num :
                    st.pop()
                    drop -= 1
                st.append(num)
        total += int(''.join(st[:k]))

                
    print(total)

