## 312. [Burst Balloons](https://leetcode-cn.com/problems/burst-balloons/solution/dong-tai-gui-hua-js312-chuo-qi-qiu-by-fe-lucifer/)

Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums. You are asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins. Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

**Note**:

- You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
- 0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
  
**Example**:

**Input**: [3,1,5,8]

**Output**: 167 

**Explanation**: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; coins =  3\*1\*5  &nbsp;&nbsp; + &nbsp;&nbsp; 3\*5\*8&nbsp; +&nbsp;1\*3\*8      + 1\*8\*1   = 167


## 312. [戳气球](https://leetcode-cn.com/problems/burst-balloons/solution/dong-tai-gui-hua-js312-chuo-qi-qiu-by-fe-lucifer/)

有 n 个气球，编号为0 到 n-1，每个气球上都标有一个数字，这些数字存在数组 nums 中。

现在要求你戳破所有的气球。如果你戳破气球 i ，就可以获得 nums[left] * nums[i] * nums[right] 个硬币。 这里的 left 和 right 代表和 i 相邻的两个气球的序号。注意当你戳破了气球 i 后，气球 left 和气球 right 就变成了相邻的气球。

求所能获得硬币的最大数量。

**说明**:

- 你可以假设 nums[-1] = nums[n] = 1，但注意它们不是真实存在的所以并不能被戳破。
- 0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
jie
**示例**:

**输入**: [3,1,5,8]

**输出**: 167 

**解释**: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; coins =  3\*1\*5  &nbsp;&nbsp; + &nbsp;&nbsp; 3\*5\*8&nbsp; +&nbsp;1\*3\*8      + 1\*8\*1   = 167


## 解题思路 -- 动态规划

从题目中来看，该问题为求解最值问题。回顾一下动态规划可能出现的提醒：**1）求最值问题(该题目)； 2）计数问题(Coin change)； 3）存在性问题(待添加)**。 

该题目中也可以使用暴力求解法，但复杂度较高，容易超出范围。故该问题记忆使用动态规划来求解。实际上就是求局部最优解。 使用动态规划求解问题分为4个步骤：

1. 定义状态
    
    假设最后戳破的气球是k，则戳破气球k获得最大数量的硬币为nums[i]\*nums[k]\*nums[j]加上前面戳破的最大数量和后面戳破的最大数量。
    
    则状态可以定义为f[i,j] = x 表示戳破气球i和气球j之间(不包括i，j)的所有气球，可以获得的最大硬币数为x

2. 定义状态转移方程

    从定义状态时，我们可以看到戳破气球k获得的最大数量的硬币为nums[i]\*nums[k]\*nums[j]，则状态转移方程即为：f[i,j]=max(f[i,j], f[i,k]+f[k,j]+nums[i]\*nums[k]\*nums[j])， k为i到j之前的所有值

3. 定义初始值和边界
   
   题目中已经提示可以假设 nums[-1] = nums[n] = 1， 则边界值为-1 到 n + 1，总共n+2个值。

   初始值设定为0表示没有开始时所有可能的结果均为0.

   当i==j时，表示两个之间已经没有气球，则完成计算

4. 定义计算顺序

    最终我们要的答案为f[0, n+1]，即戳破虚拟气球之间的所有气球获得的最大值。所以最终值i为0，j为n+1，所以该顺序应该为i从大到小计算，j从小到大计算。但因为i需要小于j，故i从n起步到-1，每次减小1，j从i+1起步到n+2，每次增加1.

最后根据所得到的上面的解题思路进行撰写代码即可。

**复杂度分析**

- 时间复杂度：O(N ^ 3)
- 空间复杂度：O(N ^ 2)

