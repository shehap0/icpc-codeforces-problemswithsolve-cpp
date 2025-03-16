import math

x,y = map(int, input().split())

print(f"floor {x} / {y} = {math.floor(x/y)}")
print(f"ceil {x} / {y} = {math.ceil(x/y)}")
print(f"round {x} / {y} = {round(x/y)}") 
# the code will not pass cuz this problem built for c++ code not python cuz
# round if take value like 2.5 in c++ will output 3 and in python will be 2