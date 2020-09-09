class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        left = 0
        return self.recursion(left, candidates, target)

    def recursion(self, left, candidates, target):
        if left >= len(candidates):
            return []
        result = []
        if target in candidates[left:]:
            result.append([target])
        
        for i in range(left, len(candidates)):
            if candidates[i] >= target:
                break
            new_target = target - candidates[i]
            new_left = i + 1

            rec_result = self.recursion(new_left, candidates, new_target)
            if len(rec_result) != 0:
                for item in rec_result:
                    item.append(candidates[i])
                    if item not in result:
                        result.append(item)
        
        return result

solution = Solution()
print(solution.combinationSum2([10,1,2,7,6,1,5], 8))