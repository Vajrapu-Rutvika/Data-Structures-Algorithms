def move_zeros_to_end(arr):
    i=0
    for j in range(len(arr)):
        if arr[j]!=0:
            arr[i],arr[j]=arr[j],arr[i]
            i=i+1
    return arr
arr=list(map(int,input("enter elements into array: ").split()))        
print("array after moving zeros to end: ",move_zeros_to_end(arr))