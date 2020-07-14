## Coin Change

You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11

Output: 3 

Explanation: 11 = 5 + 5 + 1

Example 2:

Input: coins = [2], amount = 3

Output: -1

Note:
You may assume that you have an infinite number of each kind of coin.


## 零钱兑换

给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。

 

示例 1:

输入: coins = [1, 2, 5], amount = 11

输出: 3 

解释: 11 = 5 + 5 + 1

示例 2:

输入: coins = [2], amount = 3

输出: -1
 

说明:
你可以认为每种硬币的数量是无限的。

## 解题思路：动态规划

假设现硬币coins为[1,2,5]
1. 定义状态：定义F[x] = 最优解法，即最小硬币数量。定义的数组大小为amount + 1
2. 定义转移方程：F[x] = min{F[x-1]+1, F[x-2]+1, F[x-5]+1}
3. 定义初始化值即边界值：F[0]=0, 若不存在最优解，则F[x] = -1
4. 确定计算顺序：因为该题是求最优解且后面的状态需要通过前面的状态计算，所以该题为从小到大的顺序解题。

Note: 写代码时需要注意项：
1. 需要确保剩余面额X大于硬币面额
2. 需要确保不能使用-1跟其他状态对比。因为初始化的全部状态为-1， 且不存在最优解的状态也为-1，若用-1比较，则-1一直为最小。故需要判断当前状态是否为-1。