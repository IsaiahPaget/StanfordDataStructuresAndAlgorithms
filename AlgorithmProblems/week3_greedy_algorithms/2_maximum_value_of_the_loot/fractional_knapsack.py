from sys import stdin


def optimal_value(capacity, weights, values):
    value = 0.
    # write your code here
    valuesByWeight = []
    for i in range(len(values)):
        valuesByWeight.append((values[i], weights[i]))
    valuesByWeight.sort(reverse=True, key=lambda x : x[0] / x[1])
    
    for i in range(len(valuesByWeight)):
        if valuesByWeight[i][1] <= capacity:
            capacity -= valuesByWeight[i][1] 
            value += valuesByWeight[i][0]
        else:
            value += (valuesByWeight[i][0] * capacity) / valuesByWeight[i][1]
            break

    return value


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
