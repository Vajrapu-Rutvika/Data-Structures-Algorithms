def remove_duplicates_from_array(arr):
    if len(arr)==0:
        return 0
    i=0
    for j in range(1,len(arr)):
        if arr[j]!=arr[i]:
            i=i+1
            arr[i]=arr[j]
    return i+1
arr=list(map(int,input("enter elements into array: ").split())) 
print("length of array after removing duplicates is: ", remove_duplicates_from_array(arr))       