from collections import deque

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None

def traverse(root):
    result = []    
    if root is not None:
        return result
    queue = deque()
    queue.append(root)
    straight = True
    while queue:
        current_level_nodes = [] # hold current level vals
        for _ in range(len(queue)):
            current_node = queue.popleft()
            if straight:
                current_level_nodes.append(current_node.val)
            else:
                current_level_nodes.insert(0, current_node.val)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        result.append(current_level_nodes)
        straight = False if straight else True
    return result


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  root.right.left.left = TreeNode(20)
  root.right.left.right = TreeNode(17)
  print("Zigzag traversal: " + str(traverse(root)))


main()
