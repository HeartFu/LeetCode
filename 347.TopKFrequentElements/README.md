https://leetcode-cn.com/problems/top-k-frequent-elements/

## 347. Top K Frequent Elements

Given a non-empty array of integers, return the **k** most frequent elements.

**Example 1**:

```
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
```
**Example 2:**

```
Input: nums = [1], k = 1
Output: [1]
```


## 347. 前 K 个高频元素

给定一个非空的整数数组，返回其中出现频率前 k 高的元素。

**示例 1:**
```
输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]
```
**示例 2:**
```
输入: nums = [1], k = 1
输出: [1]
```


## 解题思路

最先想到的方法为：首先遍历出来nums中对应数字个个数，然后根据数量排序map(nums中的值，数量)。大多数的排序算法的时间复杂度均超过或等于O(nlogn). 

方法一：半个快速排序

常规快速排序的时间复杂度为O(nlogn)。换一种思路，该题目并不需要全部排序出来，只需要排序出前K个数即可。也可以叫做快速切分(partition)，常用做Top K题目的解法。

首先找到一个随机的基准值pivot，这里随机而不是每次固定找一个位置，是因为这样在概率上不会把每次区分都分成特别不均匀的两块，然后找到这个基准值在整个数组中的位置。方法就是遍历其他元素，把小于（或者等于）当前元素的往前放（假设从小到大排序），把大于当前元素的往后放，我们用两个指针指向数组首部和尾部的位置，分别表示在前面放的元素的最右边界，和在后面放的元素的最左边界就可。这样在第一个指针的结尾，我们放入当前作为基准的值，这个数组在基准值之前就都是小于等于基准值的，后面就都是大于等于基准值的。这个就叫快速切分partition。之后我们再pivot左侧和右侧执行同样的逻辑，直到数组的长度为1，整个数组就是排好序的了。利用第一步的快速切分，我们可以解决求某种意义上数组中第K小元素的问题，只要pivot在数组中的索引为k-1，那么pivot就是要寻找的元素。如果不是，因为pivot分隔的数组也是它们值的分界线，我们可以只去一边查找。这样的查找时间复杂度是O(n)的，因为每次调用partition遍历的元素都是上一次的二分之一，所以时间复杂度是N+N/2+N/4+...+N/N = 2N。这是经典的Top K问题，快速选择（partition）往往是时间复杂度最快的解法。

