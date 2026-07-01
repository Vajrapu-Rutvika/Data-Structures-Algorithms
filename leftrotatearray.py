def left_rotate_array_by_d_places(arr,k):
    n=len(arr)
    k=k%n
    def reverse(l,r):
        while l<r:
            arr[l],arr[r]=arr[r],arr[l]
            l+=1
            r-=1
    reverse(0,k-1)
    reverse(k,n-1)
    reverse(0,n-1)
    return arr
arr=list(map(int,input("enter the elements into array: ").split()))
k=int(input("enter number of places to rotate array: "))
print("array after left rotation by k places: ",left_rotate_array_by_d_places(arr,k))