def sort(list):
    for i in range(len(list)-1):
        minpos=i
        for j in range(i,len(list)):
            if list[j]<list[minpos]:
                minpos=j
        temp=list[i]
        list[i]=list[minpos]
        list[minpos]=temp
    print(list)
list = [999,101, 9920, 303, 40, 50,.05, 556, 6000, 70, 802, 99,-10]
sort(list)