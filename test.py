class Solution:
    def threeSum(self, nums):
        nums.sort()
        result = []
        length = len(nums)

        for i in range(length):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            maxIndex = length - 1
            target = -nums[i]

            for j in range(i + 1, length):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                
                while maxIndex > j:
                    objectTar = nums[j] + nums[maxIndex]
                    if target == objectTar:
                        result.append([nums[i], nums[j], nums[maxIndex]])
                        break
                    elif target > objectTar:
                        break
                    else:
                        maxIndex -= 1
                
                if j == maxIndex:
                    break
        
        return result

solution = Solution()
print(solution.threeSum([-1,0,1,2,-1,-4]))