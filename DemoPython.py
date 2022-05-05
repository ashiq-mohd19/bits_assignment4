p = input('Enter the principal p')
t = input('enter the time t')
r = input('enter the rate of intrest r')

p = int(p)
t = int(t)
r = int(r)
si = int((p * t * r) / 100)

print('Simple intrest : ', si, 'for the loan')

if si > 100:
    print('high intrest')
elif si < 100:
    print('low intrest')
else:
    print("perfect intrest")

a = 34
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")

