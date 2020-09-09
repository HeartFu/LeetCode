class Solution:
    def combine(self, n, k):
        if n < 1 or n < k:
            return []
        if k == 0:
            return [[]]
        if n == k:
           return [[i for i in range(1, n+1)]]
        
        res1 = self.combine(n - 1, k - 1)
        res2 = self.combine(n - 1, k)
        print(n, k, res1, res2)
        if res1:
            for i in res1:
                i.append(n)

        return res1 + res2

solution = Solution()
print(solution.combine(4,2))