class Solution:
    def maxCoins(self, nums):
        n = len(nums)
        # 定义状态方程，该为2维数组，分别表示i和j即左边和右边
        f = [[0] * (n + 2) for _ in range(n+2)]
        new_nums = [1] + nums + [1]

        for i in range(n, -1, -1):
            for j in range(i + 1, n + 2):
                for k in range(i + 1, j):
                    f[i][j] = max(f[i][j], f[i][k] + f[k][j] + new_nums[k] * new_nums[i] * new_nums[j])
        return f[0][n + 1]

solution = Solution()
print(solution.maxCoins([3,1,5,8]))