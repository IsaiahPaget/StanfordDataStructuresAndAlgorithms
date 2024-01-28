import math
def binary_search(keys, query):
    # write your code here
    if len(keys) <= 1:
        if keys[0] == query:
            return 0
        else:
            return -1
    len_keys = len(keys)
    current_key = math.floor(len_keys / 2)

    while True:
        if query <= keys[current_key]:
            pass
            

if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')
