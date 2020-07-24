class Solution:
    def divisorGame(self, N: int) -> bool:
        if N <= 1:
            return False
        
        f = [0] * (N + 1)
        f[1] = 0
        f[2] = 1

        for i in range(3, N + 1):
            for j in range(1, i):
                if i % j == 0 and f[i-j] == 0:
                    f[i] = 1
                    break

        return f[N] == 1

solution = Solution()
print(solution.divisorGame(3))