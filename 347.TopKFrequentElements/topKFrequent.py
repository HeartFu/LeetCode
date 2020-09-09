import collections

class Solution:
    def topKFrequent(self, nums, k):
        counter = collections.Counter(nums)
        val = list(counter.keys())
        left = 0
        right = len(val) - 1

        while left <= right:
            pivot = self.partQuickSort(left, right, counter, val)
            if pivot == k - 1:
                return val[:k]
            if pivot > k - 1:
                right = pivot - 1
            else:
                left = pivot + 1


    def partQuickSort(self, l, r, counter, val):
        ran = random.randint(l, r)
        val[ran], val[r] = val[r], val[ran]
        pivot = r
        right = l
        for i in range(l, r):
            if counter.get(val[i]) >= counter.get(val[pivot]):
                val[i], val[right] = val[right], val[i]
                right += 1
        val[right], val[pivot] = val[pivot], val[right]
        return right

solution = Solution()
print(solution.topKFrequent([1,1,1,2,2,3],2))