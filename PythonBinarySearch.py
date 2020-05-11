pos=-1
def search(list, n):
    lb = 0
    ub = len(list) - 1

    while lb <= ub:
        mid = (lb + ub) // 2
        if n == list[mid]:
            globals()['pos'] = mid
            #globals()['pos'] = mid
            return True
        else:
            if(n>list[mid]):
                lb=mid
            else:
                ub=mid
    return False;

list = [10,20,30,40,50,55,56,59,60,70,80,99]
n = 59

if search(list, n):
    print("found at: " + str(pos))
else:
    print("Not found")
