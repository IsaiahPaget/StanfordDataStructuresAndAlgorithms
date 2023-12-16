def gcd_DEP(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if not (a % d != 0) and not (b % d != 0):
            if d > current_gcd:
                current_gcd = d

    return current_gcd

def gcd(a, b):
    while b != 0:
        temp = a
        a = b
        b = temp % b
    return a


if __name__ == "__main__":
    a, b = map(int, input().split())
    print(gcd(a, b))
