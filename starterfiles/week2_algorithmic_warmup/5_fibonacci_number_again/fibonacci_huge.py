def fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m

first = (0,1)
def fibonacci_huge(n, m):
    if n <= 1:
       return n

    previous = 0
    current = 1
    tmp_previous = 0

    pisano = [0, 1]

    while True:
        tmp_previous = previous
        previous = current
        current = (tmp_previous + current) % m
        if current == 1 and previous == 0:
            break
        else:
            pisano.append(current)

    pisano.pop()
    index = n % len(pisano)
    return pisano[index]

if __name__ == '__main__':
    n, m = map(int, input().split())
    print(fibonacci_huge(n, m))
