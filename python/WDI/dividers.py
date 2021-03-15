def divider(num):
    tab = [1]
    i_dev = 2
    while i_dev * 2 <= num:
        if num % i_dev == 0:
            tab.append(i_dev)
        i_dev+=1
    tab.append(num)
    return tab


num = 430
print(devider(num))
            