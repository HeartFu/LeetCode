https://leetcode-cn.com/problems/course-schedule/

## 207. Course Schedule

There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

 

**Example 1**:

**Input:** numCourses = 2, prerequisites = [[1,0]]

**Output:** true

**Explanation:** There are a total of 2 courses to take. To take course 1 you should have finished course 0. So it is possible.

**Example 2:**

**Input:** numCourses = 2, prerequisites = [[1,0],[0,1]]

**Output:** false

**Explanation:** There are a total of 2 courses to take. To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
 

**Constraints:**

- The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.

- You may assume that there are no duplicate edges in the input prerequisites.

- 1 <= numCourses <= 10^5


## 207. 课程表

你这个学期必须选修 numCourse 门课程，记为 0 到 numCourse-1 。

在选修某些课程之前需要一些先修课程。 例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们：[0,1]

给定课程总量以及它们的先决条件，请你判断是否可能完成所有课程的学习？

 

**示例 1:**

**输入:** 2, [[1,0]] 

**输出:** true

**解释:** 总共有 2 门课程。学习课程 1 之前，你需要完成课程 0。所以这是可能的。

**示例 2:**

**输入:** 2, [[1,0],[0,1]]

**输出:** false

**解释:** 总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0；并且学习课程 0 之前，你还应先完成课程 1。这是不可能的。
 

**提示：**

- 输入的先决条件是由 边缘列表 表示的图形，而不是 邻接矩阵 。详情请参见图的表示法。
- 你可以假定输入的先决条件中没有重复的边。
- 1 <= numCourses <= 10^5


## 解题思路

![Solution](https://github.com/HeartFu/LeetCode/blob/master/207.Course%20Schedule/solution.png)