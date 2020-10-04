class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0
        
        rowNum = len(grid)
        colNum = len(grid[0])

        result = 0

        for i in range(rowNum):
            for j in range(colNum):
                if grid[i][j] == '1':
                    result += 1
                    self.dfs(grid, i, j)
        
        return result
    
    def dfs(self, grid, i ,j):
        grid[i][j] = '0'

        for row, col in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
            if 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] == '1':
                self.dfs(grid, row, col) 