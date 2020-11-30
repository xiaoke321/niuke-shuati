


def func(s, i, j):
    if i < j:
        func(s, i + 1, j - 1)
        s[i], s[j] = s[j], s[i]

def main():
    a = [10, 6, 23, -90, 0, 3]
    func(a, 0, len(a) - 1)
    for i in range(6):
        print(a[i])
        print("\n")

main()