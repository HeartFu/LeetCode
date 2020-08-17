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
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def getLength(head: ListNode) -> int:
            ret = 0
            while head:
                ret += 1
                head = head.next
            return ret
        
        def buildTree(left: int, right: int) -> TreeNode:
            if left > right:
                return None
            mid = (left + right + 1) // 2
            root = TreeNode()
            root.left = buildTree(left, mid - 1)
            nonlocal head
            root.val = head.val
            head = head.next
            root.right = buildTree(mid + 1, right)
            return root
        
        length = getLength(head)
        return buildTree(0, length - 1)

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