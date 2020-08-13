class Solution:
    def longestPalindrome(self, s) -> str:
        # 将s的每个字符之间加入#来进行对称的判定，注意，#实际上不代表任何意思，仅代表对称轴
        sNew = '#'.join(s)

        sList = list(sNew)
        longest = ""
        for i in range(len(sList)):
            # 以i为中心，向两边扩散
            if i == 0:
                longest = sList[0]
                continue
            left = i - 1
            right = i + 1
            temp = sList[i] if sList[i] != '#' else ""
            # temp.append(sList[i])
            while left >= 0 and right < len(sList):
                if sList[left] == '#' or sList[right] == '#':
                    left -= 1
                    right += 1
                    continue

                if sList[left] == sList[right]:
                    temp = sList[left] + temp + sList[right]
                else:
                    break
                left -= 1
                right += 1
            
            if len(temp) > 1 and len(longest) < len(temp):
                longest = temp
            
        return longest


solution = Solution()
print(solution.longestPalindrome("cbbd"))

