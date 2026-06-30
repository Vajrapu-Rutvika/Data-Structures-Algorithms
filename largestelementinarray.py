def largest_element_in_array(arr):
    maxi=arr[0]
    for i in range(1,len(arr)):
        if arr[i]>maxi:
            maxi=arr[i]
    return maxi
arr=list(map(int,input("enter the elements into array: ").split()))
largest=largest_element_in_array(arr)
print("the largest element in the array is:", largest)