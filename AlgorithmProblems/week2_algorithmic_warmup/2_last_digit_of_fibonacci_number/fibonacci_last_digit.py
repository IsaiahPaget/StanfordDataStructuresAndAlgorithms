from functools import lru_cache

first = (0,1)

@lru_cache(maxsize=None)
def fibonacci_last_digit(n):
    if n in first:
	    return n

    previous, current = first

    for _ in range(n - 1):
	    previous, current = current, (previous + current) % 10
	    # print("Current: {}".format(current))
    return current

if __name__ == '__main__':
    n = int(input())
    print(fibonacci_last_digit(n))
