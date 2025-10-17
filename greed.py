import sys

def dfs_coins(coins:list,amount:int)->int:
    if amount == 0:
        return 0
    return None


def coinChange( coins: list, amount: int) -> int:
    # 对 coins进行排序
    minNum = sys.maxsize
    if amount!=0 and amount < min(coins):
        return -1
    if amount == 0:
        return 0
    for i in coins:
        if amount >= i:
            next_amount = amount - i
            minNum1 = coinChange(coins, next_amount)
            if minNum1 < minNum and minNum1 != -1:
                minNum = minNum1
    return minNum + 1 if minNum+1 < sys.maxsize else -1


