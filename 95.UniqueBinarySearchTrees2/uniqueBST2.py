# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n):
        if n <=0:
            return []
        
        return self.getBinaryTree(1, n) 
    
    # right is n when first to enter this function
    def getBinaryTree(self, left, right):
        trees = []
        if left > right:
            trees.append('null')
            return trees

        if left == right:
            trees.append(TreeNode(left))
            return trees
        
        for i in range(left, right + 1):
            leftTreeList = self.getBinaryTree(left, i - 1)
            rightTreeList = self.getBinaryTree(i + 1, right)
            
            for leftTree in leftTreeList:
                for rightTree in rightTreeList:
                    currTree = TreeNode(i, leftTree, rightTree)
                    trees.append(currTree)
        
        return trees

solution = Solution()
print(solution.generateTrees(3))