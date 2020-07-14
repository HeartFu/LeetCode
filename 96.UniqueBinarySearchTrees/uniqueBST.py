class Solution:
    def numTrees(self, n):
        G = [0] * (n + 1)
        G[0] = 1
        G[1] = 1

        for i in range(2, n + 1):
            for j in range(1, i + 1):
                G[i] += G[j - 1] * G[i - j]
        return G[n]

solution = Solution()
print(solution.numTrees(0))