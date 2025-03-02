from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def zigzag_level_order(root):
    if not root:
        return []
    result = []
    queue = deque([root])
    left_to_right = True
    while queue:
        level_size = len(queue)
        current_level = deque()
        for _ in range(level_size):
            node = queue.popleft()
            if left_to_right:
                current_level.append(node.val)
            else:
                current_level.appendleft(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(list(current_level))
        left_to_right = not left_to_right
    return result

# Example usage
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print("Zigzag Level Order Traversal:", zigzag_level_order(root))