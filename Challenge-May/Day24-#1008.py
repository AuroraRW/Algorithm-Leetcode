"""
Construct Binary Search Tree from Preorder Traversal
Return the root node of a binary search tree that matches the given preorder traversal.

(Recall that a binary search tree is a binary tree where for every node,
any descendant of node.left has a value < node.val, and any descendant of node.right has a value > node.val.
Also recall that a preorder traversal displays the value of the node first, then traverses node.left,
then traverses node.right.)

It's guaranteed that for the given test cases there is always possible to find a binary search tree with the given requirements.

Example 1:
Input: [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]

Constraints:
    1 <= preorder.length <= 100
    1 <= preorder[i] <= 10^8
    The values of preorder are distinct.
"""


from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inOrder(root):
    if root != None:
        inOrder(root.left)
        print(root.val,end=" ")
        inOrder(root.right)


def insert(root: TreeNode, value: int):
    while root:
        if value <= root.val:
            if root.left:
                insert(root.left, value)
            else:
                root.left = TreeNode(val=value)
                return
        else:
            if root.right:
                insert(root.right, value)
            else:
                root.right = TreeNode(val=value)
                return
        return


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        root = TreeNode()
        root.val = preorder[0]

        for i in preorder[1:]:
            insert(root, i)
        return root


if __name__ == "__main__":
    S=Solution()
    root = S.bstFromPreorder([8, 5, 1, 7, 10, 12])
    print(inOrder(root))