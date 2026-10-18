# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
arr=list(map(int,input().split()))
x=int(input())
first=arr.index(x)
last=N-1-arr[::-1].index(x)
print(first,last)