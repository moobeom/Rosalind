### Find the minimum number of coins needed to make change ###

def DPChange(money,coins):
    MinNumCoins = [0]*(money+1)
    for m in range(1, money+1):
        MinNumCoins[m] = 1000
        for i in range(len(coins)):
            if m >= coins[i]:
                if MinNumCoins[m - coins[i]] + 1 < MinNumCoins[m]:
                    MinNumCoins[m] = MinNumCoins[m - coins[i]] + 1
    return MinNumCoins[money]

sample_money = 16108
sample_coins = [1,3,5,8,11,15,21,22]
print(DPChange(sample_money,sample_coins))