# Time Complex: O(n)
# Space Complex: O(h)   best: O(ln(n)) worst: O(n)
#[0,1,2,3,4,5,6,7,8,9]
#preorder:[0,1,3,7,8,4,9,2,5,6]
#inorder:[7,3,8,1,9,4,0,5,2,6]
#postorder:[7,8,3,9,4,1,5,6,2,0]

#breadth travel

class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None


def insertLevelOrder(arr, root, i, n):
    # Base case for recursion
    if i < n:
        root = TreeNode(arr[i])

        # insert left child
        root.left = insertLevelOrder(arr, root.left, 2 * i + 1, n)
        # insert right child
        root.right = insertLevelOrder(arr, root.right, 2 * i + 2, n)

    return root


#DFS-preorder先序
def preorder(root):
    if root != None:
        print(root.val, end=" ")
        preorder(root.left)
        preorder(root.right)


#DFS-inorder中序
def inOrder(root):
    if root != None:
        inOrder(root.left)
        print(root.val,end=" ")
        inOrder(root.right)


#DFS-postorder后序
def postorder(root):
    if root != None:
        postorder(root.left)
        postorder(root.right)
        print(root.val, end=" ")

#BFS-breadth广度
def levelOrder(root):
    res = []
    if root is None:
        return res
    # 模拟一个队列储存节点
    q = []
    # 首先将根节点入队
    q.append(root)
    # 列表为空时，循环终止
    while len(q) != 0:
        length = len(q)
        for i in range(length):
            # 将同层节点依次出队
            r = q.pop(0)
            if r.left is not None:
                # 非空左孩子入队
                q.append(r.left)
            if r.right is not None:
                # 非空右孩子入队
                q.append(r.right)
            res.append(r.value)
            print(r.value)
    return res


if __name__ == '__main__':
    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    n = len(arr)
    root = None
    root = insertLevelOrder(arr, root, 0, n)
    print("preorder is:")
    preorder(root)
    print("\n")
    print("inorder is:")
    inOrder(root)
    print("\n")
    print("postorder is:")
    postorder(root)

