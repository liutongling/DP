def move(n,a,b,c):
    print(f"Move plate {n} th from {a} to {b}.")
def hanoi(n,a,b,c):
    if n == 1:
        move(n,a,b,c)
        return 1
    else:
        p = hanoi(n-1,a,c,b)
        move(n,a,b,c)
        l = hanoi(n-1,c,b,a)
        return 1+p+l


def example(n):
    if n == 1:
        return 1
    for i in range(n):
        print(f" {n}",end='')
    print("\n")
    example(n-1)
