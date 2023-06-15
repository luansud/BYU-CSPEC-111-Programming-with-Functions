with open("provinces.txt") as provinces:
    list_provinces = []
    next(provinces)
    for line in provinces:
        line = line.strip()
        if line == "AB":
            line = "Alberta"
        list_provinces.append(line)
    list_provinces.pop()
    count = list_provinces.count("Alberta")
    print(list_provinces)
    print(f"Alberta occurs {count} times in the modified list.")
        