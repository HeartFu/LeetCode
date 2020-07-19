## 167. Two Sum II - Input array is sorted

Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution and you may not use the same element twice.

Example:

Input: numbers = [2,7,11,15], target = 9

Output: [1,2]

Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.


## 两数之和 II - 输入有序数组

给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。

函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。

说明:

返回的下标值（index1 和 index2）不是从零开始的。

你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。

示例:

输入: numbers = [2, 7, 11, 15], target = 9

输出: [1,2]

解释: 2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。

## 解题思路

从题目中来看，相当于遍历所有的数字查找对应的数字是否存在相加等于target的两个数。

最简单的思路为暴力破解法。制定两个循环，第一个循环为遍历所有的numbers，第二个循环也为遍历所有的numbers（除了上个循环所在位置本身）。该方法可以解决大部分问题，其时间复杂度为O(n^2)。代价相对较大，若碰见特别大的数组时，可能会出现超时的可能行。

第二个思路为<font color="red">二分法（折半查找）</font>, 寻找两个数使得他们相加之和等于目标数，实际上时寻找其中一个数，使得目标数减去当前下标所得value为最终求解值。实际上该题时一个查找类问题。大部分的查找类问题为了减少计算量和时间复杂度，会使用二分查找来进行解决。

即实际为：在numbers中使用二分查找查询值为target - numbers[i]的位置。