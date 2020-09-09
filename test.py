class Solution:
    def combine(self, n, k):
        if n < k or n < 1:
            return []
        if k == 0:
            return [[]]
        if n == k:
            return [[i for i in range(1, n+1)]]
        ans1 = self.combine(n-1, k-1)
        ans2 = self.combine(n-1, k)
        print(n, k, ans1, ans2)
        if ans1:
            for i in ans1:
                i.append(n)
        return ans1+ans2

solution = Solution()
print(solution.combine(4,2))