import bisect
import math


def remove_insert(arr, old_val, new_val):
    idx = bisect.bisect_left(arr, old_val) # value need to remove
    # remove old value
    arr.pop(idx)
    # insert new value
    bisect.insort(arr, new_val)
    return arr

def activityNotifications(expenditure, d):
    notifications = 0
    arr = []
    if d%2 == 0:
        x = int(d/2)
        for i in range(len(expenditure) - d):
            if not arr: # it means arr == []
                arr = expenditure[:d]
                arr = sorted(arr)
            
            old_val = expenditure[i]
            new_val = expenditure[i+d]
            median = arr[x] + arr[x - 1]
            if expenditure[i+d] >= median:
                notifications += 1
            remove_insert(arr, old_val, new_val)
    else:
        x = math.floor(d/2)
        for i in range(len(expenditure) - d):
            if not arr:
                arr = expenditure[:d]
                arr = sorted(arr)
            
            old_val = expenditure[i]
            new_val = expenditure[i+d]
            median = arr[x]
            if expenditure[i+d] >= 2*median:
                notifications += 1
            remove_insert(arr, old_val, new_val)
    return notifications

expenditure = [2,3,4,2,3,6,8,4,5]
d = 5

print(activityNotifications(expenditure, d))