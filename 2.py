arr = [2,1,3,1,2]




def countInversions(arr):
    n = len(arr)
    move = 0
    for i in range(n):
        for j in range(n-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                move += 1
    return move

print(countInversions(arr))