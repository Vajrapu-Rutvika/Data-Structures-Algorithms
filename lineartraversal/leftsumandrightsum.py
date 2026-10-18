# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
arr=list(map(int,input().split()))
for i in range(n):
    leftsum=sum(arr[:i])
    rightsum=sum(arr[i+1:])
    print(abs(leftsum-rightsum),end=" ")
