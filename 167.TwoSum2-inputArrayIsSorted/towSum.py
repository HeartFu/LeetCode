class Solution:
    def twoSum(self, numbers, target):
        for i in range(len(numbers)):
            value = target - numbers[i]
            result = self.binarySearch(numbers, len(numbers), value, i)
            if result != -1:
                # 表示已经找到
                return [i+1, result+1] if i < result else [result + 1, i + 1]
        
        return []

    
    def binarySearch(self, arrays, n, value, i):
        left = 0
        right = n - 1

        while left <= right:
            middle = int((left + right) / 2)
            if value == arrays[middle]:
                if (middle == i):
                    # 不使用相同的元素
                    return -1
                else:
                    return middle
            if value > arrays[middle]:
                left = middle + 1
            else:
                right = middle - 1
        
        return -1

solution = Solution()
print(solution.twoSum([2,7,11,15], 9))
