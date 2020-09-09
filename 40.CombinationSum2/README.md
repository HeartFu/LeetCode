https://leetcode-cn.com/problems/combination-sum-ii/

## 40. Combination Sum II

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used **once** in the combination.

**Note:**

- All numbers (including target) will be positive integers.
- The solution set must not contain duplicate combinations.


**Example 1**:

```
Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]

```
**Example 2:**

```
Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]

```


## 56. 合并区间

给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的每个数字在每个组合中只能使用一次。

**说明：**

- 所有数字（包括目标数）都是正整数。
- 解集不能包含重复的组合。 

**示例 1:**
```
输入: candidates = [10,1,2,7,6,1,5], target = 8,
所求解集为:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
```
**示例 2:**
```
输入: candidates = [2,5,2,1,2], target = 5,
所求解集为:
[
  [1,2,2],
  [5]
]
```


## 解题思路

该题最简单的做法为暴力破解法， 一个一个数字拼接看是否达到target的值。该方法简单有效，缺点为复杂度太高，若遇到数组长度过长的，可能会导致超时。

第二种解题思路为递归。实际上从该题目中就能看出，该目的就是递归寻找另一个target - candidates[i] - candidates[j]...的值.

算法如下：

- 1. 排序当前的candidates.
- 2. 判断当前target是否在传入的candidates中存在， 若存在，则组成list放入到result中
- 3. 循环遍历每一个candidates中的值：a. 判断当前值是否已经大于target，若大于，则停止循环（因为若当前值已经大于target，则后续的值不可能出现与target相同的）。反之，继续。
- 4. (承接上述遍历内容) 通过target-candidates[i]获取更新后的target和子列表candidates[i:]。递归调用到步骤2.
- 5. 若当前子candidates长度为0，则直接返回空。
- 6. 将得到的结果与当前candidates[i]拼接生成新的result.
- 7. 全部遍历完后，返回result