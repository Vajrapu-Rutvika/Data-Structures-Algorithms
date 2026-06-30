def check_if_array_is_sorted(arr):
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            return False
    return True
arr=list(map(int,input("enter the elements into array: ").split()))
is_sorted=check_if_array_is_sorted(arr)
if is_sorted:
    print("the array is sorted")
else:
    print("the array is not sorted")    