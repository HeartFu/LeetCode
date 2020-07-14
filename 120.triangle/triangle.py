class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        length = len(triangle)
        for r in range(length - 2, -1, -1):
            for c in range(len(triangle[r])):
                triangle[r][c] += min(triangle[r+1][c:c+2])
        return triangle[0][0]

solution = Solution()
print(solution.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))