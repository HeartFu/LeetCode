class Solution:
    def minArray(self, numbers) -> int:
        if len(numbers) == 1:
            return numbers[0]
        # 确定左边数组大还是右边数组大
        if numbers[0] < numbers[len(numbers) - 1]:
            return numbers[0]
        
        # 二分查找
        left = 0
        right = len(numbers) - 1
        min_value = numbers[right]
        while left < right:
            mid = int((left + right) / 2)
            if numbers[mid] >= min_value:
                left = mid + 1
            elif numbers[mid] < min_value:
                right = mid - 1

        return numbers[left]

solution = Solution()
print(solution.minArray([1,1]))