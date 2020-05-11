def sort(list):
    for i in range(len(list) - 1, 0, -1):
        for j in range(i):
            if list[j] > list[j + 1]:
                temp = list[j]
                list[j] = list[j + 1]
                list[j + 1] = temp
    print(list)
list = [999,101, 9920, 303, 40, 50,.05, 556, 56, 59, 6000, 70, 802, 99,-10,-414]
sort(list)
