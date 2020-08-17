# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedListToBST(self, head) -> TreeNode:
        headlist = []
        while head:
            headlist.append(head.val)
            head = head.next
        
        left = 0
        right = len(headlist) - 1

        return self.buildBST(headlist, left, right)

    def buildBST(self, headlist, left, right):
        if left > right:
            return None
        elif left == right:
            return TreeNode(headlist[left])
        
        lenght = right - left + 1
        if lenght % 2 == 0:
            # 表示当前list长度为偶数
            mid = int(left + lenght / 2)
        else:
            # 表示当前list长度为奇数
            mid = int(left + lenght / 2)
        
        newNode = TreeNode(headlist[mid])
        newNode.left = self.buildBST(headlist, left, mid - 1)
        newNode.right = self.buildBST(headlist, mid + 1, right)

        return newNode

def buildNodeList(list_pre, i):
    if i >= len(list_pre):
        return None
    newNode = ListNode(list_pre[i])
    newNode.next = buildNodeList(list_pre, i + 1)

    return newNode


solution = Solution()
list1 = [-10,-3,0,5,9]

head_org = buildNodeList(list1, 0)

print(solution.sortedListToBST(head_org))