https://leetcode-cn.com/problems/convert-sorted-list-to-binary-search-tree/

难度：中等

## 109. Convert Sorted List to Binary Search Tree

Given the head of a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

**Example 1:**

![avatar](linked.jpg)

```
Input: head = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: One possible answer is [0,-3,9,-10,null,5], which represents the shown height balanced BST.
```

**Example 2:**

```
Input: head = []
Output: []
```

**Example 3:**

```
Input: head = [0]
Output: [0]
```

**Example 4:**

```
Input: head = [1,3]
Output: [3,1]
```

## 109. 有序链表转换二叉搜索树

给定一个单链表，其中的元素按升序排序，将其转换为高度平衡的二叉搜索树。

本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

**示例:**

给定的有序链表： [-10, -3, 0, 5, 9],

一个可能的答案是：[0, -3, 9, -10, null, 5], 它可以表示下面这个高度平衡二叉搜索树：

![avatar](linked.jpg)

## 名词解释

**二叉查找树**（英语：Binary Search Tree），也称为**二叉搜索树、有序二叉树**（ordered binary tree）或**排序二叉树**（sorted binary tree），是指一棵空树或者具有下列性质的二叉树：

- 若任意节点的左子树不空，则左子树上所有节点的值均小于它的根节点的值；
- 若任意节点的右子树不空，则右子树上所有节点的值均大于或等于它的根节点的值；
- 任意节点的左、右子树也分别为二叉查找树；

**a height balanced BST**，高度平衡二叉树，左右子树深度差不超过1。即当**所有节点**的左子树深度为2时，右子树深度为1-3。

## 解题思路

从名词解释中可以得知，1）二叉搜索树左子树上节点值均小于其根节点的值，右子树上节点值均大于或等于其根节点的值；2）左右子树深度差不超过1.

从上述解释中可以得到，需要将链表一分为二，中位数为根节点，中位数左边的所有值构建根节点的左子树，中位数右边的所有值构建根节点的右子树。因为一分为二从中间取，a) 当链表长度为偶数时，中位数除去后，左右子链表长度差为1，符合高度平衡二叉树，b) 当链表长度为奇数时，中位数除去后，左右子链表长度相等，满足高度平衡二叉树。

### 链表转化为数组便于寻找中位数

故现在需要确定中位数。因为链表不像数组，无法直接按照index取值，故第一个方法可以将链表遍历生成数组，然后结合递归进行生成高度平衡二叉树。

- step1： 确定left和right，用于截断数组。left表示当前最左边的index，right表示当前最右边的index
- step2： 根据left和right得到mid，若当前数组（由left和right截断的数组）长度为偶数，则直接取中间的值，若为奇数，则取中间两个数中的右边的数。
- step3： 构建根结构。
- step4： 根据根结构所在index，更新根结构对应左子树中left和right的值，根据step1-4构建其左子树
- step5： 根据根结构所在index，更新根结构对应右子树中left和right的值，根据step1-5构建其右子树
- step6： 返回树

See the Solution_convertolist.py

### 根据链表和中序遍历寻找中位数

另一个思路为知道链表的长度的情况下，链表最左边的值一定为根节点左子树最左边的一个叶子节点。所以在递归的时候，我们可以先不设定该节点的值，因为当遍历到左子树最后一个节点时一定是对应的链表最左边的一个值。

同理，当去掉该值后，下一个值要么是该节点的左子树，要么是该节点的右子树，故根据递归可以得到该值。

查看 https://leetcode-cn.com/problems/convert-sorted-list-to-binary-search-tree/solution/you-xu-lian-biao-zhuan-huan-er-cha-sou-suo-shu-1-3/ 中的方法二。

See the Solution.py



