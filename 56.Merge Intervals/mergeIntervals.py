import operator
from functools import reduce

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=(lambda x: x[0]))

        stack = []

        for i in range(len(intervals)):
            if i == 0:
                stack.append(intervals[0])
                continue
            
            intervalOfStack = stack[len(stack) - 1]
            currentInterval = intervals[i]

            if intervalOfStack[1] >= currentInterval[0]:
                if intervalOfStack[1] <= currentInterval[1]:
                    # 与currentInterval重新组成新数组
                    stack.pop()
                    newInterval = [intervalOfStack[0], currentInterval[1]]
                    stack.append(newInterval)
            else:
                stack.append(currentInterval)
        return stack
            