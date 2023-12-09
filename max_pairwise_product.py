import random
import math

def max_pairwise_product(numbers):
    n = len(numbers)
    max_one = 0
    i1 = 0
    for i in range(n):
        if numbers[i] > max_one:
            max_one = numbers[i]
            i1 = i
    max_two = -1
    for j in range(n):
        if numbers[j] > max_two and j != i1:
            max_two = numbers[j]

    return (max_one * max_two)

def max_pairwise_product_slow(numbers):
    n = len(numbers)
    max = -1
    for i in range(n):
        for j in range(n):
            if numbers[j] * numbers[i] > max:
                max = numbers[j] * numbers[i] 
    
    return max

def stress_test():

    while (True):
        n = random.randint(0, 100) 
        print(f"n: {n}")

        a = []
        for i in range(n):
            a.append(random.randint(0, 10))

        for i in range(n):
            print(f"a[i]: {a[i]} ")

        res1 = max_pairwise_product(a)
        res2 = max_pairwise_product_slow(a)

        if res1 != res2:
            print(f"Wrong -> res1: {res1}, res2: {res2}")
            break
        else:
            print("OK")

if __name__ == '__main__':

    # stress_test() 
    _ = int(input())
    input_numbers = list(map(int, input().split()))
    print(max_pairwise_product(input_numbers))
