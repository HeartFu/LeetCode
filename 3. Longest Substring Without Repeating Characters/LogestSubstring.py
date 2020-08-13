class Solution:
    def lengthOfLongestSubstring(self, s) -> int:

        sList = list(s)
        maxLength = 0
        result = []
        for i in range(len(sList)):
            if sList[i] in result:
                # 从这个index截断前面所有的值
                index = result.index(sList[i])
                if index >= len(result):
                    result = []
                else:
                    result = result[index+1:]
            
            result.append(sList[i])
            if maxLength < len(result):
                maxLength = len(result)
        
        return maxLength

solution = Solution()
print(solution.lengthOfLongestSubstring("abcabcbb")) # result = 3
