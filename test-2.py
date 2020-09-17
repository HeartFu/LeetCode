class Solution:
    def solveNQueens(self, n):
        status_matrix = [[0]*n for i in range(n)]
        row = 0
        final_result = []
        self.backTracking(n, status_matrix, row, final_result)
        return final_result

    def backTracking(self, n, status_matrix, row, final_result):
        if row == n:
            # if status_matrix not in final_result:
            queens = []
            for i in range(n):
                curstr = ''
                for j in range(n):
                    if status_matrix[i][j] == 1:
                        curstr += 'Q'
                    else:
                        curstr += '.'
                queens.append(curstr)
            final_result.append(queens)
            return
        
        for j in range(n):
            if (row - 1 >= 0 and j - 1 >= 0 and status_matrix[row - 1][j - 1] == 1) \
                or (row -1 >= 0 and j + 1 < n and status_matrix[row - 1][j + 1] == 1) \
                or (row +1 < n and j - 1 >= 0 and status_matrix[row + 1][j - 1] == 1) \
                or (row +1 < n and j + 1 < n and status_matrix[row + 1][j + 1] == 1):
                continue
            
            flag = True # 标识列是否存在Q
            for i in range(n):
                if status_matrix[i][j] == 1:
                    flag = False

            if flag == False:
                continue
            
            status_matrix[row][j] = 1
            self.backTracking(n, status_matrix, row + 1, final_result)
            status_matrix[row][j] = 0

solution = Solution()
print(solution.solveNQueens(4))