# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())
for _ in range(T):
    N = int(input())
    total = sum(map(int,input().split()))
    print(total)