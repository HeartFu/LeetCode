class Solution:
    def coinChange(self, coins, amount) -> int:
        f = [-1] * (amount + 1)

        f[0] = 0

        for i in range(1, amount + 1):
            for j in range(0, len(coins)):
                if i >= coins[j] and f[i - coins[j]] >=0:
                    if f[i] < 0:
                        f[i] = f[i - coins[j]] + 1
                    else:
                        f[i] = min(f[i - coins[j]] + 1, f[i])
            
        return f[amount]

solution = Solution()
print(solution.coinChange([2,5,10,1], 27))
# print(solution.coinChange([2], 3))
