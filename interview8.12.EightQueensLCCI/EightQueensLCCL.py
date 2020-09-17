class Solution:
    def solveNQueens(self, n):
        status_matrix = [[0]*n for i in range(n)]
        row = 0
        final_result = []
        diagonals1 = []
        diagonals2 = []
        self.backTracking(n, status_matrix, row, final_result, diagonals1, diagonals2)
        return final_result

    def backTracking(self, n, status_matrix, row, final_result, diagonals1, diagonals2):
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
            # if (row - 1 >= 0 and j - 1 >= 0 and status_matrix[row - 1][j - 1] == 1) \
            #     or (row -1 >= 0 and j + 1 < n and status_matrix[row - 1][j + 1] == 1) \
            #     or (row +1 < n and j - 1 >= 0 and status_matrix[row + 1][j - 1] == 1) \
            #     or (row +1 < n and j + 1 < n and status_matrix[row + 1][j + 1] == 1):
            #     continue
            
            # if (j + 1 >= n and row - 1 >= 0 and status_matrix[row - 1][0] == 1) \
            #     or (j + 1 >= n and row + 1 < n and status_matrix[row + 1][0] == 1) \
            #     or (j - 1 < 0 and row - 1 >= 0 and status_matrix[row - 1][n - 1] == 1) \
            #     or (j - 1 < 0 and row + 1 < 0 and status_matrix[row + 1][n - 1] == 1):
            #     # 当为最右边的一个时，也需要与第0位进行比较，不在对角线上
            #     continue

            # flag = True # 标识列是否存在Q
            # for i in range(n):
            #     if status_matrix[i][j] == 1:
            #         flag = False

            # if flag == False:
            #     continue

            flag = True # 标识列是否存在Q
            for i in range(n):
                if status_matrix[i][j] == 1:
                    flag = False

            if flag == False:
                continue

            if row - j in diagonals1 or row + j in diagonals2:
                continue
            diagonals1.append(row - j)
            diagonals2.append(row + j)
            status_matrix[row][j] = 1
            self.backTracking(n, status_matrix, row + 1, final_result, diagonals1, diagonals2)
            status_matrix[row][j] = 0
            diagonals1.remove(row - j)
            diagonals2.remove(row + j)

solution = Solution()
print(solution.solveNQueens(5))