import math

print(math.pi)

# math.pi = 10
# print(math.pi)

while True:
    x = input("Introdu un numar ")
    print("Ai introdus: ", x, type(x))

    aria = math.pi * int(x) ** 2
    print("Aria: ", aria)