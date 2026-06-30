def second_largest_elemrnt_in_array(arr):
    largest=arr[0]
    secondlargest=-1
    for i in range(1,len(arr)):
        if arr[i]>largest:
            secondlargest=largest
            largest=arr[i]
        elif arr[i]<largest and arr[i]>secondlargest:
            secondlargest=arr[i]
    return secondlargest
arr=list(map(int,input("enter the array of elements: ").split()))
secondlargestelement=second_largest_elemrnt_in_array(arr) 
print("second largest element in the array is: ",secondlargestelement)       


