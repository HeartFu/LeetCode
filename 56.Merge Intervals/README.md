https://leetcode-cn.com/problems/merge-intervals/

## 56. Merge Intervals

Given a collection of intervals, merge all overlapping intervals.

**Example 1**:

```
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
```
**Example 2:**

```
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
```

**NOTE:** input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.

**Constraints:**

intervals[i][0] <= intervals[i][1]


## 56. 合并区间

给出一个区间的集合，请合并所有重叠的区间。

**示例 1:**
```
输入: [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
```
**示例 2:**
```
输入: [[1,4],[4,5]]
输出: [[1,5]]
解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。
```


## 解题思路

该题不需要考虑太多的技巧，直接**暴力遍历**，时间复杂度为O(n)。

1. 因为当前的区间集合可能存在未排序的状态，e.g.[[1,4],[2,6],[0, 5]], 所以需要先以区间左端的数值为基准进行排序。使用python中的sorted函数sorted(intervals, key=(lambda x: x[0])), x[0]表示以数组第一个元素为基准进行排序。

2. 设定一个栈，因为栈是先进后出，方便当前操作，最后结果即为栈中所存区间。

3. 遍历intervals, 
    
    a. 如果stack为空，表示当前为第一个数，则需要将其压入栈中。

    b. 将栈中最后一个区间跟当前区间进行对比，若栈中区间右侧 >= 当前区间左侧 and 栈中区间右侧 <= 当前区间右侧， 表示当前存在重合，则将栈中区间左侧与当前区间右侧进行合并为一个新的区间替换栈中最后一个区间。

    c. 反之，则不存在重合，又因为intervals已经进行过排序，栈中区间也不会和后面的区间重合，故将当前区间压入栈中。

4. 返回栈。