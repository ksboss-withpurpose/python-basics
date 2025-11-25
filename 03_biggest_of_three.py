a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
c = int(input("Enter number 3: "))

if a >= b and a >= c:
    print("Biggest number is:", a)
elif b >= a and b >= c:
    print("Biggest number is:", b)
else:
    print("Biggest number is:", c)
