class Solution:
    def minPathSum(self, grid) -> int:
        m = len(grid)
        n = len(grid[0])

        # 定义状态
        f = [[0] * n for _ in range(m)]

        # 初始化值
        f[0][0] = grid[0][0]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue;
                elif i == 0 and j != 0:
                    f[i][j] = f[i][j - 1] + grid[i][j]
                elif i != 0 and j == 0:
                    f[i][j] = f[i - 1][j] + grid[i][j]
                else:
                    f[i][j] = min(f[i - 1][j], f[i][j - 1]) + grid[i][j]
        
        return f[m-1][n-1]

solution = Solution()
print(solution.minPathSum([[1,2,5],[3,2,1]]))