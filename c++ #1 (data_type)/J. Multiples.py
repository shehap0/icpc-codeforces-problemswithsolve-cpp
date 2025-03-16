x, y= map(float, input().split())

if x%y == 0:
    print("Multiples")
elif y%x == 0:
    print("Multiples")
else:
    print("No Multiples")