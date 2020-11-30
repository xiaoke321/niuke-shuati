


def f (a, b):
    if b == 0:
        print(a)
    else:
        f(b, a % b)


a, b = input("Enter two natural numbers: ")
print(f(a, b))