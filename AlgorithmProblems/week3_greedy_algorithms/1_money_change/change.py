def change(money):
    # write your code here
    numCoin = 0
    while money > 0:
        if money >= 10:
            money -= 10
        elif money >= 5:
            money -= 5
        else:
            money -= 1
        numCoin = numCoin + 1
    return numCoin

if __name__ == '__main__':
    m = int(input())
    print(change(m))
