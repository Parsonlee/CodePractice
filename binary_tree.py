from collections import deque
from typing import Optional, List

# 定义二叉树节点
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# --- 递归实现 ---

def preorder_traversal(root: Optional[TreeNode]) -> List[int]:
    """前序遍历: 根 -> 左 -> 右"""
    result = []
    def traverse(node):
        if not node:
            return
        result.append(node.val)
        traverse(node.left)
        traverse(node.right)
    traverse(root)
    return result

def inorder_traversal(root: Optional[TreeNode]) -> List[int]:
    """中序遍历: 左 -> 根 -> 右"""
    result = []
    def traverse(node):
        if not node:
            return
        traverse(node.left)
        result.append(node.val)
        traverse(node.right)
    traverse(root)
    return result

def postorder_traversal(root: Optional[TreeNode]) -> List[int]:
    """后序遍历: 左 -> 右 -> 根"""
    result = []
    def traverse(node):
        if not node:
            return
        traverse(node.left)
        traverse(node.right)
        result.append(node.val)
    traverse(root)
    return result

# --- 迭代实现 (使用栈) ---

def dfs_preorder_iterative(root: Optional[TreeNode]) -> List[int]:
    """前序遍历（迭代实现，根->左->右）"""
    if not root:
        return []
    result = []
    stack = [root]
    while stack:
        node = stack.pop()
        result.append(node.val)
        # 先右后左，保证左子树先出栈
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return result

def dfs_inorder_iterative(root: Optional[TreeNode]) -> List[int]:
    """中序遍历（迭代实现，左->根->右）"""
    result = []
    stack = []
    curr = root
    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        result.append(curr.val)
        curr = curr.right
    return result

def dfs_postorder_iterative(root: Optional[TreeNode]) -> List[int]:
    """后序遍历（迭代实现，左->右->根）"""
    if not root:
        return []
    result = []
    stack = [root]
    while stack:
        node = stack.pop()
        result.append(node.val)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return result[::-1]  # 逆序得到左->右->根

# --- 迭代实现 (使用队列) ---

def levelorder_traversal(root: Optional[TreeNode]) -> List[int]:
    """层序遍历 (广度优先搜索)"""
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        result.append(node.val)
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
            
    return result

# --- 示例 ---
if __name__ == "__main__":
    # 构建一个示例二叉树:
    #      2
    #     / \
    #    1    1
    #   / \  / \
    #  2   3 3  2
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(1)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(2)

    # 执行并打印各种遍历结果
    print(f"前序遍历 (根->左->右): {preorder_traversal(root)}")
    print(f"中序遍历 (左->根->右): {inorder_traversal(root)}")
    print(f"后序遍历 (左->右->根): {postorder_traversal(root)}")
    print(f"层序遍历 (逐层):     {levelorder_traversal(root)}")

