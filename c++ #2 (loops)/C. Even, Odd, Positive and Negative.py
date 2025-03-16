x= int(input())
numbers = list(map(int, input().split()))

even=0
odd=0
position=0
negative=0

for i in numbers:
    
    if i%2==0:
        even+=1
    else: odd+=1
    if i>0:
        position+=1
    elif i<0:
        negative+=1    
        
print(f"Even: {even}")
print(f"Odd: {odd}")
print(f"Positive: {position}")
print(f"Negative: {negative}")
    