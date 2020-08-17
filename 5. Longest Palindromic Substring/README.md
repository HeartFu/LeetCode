https://leetcode-cn.com/problems/longest-palindromic-substring/

**难度：中等**

## 5. Longest Palindromic Substring

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

**Example 1:**
```
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
```
**Example 2:**
```
Input: "cbbd"
Output: "bb"
```

## 5. 最长回文子串

给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

**示例 1：**
```
输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
```
示例 2：
```
输入: "cbbd"
输出: "bb"
```

## 名词解释

1. Palindromic String(回文字符串)：若当前字符串正序倒叙均一样，则成为回文字符串。
    
    e.g. aba：正序aba  倒叙aba 均一样，故aba是回文字符串。

## 解题思路--对称法

那道题的第一反应，暴力法解决，即将所有子串遍历出来后，判断是否存在最长的回文子串，但该方法的时间复杂度和空间复杂度均很高。放弃

因为回文字符串都是对称的，对称轴为某个字符或者某两个字符之间，故可以使用对称性来进行计算。

1. 因为不确定回文串是奇数还是偶数，故通过每个字符之间插入#来代替对称轴在两个字符串之间的情况，e.g. aba -》 a#b#a

2. 遍历每一个字符，并向左向右拓展知道左右两边的字符不同或者到达边界为止。

3. 在每一个字符遍历中，得到的回文串需要跟已经存储的最大回文串进行比较，若长度大于已经存储的回文串的话，则将新得到的回文串替换已经存储的最大回文串。

4. 遍历完成后返回已经存储的最大回文串即可。

时间复杂度为O(n^2)


## 解题思路 -- Manacher方法 待添加

