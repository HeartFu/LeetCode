class Solution:
    def searchInsert(self, nums, target) -> int:
        length = len(nums)
        left = 0
        right = length - 1
        while True:
            if left > right:
                return left
            # if left <= right:
            #     if nums[left] <= target:
            #         return left
            #     else:
            #         return left + 1
            middle = int((left + right) / 2)
            # if middle >= len(nums) - 1:
            #     return len(nums)
            # if middle < 0:
            #     return 0
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1
        return 0

solution = Solution()
print(solution.searchInsert([1,3,5,6], 2))