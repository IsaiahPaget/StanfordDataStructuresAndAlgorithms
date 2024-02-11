def majority_element_naive(elements):
    maxCount = 0
    length = len(elements)
    for i in range(length):
        count = 1

        for j  in range(i+1, length):
            if elements[i] == elements[j]:
                count += 1

        if count > maxCount:
            maxCount = count

    if maxCount > length // 2:
        return 1

    return 0

def majority_element(elements):
    current = 0
    counter = 0
    length = len(elements) / 2

    for element in elements:
        if counter == 0:
            current = element
            counter = 1
        elif current == element:
            counter += 1
        else:
            counter -= 1

    if elements.count(current) > length:
        return 1
    else:
        return 0

if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element(input_elements))
