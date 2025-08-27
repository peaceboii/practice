# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

total_shoes = int(input())
available_sizes=Counter(map(int,input().split()))
total_customers = int(input())


revenue = 0
for i in range (total_customers):
    shoe_size,amount =map(int,input().split())

    if available_sizes[shoe_size]>0:
        revenue+=amount
        available_sizes[shoe_size]-=1 
      
    
    
print(revenue)
    