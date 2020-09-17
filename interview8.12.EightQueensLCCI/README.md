https://leetcode-cn.com/problems/eight-queens-lcci/

Level: **Difficult**

## Interview 08.12. Eight Queens LCCI

Write an algorithm to print all ways of arranging n queens on an n x n chess board so that none of them share the same row, column, or diagonal. In this case, "diagonal" means all diagonals, not just the two that bisect the board.

**Notes**: This problem is a generalization of the original one in the book.


**Example:**

**Input**: 4

**Output:** [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]

**Explanation**: 4 queens has following two solutions

[

 [".Q..",  // solution 1

  &nbsp;"...Q",

  &nbsp;"Q...",

  &nbsp;"..Q."],


 ["..Q.",  // solution 2

  &nbsp;"Q...",

  &nbsp;"...Q",

  &nbsp;".Q.."]

]



## 面试题 08.12. 八皇后

设计一种算法，打印 N 皇后在 N × N 棋盘上的各种摆法，其中每个皇后都不同行、不同列，也不在对角线上。这里的“对角线”指的是所有的对角线，不只是平分整个棋盘的那两条对角线。

**注意：**本题相对原题做了扩展

**示例:**

 **输入：**4

 **输出：**[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
 
 **解释**: 4 皇后问题存在如下两个不同的解法。

[

 [".Q..",  // solution 1

  &nbsp;"...Q",

  &nbsp;"Q...",

  &nbsp;"..Q."],


 ["..Q.",  // solution 2

  &nbsp;"Q...",

  &nbsp;"...Q",

  &nbsp;".Q.."]

]


## 题目解析 -- 回溯 backTracking

从题目中可以看出，该问题需要使用回溯的方法进行递归的查找可能存在的解。

该问题主要需要注意的是判定条件，什么样的solution是合适的。

1. 对角线上不能有重复的Queen
2. 同一行上不能有重复的Queen
3. 同一列上不能有重复的Queen

针对3的判定条件比较好解决：
    
    设定一个states，一个n*n的二维数组，当Queen在该位置时，将该位置的states置为1。
    循环查找当前列上是否存在states为1的情况。

针对2的判定条件：

    在循环遍历中，每一行只存储一个Queen后，递归直接调用的下一行中，故在递归调用时已经满足的该判定条件。

针对1的判定条件：

    1. 当从左上到右下的对角线时，可以观察到row - column的值固定。
    2. 当从右上到左下的对角线时，可以观察到row + column的值固定。
    根据上述规则，将每一个置为Queen的位置对应的row和column进行减法和加法来存储当前可能存在的对角线的位置，将结果存在diagonals1和diagonals2中。
    在每一次递归的时候将当前位置的row-column和row+column与diagonals1/diagonalis2中的值进行对比，若存在，则表示当前位置的对角线已经放置了Queen。

**注：** 在递归完成之后，需要将该位置的states和diagonals1/diagonals2中对应的值置为0和删除。



