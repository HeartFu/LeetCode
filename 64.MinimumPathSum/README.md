https://leetcode-cn.com/problems/minimum-path-sum/

## 64. Minimum Path Sum

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

**Note**: You can only move either down or right at any point in time.

**Example**:

**Input**:

[

  [1,3,1],

  [1,5,1],

  [4,2,1]

]

**Output**: 7

**Explanation**: Because the path 1→3→1→1→1 minimizes the sum.

## 64. 最小路径和

给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。

**示例**:

**输入**:

[

  [1,3,1],

  [1,5,1],

  [4,2,1]

]

**输出**: 7

**解释**: 因为路径 1→3→1→1→1 的总和最小。

## 题目解析 -- 动态规划

从题目中来看，这是一个求最值的问题，第一思路就是往动态规划上面靠。使用动态规划的四个步骤来求解。

1. 定义状态

    因为该题目时左上角为起点到右下角的最小路径，起始点已经确定为（0,0）点，故定义f(i,j)为从（0,0）点到（i,j）点的最小路径和。则最终状态为f(m-1,n-1)。初始化状态为二维数组。

2. 定义状态转移方程

    状态转移方程为：f(i,j) = min(f(i-1, j), f(i, j-1)) + grid(i,j)

3. 确定初始值与边界值

    初始值为起始点拥有的数字，故f(0,0) = grid(0,0) = 1

    边界值：
        a. 网格边界值为m * n, 故i 与 j的边界值为i<\m,j<\n.

        b. 因为每次只能向下或者向右移动一步，故
            当i==0时表示当前网格的上一步来源只能是其上边（上一步的动作为向<font color='red'>**下**</font>移动一步），即不存在f(i-1, j)， 故f(i,j) = f(i, j-1) + grid(i,j).

            当j==0时表示当前网格的上一步来源只能是其左边（上一步的动作为向<font color='red'>**左**</font>移动一步），即不存在f(i, j-1)， 故f(i,j) = f(i-1, j) + grid(i,j).
    
    故状态转移方程根据边界值可以调整为：

        当i==0 && j==0时， f(i,j) = grid(0,0)
        当i==0 && j!=0时， f(i,j) = f(i, j-1) + grid(i,j)
        当i!=0 && j==0时， f(i,j) = f(i-1, j) + grid(i,j).
        当i!=0 && j!=0时， f(i,j) = min(f(i-1, j), f(i, j-1)) + grid(i,j)

4. 确定顺序

    最终求解的为f(m,n)，故计算顺序为正序。

