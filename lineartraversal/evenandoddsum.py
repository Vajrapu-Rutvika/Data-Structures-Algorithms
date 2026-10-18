# Enter your code here. Read input from STDIN. Print output to STDO
N=int(input())
nums=map(int,input().split())
even_sum=0
odd_sum=0

for num in nums:
    if num%2==0:
        even_sum+=num
    else:
        odd_sum+=num

print(odd_sum,even_sum)
           
    