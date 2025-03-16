x= int(input())
y=True

for i in range(1,x+1):
    if i%2==0:
        print(i)
        y=False

if y==True:
    print(-1)