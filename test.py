class Solution:
    def multiply(self, num1, num2) -> str:
        
        num1 = list(num1)
        num2 = list(num2)
        result = []
        len1 = len(num1)
        len2 = len(num2)

        for i in range(len1):
            curPos1 = int(num1[len1 - 1 - i])
            for j in range(len2):
                curPos2 = int(num2[len2 - 1 - j])
                curResult = curPos1 * curPos2
                if i + j >= len(result):
                    result.append(curResult)
                else:
                    result[i + j] = result[i + j] + curResult

                if result[i + j] >= 10:
                    upper = int(result[i + j] / 10)
                    remainder = result[i + j] % 10
                    result[i + j] = remainder
                    if i + j + 1 >= len(result):
                        result.append(upper)
                    else:
                        result[i + j + 1] = result[i + j + 1] + upper

        # 反转数组
        resultStr = [str(x) for x in result]
        resultRev = list(reversed(resultStr))
        return "".join(resultRev)

solution = Solution()
print(solution.multiply("123","456"))