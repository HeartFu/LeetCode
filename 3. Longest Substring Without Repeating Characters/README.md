https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/


**难度：** 中等

## 3. Longest Substring Without Repeating Characters

Given a string, find the length of the longest substring without repeating characters.

**Example 1:**

```markdown
Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
```

**Example 2:**

```
Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
```
**Example 3:**
```
Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 

Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
```

## 3. 无重复字符的最长子串 


给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

**示例 1:**
```
输入: "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
```
**示例 2:**
```
输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
```

**示例 3:**
```
输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
```


## 解题思路

因为需要找出最长的子串且子串中不能存在重复的字符，所以需要遍历整个字符串才能找到对应的答案。

在遍历中需要针对不同的情况进行不同的判断。

1. 如果当前值x已经存在在子串s中，表示已经遇到了重复的字符x，则需要将该字符x在子串s中的位置找到，并截取该位置后面的子串s的所有字符。因为该子串s中字符x前的所有字符均不可能再出现在包含第二个重复的字符x的另一个子串中，这样可以减少对应的重复遍历的时间和空间。

2. 如果当前值x不存在在子串s中，则将该字符x加入到子串s中

3. 完成子串s的创建后，判断当前子串与之前所保存的最长子串的长度进行对比，若大于，则替换maxLength值，反之则继续遍历。

