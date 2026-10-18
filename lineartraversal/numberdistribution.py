# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
arr=list(map(int,input().split()))
zero=0
positive=0
negative=0
for i in arr:
    if i==0:
        zero+=1
    elif i>0:
        positive+=1
    else:
        negative+=1
print(zero,positive,negative)                